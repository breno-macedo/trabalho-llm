"""
=============================================================================
2ª Camada — Reanálise com LLM para REDUÇÃO DE FALSOS POSITIVOS
=============================================================================

Entra aqui a contribuição original do projeto. A 1ª camada (pipeline_deteccao.py)
já classificou o tráfego e separou os casos DUVIDOSOS (casos_borderline.csv).
A LLM reavalia SÓ esses casos — é onde o falso positivo nasce — converte o fluxo
em texto, decide "ataque" vs "benigno" e EXPLICA o porquê.

Métrica-chave: quantos falsos positivos da 1ª camada a LLM consegue corrigir,
sem transformar ataques reais em "benigno" (ou seja, sem aumentar o falso negativo).

DESIGN
------
- Funciona offline com um classificador "mock" (heurístico) para você testar o
  fluxo todo sem chave de API.
- Para usar uma LLM de verdade, preencha chamar_llm() com a sua API
  (OpenAI, Anthropic, Gemini, ou um modelo local via Ollama). O resto não muda.

COMO USAR
---------
1. Rode antes o pipeline_deteccao.py (gera saidas/casos_borderline.csv).
2. (opcional) export OPENAI_API_KEY=...  e troque USE_MOCK=False.
3. python camada_llm.py
"""

import os
import json
import pandas as pd

CONFIG = {
    "BORDERLINE_CSV": "./saidas/casos_borderline.csv",
    "OUT_CSV": "./saidas/resultado_llm.csv",
    "USE_MOCK": True,           # True = heurística local (sem API). False = LLM real.
    "MODEL": "gpt-4o-mini",     # usado só quando USE_MOCK=False
    "MAX_CASOS": 200,           # limite p/ não gastar muitos tokens em teste
}


# =============================================================================
# 1. FLUXO -> TEXTO
# =============================================================================
def fluxo_para_texto(linha):
    """
    Converte uma linha de features de fluxo em uma descrição textual que a LLM
    entende. Selecione as features mais interpretáveis; não jogue as 50 colunas.
    Ajuste os nomes às colunas que existirem no seu CSV.
    """
    def g(*nomes, default="n/d"):
        for n in nomes:
            if n in linha and pd.notna(linha[n]):
                return linha[n]
        return default

    partes = [
        f"Duração do fluxo: {g('Flow Duration')} microssegundos.",
        f"Pacotes enviados (fwd): {g('Total Fwd Packets')}; "
        f"recebidos (bwd): {g('Total Backward Packets')}.",
        f"Bytes fwd: {g('Total Length of Fwd Packets', 'Fwd Packets Length Total')}; "
        f"bwd: {g('Total Length of Bwd Packets', 'Bwd Packets Length Total')}.",
        f"Taxa de pacotes/s: {g('Flow Packets/s')}; bytes/s: {g('Flow Bytes/s')}.",
        f"Flags SYN: {g('SYN Flag Count')}, ACK: {g('ACK Flag Count')}, "
        f"RST: {g('RST Flag Count')}, PSH: {g('PSH Flag Count')}.",
        f"Tamanho médio de pacote: {g('Average Packet Size', 'Packet Length Mean')}.",
    ]
    return " ".join(str(p) for p in partes)


# =============================================================================
# 2. PROMPT
# =============================================================================
SYSTEM_PROMPT = (
    "Você é um analista sênior de segurança de redes (SOC). Recebe a descrição "
    "de um fluxo de rede que um detector automático marcou como SUSPEITO, mas com "
    "baixa confiança. Sua tarefa é decidir se o fluxo é realmente um ATAQUE ou "
    "tráfego BENIGNO (falso positivo), e justificar em 1-2 frases. "
    "Responda SOMENTE em JSON: "
    '{"veredito": "ataque" | "benigno", "tipo": "<categoria ou n/d>", '
    '"confianca": 0..1, "justificativa": "<texto curto>"}.'
)

def montar_prompt_usuario(texto_fluxo, palpite_modelo):
    return (
        f"Decisão preliminar do modelo clássico: {palpite_modelo}.\n"
        f"Descrição do fluxo:\n{texto_fluxo}\n\n"
        "Reavalie criticamente. Padrões muito regulares, volumes pequenos e "
        "ausência de flags de varredura costumam indicar tráfego legítimo."
    )


# =============================================================================
# 3. CHAMADA À LLM (real ou mock)
# =============================================================================
def chamar_llm_mock(texto_fluxo, palpite_modelo):
    """
    Heurística simples só para validar o pipeline sem API.
    Tende a reclassificar como 'benigno' fluxos pequenos/regulares.
    SUBSTITUA por uma LLM real para os resultados do trabalho.
    """
    t = texto_fluxo.lower()
    benigno = ("syn flags: 0" in t) or ("flags syn: 0" in t)
    return {
        "veredito": "benigno" if benigno else "ataque",
        "tipo": "n/d" if benigno else str(palpite_modelo),
        "confianca": 0.6,
        "justificativa": ("Heurística mock: poucas flags de varredura sugerem "
                          "tráfego legítimo." if benigno
                          else "Heurística mock: padrão compatível com ataque."),
    }


def chamar_llm_real(texto_fluxo, palpite_modelo, model):
    """
    Exemplo com a API da OpenAI (formato chat). Troque pelo provedor que usarem.
    Requer: pip install openai  e  export OPENAI_API_KEY=...
    """
    from openai import OpenAI
    client = OpenAI()
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": montar_prompt_usuario(texto_fluxo, palpite_modelo)},
        ],
        temperature=0,
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)


def chamar_llm(texto_fluxo, palpite_modelo):
    if CONFIG["USE_MOCK"]:
        return chamar_llm_mock(texto_fluxo, palpite_modelo)
    return chamar_llm_real(texto_fluxo, palpite_modelo, CONFIG["MODEL"])


# =============================================================================
# 4. EXECUÇÃO E MÉTRICA DE REDUÇÃO DE FALSO POSITIVO
# =============================================================================
def main():
    df = pd.read_csv(CONFIG["BORDERLINE_CSV"]).head(CONFIG["MAX_CASOS"])
    print(f"[llm] reavaliando {len(df)} casos borderline "
          f"({'MOCK' if CONFIG['USE_MOCK'] else CONFIG['MODEL']})")

    resultados = []
    for _, linha in df.iterrows():
        texto = fluxo_para_texto(linha)
        palpite = linha.get("pred", "n/d")
        veredito = chamar_llm(texto, palpite)
        resultados.append({
            "pred_modelo": palpite,
            "real": linha.get("real", "n/d"),
            "llm_veredito": veredito.get("veredito"),
            "llm_tipo": veredito.get("tipo"),
            "llm_justificativa": veredito.get("justificativa"),
            "texto_fluxo": texto,
        })
    out = pd.DataFrame(resultados)
    os.makedirs(os.path.dirname(CONFIG["OUT_CSV"]), exist_ok=True)
    out.to_csv(CONFIG["OUT_CSV"], index=False)

    # --- Métrica: a LLM corrigiu falsos positivos sem criar falsos negativos? ---
    real_bin = out["real"].astype(str).ne("Benign")          # True = ataque real
    pred_bin = out["pred_modelo"].astype(str).ne("Benign")   # True = modelo disse ataque
    llm_bin = out["llm_veredito"].astype(str).eq("ataque")   # True = LLM disse ataque

    # Falsos positivos da 1ª camada entre os borderline:
    fp_antes = (~real_bin & pred_bin)
    # Desses, quantos a LLM corrigiu para benigno:
    fp_corrigidos = (fp_antes & ~llm_bin).sum()
    # Ataques reais que a LLM rebaixou para benigno (efeito colateral ruim):
    fn_novos = (real_bin & pred_bin & ~llm_bin).sum()

    print("\n" + "=" * 60)
    print("IMPACTO DA 2ª CAMADA (sobre os casos borderline)")
    print("=" * 60)
    print(f"Falsos positivos da 1ª camada : {int(fp_antes.sum())}")
    print(f"  -> corrigidos pela LLM      : {int(fp_corrigidos)}")
    print(f"Ataques reais rebaixados (ruim): {int(fn_novos)}")
    if fp_antes.sum():
        print(f"Redução de FP nos borderline   : "
              f"{fp_corrigidos / fp_antes.sum():.1%}")
    print(f"\n[llm] resultado completo salvo em {CONFIG['OUT_CSV']}")
    print("[llm] inclui a justificativa textual de cada decisão -> explicabilidade.")


if __name__ == "__main__":
    main()
