#!/usr/bin/env python3
"""Mede o efeito da 2a camada (LLM) comparando os vereditos com a verdade.
1a camada: LSTM (os 63 eventos sao alertas de ataque emitidos pela LSTM).
2a camada: o LLM decide manter (ATAQUE) ou reverter (FALSO_POSITIVO=legitimo).

Le de resultados/: review_truth.json, llm_verdicts.json, fp_gating.json.
Escreve resultados/llm_layer_results.json e imprime as metricas REAIS.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RES  = os.path.join(ROOT, "resultados")
ART  = os.path.join(ROOT, "artifacts")
def _find(name):
    for base in (ART, RES):
        p = os.path.join(base, name)
        if os.path.exists(p):
            return p
    return os.path.join(RES, name)

truth = json.load(open(_find("review_truth.json"), encoding="utf-8"))
verd  = json.load(open(_find("llm_verdicts.json"), encoding="utf-8"))
TOTAL_FP_LSTM = json.load(open(_find("fp_gating.json")))["baseline"]["fp"]  # 33

n = len(truth)
fp_real = sum(1 for v in truth.values() if v["is_fp"])
atk_real = n - fp_real

TP_rev = FP_rev = mantidos_ataque = 0
rev_corretas, rev_erradas = [], []
for i, t in truth.items():
    v = verd.get(str(i)) or verd.get(i)
    if v is None:
        raise KeyError(f"sem veredito para o alerta {i}")
    reverteu = str(v["veredito"]).upper() == "FALSO_POSITIVO"
    is_legit = t["is_fp"]
    if is_legit and reverteu:
        TP_rev += 1; rev_corretas.append(int(i))       # FP corretamente eliminado
    elif is_legit and not reverteu:
        pass                                            # FP nao detectado (permanece)
    elif (not is_legit) and reverteu:
        FP_rev += 1; rev_erradas.append(int(i))         # ATAQUE perdido (FN introduzido)
    else:
        mantidos_ataque += 1                            # ataque corretamente mantido

prec = TP_rev / (TP_rev + FP_rev) if (TP_rev + FP_rev) else 0.0
rec  = TP_rev / fp_real if fp_real else 0.0
spec = mantidos_ataque / atk_real if atk_real else 0.0

fp_antes = TOTAL_FP_LSTM
fp_depois = TOTAL_FP_LSTM - TP_rev
red_pct = 100 * TP_rev / TOTAL_FP_LSTM if TOTAL_FP_LSTM else 0.0

out = {
 "conjunto_revisado": {"total": n, "falsos_positivos_reais": fp_real, "ataques_reais": atk_real},
 "decisao_llm": {
   "FP_eliminados_corretamente": TP_rev,
   "FP_nao_detectados": fp_real - TP_rev,
   "ataques_mantidos_corretamente": mantidos_ataque,
   "ataques_revertidos_por_engano(FN)": FP_rev},
 "metricas_2a_camada": {
   "precisao_em_detectar_FP": round(prec, 4),
   "revocacao_em_detectar_FP": round(rec, 4),
   "especificidade_preserva_ataques": round(spec, 4)},
 "efeito_global_FP": {
   "FP_LSTM_antes": fp_antes, "FP_apos_LLM": fp_depois,
   "reducao_FP_pct": round(red_pct, 1),
   "ataques_perdidos": FP_rev},
 "exemplos_FP_eliminados": rev_corretas,
 "exemplos_FN_introduzidos": rev_erradas,
}
json.dump(out, open(os.path.join(RES, "llm_layer_results.json"), "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print(json.dumps(out, indent=2, ensure_ascii=False))
print("\nRESUMO: FP", fp_antes, "->", fp_depois, f"(-{red_pct:.1f}%) | "
      f"precisao {prec:.2f} | ataques preservados {mantidos_ataque}/{atk_real} | FN {FP_rev}")
