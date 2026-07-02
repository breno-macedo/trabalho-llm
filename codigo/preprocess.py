#!/usr/bin/env python3
"""Limpeza e pre-processamento do CIC-IDS2017 (reproduz o pipeline do projeto)."""
import glob, os, json, warnings, numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

DATA = "/sessions/upbeat-gracious-mayer/mnt/uploads"
OUT  = "/sessions/upbeat-gracious-mayer/mnt/outputs/artifacts"
os.makedirs(OUT, exist_ok=True)
SEED = 42
np.random.seed(SEED)

LABEL_MAP = {
    "BENIGN": "Normal Traffic",
    "DoS Hulk": "DoS", "DoS GoldenEye": "DoS", "DoS slowloris": "DoS", "DoS Slowhttptest": "DoS",
    "DDoS": "DDoS",
    "PortScan": "Port Scanning",
    "FTP-Patator": "Brute Force", "SSH-Patator": "Brute Force",
    "Bot": "Bots",
}
def map_web(l):
    return "Web Attacks" if l.startswith("Web Attack") else None

TARGETS = {"Normal Traffic":3000, "Port Scanning":3000, "Web Attacks":2000,
           "Brute Force":3000, "DDoS":3000, "Bots":1800, "DoS":3000}

stats = {}

# ---- 1. Integracao dos 8 CSVs ----
frames = []
for f in sorted(glob.glob(os.path.join(DATA, "*.csv"))):
    df = pd.read_csv(f, low_memory=False)
    df.columns = [c.strip() for c in df.columns]
    for c in df.columns:
        if c != "Label":
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("float32")
    df["Label"] = df["Label"].astype(str).str.strip()
    frames.append(df)
data = pd.concat(frames, ignore_index=True)
del frames
stats["registros_originais"] = int(data.shape[0])
stats["atributos_originais"] = int(data.shape[1] - 1)
print("Original:", data.shape)

# ---- 2. Padronizacao dos rotulos ----
def to_class(l):
    if l in LABEL_MAP: return LABEL_MAP[l]
    return map_web(l)

data["Classe"] = data["Label"].map(to_class)
data = data.drop(columns=["Label"])
data = data[data["Classe"].notna()].copy()
stats["registros_apos_padronizacao"] = int(data.shape[0])

# ---- 3. Remocao de duplicados ----
antes = data.shape[0]
data = data.drop_duplicates().reset_index(drop=True)
stats["duplicados_removidos"] = int(antes - data.shape[0])
print("Duplicados removidos:", stats["duplicados_removidos"])

# ---- 4. Tratamento de infinitos e NaN ----
num_cols = [c for c in data.columns if c != "Classe"]
data[num_cols] = data[num_cols].replace([np.inf, -np.inf], np.nan)
nan_rows = int(data[num_cols].isna().any(axis=1).sum())
stats["linhas_com_nan_antes"] = nan_rows
data = data.dropna(subset=num_cols).reset_index(drop=True)
stats["nan_apos"] = int(data[num_cols].isna().sum().sum())
stats["infinitos_apos"] = int(np.isinf(data[num_cols].values).sum())
print("Linhas com NaN/inf removidas:", nan_rows)

# ---- 5. Selecao de atributos ----
variances = data[num_cols].var(numeric_only=True)
zero_var = variances[variances <= 1e-12].index.tolist()
keep = [c for c in num_cols if c not in zero_var]
dedup_cols, seen = [], {}
for c in keep:
    h = pd.util.hash_pandas_object(data[c], index=False).sum()
    if h in seen:
        continue
    seen[h] = c; dedup_cols.append(c)
feature_cols = dedup_cols
stats["atributos_removidos_varzero"] = zero_var
stats["n_atributos_finais"] = len(feature_cols)
print("Atributos finais:", len(feature_cols))

# ---- 6. Balanceamento ----
parts = []
for cls, n in TARGETS.items():
    sub = data[data["Classe"] == cls]
    n = min(n, len(sub))
    parts.append(sub.sample(n=n, random_state=SEED))
bal = pd.concat(parts).sample(frac=1, random_state=SEED).reset_index(drop=True)
stats["distribuicao_balanceada"] = bal["Classe"].value_counts().to_dict()
stats["base_final"] = int(bal.shape[0])
print("Base final:", bal.shape, stats["distribuicao_balanceada"])

X = bal[feature_cols].astype("float32").values
classes = sorted(bal["Classe"].unique())
cls2idx = {c:i for i,c in enumerate(classes)}
y = bal["Classe"].map(cls2idx).values

# ---- 7. Split 80/20 + StandardScaler ----
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)
scaler = StandardScaler().fit(X_tr)
X_tr = scaler.transform(X_tr).astype("float32")
X_te = scaler.transform(X_te).astype("float32")
stats["n_treino"] = int(len(y_tr)); stats["n_teste"] = int(len(y_te))

np.savez_compressed(os.path.join(OUT,"data.npz"), X_tr=X_tr, X_te=X_te, y_tr=y_tr, y_te=y_te)
import pickle
with open(os.path.join(OUT,"meta.pkl"),"wb") as fh:
    pickle.dump({"classes":classes, "feature_cols":feature_cols,
                 "scaler_mean":scaler.mean_, "scaler_scale":scaler.scale_}, fh)
bal[feature_cols+["Classe"]].to_parquet(os.path.join(OUT,"balanced_raw.parquet"))
with open(os.path.join(OUT,"prep_stats.json"),"w") as fh:
    json.dump(stats, fh, indent=2, ensure_ascii=False, default=str)
print(json.dumps(stats, indent=2, ensure_ascii=False, default=str))
print("OK preprocess")
