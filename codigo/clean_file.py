#!/usr/bin/env python3
"""Limpa um ou mais CSVs e salva em artifacts/clean/ (cache local)."""
import sys, os, glob, numpy as np, pandas as pd
_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA=os.environ.get("DADOS_DIR", os.path.join(_ROOT,"dados"))
OUTD=os.path.join(_ROOT,"artifacts","clean"); os.makedirs(OUTD, exist_ok=True)
LABEL_MAP={"BENIGN":"Normal Traffic","DoS Hulk":"DoS","DoS GoldenEye":"DoS",
 "DoS slowloris":"DoS","DoS Slowhttptest":"DoS","DDoS":"DDoS","PortScan":"Port Scanning",
 "FTP-Patator":"Brute Force","SSH-Patator":"Brute Force","Bot":"Bots"}
def to_class(l):
    if l in LABEL_MAP: return LABEL_MAP[l]
    return "Web Attacks" if l.startswith("Web Attack") else None
for name in sys.argv[1:]:
    f=os.path.join(DATA,name)
    df=pd.read_csv(f, low_memory=False)
    df.columns=[c.strip() for c in df.columns]
    df["Label"]=df["Label"].astype(str).str.strip()
    df["Classe"]=df["Label"].map(to_class)
    df=df.drop(columns=["Label"])
    df=df[df["Classe"].notna()].copy()
    num=[c for c in df.columns if c!="Classe"]
    for c in num: df[c]=pd.to_numeric(df[c],errors="coerce").astype("float32")
    out=os.path.join(OUTD, name.replace(".csv",".pkl"))
    df.to_pickle(out)
    print(f"{name}: {df.shape} -> {out}")
print("OK")
