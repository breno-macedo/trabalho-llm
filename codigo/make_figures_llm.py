#!/usr/bin/env python3
import json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
A="/sessions/upbeat-gracious-mayer/mnt/outputs/artifacts"; G=A+"/figs"
plt.rcParams.update({"figure.dpi":130,"font.size":10})
r=json.load(open(A+"/llm_layer_results.json"))
g=json.load(open(A+"/fp_gating.json"))

# 1) comparacao de FP: LSTM base / +gating / +LLM
base=g["baseline"]["fp"]; gat=g["gated"]["fp"]; llm=r["efeito_global_FP"]["FP_apos_LLM"]
fig,ax=plt.subplots(figsize=(6,4))
bars=ax.bar(["LSTM\n(base)","+ Gating\nde confianca","+ Camada LLM\n(2a camada)"],
            [base,gat,llm], color=["#e03131","#f59f00","#2f9e44"])
for b,v in zip(bars,[base,gat,llm]): ax.text(b.get_x()+b.get_width()/2,v+0.4,str(v),ha="center",fontweight="bold")
ax.set_ylabel("Falsos positivos (Normal -> Ataque)")
ax.set_title("Reducao de Falsos Positivos por Camada")
ax.set_ylim(0,base+5); fig.tight_layout(); fig.savefig(G+"/fp_layers.png"); plt.close()

# 2) matriz 2x2 da decisao do LLM
d=r["decisao_llm"]
M=np.array([[d["FP_eliminados_corretamente"], d["FP_nao_detectados"]],
            [d["ataques_revertidos_por_engano(FN)"], d["ataques_mantidos_corretamente"]]])
fig,ax=plt.subplots(figsize=(5.2,4.4))
im=ax.imshow(M,cmap="Blues")
ax.set_xticks([0,1]); ax.set_yticks([0,1])
ax.set_xticklabels(["LLM: Falso Positivo\n(reverte)","LLM: Ataque\n(mantem)"])
ax.set_yticklabels(["Verdade:\nLegitimo","Verdade:\nAtaque"])
for i in range(2):
    for j in range(2):
        ax.text(j,i,M[i,j],ha="center",va="center",fontsize=14,
                color="white" if M[i,j]>M.max()/2 else "black",fontweight="bold")
ax.set_title("Decisao da 2a Camada (LLM) sobre 63 alertas")
fig.tight_layout(); fig.savefig(G+"/llm_confusion.png"); plt.close()

# 3) diagrama da arquitetura em duas camadas
fig,ax=plt.subplots(figsize=(8,3.2)); ax.axis("off")
def box(x,y,w,h,txt,c):
    ax.add_patch(mp.FancyBboxBox if False else mp.FancyBboxPatch((x,y),w,h,
        boxstyle="round,pad=0.02",fc=c,ec="#333"));
    ax.text(x+w/2,y+h/2,txt,ha="center",va="center",fontsize=9)
def arrow(x1,y1,x2,y2,t=""):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="->",lw=1.6,color="#333"))
    if t: ax.text((x1+x2)/2,(y1+y2)/2+0.04,t,ha="center",fontsize=8)
box(0.00,0.35,0.16,0.3,"Trafego\nde rede\n(fluxos)","#e7f5ff")
box(0.21,0.35,0.18,0.3,"1a camada\nLSTM\n(deteccao)","#d0ebff")
box(0.45,0.62,0.20,0.26,"Alerta confiavel\n-> SOC","#ebfbee")
box(0.45,0.08,0.20,0.26,"Alerta incerto\n(baixa confianca)","#fff3bf")
box(0.70,0.08,0.27,0.26,"2a camada: LLM\nevento->texto + SHAP\nveredito + justificativa","#d3f9d8")
arrow(0.16,0.5,0.21,0.5)
arrow(0.39,0.5,0.45,0.72,"conf. alta")
arrow(0.39,0.5,0.45,0.24,"conf. baixa")
arrow(0.65,0.21,0.70,0.21)
arrow(0.835,0.34,0.70,0.62,"reclassifica /\nexplica")
ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.set_title("Arquitetura de deteccao em duas camadas (LSTM + LLM)")
fig.tight_layout(); fig.savefig(G+"/arquitetura.png"); plt.close()
print("OK make_figures_llm")
