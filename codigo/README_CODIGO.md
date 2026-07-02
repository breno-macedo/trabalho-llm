# Guia de execução do código

Os scripts compartilham uma pasta `artifacts/` (criada automaticamente): cada etapa lê
as saídas da etapa anterior. **Siga a ordem abaixo.**

## 0. Dependências (uma vez)
```bash
pip install pandas numpy scikit-learn tensorflow shap matplotlib
```

## ⚠️ Ajuste de caminhos (importante)
Os scripts foram rodados num ambiente Linux e têm caminhos fixos no topo, por exemplo:
```python
DATA = "/sessions/.../uploads"     # onde estão os 8 CSVs
OUT  = "/sessions/.../artifacts"   # onde salvar os resultados
```
No seu computador, edite essas duas variáveis no topo de **`clean_file.py`** e
**`aggregate.py`** (e o `A=...` nos demais) para apontar para a pasta dos CSVs e para
uma pasta `artifacts/` sua. (Ou me peça para deixar os caminhos automáticos.)

---

## Etapa 1 — Limpeza e pré-processamento → gera a base 52 atributos
Use a versão em **dois passos** (foi a que gerou os resultados do artigo; é segura em
memória, porque os 8 CSVs somam ~1 GB):

1. `python clean_file.py <CSV1> <CSV2> ...` — limpa cada CSV (padroniza rótulos, trata
   tipos) e salva um cache `.pkl`. Pode passar todos de uma vez ou em grupos.
2. `python aggregate.py` — junta tudo, remove duplicados, trata NaN/inf, **seleciona os
   52 atributos** (variância zero + duplicadas + correlação), balanceia, faz o split
   80/20 e normaliza. Gera: `data.npz`, `meta.pkl`, `balanced_raw.pkl`, `prep_stats.json`.

> `preprocess.py` é uma versão alternativa "tudo-em-um" (lê os 8 CSVs de uma vez). É mais
> simples, mas pede mais RAM **e produz 61 atributos** (não tem o corte por correlação).
> Para reproduzir o artigo (52 atributos), use o caminho `clean_file.py` + `aggregate.py`.

## Etapa 2 — Modelos da 1ª camada
3. `python train_lstm.py` — treina a LSTM (30 épocas). Gera `lstm_results.json`,
   `lstm_model.keras`, `lstm_prob.npy`.
4. `python train_rf.py` — treina o Random Forest. Gera `rf_results.json`, `rf_model.pkl`.

## Etapa 3 — Explicabilidade, gating e modelo melhorado
5. `python part2_explain.py` — SHAP (importância dos atributos) + gating de confiança
   (redução de FP) + descrição textual base. Gera `shap_results.json`, `fp_gating.json`,
   `llm_layer.json`.
6. `python train_improved.py` — Bi-LSTM + atenção (estudo de arquitetura). Gera
   `improved_results.json`. *No seu PC roda direto até as 30 épocas (~2 min); o script
   tem checkpoint, então se parar no meio é só rodar de novo que ele continua.*

## Etapa 4 — Experimento da camada LLM (a contribuição central)
7. `python gen_review_set.py` — monta os 63 alertas a revisar (33 FP + 30 ataques) e
   gera a descrição textual de cada um. Saídas: `review_events.md` (o que o LLM lê),
   `review_events.json` e `review_truth.json` (gabarito, **separado**).
8. **Revisão pelo LLM** — o LLM lê `review_events.md` e produz um veredito por alerta em
   `llm_verdicts.json`. No nosso caso fui eu (Claude) que fiz isso; o arquivo já está em
   `../resultados/llm_verdicts.json`. Em produção, basta chamar a API de um LLM com o
   mesmo prompt e salvar nesse formato.
9. `python score_llm_layer.py` — compara os vereditos com o gabarito e calcula o efeito
   (FP 33→24, precisão 0,90 etc.). Gera `llm_layer_results.json`.

## Etapa 5 — Figuras do artigo
10. `python make_figures.py` — matrizes de confusão, curvas de perda, SHAP, comparação.
11. `python make_figures_llm.py` — FP por camada, matriz de decisão do LLM, diagrama da
    arquitetura.

---

## Resumo da ordem
```
clean_file.py → aggregate.py → train_lstm.py → train_rf.py →
part2_explain.py → train_improved.py → gen_review_set.py →
(LLM gera llm_verdicts.json) → score_llm_layer.py →
make_figures.py → make_figures_llm.py
```
As figuras vão para `artifacts/figs/`; copie-as para `artigo/figuras/` e recompile o
`main.tex` no Overleaf.
