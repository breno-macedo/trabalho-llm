#!/usr/bin/env python3
import os, json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
A="/sessions/upbeat-gracious-mayer/mnt/outputs/artifacts"; G=A+"/figs"; os.makedirs(G, exist_ok=True)
plt.rcParams.update({"figure.dpi":130,"font.size":10})
def J(f): return json.load(open(A+"/"+f))
lstm=J("lstm_results.json"); rf=J("rf_results.json"); imp=J("improved_results.json")
shp=J("shap_results.json"); gat=J("fp_gating.json"); classes=lstm["classes"]
short={"Normal Traffic":"Normal","Port Scanning":"PortScan","Brute Force":"BruteF",
       "Web Attacks":"WebAtk","DDoS":"DDoS","DoS":"DoS","Bots":"Bots"}
lab=[short[c] for c in classes]

def cm_plot(cm, title, fn, cmap="Blues"):
    cm=np.array(cm); fig,ax=plt.subplots(figsize=(6,5))
    im=ax.imshow(cm,cmap=cmap)
    ax.set_xticks(range(len(lab))); ax.set_yticks(range(len(lab)))
    ax.set_xticklabels(lab,rotation=45,ha="right"); ax.set_yticklabels(lab)
    th=cm.max()/2
    for i in range(len(lab)):
        for j in range(len(lab)):
            ax.text(j,i,cm[i,j],ha="center",va="center",
                    color="white" if cm[i,j]>th else "black",fontsize=8)
    ax.set_xlabel("Classe prevista"); ax.set_ylabel("Classe real"); ax.set_title(title)
    fig.colorbar(im,fraction=0.046,pad=0.04); fig.tight_layout(); fig.savefig(G+"/"+fn); plt.close()
cm_plot(lstm["confusion_matrix"],"Matriz de Confusão — LSTM (CIC-IDS2017)","cm_lstm.png")
cm_plot(rf["confusion_matrix"],"Matriz de Confusão — Random Forest","cm_rf.png","Greens")
cm_plot(imp["confusion_matrix"],"Matriz de Confusão — Bi-LSTM + Atenção","cm_improved.png","Purples")

# curva de convergencia LSTM
fig,ax=plt.subplots(figsize=(6.5,4))
ax.plot(lstm["loss_curve"],color="#e8590c",label="Perda treino")
ax.plot(lstm["val_loss"],color="#1c7ed6",label="Perda validação")
ax.set_xlabel("Época"); ax.set_ylabel("Perda (Loss)")
ax.set_title("Curva de Convergência — LSTM"); ax.legend(); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(G+"/loss_lstm.png"); plt.close()

# curva improved
fig,ax=plt.subplots(figsize=(6.5,4))
ax.plot(imp["loss_curve"],color="#7048e8",label="Perda treino")
ax.plot(imp["val_loss"],color="#1c7ed6",label="Perda validação")
ax.set_xlabel("Época"); ax.set_ylabel("Perda (Loss)")
ax.set_title("Curva de Convergência — Bi-LSTM + Atenção"); ax.legend(); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(G+"/loss_improved.png"); plt.close()

# comparacao de modelos
models=["LSTM","Random Forest","Bi-LSTM+Attn"]
accs=[lstm["accuracy"],rf["accuracy"],imp["accuracy"]]
f1s=[lstm["macro_f1"],rf["macro_f1"],imp["macro_f1"]]
x=np.arange(3); w=0.38
fig,ax=plt.subplots(figsize=(6.5,4))
ax.bar(x-w/2,accs,w,label="Acurácia",color="#1c7ed6")
ax.bar(x+w/2,f1s,w,label="Macro F1",color="#f08c00")
for i,(a,f) in enumerate(zip(accs,f1s)):
    ax.text(i-w/2,a+.005,"%.3f"%a,ha="center",fontsize=8)
    ax.text(i+w/2,f+.005,"%.3f"%f,ha="center",fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(models); ax.set_ylim(0.8,1.02)
ax.set_title("Comparação de Modelos"); ax.legend(); ax.grid(axis="y",alpha=.3)
fig.tight_layout(); fig.savefig(G+"/model_compare.png"); plt.close()

# SHAP global top15
top=shp["global"][:15][::-1]
names=[t[0] for t in top]; vals=[t[1] for t in top]
fig,ax=plt.subplots(figsize=(7,5))
ax.barh(range(len(names)),vals,color="#2f9e44")
ax.set_yticks(range(len(names))); ax.set_yticklabels(names,fontsize=8)
ax.set_xlabel("Importância média |SHAP|")
ax.set_title("Explicabilidade — Importância Global (SHAP, Random Forest)")
fig.tight_layout(); fig.savefig(G+"/shap_global.png"); plt.close()

# reducao de FP
b=gat["baseline"]; g=gat["gated"]
fig,ax=plt.subplots(figsize=(5.5,4))
ax.bar(["LSTM base","LSTM + gating"],[b["fp"],g["fp"]],color=["#e03131","#2f9e44"])
ax.text(0,b["fp"]+0.5,str(b["fp"]),ha="center"); ax.text(1,g["fp"]+0.5,str(g["fp"]),ha="center")
ax.set_ylabel("Falsos positivos (Normal→Ataque)")
ax.set_title("Redução de Falsos Positivos (-%.1f%%)"%gat["reducao_fp_pct"])
fig.tight_layout(); fig.savefig(G+"/fp_reduction.png"); plt.close()
print("figs:", sorted(os.listdir(G)))
print("OK figures")
