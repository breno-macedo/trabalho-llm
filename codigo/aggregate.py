#!/usr/bin/env python3
"""Agrega pickles limpos (memoria-segura, dois passes)."""
import glob, os, json, time, pickle, numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
t0=time.time()
_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEAN=os.path.join(_ROOT,"artifacts","clean"); OUT=os.path.join(_ROOT,"artifacts")
os.makedirs(OUT, exist_ok=True); SEED=42; rng=np.random.RandomState(SEED)
TARGETS={"Normal Traffic":3000,"Port Scanning":3000,"Web Attacks":2000,
 "Brute Force":3000,"DDoS":3000,"Bots":1800,"DoS":3000}
files=sorted(glob.glob(CLEAN+"/*.pkl"))
cols=[c for c in pd.read_pickle(files[0]).columns]
num=[c for c in cols if c!="Classe"]
stats={"registros_originais":2830743,"atributos_originais":len(num)}

# ---------- PASS 1: stats globais ----------
hashes=set(); total=0; dup=0
gmin=pd.Series(np.inf,index=num); gmax=pd.Series(-np.inf,index=num)
nan_rows=0; classcount={}
for f in files:
    df=pd.read_pickle(f)
    total+=len(df)
    h=pd.util.hash_pandas_object(df, index=False).values
    before=len(hashes); hashes.update(h.tolist())
    dup+=len(df)-(len(hashes)-before)
    fin=df[num].replace([np.inf,-np.inf],np.nan)
    gmin=np.minimum(gmin, fin.min()); gmax=np.maximum(gmax, fin.max())
    nan_rows+=int((fin.isna().any(axis=1) | np.isinf(df[num].values).any(axis=1)).sum())
    for k,v in df["Classe"].value_counts().items(): classcount[k]=classcount.get(k,0)+int(v)
    del df, h
stats["registros_apos_padronizacao"]=total
stats["duplicados_removidos"]=int(dup)
stats["linhas_com_nan_antes"]=int(nan_rows)
stats["distribuicao_original_classes"]=classcount
zero_var=[c for c in num if (pd.isna(gmin[c]) or gmin[c]==gmax[c])]
print("PASS1 %.1fs total=%d dup=%d nan=%d zerovar=%d"%(time.time()-t0,total,dup,nan_rows,len(zero_var)))
del hashes

# ---------- PASS 2: coleta subset p/ amostra ----------
keepcols=[c for c in num if c not in zero_var]
buf={c:[] for c in TARGETS}
for f in files:
    df=pd.read_pickle(f)
    df[num]=df[num].replace([np.inf,-np.inf],np.nan)
    df=df.dropna(subset=num)
    for cls in TARGETS:
        sub=df[df["Classe"]==cls]
        if cls=="Normal Traffic" and len(sub)>12000:
            sub=sub.sample(n=12000, random_state=SEED)  # cap benigno (so precisamos 3000)
        if len(sub): buf[cls].append(sub[keepcols+["Classe"]])
    del df
data=pd.concat([pd.concat(v) for v in buf.values() if v], ignore_index=True)
del buf
data=data.drop_duplicates().reset_index(drop=True)
stats["registros_limpos_aprox"]=int(data.shape[0])
# remove colunas duplicadas (conteudo identico) no subset
seen={}; feat=[]
for c in keepcols:
    hh=pd.util.hash_pandas_object(data[c], index=False).sum()
    if hh in seen: continue
    seen[hh]=c; feat.append(c)
stats["atributos_removidos_varzero"]=zero_var
stats["atributos_duplicados_removidos"]=[c for c in keepcols if c not in feat]
stats["n_atributos_finais"]=len(feat)
stats["nan_apos"]=0; stats["infinitos_apos"]=0
print("PASS2 %.1fs subset=%s feat=%d"%(time.time()-t0,data.shape,len(feat)))

# ---------- balanceamento ----------
parts=[]
for cls,n in TARGETS.items():
    sub=data[data["Classe"]==cls]; n=min(n,len(sub))
    parts.append(sub.sample(n=n, random_state=SEED))
bal=pd.concat(parts).sample(frac=1, random_state=SEED).reset_index(drop=True)
stats["distribuicao_balanceada"]=bal["Classe"].value_counts().to_dict()
stats["base_final"]=int(bal.shape[0])

X=bal[feat].astype("float32").values
classes=sorted(bal["Classe"].unique()); c2i={c:i for i,c in enumerate(classes)}
y=bal["Classe"].map(c2i).values
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=SEED,stratify=y)
sc=StandardScaler().fit(Xtr)
Xtr=sc.transform(Xtr).astype("float32"); Xte=sc.transform(Xte).astype("float32")
stats["n_treino"]=int(len(ytr)); stats["n_teste"]=int(len(yte))
np.savez_compressed(OUT+"/data.npz", X_tr=Xtr, X_te=Xte, y_tr=ytr, y_te=yte)
with open(OUT+"/meta.pkl","wb") as fh:
    pickle.dump({"classes":classes,"feature_cols":feat,
      "scaler_mean":sc.mean_,"scaler_scale":sc.scale_}, fh)
bal[feat+["Classe"]].to_pickle(OUT+"/balanced_raw.pkl")
with open(OUT+"/prep_stats.json","w") as fh:
    json.dump(stats, fh, indent=2, ensure_ascii=False, default=str)
print("TOTAL %.1fs"%(time.time()-t0))
print(json.dumps({k:v for k,v in stats.items() if not k.startswith("atributos_remov")}, indent=2, ensure_ascii=False, default=str))
print("OK aggregate")
