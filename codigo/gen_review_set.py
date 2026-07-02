#!/usr/bin/env python3
"""Gera o conjunto de alertas a ser revisado pela 2a camada (LLM).
Cada alerta vira uma descricao textual rica (valores reais vs. faixas do trafego
normal). O rotulo verdadeiro fica em arquivo separado (so para a correcao)."""
import numpy as np, pickle, json, os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"artifacts"); os.makedirs(A,exist_ok=True)
d=np.load(A+"/data.npz"); meta=pickle.load(open(A+"/meta.pkl","rb"))
classes=meta["classes"]; feat=meta["feature_cols"]
mean=np.array(meta["scaler_mean"]); scale=np.array(meta["scaler_scale"])
NORMAL=classes.index("Normal Traffic")
Xtr,ytr=d["X_tr"],d["y_tr"]; Xte,yte=d["X_te"],d["y_te"]
prob=np.load(A+"/lstm_prob.npy"); yp=prob.argmax(1); conf=prob.max(1)
shp=json.load(open(A+"/shap_results.json"))
TOPF=[f for f,_ in shp["global"][:10]]
fidx=[feat.index(f) for f in TOPF]

# de-normaliza
def real(Xrow): return Xrow*scale+mean
# faixas do trafego NORMAL (treino) p/ os atributos escolhidos
norm_raw=real(Xtr[ytr==NORMAL])
ref={}
for f,j in zip(TOPF,fidx):
    col=norm_raw[:,j]
    ref[f]=(float(np.median(col)), float(np.percentile(col,10)), float(np.percentile(col,90)))

rng=np.random.RandomState(7)
alert=(yp!=NORMAL)
fp_idx=np.where(alert&(yte==NORMAL))[0]                 # todos os 33 FP
tp_pool=np.where(alert&(yte!=NORMAL))[0]
# amostra estratificada de ataques verdadeiros (4-5 por classe de ataque)
tp_idx=[]
for c in range(len(classes)):
    if c==NORMAL: continue
    pool=tp_pool[yte[tp_pool]==c]
    if len(pool): tp_idx+=list(rng.choice(pool, min(5,len(pool)), replace=False))
tp_idx=np.array(tp_idx)
review=np.concatenate([fp_idx, tp_idx])
rng.shuffle(review)

events=[]; truth={}
for k,i in enumerate(review):
    rv=real(Xte[i]);
    feats=[]
    for f,j in zip(TOPF,fidx):
        v=float(rv[j]); med,p10,p90=ref[f]
        flag="dentro do normal" if p10<=v<=p90 else ("ACIMA do normal" if v>p90 else "ABAIXO do normal")
        feats.append({"atributo":f,"valor":round(v,2),
                      "normal_mediana":round(med,2),"normal_p10":round(p10,2),
                      "normal_p90":round(p90,2),"situacao":flag})
    top3=np.argsort(-prob[i])[:3]
    events.append({"id":int(k),
        "classe_prevista_camada1":classes[int(yp[i])],
        "confianca_camada1":round(float(conf[i]),3),
        "distribuicao_prob":{classes[t]:round(float(prob[i][t]),3) for t in top3},
        "atributos":feats})
    truth[int(k)]={"true":classes[int(yte[i])],"pred":classes[int(yp[i])],
                   "is_fp":bool(yte[i]==NORMAL)}

json.dump({"top_features":TOPF,"referencia_normal":ref,"eventos":events},
          open(A+"/review_events.json","w"), indent=2, ensure_ascii=False)
json.dump(truth, open(A+"/review_truth.json","w"), indent=2, ensure_ascii=False)

# versao legivel (SEM rotulo) para a revisao do LLM
with open(A+"/review_events.md","w") as fh:
    fh.write("# Alertas para triagem da 2a camada (LLM)\n")
    fh.write("Faixa normal = [p10, p90] dos fluxos LEGITIMOS (treino). ")
    fh.write("Decida: ATAQUE REAL ou FALSO POSITIVO (trafego legitimo).\n\n")
    for e in events:
        fh.write(f"## Alerta {e['id']}\n")
        fh.write(f"- 1a camada previu: **{e['classe_prevista_camada1']}** "
                 f"(confianca {e['confianca_camada1']}); prob: {e['distribuicao_prob']}\n")
        for a in e["atributos"]:
            fh.write(f"  - {a['atributo']}: {a['valor']} "
                     f"(normal ~{a['normal_mediana']}, faixa {a['normal_p10']}..{a['normal_p90']}) -> {a['situacao']}\n")
        fh.write("\n")
print("review set:",len(review),"eventos | FP:",len(fp_idx),"| TP amostrados:",len(tp_idx))
print("top features:",TOPF)
print("OK gen_review_set")
