# Detecção de Tráfego Malicioso — CIC-IDS2017 (LSTM, Random Forest e camada LLM)

Resultados reais obtidos a partir dos 8 CSVs do CIC-IDS2017. Todo o código está em
`codigo/`, os resultados brutos (JSON) em `resultados/`, as figuras em
`artigo/figuras/` e o artigo em `artigo/main.tex`.

## 1. Limpeza e pré-processamento (`codigo/clean_file.py` + `aggregate.py`)
| Etapa | Valor |
|---|---|
| Registros originais | 2.830.743 |
| Após padronização de rótulos (7 classes) | 2.830.696 |
| Duplicados removidos | 331.200 |
| Linhas com NaN/infinito removidas | 2.867 |
| Atributos após seleção (var. zero + duplicadas + correlação) | **52** + Classe |
| Base balanceada final | **18.800** (treino 15.040 / teste 3.760) |

Balanceamento: 3.000 para Normal, DoS, DDoS, Port Scanning e Brute Force; 2.000 para
Web Attacks; 1.800 para Bots. Normalização com `StandardScaler`, split estratificado
80/20.

> Observação: o pré-processamento foi feito em duas etapas por restrição de memória
> (8 CSVs ≈ 1 GB). `clean_file.py` limpa cada arquivo e salva um cache local;
> `aggregate.py` agrega, deduplica globalmente, seleciona atributos, balanceia e divide.

## 2. Resultados dos modelos
| Modelo | Acurácia | Precisão macro | Revocação macro | F1 macro |
|---|---|---|---|---|
| LSTM (30 épocas) | 0,9832 | 0,9811 | 0,9839 | 0,9824 |
| **Random Forest (200 árvores)** | **0,9949** | **0,9942** | **0,9952** | **0,9947** |
| Bi-LSTM + Atenção (30 épocas) | 0,9561 | 0,9516 | 0,9585 | 0,9539 |

- A **LSTM** reproduz o resultado do projeto (F1 macro ≈ 0,98). A classe *Normal*
  tem a menor revocação (0,9450) → é onde se concentram os falsos positivos.
- O **Random Forest** supera a LSTM em todas as métricas e reduz os falsos positivos
  (revocação de *Normal* sobe para 0,9867).
- A **Bi-LSTM+Atenção** (atributos como sequência) converge mais devagar e, dentro
  do mesmo orçamento de 30 épocas, **não** supera a base — resultado honesto que
  indica que mais complexidade nem sempre compensa nesta representação tabular.

## 3. Parte 2 — melhorias e explicabilidade
- **SHAP** (`part2_explain.py`): atributos mais influentes — *Destination Port*,
  *Total Length of Fwd Packets*, *Fwd Packet Length Max*, *Init_Win_bytes_backward*,
  *Fwd Packet Length Mean*, *Average Packet Size*. Responde à crítica de "caixa-preta".
- **Redução de falsos positivos** (gating de confiança na saída da LSTM):
  **33 → 28 falsos positivos (−15,2%)**, mantendo a acurácia praticamente inalterada
  (0,9832 → 0,9827), **sem re-treinamento**.
## 3b. Camada LLM — a novidade (experimento medido)
A segunda camada é a contribuição central: um LLM revisa os alertas **incertos** da 1ª
camada, recebendo só a descrição textual do fluxo (top-10 atributos SHAP + valor vs.
faixa do tráfego legítimo + probabilidades do modelo), **sem o rótulo verdadeiro**, e
decide *ataque real* ou *falso positivo* com justificativa.

Conjunto de revisão: 63 alertas da LSTM (**33 falsos positivos + 30 ataques reais**).

| Métrica da 2ª camada (LLM) | Valor |
|---|---|
| Falsos positivos revertidos corretamente | **9 / 33** |
| Ataques preservados | **29 / 30** |
| Falsos negativos introduzidos | 1 |
| Precisão em detectar FP | **0,90** |
| Especificidade (preserva ataques) | 0,967 |
| **Falsos positivos da LSTM: antes → depois** | **33 → 24 (−27,3%)** |

Comparação direta: o LLM (−27,3%) reduz quase o **dobro** de falsos positivos do
*gating* estatístico (−15,2%) e ainda explica cada decisão. Código: `codigo/gen_review_set.py`
(gera os alertas), meus vereditos em `resultados/llm_verdicts.json`, correção em
`codigo/score_llm_layer.py` → `resultados/llm_layer_results.json`.

> Nota: aqui o LLM analista foi o próprio Claude, atuando como a 2ª camada exatamente
> como um LLM faria em produção (vê só o texto do alerta, não o rótulo). Em deploy,
> basta plugar a API de um LLM no mesmo *prompt*.

## 4. Como reexecutar
```bash
pip install scikit-learn tensorflow shap pandas matplotlib
python codigo/clean_file.py <cada CSV>      # gera cache /tmp/clean
python codigo/aggregate.py                  # gera artifacts/data.npz, meta.pkl
python codigo/train_lstm.py                 # LSTM
python codigo/train_rf.py                   # Random Forest
python codigo/part2_explain.py              # SHAP + gating de FP + camada LLM
python codigo/train_improved.py             # Bi-LSTM+Atenção (rode até concluir 30 épocas)
python codigo/make_figures.py               # figuras
```

