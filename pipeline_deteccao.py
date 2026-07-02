"""
=============================================================================
Pipeline de Detecção de Tráfego Malicioso — CIC-IDS-2017
1ª Camada (detecção clássica/DL) com avaliação HONESTA (sem vazamento)
=============================================================================

Projeto: "Uso de Modelos de Linguagem de Grande Escala na Análise de Tráfego
          Malicioso em Redes Internas"
Alunos:  Breno Lourenço Macedo / Mateus Ferreira da Silva

POR QUE ESTE SCRIPT EXISTE
--------------------------
O pré-processamento anterior produzia acurácia ~97-99% porque:
  (1) o conjunto de TESTE estava balanceado (30k registros, classes iguais).
      Tráfego real é ~99% benigno; testar balanceado ESCONDE o falso positivo,
      que é exatamente o problema que o projeto promete resolver.
  (2) features identificadoras (porta de destino, e nos arquivos completos
      IPs/timestamp) deixam o modelo "decorar" o atacante -> vazamento.
  (3) StandardScaler e balanceamento eram aplicados ANTES do split treino/teste
      -> informação do teste vaza para o treino.

Este script corrige os três pontos e mede o impacto. Ele roda DOIS cenários
lado a lado para você poder mostrar a diferença ao professor:
  - CENÁRIO A ("inflado"): reproduz a forma antiga (porta inclusa, teste balanceado)
  - CENÁRIO B ("honesto"): drop de colunas que vazam, teste na distribuição real,
                           scaler/balanceamento só no treino.

Também exporta train.csv / test.csv (split único, sem vazamento) para o Mateus
carregar a MESMA divisão na LSTM do MATLAB — assim os números são comparáveis.

COMO USAR
---------
1. Baixe o dataset (8 CSVs "MachineLearningCVE" do CIC-IDS-2017):
   https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset
2. Aponte DATA_DIR para a pasta com os .csv.
3. pip install pandas numpy scikit-learn imbalanced-learn matplotlib
   (opcional p/ rede neural: pip install tensorflow)
4. python pipeline_deteccao.py
"""

import os
import glob
import warnings
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix, f1_score,
    precision_score, recall_score, accuracy_score,
)

warnings.filterwarnings("ignore")

# =============================================================================
# CONFIGURAÇÃO
# =============================================================================
CONFIG = {
    # Pasta com os 8 CSVs do CIC-IDS-2017 (MachineLearningCVE)
    "DATA_DIR": "./MachineLearningCVE",
    # Pasta de saída (splits exportados, casos borderline, figuras)
    "OUT_DIR": "./saidas",
    "RANDOM_STATE": 42,
    "TEST_SIZE": 0.20,
    # Tamanho máximo da amostra de TREINO por classe (subamostragem só no treino).
    # O TESTE NUNCA é balanceado — fica na distribuição natural.
    "MAX_TRAIN_PER_CLASS": 20000,
    # Colunas que vazam: serão removidas no cenário honesto.
    # Detecção por substring (case-insensitive), robusta a espaços nos nomes.
    "LEAKY_SUBSTRINGS": [
        "flow id", "source ip", "src ip", "destination ip", "dst ip",
        "source port", "src port", "timestamp", "fwd header length.1",
        # Porta de DESTINO também vaza no CIC-IDS-2017 (ex.: 80->web, 21->ftp,
        # 22->ssh). Mantê-la inflaria o resultado. Remova no cenário honesto.
        "destination port", "dst port",
    ],
}


# =============================================================================
# 1. CARGA E LIMPEZA
# =============================================================================
def carregar_dados(data_dir):
    arquivos = sorted(glob.glob(os.path.join(data_dir, "*.csv")))
    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum CSV em {data_dir}. Baixe o dataset e ajuste CONFIG['DATA_DIR']."
        )
    print(f"[carga] {len(arquivos)} arquivos encontrados.")
    dfs = []
    for a in arquivos:
        df = pd.read_csv(a, low_memory=False)
        dfs.append(df)
        print(f"   - {os.path.basename(a)}: {df.shape[0]:>8} linhas")
    df = pd.concat(dfs, ignore_index=True)
    # Normaliza nomes de colunas (o CIC-IDS-2017 vem com espaços à esquerda)
    df.columns = [c.strip() for c in df.columns]
    print(f"[carga] total bruto: {df.shape[0]} linhas, {df.shape[1]} colunas")
    return df


def padronizar_rotulos(df, label_col="Label"):
    """Cria 'Label_multi' (categoria do ataque) e 'Label_bin' (0=benigno,1=ataque)."""
    df[label_col] = df[label_col].astype(str).str.strip()
    # Agrupa rótulos finos do CIC-IDS-2017 em famílias
    def familia(lbl):
        l = lbl.upper()
        if "BENIGN" in l:
            return "Benign"
        if "PORTSCAN" in l or "PORT SCAN" in l:
            return "PortScan"
        if "DDOS" in l:
            return "DDoS"
        if l.startswith("DOS") or "DOS " in l or "HULK" in l or "GOLDENEYE" in l \
           or "SLOWLORIS" in l or "SLOWHTTP" in l:
            return "DoS"
        if "BRUTE" in l or "PATATOR" in l or "FTP" in l or "SSH" in l:
            return "BruteForce"
        if "WEB ATTACK" in l or "XSS" in l or "SQL" in l:
            return "WebAttack"
        if "BOT" in l:
            return "Bot"
        if "INFILTRAT" in l:
            return "Infiltration"
        if "HEARTBLEED" in l:
            return "Heartbleed"
        return lbl  # mantém o que não casar
    df["Label_multi"] = df[label_col].apply(familia)
    df["Label_bin"] = (df["Label_multi"] != "Benign").astype(int)
    return df


def limpar(df):
    """inf -> NaN, remove linhas NaN, remove duplicatas exatas."""
    n0 = len(df)
    num = df.select_dtypes(include=[np.number]).columns
    df[num] = df[num].replace([np.inf, -np.inf], np.nan)
    df = df.dropna()
    n1 = len(df)
    df = df.drop_duplicates()
    n2 = len(df)
    print(f"[limpeza] NaN/inf removidos: {n0 - n1:>8} | duplicatas: {n1 - n2:>8}")
    print(f"[limpeza] restante: {n2} linhas")
    return df.reset_index(drop=True)


# =============================================================================
# 2. SELEÇÃO DE FEATURES (com/sem vazamento)
# =============================================================================
def colunas_que_vazam(df, leaky_substrings):
    achadas = []
    for c in df.columns:
        cl = c.lower().strip()
        if any(s in cl for s in leaky_substrings):
            achadas.append(c)
    return achadas


def montar_X_y(df, drop_leaky, leaky_substrings, target="Label_multi"):
    nao_features = {"Label", "Label_multi", "Label_bin"}
    leaky = colunas_que_vazam(df, leaky_substrings) if drop_leaky else []
    if leaky:
        print(f"[features] removendo {len(leaky)} colunas que vazam: {leaky}")
    cols = [c for c in df.columns if c not in nao_features and c not in leaky]
    # Mantém apenas numéricas
    X = df[cols].select_dtypes(include=[np.number]).copy()
    y = df[target].copy()
    return X, y


# =============================================================================
# 3. SUBAMOSTRAGEM (SÓ NO TREINO!)
# =============================================================================
def subamostrar_treino(X_tr, y_tr, max_por_classe, random_state):
    """Limita o nº de exemplos por classe NO TREINO. O teste fica intocado."""
    df = X_tr.copy()
    df["_y"] = y_tr.values
    partes = []
    for classe, grupo in df.groupby("_y"):
        if len(grupo) > max_por_classe:
            grupo = grupo.sample(max_por_classe, random_state=random_state)
        partes.append(grupo)
    bal = pd.concat(partes).sample(frac=1, random_state=random_state)
    y = bal.pop("_y")
    return bal, y


# =============================================================================
# 4. AVALIAÇÃO
# =============================================================================
def avaliar(nome, y_true, y_pred, labels=None):
    print(f"\n================ {nome} ================")
    print(f"Acurácia : {accuracy_score(y_true, y_pred):.4f}")
    print(f"F1 macro : {f1_score(y_true, y_pred, average='macro'):.4f}")
    print(f"F1 weight: {f1_score(y_true, y_pred, average='weighted'):.4f}")
    print("\nRelatório por classe:")
    print(classification_report(y_true, y_pred, digits=4, zero_division=0))

    # Falso positivo no nível BINÁRIO (benigno classificado como ataque)
    yt = pd.Series(y_true).astype(str)
    yp = pd.Series(y_pred).astype(str)
    bin_t = (yt != "Benign").astype(int)
    bin_p = (yp != "Benign").astype(int)
    tn = int(((bin_t == 0) & (bin_p == 0)).sum())
    fp = int(((bin_t == 0) & (bin_p == 1)).sum())
    fn = int(((bin_t == 1) & (bin_p == 0)).sum())
    tp = int(((bin_t == 1) & (bin_p == 1)).sum())
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    fnr = fn / (fn + tp) if (fn + tp) else 0.0
    print(f"[binário] Benigno total no teste: {fp + tn}  |  Ataque total: {fn + tp}")
    print(f"[binário] Falsos positivos (FP): {fp}  ->  FPR = {fpr:.4%}")
    print(f"[binário] Falsos negativos (FN): {fn}  ->  FNR = {fnr:.4%}")
    return {"acc": accuracy_score(y_true, y_pred),
            "f1_macro": f1_score(y_true, y_pred, average="macro"),
            "fpr": fpr, "fnr": fnr, "fp": fp, "fn": fn}


# =============================================================================
# 5. EXECUÇÃO DE UM CENÁRIO
# =============================================================================
def rodar_cenario(df, drop_leaky, teste_balanceado, nome):
    print("\n" + "#" * 78)
    print(f"# CENÁRIO: {nome}")
    print(f"#   drop colunas que vazam = {drop_leaky}")
    print(f"#   teste balanceado       = {teste_balanceado}  (False = distribuição real)")
    print("#" * 78)

    X, y = montar_X_y(df, drop_leaky, CONFIG["LEAKY_SUBSTRINGS"])

    if teste_balanceado:
        # Reproduz o erro antigo: balanceia TUDO e depois divide.
        d = X.copy(); d["_y"] = y.values
        partes = []
        for _, g in d.groupby("_y"):
            partes.append(g.sample(min(len(g), 3000), random_state=CONFIG["RANDOM_STATE"]))
        d = pd.concat(partes)
        y = d.pop("_y")
        X = d
        X_tr, X_te, y_tr, y_te = train_test_split(
            X, y, test_size=CONFIG["TEST_SIZE"],
            random_state=CONFIG["RANDOM_STATE"], stratify=y)
    else:
        # Correto: split primeiro (teste fica na distribuição NATURAL),
        # subamostragem só no treino.
        X_tr, X_te, y_tr, y_te = train_test_split(
            X, y, test_size=CONFIG["TEST_SIZE"],
            random_state=CONFIG["RANDOM_STATE"], stratify=y)
        X_tr, y_tr = subamostrar_treino(
            X_tr, y_tr, CONFIG["MAX_TRAIN_PER_CLASS"], CONFIG["RANDOM_STATE"])

    print(f"[split] treino: {len(X_tr)} | teste: {len(X_te)}")
    print(f"[split] distribuição do TESTE (o que importa):")
    print(y_te.value_counts().to_string())

    # Scaler ajustado SÓ no treino
    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_tr)
    X_te_s = scaler.transform(X_te)

    # class_weight balanced compensa o desbalanceamento sem mexer no teste
    clf = RandomForestClassifier(
        n_estimators=200, n_jobs=-1, class_weight="balanced",
        random_state=CONFIG["RANDOM_STATE"])
    clf.fit(X_tr_s, y_tr)
    y_pred = clf.predict(X_te_s)

    met = avaliar(f"{nome} — RandomForest", y_te, y_pred)

    return {"clf": clf, "scaler": scaler, "X_te": X_te, "X_te_s": X_te_s,
            "y_te": y_te, "y_pred": y_pred, "metricas": met,
            "X_tr": X_tr, "y_tr": y_tr}


# =============================================================================
# 6. EXPORT PARA O MATLAB + CASOS BORDERLINE PARA A 2ª CAMADA (LLM)
# =============================================================================
def exportar_para_matlab(res, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    tr = res["X_tr"].copy(); tr["Label"] = res["y_tr"].values
    te = res["X_te"].copy(); te["Label"] = res["y_te"].values
    tr.to_csv(os.path.join(out_dir, "train.csv"), index=False)
    te.to_csv(os.path.join(out_dir, "test.csv"), index=False)
    print(f"\n[export] train.csv / test.csv salvos em {out_dir}")
    print("[export] o Mateus deve carregar ESTES arquivos na LSTM do MATLAB,")
    print("[export] para treinar/avaliar na MESMA divisão sem vazamento.")


def salvar_casos_borderline(res, out_dir, low=0.45, high=0.75):
    """
    Seleciona casos de baixa confiança (a fronteira de decisão) que serão a
    entrada da 2ª camada (LLM). A ideia: a LLM só reavalia o que o modelo
    clássico tem dúvida -> reduz custo e foca onde o falso positivo nasce.
    """
    clf, X_te, X_te_s = res["clf"], res["X_te"], res["X_te_s"]
    proba = clf.predict_proba(X_te_s)
    conf = proba.max(axis=1)  # confiança da classe vencedora
    mask = (conf >= low) & (conf <= high)
    borderline = X_te[mask].copy()
    borderline["pred"] = res["y_pred"][mask]
    borderline["real"] = res["y_te"].values[mask]
    borderline["confianca"] = conf[mask]
    path = os.path.join(out_dir, "casos_borderline.csv")
    borderline.to_csv(path, index=False)
    print(f"[2ª camada] {len(borderline)} casos borderline "
          f"(confiança {low}-{high}) salvos em {path}")
    print("[2ª camada] use estes casos como entrada do módulo LLM (camada_llm.py).")
    return borderline


# =============================================================================
# MAIN
# =============================================================================
def main():
    os.makedirs(CONFIG["OUT_DIR"], exist_ok=True)
    df = carregar_dados(CONFIG["DATA_DIR"])
    df = padronizar_rotulos(df)
    df = limpar(df)

    print("\n[distribuição real das classes no dataset limpo]")
    print(df["Label_multi"].value_counts().to_string())
    print(f"\nProporção de benigno: "
          f"{(df['Label_multi'] == 'Benign').mean():.2%}  <-- tráfego real é assim")

    # CENÁRIO A: reproduz o número inflado (para comparação/didática)
    rodar_cenario(df, drop_leaky=False, teste_balanceado=True,
                  nome="A) INFLADO (porta inclusa + teste balanceado)")

    # CENÁRIO B: avaliação honesta
    res = rodar_cenario(df, drop_leaky=True, teste_balanceado=False,
                        nome="B) HONESTO (sem vazamento + teste realista)")

    # Exporta split e casos borderline a partir do cenário honesto
    exportar_para_matlab(res, CONFIG["OUT_DIR"])
    salvar_casos_borderline(res, CONFIG["OUT_DIR"])

    print("\n" + "=" * 78)
    print("RESUMO: compare a acurácia/FPR do cenário A vs B.")
    print("O número 'honesto' (B) é o que deve ir para o relatório — e é a base")
    print("sobre a qual a 2ª camada (LLM) vai mostrar redução de falso positivo.")
    print("=" * 78)


if __name__ == "__main__":
    main()
