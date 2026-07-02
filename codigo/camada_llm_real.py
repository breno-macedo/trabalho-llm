#!/usr/bin/env python3
"""
2a CAMADA — TRIAGEM POR LLM REAL (substitui a heuristica mock).

Le os 63 alertas ja descritos em texto (resultados/review_events.json), envia
cada um a uma LLM REAL (Claude, via API da Anthropic) atuando como analista de
SOC, e grava o veredito em resultados/llm_verdicts.json — no formato que o
score_llm_layer.py espera (veredito = "ATAQUE" ou "FALSO_POSITIVO").

O rotulo verdadeiro NAO entra no prompt (fica em review_truth.json, usado so na
correcao). Isso garante avaliacao honesta.

COMO RODAR
----------
    pip install anthropic
    export ANTHROPIC_API_KEY=sk-ant-...        # sua chave
    python codigo/camada_llm_real.py

Depois rode:  python codigo/score_llm_layer.py   (recalcula as metricas reais)

Para usar OpenAI em vez de Claude, defina PROVIDER=openai e OPENAI_API_KEY.
"""
import os, re, json, time, sys

# ----- caminhos relativos a este arquivo -----
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RES  = os.path.join(ROOT, "resultados")
ART  = os.path.join(ROOT, "artifacts")
def _find(name):
    # procura em artifacts/ (run completo) e cai para resultados/ (snapshot commitado)
    for base in (ART, RES):
        p = os.path.join(base, name)
        if os.path.exists(p):
            return p
    return os.path.join(RES, name)
EVENTS_IN  = _find("review_events.json")
VERDICTS_OUT = os.path.join(RES, "llm_verdicts.json")

# ----- configuracao do modelo -----
PROVIDER = os.environ.get("LLM_PROVIDER", "anthropic")   # "anthropic" ou "openai"
# ajuste para um modelo a que voce tem acesso; ex.: claude-sonnet-5, claude-opus-4-8
MODEL = os.environ.get("LLM_MODEL", "claude-sonnet-5")

SYSTEM = (
    "Voce e um analista senior de seguranca de redes (SOC). Recebe a descricao de "
    "um fluxo de rede que um detector automatico (1a camada) marcou como ataque, "
    "mas possivelmente com baixa confianca. Cada atributo vem com o valor do fluxo "
    "comparado a faixa tipica do trafego LEGITIMO (percentis 10-90). Sua tarefa e "
    "decidir se o fluxo e um ATAQUE real ou um FALSO POSITIVO (trafego legitimo "
    "classificado como ataque) e justificar em 1-2 frases. "
    "Responda SOMENTE em JSON valido, sem markdown, no formato: "
    '{"veredito": "ATAQUE" | "FALSO_POSITIVO", "confianca": 0..1, '
    '"justificativa": "<texto curto>"}.'
)

def evento_para_texto(e):
    linhas = [
        f"Classe prevista pela 1a camada: {e['classe_prevista_camada1']} "
        f"(confianca {e['confianca_camada1']}).",
        f"Distribuicao de probabilidade: {e['distribuicao_prob']}.",
        "Atributos (valor do fluxo vs. faixa do trafego legitimo):",
    ]
    for a in e["atributos"]:
        linhas.append(
            f"  - {a['atributo']}: {a['valor']} "
            f"(normal ~{a['normal_mediana']}, faixa {a['normal_p10']}..{a['normal_p90']}) "
            f"-> {a['situacao']}"
        )
    linhas.append(
        "\nDecida criticamente. Fluxos pequenos, regulares e com atributos dentro "
        "da faixa legitima tendem a ser FALSO_POSITIVO; cargas muito acima do "
        "normal ou assinaturas de varredura tendem a ser ATAQUE."
    )
    return "\n".join(linhas)

def parse_json(txt):
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        raise ValueError("resposta sem JSON: " + txt[:200])
    return json.loads(m.group(0))

def normaliza_veredito(v):
    s = str(v).strip().upper()
    if "FALSO" in s or "BENIGN" in s or "LEGIT" in s:
        return "FALSO_POSITIVO"
    return "ATAQUE"

# ----- clientes -----
def call_anthropic(user):
    import anthropic
    client = anthropic.Anthropic()   # le ANTHROPIC_API_KEY do ambiente
    msg = client.messages.create(
        model=MODEL, max_tokens=400, temperature=0,
        system=SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")

def call_openai(user):
    from openai import OpenAI
    client = OpenAI()
    resp = client.chat.completions.create(
        model=os.environ.get("LLM_MODEL", "gpt-4o-mini"), temperature=0,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": user}],
    )
    return resp.choices[0].message.content

def chamar_llm(user):
    return call_openai(user) if PROVIDER == "openai" else call_anthropic(user)

def main():
    data = json.load(open(EVENTS_IN, encoding="utf-8"))
    eventos = data["eventos"]
    print(f"[llm-real] provider={PROVIDER} model={MODEL} | {len(eventos)} alertas")

    verdicts = {}
    for e in eventos:
        eid = str(e["id"])
        user = evento_para_texto(e)
        for tent in range(3):
            try:
                raw = chamar_llm(user)
                j = parse_json(raw)
                verdicts[eid] = {
                    "veredito": normaliza_veredito(j.get("veredito")),
                    "confianca": j.get("confianca"),
                    "justificativa": j.get("justificativa", ""),
                }
                break
            except Exception as ex:
                print(f"  alerta {eid}: tentativa {tent+1} falhou ({ex})", file=sys.stderr)
                time.sleep(2 * (tent + 1))
        else:
            print(f"  alerta {eid}: FALHOU 3x — marque manualmente", file=sys.stderr)
            verdicts[eid] = {"veredito": "ATAQUE", "confianca": None,
                             "justificativa": "ERRO: sem resposta da LLM"}
        print(f"  {eid}: {verdicts[eid]['veredito']}")

    json.dump(verdicts, open(VERDICTS_OUT, "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(f"[llm-real] gravado {VERDICTS_OUT} ({len(verdicts)} vereditos)")

if __name__ == "__main__":
    main()
