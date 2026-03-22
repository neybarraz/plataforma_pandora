from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_09"

Q_D_001 = f"{BASE_ID}_001"
Q_D_002 = f"{BASE_ID}_002"
Q_F_001 = f"{BASE_ID}_003"
Q_F_002 = f"{BASE_ID}_004"


DIAG_QUESTOES = (Q_D_001, Q_D_002)
DIAG_CORRETAS = {
    Q_D_001: "c",
    Q_D_002: "b",
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
            "No circuito de alimentação de um motor de bomba, a corrente de projeto calculada é de 28 A. "
            "O cabo instalado possui capacidade de condução de corrente de 24 A nas condições reais de instalação. "
            "Do ponto de vista do dimensionamento, conclui-se que:"
        ),
        "alternativas": {
            "a": "O cabo está adequado, porque a tensão do sistema não foi informada",
            "b": "O cabo está adequado, porque 24 A e 28 A são valores próximos",
            "c": "O cabo está inadequado, porque a capacidade do condutor deve ser igual ou superior à corrente exigida",
            "d": "O cabo está inadequado apenas se houver circuito trifásico",
        },
        "alternativa_correta": "c",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "Em um circuito relativamente longo que alimenta um motor, observa-se que o aumento do comprimento "
            "dos condutores, mantendo corrente e seção constantes, tende a provocar:"
        ),
        "alternativas": {
            "a": "Redução da resistência elétrica e da queda de tensão",
            "b": "Aumento da resistência elétrica e da queda de tensão no circuito",
            "c": "Redução da corrente nominal do motor independentemente da carga",
            "d": "Eliminação das perdas por efeito Joule no cabo",
        },
        "alternativa_correta": "b",
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
                "Você demonstrou domínio inicial sobre as relações fundamentais de circuitos aplicadas ao "
                "dimensionamento de condutores, incluindo compatibilidade entre corrente do circuito e "
                "capacidade de condução do cabo, além da limitação da queda de tensão."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao salvar ou concluir esta etapa, você poderá seguir para o próximo conteúdo."
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
                "Você errou uma ou mais questões do diagnóstico. "
                "Antes de seguir, revise os pontos principais abaixo."
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
                    "Na questão 1, a resposta correta é **c**. No dimensionamento elétrico, a corrente de projeto "
                    "do circuito deve ser compatível com a capacidade de condução de corrente do condutor nas "
                    "condições reais de instalação. Se o cabo admite 24 A e o circuito exige 28 A, o condutor está "
                    "subdimensionado. Nessa condição, o cabo pode operar com aquecimento excessivo, aceleração do "
                    "envelhecimento da isolação e aumento do risco de falha. O critério básico é que a capacidade "
                    "admissível do condutor seja igual ou superior à corrente exigida pelo circuito."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **b**. A resistência elétrica do condutor cresce com o "
                    "comprimento do percurso elétrico, de acordo com a relação **R = \\rho\\,L/A**. Mantidas a "
                    "corrente e a seção, o aumento do comprimento implica maior resistência total. Como a queda de "
                    "tensão no circuito pode ser interpretada por **\\Delta V = R\\,I**, conclui-se que trechos mais "
                    "longos tendem a produzir maior queda de tensão. Esse efeito pode comprometer a qualidade da "
                    "alimentação do motor, especialmente em sistemas de bombeamento com partidas frequentes ou cabos longos."
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
                "No circuito de alimentação de um motor elétrico, as relações fundamentais entre tensão, corrente, "
                "potência e resistência permitem interpretar se os condutores estão tecnicamente adequados para a "
                "operação. Em aplicações de engenharia ambiental e civil, esse raciocínio é relevante em sistemas "
                "de bombeamento, elevatórias, pressurização e infraestrutura predial."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A potência elétrica ativa absorvida por uma carga pode ser relacionada à tensão e à corrente. "
                "Em circuito monofásico, uma forma usual é:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "Em circuito trifásico equilibrado, utiliza-se:\n\n"
                "$$ P = \\sqrt{3}\\,V_L\\,I_L\\,\\cos\\varphi $$\n\n"
                "Essas expressões permitem estimar a corrente exigida pelo motor a partir da potência e da tensão "
                "de alimentação. Para motores reais, também é necessário considerar o rendimento **\\eta**, de modo que "
                "a potência elétrica de entrada seja superior à potência mecânica útil fornecida no eixo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma vez conhecida a corrente do circuito, surge o primeiro critério de dimensionamento: a "
                "compatibilidade entre a corrente exigida e a capacidade de condução de corrente do cabo. "
                "Fisicamente, esse critério está associado ao limite térmico do condutor. Se a corrente for elevada "
                "demais para a seção e para as condições de instalação, ocorre aumento da temperatura por efeito Joule. "
                "A potência dissipada no condutor pode ser representada por:\n\n"
                "$$ P_J = R\\,I^2 $$\n\n"
                "Essa relação mostra que o aquecimento cresce com o quadrado da corrente. Por isso, pequenas elevações "
                "de corrente podem produzir acréscimos significativos nas perdas térmicas do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O segundo critério central é a limitação da queda de tensão. O condutor possui resistência elétrica, "
                "que depende do material, do comprimento e da seção transversal. Em primeira aproximação:\n\n"
                "$$ R = \\rho\\,\\frac{L}{A} $$\n\n"
                "em que **\\rho** é a resistividade do material, **L** é o comprimento elétrico e **A** é a área da seção "
                "transversal. A queda de tensão pode ser interpretada pela relação:\n\n"
                "$$ \\Delta V = R\\,I $$\n\n"
                "Assim, quanto maior a corrente e o comprimento do circuito, maior tende a ser a queda de tensão; "
                "quanto maior a seção do condutor, menor tende a ser esse efeito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em termos de desempenho, a queda de tensão é relevante porque a tensão efetivamente disponível no motor "
                "pode ficar inferior à tensão nominal de projeto. Em motores de bombas, isso pode comprometer partida, "
                "torque disponível, rendimento e estabilidade operacional. Em avaliação de projeto, costuma-se analisar "
                "a queda percentual:\n\n"
                "$$ \\%\\Delta V = \\frac{\\Delta V}{V}\\times 100 $$\n\n"
                "A verificação não se limita, portanto, a evitar sobreaquecimento do cabo; ela também busca garantir "
                "qualidade adequada de alimentação elétrica no ponto de consumo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No dimensionamento técnico, os dois critérios devem ser atendidos simultaneamente: o cabo precisa "
                "suportar termicamente a corrente do circuito e, ao mesmo tempo, manter a queda de tensão dentro dos "
                "limites aceitáveis. Em muitos casos, a seção mínima obtida pelo critério térmico não é suficiente para "
                "o critério funcional de queda de tensão, especialmente em trajetos longos."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=Z_pUXHJaRyg",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=_f3T4-qvBmw",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, o motor da bomba impõe uma demanda elétrica ao circuito. Essa demanda se manifesta "
                "como corrente nos condutores de alimentação. Se a seção do cabo for insuficiente, o circuito passa a "
                "operar com maior aquecimento e maiores perdas. Se o percurso for longo e a seção pequena, a queda de "
                "tensão também pode se tornar significativa."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Isso significa que a análise do circuito de alimentação da bomba deve conectar diretamente as relações "
                "fundamentais de circuitos ao comportamento real da instalação. A potência do motor permite estimar a "
                "corrente; a geometria e o material do cabo definem sua resistência; e a combinação entre corrente, "
                "resistência e comprimento permite avaliar aquecimento e queda de tensão."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A corrente do circuito decorre da potência exigida pela carga e da tensão de alimentação.",
                "A capacidade do condutor deve ser compatível com a corrente exigida em serviço.",
                "O aquecimento por efeito Joule cresce com o quadrado da corrente.",
                "A resistência do cabo aumenta com o comprimento e diminui com o aumento da seção.",
                "A queda de tensão depende da corrente, da resistência e do percurso elétrico.",
                "O dimensionamento adequado exige atender simultaneamente aos critérios térmico e funcional.",
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
                "No redimensionamento do circuito de uma bomba, verificou-se que a corrente de projeto é 32 A e que "
                "o cabo selecionado admite 36 A nas condições de instalação. Sob o critério de capacidade de condução "
                "de corrente, a interpretação adequada é:"
            ),
            "alternativas": {
                "a": "O cabo atende ao critério térmico básico, pois sua capacidade é superior à corrente de projeto",
                "b": "O cabo está inadequado, porque deveria admitir exatamente 32 A",
                "c": "O cabo está inadequado, porque a capacidade do condutor deve ser inferior à corrente de projeto",
                "d": "Não é possível avaliar, porque a queda de tensão substitui o critério térmico",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Em um mesmo circuito, a corrente e o material do condutor permanecem constantes. Se o comprimento "
                "aumenta e a seção transversal também aumenta, a medida adotada para reduzir a tendência de aumento "
                "da queda de tensão é principalmente:"
            ),
            "alternativas": {
                "a": "Reduzir o fator de potência do motor",
                "b": "Aumentar a resistividade elétrica do cabo",
                "c": "Aumentar a seção do condutor",
                "d": "Diminuir a tensão nominal para elevar a corrente",
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