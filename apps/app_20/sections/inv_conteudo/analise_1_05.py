from __future__ import annotations

import streamlit as st


BASE_ID = "analise_04"

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
            "No circuito de alimentação de um motor de bomba, deseja-se comparar dois condutores "
            "de mesma seção e mesmo comprimento: um de cobre e outro de alumínio. "
            "Considerando condições equivalentes de instalação, a afirmação mais adequada é:"
        ),
        "alternativas": {
            "a": "O alumínio apresenta menor resistividade que o cobre, logo tende a produzir menor queda de tensão",
            "b": "O cobre apresenta menor resistividade que o alumínio, logo tende a oferecer menor resistência elétrica ao circuito",
            "c": "Cobre e alumínio apresentam exatamente a mesma resistividade em temperatura ambiente",
            "d": "A escolha entre cobre e alumínio não influencia a resistência elétrica do condutor",
        },
        "alternativa_correta": "b",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "A resistência elétrica de um condutor homogêneo pode ser modelada por "
            "**R = \\rho L / A**. Nessa expressão, o significado físico da grandeza "
            "**\\rho** é:"
        ),
        "alternativas": {
            "a": "A potência dissipada por unidade de volume do material",
            "b": "A corrente máxima admissível do cabo",
            "c": "A propriedade intrínseca do material que expressa sua oposição à condução de corrente elétrica",
            "d": "A tensão nominal de operação do circuito",
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
                "Você demonstrou domínio inicial sobre material do condutor, resistividade elétrica "
                "e sua influência na resistência do circuito."
            ),
        },
    ]


def _blocos_correcao_diagnostico() -> list[dict]:
    resultado = _resultado_diagnostico()

    blocos: list[dict] = [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": (
                "Você errou uma ou mais questões do diagnóstico. Revise os conceitos abaixo."
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
                    "Na questão 1, a resposta correta é **b**. O cobre apresenta, em temperatura ambiente, "
                    "menor resistividade elétrica que o alumínio. Como a resistência de um condutor uniforme "
                    "é dada por **R = \\rho L / A**, para mesmo comprimento **L** e mesma seção transversal "
                    "**A**, o material com menor **\\rho** resulta em menor resistência elétrica."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A resistividade elétrica **\\rho** é uma "
                    "propriedade intrínseca do material e expressa sua oposição à condução de corrente elétrica. "
                    "Ela se relaciona com a resistência total do condutor por meio da expressão "
                    "**R = \\rho L / A**."
                ),
            }
        )

    return blocos


def _blocos_reforco() -> list[dict]:
    return [
        {"tipo": "subtitulo", "texto": "Reforço do conteúdo"},
        {
            "tipo": "texto",
            "texto": (
                "Em circuitos de alimentação elétrica, os condutores não são elementos ideais. "
                "Eles apresentam resistência elétrica e, por isso, influenciam diretamente a corrente, "
                "as perdas de potência e a queda de tensão no sistema."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Material do Condutor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Os materiais mais usuais em condutores de potência são **cobre** e **alumínio**. "
                "O cobre apresenta menor resistividade elétrica e, portanto, para uma mesma geometria "
                "de cabo, tende a oferecer menor resistência ao escoamento de corrente."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Resistividade e Resistência",
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência elétrica de um condutor uniforme pode ser modelada por:\n\n"
                "$$ R = \\frac{\\rho L}{A} $$\n\n"
                "em que **R** é a resistência elétrica do condutor, **\\rho** é a resistividade elétrica "
                "do material, **L** é o comprimento do trecho analisado e **A** é a área da seção transversal."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa relação mostra que a resistência cresce com o comprimento e com a resistividade, "
                "e diminui com o aumento da seção transversal do cabo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em engenharia, essa análise é importante porque o aumento da resistência provoca "
                "maiores perdas por efeito Joule:\n\n"
                "$$ P_J = I^2 R $$\n\n"
                "onde **I** é a corrente elétrica no circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A influência do material do condutor também aparece na queda de tensão ao longo da linha:\n\n"
                "$$ \\Delta V = I R $$\n\n"
                "Substituindo a expressão da resistência, obtém-se:\n\n"
                "$$ \\Delta V = I \\frac{\\rho L}{A} $$"
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=ok4O4VwbnKQ",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=-zCx4Y3I99o",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, o motor da bomba impõe uma corrente ao circuito de alimentação. "
                "Os cabos devem conduzir essa corrente com segurança, limitando o aquecimento e preservando "
                "a tensão nos terminais do equipamento."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Cobre e alumínio possuem resistividades elétricas diferentes.",
                "A resistência do cabo depende de material, comprimento e seção transversal.",
                "A relação fundamental é R = ρL/A.",
                "Perdas por aquecimento crescem com a resistência e com o quadrado da corrente.",
                "A queda de tensão aumenta quando a resistividade é maior ou a seção do cabo é menor.",
                "Esses conceitos são essenciais no dimensionamento do circuito de alimentação do motor.",
            ],
        },
    ]


def _blocos_reflexao_final() -> list[dict]:
    return [
        {"tipo": "subtitulo", "texto": "Reflexão final"},
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_001,
            "pergunta": (
                "Dois condutores possuem o mesmo comprimento e conduzem a mesma corrente. "
                "Se um deles for substituído por outro de maior seção transversal, conclui-se que:"
            ),
            "alternativas": {
                "a": "A resistência elétrica aumenta e a queda de tensão também aumenta",
                "b": "A resistência elétrica diminui e a queda de tensão tende a diminuir",
                "c": "A resistividade do material aumenta automaticamente",
                "d": "A corrente no circuito necessariamente zera",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Na comparação entre cobre e alumínio, para mesma geometria e mesma temperatura, "
                "o material com menor resistividade tende a apresentar:"
            ),
            "alternativas": {
                "a": "Maior resistência elétrica",
                "b": "Maior queda de tensão para a mesma corrente",
                "c": "Menor resistência elétrica e menores perdas por efeito Joule",
                "d": "Menor tensão de alimentação da concessionária",
            },
            "alternativa_correta": "c",
        },
    ]


def get_blocos() -> list[dict]:
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        return _blocos_diagnostico_completo()

    if resultado["acertou_tudo"]:
        return _blocos_sucesso_diagnostico()

    return (
        _blocos_correcao_diagnostico()
        + _blocos_reforco()
        + _blocos_reflexao_final()
    )