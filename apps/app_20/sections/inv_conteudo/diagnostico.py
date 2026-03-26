from __future__ import annotations

from typing import Any
import streamlit as st


# ============================================================
# LEITURA DE WIDGET (compatível com Investigação e legado)
# ============================================================

def get_widget_value(question_id: str):
    key_inv = f"investigacao_widget_{question_id}"
    key_old = f"analise_widget_{question_id}"

    if key_inv in st.session_state:
        return st.session_state.get(key_inv)

    return st.session_state.get(key_old)


def normalizar(valor: Any) -> str:
    if valor is None:
        return ""
    return str(valor).strip().lower()


# ============================================================
# CÁLCULO DO DIAGNÓSTICO (GENÉRICO)
# ============================================================

def calcular_resultado(questoes: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [q["id"] for q in questoes]

    gabarito = {
        q["id"]: str(q["alternativa_correta"]).strip().lower()
        for q in questoes
    }

    respostas = {
        q["id"]: normalizar(get_widget_value(q["id"]))
        for q in questoes
    }

    pendentes = [qid for qid in ids if not respostas[qid]]

    corretas = []
    erradas = []

    for qid in ids:
        r = respostas[qid]
        if not r:
            continue

        if r == gabarito[qid]:
            corretas.append(qid)
        else:
            erradas.append(qid)

    total_acertos = len(corretas)
    respondido = len(pendentes) == 0
    acertou_tudo = respondido and total_acertos == len(ids)

    return {
        "respondido": respondido,
        "pendentes": pendentes,
        "respostas": respostas,
        "corretas": corretas,
        "erradas": erradas,
        "total_acertos": total_acertos,
        "acertou_tudo": acertou_tudo,
        "precisa_reforco": respondido and not acertou_tudo,
    }


# ============================================================
# BUILDERS GENÉRICOS DE BLOCOS
# ============================================================

def bloco_questao(q: dict[str, Any]) -> dict[str, Any]:
    return {
        "tipo": "questao_multipla_escolha",
        "id": q["id"],
        "pergunta": q["pergunta"],
        "alternativas": q["alternativas"],
        "alternativa_correta": q["alternativa_correta"],
    }


def blocos_diagnostico_completo(questoes):
    return [bloco_questao(q) for q in questoes]


def blocos_diagnostico_pendentes(questoes, resultado):
    mapa = {q["id"]: q for q in questoes}

    blocos = [
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": "Você já iniciou o diagnóstico. Responda apenas as questões pendentes.",
        }
    ]

    for qid in resultado["pendentes"]:
        blocos.append(bloco_questao(mapa[qid]))

    return blocos


def blocos_correcao(questoes, resultado):
    blocos = [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": "Você errou uma ou mais questões do diagnóstico.",
        },
        {"tipo": "subtitulo", "texto": "Correção do diagnóstico"},
    ]

    for q in questoes:
        if q["id"] not in resultado["corretas"]:
            blocos.append({"tipo": "texto", "texto": q["correcao"]})

    return blocos