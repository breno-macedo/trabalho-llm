# Detecção de Tráfego Malicioso com LSTM/Random Forest e Segunda Camada por LLM

Código e resultados do trabalho de detecção de tráfego malicioso em redes internas sobre o
**CIC-IDS2017**, com uma arquitetura em duas camadas:

1. **Primeira camada** — classificação do tráfego com **LSTM** e **Random Forest** (linha de base).
2. **Segunda camada (contribuição)** — um **LLM (Claude)** faz a triagem dos alertas incertos,
   decidindo se são ataque real ou falso positivo e produzindo justificativas em linguagem natural,
   reduzindo os falsos positivos da primeira camada.

## Resultados principais

- LSTM: acurácia **98,32%** · Random Forest: **99,49%**.
- Baseline estatístico (*gating* por confiança): falsos positivos 33 → 28 (**−15,2%**).
- Segunda camada por LLM: falsos positivos 33 → 24 (**−27,3%**), precisão **90%**, preservando
  **29 de 30** ataques reais.

## Estrutura

```
codigo/                 scripts Python (pipeline completo)
  preprocess.py           limpeza e pré-processamento
  clean_file.py           utilitário de limpeza
  train_lstm.py           treino da LSTM
  train_rf.py             treino do Random Forest
  train_improved.py       Bi-LSTM + atenção (estudo)
  part2_explain.py        SHAP + gating por confiança (busca em grade de τ, β)
  gen_review_set.py       gera os 63 alertas de revisão (descrição textual)
  camada_llm_real.py      2ª camada: chama um LLM real (Claude/OpenAI)
  score_llm_layer.py      métricas da 2ª camada vs. gabarito
  make_figures.py         figuras da 1ª camada
  make_figures_llm.py     figuras da 2ª camada
  aggregate.py            consolidação de resultados
resultados/             saídas em JSON + conjunto de revisão (review_events / review_truth)
pipeline_deteccao.py    pipeline da 1ª camada (entrada da 2ª camada)
camada_llm.py           versão inicial da 2ª camada (mock + exemplo de API)
```

## Conjunto de dados

CIC-IDS2017 — *Network Intrusion Dataset* (Kaggle):
https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

O dataset **não** está versionado aqui (é grande e público); baixe-o do link acima.

## Dependências

```bash
pip install pandas numpy scikit-learn tensorflow shap
pip install anthropic        # para a 2ª camada com Claude (ou: pip install openai)
```

## Como executar (visão geral)

```bash
# 1) pré-processamento
python codigo/preprocess.py
# 2) primeira camada
python codigo/train_lstm.py
python codigo/train_rf.py
# 3) explicabilidade + baseline de gating
python codigo/part2_explain.py
# 4) conjunto de revisão para a 2ª camada
python codigo/gen_review_set.py
# 5) segunda camada com LLM real (Claude)
export ANTHROPIC_API_KEY=sk-ant-...
python codigo/camada_llm_real.py
# 6) métricas da 2ª camada
python codigo/score_llm_layer.py
```

## Segunda camada (LLM)

`camada_llm_real.py` envia cada alerta (descrito em texto: atributos SHAP com o valor real
comparado à faixa do tráfego legítimo — percentis 10–90 da classe *Normal* —, a classe prevista
e a distribuição de probabilidade) a um modelo **Claude**, com temperatura 0. O **rótulo verdadeiro
nunca entra no prompt**: fica em `resultados/review_truth.json` e é usado apenas na correção por
`score_llm_layer.py`.

## Nota sobre caminhos

Alguns scripts (`preprocess.py`, `gen_review_set.py`, `part2_explain.py`, `train_*.py`,
`make_figures*.py`) contêm caminhos absolutos de uma sessão de desenvolvimento anterior
(`/sessions/.../artifacts`). Para reproduzir do zero, ajuste esses caminhos para a sua máquina.
Os scripts `camada_llm_real.py` e `score_llm_layer.py` já usam caminhos relativos à pasta
`resultados/`.
