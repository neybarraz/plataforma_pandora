from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_08"

Q_D_001 = f"{BASE_ID}_001"
Q_D_002 = f"{BASE_ID}_002"
Q_F_001 = f"{BASE_ID}_003"
Q_F_002 = f"{BASE_ID}_004"


DIAG_QUESTOES = (Q_D_001, Q_D_002)
DIAG_CORRETAS = {
    Q_D_001: "b",
    Q_D_002: "c",
}


def _get_widget_value(question_id: str):
    return st.session_state.get(f"analise_widget_{question_id}")


def _normalizar_resposta(valor) -> str:
    if valor is None:
        return ""
    return str(valor).strip().lower()


def _respostas_diagnostico() -> dict[str, str]:
    return {
        qid: _normalizar_resposta(_get_widget_value(qid))
        for qid in DIAG_QUESTOES
    }


def _questoes_pendentes() -> list[str]:
    respostas = _respostas_diagnostico()
    return [qid for qid in DIAG_QUESTOES if not respostas[qid]]


def _diagnostico_respondido() -> bool:
    return len(_questoes_pendentes()) == 0


def _resultado_diagnostico() -> dict:
    respostas = _respostas_diagnostico()
    pendentes = _questoes_pendentes()

    corretas: list[str] = []
    erradas: list[str] = []

    for qid in DIAG_QUESTOES:
        resposta = respostas[qid]
        if not resposta:
            continue

        if resposta == DIAG_CORRETAS[qid]:
            corretas.append(qid)
        else:
            erradas.append(qid)

    total_acertos = len(corretas)
    respondido = len(pendentes) == 0
    acertou_tudo = respondido and total_acertos == len(DIAG_QUESTOES)
    precisa_reforco = respondido and total_acertos < len(DIAG_QUESTOES)

    return {
        "respondido": respondido,
        "pendentes": pendentes,
        "respostas": respostas,
        "corretas": corretas,
        "erradas": erradas,
        "q1_correta": Q_D_001 in corretas,
        "q2_correta": Q_D_002 in corretas,
        "total_acertos": total_acertos,
        "acertou_tudo": acertou_tudo,
        "precisa_reforco": precisa_reforco,
    }


def _bloco_diagnostico_q1() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_001,
        "pergunta": (
            "Em um circuito de alimentação de motor, dois cabos possuem o mesmo material e "
            "a mesma seção transversal, mas um deles possui comprimento significativamente "
            "maior. Considerando o comportamento elétrico do circuito, conclui-se que:"
        ),
        "alternativas": {
            "a": "O comprimento não influencia o circuito se a seção do cabo for a mesma",
            "b": "O aumento do comprimento eleva a resistência elétrica do condutor e pode aumentar a queda de tensão",
            "c": "O comprimento reduz a corrente elétrica do motor independentemente da tensão",
            "d": "O comprimento apenas influencia o aquecimento do motor, não do condutor",
        },
        "alternativa_correta": "b",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "Ao calcular a resistência elétrica de um circuito monofásico que alimenta um "
            "motor localizado a certa distância do quadro elétrico, como deve ser considerado "
            "o comprimento do percurso elétrico no cálculo da resistência do circuito?"
        ),
        "alternativas": {
            "a": "Considera-se apenas o comprimento físico entre o quadro e o motor",
            "b": "Considera-se apenas o comprimento do condutor de fase",
            "c": "Considera-se o percurso completo de ida e retorno da corrente no circuito",
            "d": "O comprimento não é necessário para o cálculo da resistência elétrica",
        },
        "alternativa_correta": "c",
    }


def _mapa_blocos_diagnostico() -> dict[str, dict]:
    return {
        Q_D_001: _bloco_diagnostico_q1(),
        Q_D_002: _bloco_diagnostico_q2(),
    }


def _blocos_diagnostico_completo() -> list[dict]:
    return [
        _bloco_diagnostico_q1(),
        _bloco_diagnostico_q2(),
    ]


def _blocos_diagnostico_pendentes() -> list[dict]:
    resultado = _resultado_diagnostico()
    pendentes = resultado["pendentes"]
    mapa = _mapa_blocos_diagnostico()

    blocos: list[dict] = [
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
            blocos.append(mapa[qid])

    return blocos


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre a influência do comprimento do circuito "
                "no comportamento elétrico de condutores e na queda de tensão em instalações elétricas."
            ),
        }
    ]


def _blocos_correcao_diagnostico() -> list[dict]:
    resultado = _resultado_diagnostico()

    blocos: list[dict] = [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": (
                "Uma ou mais respostas do diagnóstico não estavam corretas. "
                "Revise os conceitos fundamentais abaixo."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Correção do diagnóstico",
        },
    ]

    if not resultado.get("q1_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 1, a resposta correta é **b**. A resistência elétrica de um condutor "
                    "depende diretamente de seu comprimento. Essa relação é descrita pela expressão:\n\n"
                    "$$ R = \\rho \\frac{L}{A} $$\n\n"
                    "em que **R** é a resistência elétrica do condutor, **\\rho** é a resistividade do material, "
                    "**L** é o comprimento do condutor e **A** é a área de sua seção transversal. "
                    "Assim, quanto maior o comprimento do cabo, maior será sua resistência elétrica, "
                    "o que pode aumentar a queda de tensão ao longo do circuito."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. Em um circuito real, a corrente elétrica "
                    "percorre um caminho completo entre a fonte e a carga. Em sistemas monofásicos, isso "
                    "significa que a corrente circula pelo condutor de ida e retorna pelo condutor de retorno. "
                    "Portanto, o comprimento elétrico considerado no cálculo deve incluir o percurso total "
                    "do circuito, isto é, ida e retorno."
                ),
            }
        )

    return blocos


def _blocos_reforco() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Reforço do conteúdo",
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência elétrica de um condutor depende das propriedades físicas do "
                "material e da geometria do cabo. A relação fundamental que descreve esse "
                "comportamento é dada por:\n\n"
                "$$ R = \\rho \\frac{L}{A} $$\n\n"
                "em que **\\rho** representa a resistividade elétrica do material, **L** o comprimento "
                "do condutor e **A** a área da seção transversal. Essa equação mostra que o "
                "aumento do comprimento do cabo provoca aumento proporcional da resistência elétrica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência do condutor influencia diretamente a queda de tensão ao longo "
                "do circuito. Utilizando a Lei de Ohm, a queda de tensão pode ser estimada por:\n\n"
                "$$ \\Delta V = I R $$\n\n"
                "em que **I** é a corrente elétrica do circuito e **R** é a resistência total do "
                "percurso elétrico."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em circuitos monofásicos utilizados para alimentação de motores, a corrente "
                "percorre o trajeto completo entre fonte e carga, retornando pelo condutor de "
                "retorno. Assim, o comprimento elétrico considerado no cálculo deve incluir "
                "o percurso total do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Isso significa que, ao avaliar a resistência total do circuito, não basta considerar "
                "apenas a distância física entre o quadro e o motor. É necessário considerar o percurso "
                "completo da corrente elétrica. Em consequência, o aumento da distância entre fonte e carga "
                "tende a elevar a resistência total e, portanto, a queda de tensão."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Do ponto de vista de projeto, esse conceito é decisivo porque motores instalados a grandes "
                "distâncias do quadro elétrico podem apresentar desempenho comprometido caso o dimensionamento "
                "dos condutores não considere adequadamente o comprimento do circuito."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A resistência elétrica do condutor cresce com o comprimento.",
                "A relação fundamental é R = ρL/A.",
                "A queda de tensão depende da corrente e da resistência do percurso.",
                "Em circuitos monofásicos, deve-se considerar o percurso de ida e retorno.",
                "Comprimentos maiores tendem a aumentar a resistência total do circuito.",
                "Esse efeito influencia diretamente a alimentação elétrica do motor.",
            ],
        },
    ]


def _blocos_reflexao_final() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Reflexão final",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_001,
            "pergunta": (
                "Em um circuito que alimenta um motor localizado a grande distância do "
                "quadro elétrico, qual efeito físico tende a se tornar mais relevante "
                "devido ao aumento do comprimento dos condutores?"
            ),
            "alternativas": {
                "a": "Redução da resistividade do material",
                "b": "Aumento da resistência elétrica e da queda de tensão",
                "c": "Eliminação da corrente elétrica",
                "d": "Aumento da potência nominal do motor",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "No cálculo da queda de tensão em um circuito monofásico que alimenta um motor, "
                "o comprimento considerado deve representar:"
            ),
            "alternativas": {
                "a": "Somente o trecho entre o quadro e o motor",
                "b": "Apenas o condutor de fase",
                "c": "O percurso completo de ida e retorno da corrente no circuito",
                "d": "Apenas o trecho onde ocorre maior corrente",
            },
            "alternativa_correta": "c",
        },
    ]


def get_blocos() -> list[dict]:
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAG_QUESTOES):
            return _blocos_diagnostico_pendentes()
        return _blocos_diagnostico_completo()

    if resultado["acertou_tudo"]:
        return _blocos_sucesso_diagnostico()

    return (
        _blocos_correcao_diagnostico()
        + _blocos_reforco()
        + _blocos_reflexao_final()
    )


def render_controles_especiais() -> None:
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAG_QUESTOES):
            st.info("Diagnóstico em andamento. Responda apenas as questões pendentes.")
        else:
            st.info("Responda às duas questões iniciais. O reforço será liberado automaticamente se necessário.")
        return

    if resultado["acertou_tudo"]:
        st.success("Diagnóstico concluído com domínio.")
        return

    st.warning("Diagnóstico concluído. O bloco de reforço foi liberado com base nas suas respostas.")