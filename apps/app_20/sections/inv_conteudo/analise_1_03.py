from __future__ import annotations

from typing import Any

import streamlit as st


# ============================================================
# IDENTIDADE DO MÓDULO
# ============================================================

BASE_ID = "analise_1_01"

Q_D_001 = f"{BASE_ID}_001"
Q_D_002 = f"{BASE_ID}_002"
Q_F_001 = f"{BASE_ID}_003"
Q_F_002 = f"{BASE_ID}_004"


# ============================================================
# CONFIGURAÇÃO DECLARATIVA
# ============================================================

DIAGNOSTICO_QUESTOES = [
    {
        "id": Q_D_001,
        "pergunta": (
            "No circuito de alimentação de um motor de bomba, a grandeza tensão elétrica pode ser "
            "interpretada fisicamente como:"
        ),
        "alternativas": {
            "a": "A quantidade de carga que atravessa o condutor por segundo",
            "b": "A diferença de potencial elétrico que impulsiona o movimento de cargas no circuito",
            "c": "A resistência oferecida pelo motor à passagem de corrente",
            "d": "A energia dissipada exclusivamente na forma de calor nos cabos",
        },
        "alternativa_correta": "b",
        "correcao": (
            "Na questão 1, a resposta correta é <b>b</b>. A <b>tensão elétrica</b> é a "
            "<b>diferença de potencial</b> entre dois pontos do circuito. Ela representa a "
            "energia potencial elétrica disponível por unidade de carga para impulsionar o "
            "movimento das cargas. Em termos gerais:\n\n"
            "$$ V = \\frac{W}{q} $$\n\n"
            "em que <b>V</b> é a tensão, <b>W</b> é o trabalho ou energia transferida e "
            "<b>q</b> é a carga elétrica. No circuito de alimentação do motor, a tensão "
            "fornecida pela rede estabelece a condição energética necessária para a circulação "
            "de corrente."
        ),
    },
    {
        "id": Q_D_002,
        "pergunta": (
            "Em regime de operação, a corrente elétrica que circula no circuito de alimentação do motor "
            "representa principalmente:"
        ),
        "alternativas": {
            "a": "A tensão nominal aplicada entre os terminais do motor",
            "b": "A potência mecânica útil já convertida no eixo",
            "c": "A taxa de escoamento de carga elétrica através dos condutores",
            "d": "A oposição elétrica do isolamento do cabo ao campo elétrico",
        },
        "alternativa_correta": "c",
        "correcao": (
            "Na questão 2, a resposta correta é <b>c</b>. A <b>corrente elétrica</b> expressa "
            "a taxa de escoamento de carga elétrica através de uma seção transversal do condutor. "
            "Sua definição fundamental é:\n\n"
            "$$ I = \\frac{\\Delta q}{\\Delta t} $$\n\n"
            "em que <b>I</b> é a corrente, <b>Δq</b> é a quantidade de carga transportada e "
            "<b>Δt</b> é o intervalo de tempo. No circuito do motor, a corrente indica a "
            "intensidade da solicitação elétrica imposta aos cabos e está diretamente ligada "
            "à análise de aquecimento, perdas e dimensionamento."
        ),
    },
]

REFORCO_BLOCOS = [
    {
        "tipo": "subtitulo",
        "texto": "Reforço conceitual",
    },
    {
        "tipo": "texto",
        "texto": (
            "Para interpretar corretamente a alimentação elétrica de um motor, é necessário distinguir "
            "com clareza as grandezas tensão, corrente e potência."
        ),
    },
    {
        "tipo": "texto",
        "texto": (
            "<b>Tensão elétrica</b> é a energia potencial disponível por unidade de carga entre dois "
            "pontos do circuito. É essa diferença de potencial que cria a condição para o movimento "
            "das cargas."
        ),
    },
    {
        "tipo": "texto",
        "texto": (
            "<b>Corrente elétrica</b> é a taxa de escoamento de carga elétrica ao longo do tempo. "
            "Ela indica o quanto o circuito está sendo solicitado eletricamente."
        ),
    },
    {
        "tipo": "texto",
        "texto": (
            "<b>Potência elétrica</b> representa a taxa de transferência ou conversão de energia. "
            "Na alimentação de motores trifásicos, uma relação central é:\n\n"
            "$$ P = \\sqrt{3}\\,V\\,I\\,\\cos\\varphi $$"
        ),
    },
    {
        "tipo": "texto",
        "texto": (
            "Portanto, compreender tensão, corrente e potência é o primeiro passo para interpretar "
            "tecnicamente o funcionamento do sistema de bombeamento. Sem esse bloco conceitual, "
            "não é possível avaliar com rigor se os cabos instalados são suficientes para alimentar "
            "o motor com segurança e desempenho adequado."
        ),
    },
    {
        "tipo": "texto",
        "texto": (
            "<b>Síntese conceitual</b>\n\n"
            "A tensão elétrica representa diferença de potencial e energia por unidade de carga. "
            "A corrente elétrica mede a taxa de escoamento de cargas no circuito. A potência elétrica "
            "expressa a taxa de transferência ou conversão de energia. Em motores, a corrente depende "
            "de tensão, potência, fator de potência e rendimento. Essas grandezas constituem a base "
            "para analisar a alimentação elétrica do motor da bomba."
        ),
    },
]

REFLEXAO_FINAL_BLOCOS = [
    {
        "tipo": "subtitulo",
        "texto": "Reflexão final",
    },
    {
        "tipo": "alerta",
        "nivel": "info",
        "texto": (
            "Nesta etapa final, suas respostas serão registradas para análise. "
            "Não será exibido feedback imediato de certo ou errado."
        ),
    },
    {
        "tipo": "questao_multipla_escolha",
        "id": Q_F_001,
        "pergunta": (
            "Em um circuito que alimenta um motor, a tensão elétrica é mais corretamente interpretada como:"
        ),
        "alternativas": {
            "a": "A taxa de transporte de carga no condutor",
            "b": "A energia potencial elétrica disponível por unidade de carga entre dois pontos",
            "c": "A potência dissipada em regime permanente",
            "d": "A resistência total equivalente do sistema",
        },
        "alternativa_correta": "b",
    },
    {
        "tipo": "questao_multipla_escolha",
        "id": Q_F_002,
        "pergunta": (
            "Na análise de um motor trifásico, a potência ativa elétrica absorvida é associada principalmente à relação:"
        ),
        "alternativas": {
            "a": "$$P = \\sqrt{3}\\,V\\,I\\,\\cos\\varphi$$",
            "b": "$$P = \\frac{V}{I}$$",
            "c": "$$P = R\\,V$$",
            "d": "$$P = \\frac{I}{R}$$",
        },
        "alternativa_correta": "a",
    },
]

MENSAGEM_SUCESSO = (
    "Você demonstrou domínio inicial sobre tensão elétrica, corrente elétrica e suas "
    "relações com a análise da alimentação do motor. Este conteúdo pode ser considerado "
    "concluído nesta etapa."
)


# ============================================================
# NÚCLEO REUTILIZÁVEL
# ============================================================

def _get_widget_value(question_id: str):
    key_inv = f"investigacao_widget_{question_id}"
    key_old = f"analise_widget_{question_id}"

    if key_inv in st.session_state:
        return st.session_state.get(key_inv)

    return st.session_state.get(key_old)


def _normalizar_resposta(valor: Any) -> str:
    if valor is None:
        return ""
    return str(valor).strip().lower()


def _questoes_ids(questoes: list[dict[str, Any]]) -> tuple[str, ...]:
    return tuple(q["id"] for q in questoes)


def _gabarito(questoes: list[dict[str, Any]]) -> dict[str, str]:
    return {
        q["id"]: str(q["alternativa_correta"]).strip().lower()
        for q in questoes
    }


def _respostas(questoes: list[dict[str, Any]]) -> dict[str, str]:
    return {
        q["id"]: _normalizar_resposta(_get_widget_value(q["id"]))
        for q in questoes
    }


def _resultado_diagnostico(
    questoes: list[dict[str, Any]],
) -> dict[str, Any]:
    ids = _questoes_ids(questoes)
    corretas_map = _gabarito(questoes)
    respostas = _respostas(questoes)

    pendentes = [qid for qid in ids if not respostas[qid]]

    corretas: list[str] = []
    erradas: list[str] = []

    for qid in ids:
        resposta = respostas[qid]
        if not resposta:
            continue

        if resposta == corretas_map[qid]:
            corretas.append(qid)
        else:
            erradas.append(qid)

    total_acertos = len(corretas)
    respondido = len(pendentes) == 0
    acertou_tudo = respondido and total_acertos == len(ids)
    precisa_reforco = respondido and total_acertos < len(ids)

    return {
        "respondido": respondido,
        "pendentes": pendentes,
        "respostas": respostas,
        "corretas": corretas,
        "erradas": erradas,
        "total_acertos": total_acertos,
        "acertou_tudo": acertou_tudo,
        "precisa_reforco": precisa_reforco,
    }


def _bloco_questao(q: dict[str, Any]) -> dict[str, Any]:
    return {
        "tipo": "questao_multipla_escolha",
        "id": q["id"],
        "pergunta": q["pergunta"],
        "alternativas": q["alternativas"],
        "alternativa_correta": q["alternativa_correta"],
    }


def _mapa_questoes(questoes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {q["id"]: q for q in questoes}


def _blocos_diagnostico_completo(
    questoes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [_bloco_questao(q) for q in questoes]


def _blocos_diagnostico_pendentes(
    questoes: list[dict[str, Any]],
    resultado: dict[str, Any],
) -> list[dict[str, Any]]:
    pendentes = resultado["pendentes"]
    mapa = _mapa_questoes(questoes)

    blocos: list[dict[str, Any]] = [
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Você já iniciou o diagnóstico. Responda apenas as questões que ainda estão pendentes."
            ),
        }
    ]

    for qid in pendentes:
        if qid in mapa:
            blocos.append(_bloco_questao(mapa[qid]))

    return blocos


def _blocos_sucesso_diagnostico() -> list[dict[str, Any]]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": MENSAGEM_SUCESSO,
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao salvar ou concluir esta etapa, você poderá seguir para o próximo conteúdo."
            ),
        },
    ]


def _blocos_correcao_diagnostico(
    questoes: list[dict[str, Any]],
    resultado: dict[str, Any],
) -> list[dict[str, Any]]:
    blocos: list[dict[str, Any]] = [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": (
                "Você errou uma ou mais questões do diagnóstico. "
                "Antes de seguir, revise os pontos principais abaixo."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Correção do diagnóstico",
        },
    ]

    for q in questoes:
        if q["id"] not in resultado["corretas"]:
            blocos.append(
                {
                    "tipo": "texto",
                    "texto": q["correcao"],
                }
            )

    return blocos


def _blocos_reforco() -> list[dict[str, Any]]:
    return REFORCO_BLOCOS.copy()


def _blocos_reflexao_final() -> list[dict[str, Any]]:
    return REFLEXAO_FINAL_BLOCOS.copy()


# ============================================================
# API DO MÓDULO
# ============================================================

def get_blocos() -> list[dict[str, Any]]:
    resultado = _resultado_diagnostico(DIAGNOSTICO_QUESTOES)

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAGNOSTICO_QUESTOES):
            return _blocos_diagnostico_pendentes(DIAGNOSTICO_QUESTOES, resultado)
        return _blocos_diagnostico_completo(DIAGNOSTICO_QUESTOES)

    if resultado["acertou_tudo"]:
        return _blocos_sucesso_diagnostico()

    return (
        _blocos_correcao_diagnostico(DIAGNOSTICO_QUESTOES, resultado)
        + _blocos_reforco()
        + _blocos_reflexao_final()
    )


def render_controles_especiais() -> None:
    resultado = _resultado_diagnostico(DIAGNOSTICO_QUESTOES)

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAGNOSTICO_QUESTOES):
            st.info("Diagnóstico em andamento. Responda apenas as questões pendentes.")
        else:
            st.info("Responda às duas questões iniciais. O reforço será liberado automaticamente se necessário.")
        return

    if resultado["acertou_tudo"]:
        st.success("Diagnóstico concluído com domínio.")
        return

    st.warning("Diagnóstico concluído. O bloco de reforço foi liberado com base nas suas respostas.")
