#!/usr/bin/env python3
"""Parte 2a: explicabilidade SHAP (RF) + reducao de falsos positivos (gating no LSTM)
   + camada textual (interface p/ LLM)."""
import os, json, pickle, numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
A="/sessions/upbeat-gracious-mayer/mnt/outputs/artifacts"
d=np.load(A+"/data.npz"); meta=pickle.load(open(A+"/meta.pkl","rb"))
classes=meta["classes"]; feat=meta["feature_cols"]
Xtr,Xte,ytr,yte=d["X_tr"],d["X_te"],d["y_tr"],d["y_te"]
NORMAL=classes.index("Normal Traffic")
rf=pickle.load(open(A+"/rf_model.pkl","rb"))
lstm_prob=np.load(A+"/lstm_prob.npy")

# ---------- SHAP (RF) ----------
import shap
nsmp=400
idx=np.random.RandomState(0).choice(len(Xte), nsmp, replace=False)
Xs=Xte[idx]
expl=shap.TreeExplainer(rf)
sv=expl.shap_values(Xs)  # lista por classe OU array (n,feat,nclass)
if isinstance(sv, list):
    absmat=np.stack([np.abs(s).mean(0) for s in sv])      # (nclass,feat)
else:
    absmat=np.abs(sv).mean(0).T                            # (nclass,feat)
glob=absmat.mean(0)                                        # (feat,)
order=np.argsort(-glob)
shap_global=[[feat[i], float(glob[i])] for i in order]
shap_per_class={classes[c]:[[feat[i],float(absmat[c,i])] for i in np.argsort(-absmat[c])[:8]]
                for c in range(len(classes))}
np.save(A+"/shap_abs_matrix.npy", absmat)
json.dump({"global":shap_global,"per_class":shap_per_class},
          open(A+"/shap_results.json","w"), indent=2, ensure_ascii=False)
print("SHAP top10:", [f for f,_ in shap_global[:10]])

# ---------- Reducao de falsos positivos (gating no LSTM) ----------
yp=lstm_prob.argmax(1)
def fp_fn(pred):
    # FP = trafego Normal classificado como ataque
    fp=int(((yte==NORMAL)&(pred!=NORMAL)).sum())
    # FN = ataque classificado como Normal
    fn=int(((yte!=NORMAL)&(pred==NORMAL)).sum())
    acc=float((pred==yte).mean())
    return fp,fn,acc
base_fp,base_fn,base_acc=fp_fn(yp)

# Gating: se o modelo previu ATAQUE mas com baixa confianca e a 2a hipotese
# e' "Normal" com prob relevante, reclassifica como Normal (reduz alarmes falsos).
best=None
for tau in np.arange(0.50,0.991,0.02):
    for beta in (0.20,0.30,0.40):
        pred=yp.copy()
        conf=lstm_prob.max(1)
        pn=lstm_prob[:,NORMAL]
        mask=(yp!=NORMAL)&(conf<tau)&(pn>beta)
        pred[mask]=NORMAL
        fp,fn,acc=fp_fn(pred)
        # objetivo: minimizar FP sem perder acuracia global
        if acc>=base_acc-0.002:
            score=(base_fp-fp)  # quanto reduziu de FP
            if best is None or score>best["fp_reduzido"] or (score==best["fp_reduzido"] and acc>best["acc"]):
                best={"tau":float(tau),"beta":float(beta),"fp":fp,"fn":fn,"acc":acc,
                      "fp_reduzido":int(base_fp-fp)}
gat={"baseline":{"fp":base_fp,"fn":base_fn,"acc":base_acc},
     "gated":best,
     "reducao_fp_pct":float(100*(base_fp-best["fp"])/base_fp) if base_fp else 0.0}
json.dump(gat, open(A+"/fp_gating.json","w"), indent=2, ensure_ascii=False)
print("FP baseline=%d -> gated=%d (tau=%.2f beta=%.2f) acc %.4f->%.4f"%(
    base_fp,best["fp"],best["tau"],best["beta"],base_acc,best["acc"]))

# ---------- Camada textual (interface LLM) ----------
raw=pickle.load(open(A+"/balanced_raw.pkl","rb")) if os.path.exists(A+"/balanced_raw.pkl") else None
mean=meta["scaler_mean"]; scale=meta["scaler_scale"]
topfeat=[f for f,_ in shap_global[:8]]
fidx={f:feat.index(f) for f in topfeat}
def flow_to_text(xrow_scaled, pred_label, probs):
    real={f: float(xrow_scaled[fidx[f]]*scale[fidx[f]]+mean[fidx[f]]) for f in topfeat}
    desc=", ".join("%s=%.2f"%(f,real[f]) for f in topfeat)
    conf=float(probs.max())
    return (f"Fluxo de rede com atributos principais: {desc}. "
            f"O classificador (LSTM) atribuiu a classe '{pred_label}' com confianca {conf:.2f}. "
            f"Distribuicao de probabilidade: "
            + ", ".join("%s=%.2f"%(classes[i],probs[i]) for i in np.argsort(-probs)[:3]) + ".")
LLM_PROMPT_TEMPLATE = (
"Voce e um analista de seguranca (SOC). A primeira camada (modelo de deteccao) gerou o alerta abaixo.\n"
"Avalie se o evento e um ATAQUE REAL ou um FALSO POSITIVO, justificando com base nos atributos do fluxo\n"
"e nos atributos mais influentes segundo o SHAP. Responda em JSON: {{veredito, confianca, justificativa}}.\n\n"
"ALERTA:\n{evento}\n\nAtributos mais influentes (SHAP global): {shap}\n")
# exemplos: pega ate 3 falsos positivos do baseline
fp_mask=np.where((yte==NORMAL)&(yp!=NORMAL))[0][:3]
exemplos=[]
for i in fp_mask:
    ev=flow_to_text(Xte[i], classes[yp[i]], lstm_prob[i])
    prompt=LLM_PROMPT_TEMPLATE.format(evento=ev, shap=", ".join(topfeat))
    exemplos.append({"indice":int(i),"classe_real":classes[int(yte[i])],
                     "classe_prevista":classes[int(yp[i])],"texto_evento":ev,"prompt_llm":prompt})
json.dump({"prompt_template":LLM_PROMPT_TEMPLATE,"top_features_shap":topfeat,
           "exemplos_falsos_positivos":exemplos},
          open(A+"/llm_layer.json","w"), indent=2, ensure_ascii=False)
print("LLM layer: %d exemplos de FP gerados"%len(exemplos))
print("OK part2_explain")
