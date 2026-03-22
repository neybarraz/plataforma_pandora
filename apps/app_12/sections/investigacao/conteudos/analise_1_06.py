from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_06"

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
            "No circuito de alimentação de um motor de bomba, a capacidade de condução de corrente "
            "de um cabo elétrico deve ser entendida como:"
        ),
        "alternativas": {
            "a": "A corrente máxima que circula sem qualquer queda de tensão ao longo do circuito",
            "b": "A corrente máxima que o condutor pode transportar continuamente sem ultrapassar limites térmicos admissíveis",
            "c": "A corrente de curto-circuito suportada pelo cabo durante falhas transitórias",
            "d": "A corrente nominal do motor independentemente das condições de instalação",
        },
        "alternativa_correta": "b",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "Mantidas as demais condições de instalação, qual interpretação física é mais adequada "
            "sobre a relação entre seção transversal do condutor e corrente admissível?"
        ),
        "alternativas": {
            "a": "A corrente admissível independe da seção, pois depende apenas da tensão da rede",
            "b": "A redução da seção aumenta a corrente admissível por concentrar o fluxo de elétrons",
            "c": "O aumento da seção tende a elevar a corrente admissível porque reduz a densidade de corrente e o aquecimento por efeito Joule",
            "d": "A seção só influencia a queda de tensão, não a capacidade de condução de corrente",
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
                "Você demonstrou domínio inicial sobre capacidade de condução de corrente, relação entre "
                "seção do condutor e corrente admissível, efeito Joule e critérios físicos básicos de "
                "dimensionamento de cabos em circuitos de alimentação."
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
                    "Na questão 1, a resposta correta é <b>b</b>. A <b>capacidade de condução de corrente</b>, "
                    "também chamada de <b>ampacidade</b>, corresponde à corrente máxima que o condutor pode "
                    "transportar em regime permanente sem que sua temperatura ultrapasse o limite admissível "
                    "para a isolação e para as condições de instalação. Portanto, não se trata de ausência "
                    "de queda de tensão nem de corrente de curto-circuito, mas de um limite térmico "
                    "operacional do circuito."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é <b>c</b>. Para uma mesma corrente elétrica, um "
                    "condutor com maior seção transversal apresenta menor densidade de corrente e, em "
                    "geral, menor resistência elétrica por unidade de comprimento. Isso reduz a potência "
                    "dissipada por efeito Joule, expressa por <b>P<sub>J</sub> = I²R</b>, o que favorece "
                    "a operação dentro de limites térmicos seguros. Assim, a seção do condutor influencia "
                    "diretamente sua corrente admissível."
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
                "Em circuitos de alimentação, a corrente elétrica que atravessa o condutor produz "
                "aquecimento devido ao efeito Joule. Em termos físicos, a potência dissipada no cabo "
                "pode ser representada por:\n\n"
                "$$ P_J = I^2 R $$\n\n"
                "em que <b>I</b> é a corrente elétrica e <b>R</b> é a resistência do trecho condutor. "
                "Essa relação mostra que o aquecimento cresce com o quadrado da corrente. Por isso, "
                "o dimensionamento de cabos não pode ser feito apenas observando a existência de "
                "continuidade elétrica no circuito; é necessário verificar se o condutor suporta a "
                "corrente em regime permanente sem exceder limites térmicos admissíveis."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência elétrica do condutor depende de suas propriedades geométricas e do material. "
                "Para um trecho uniforme, utiliza-se:\n\n"
                "$$ R = \\rho \\frac{L}{S} $$\n\n"
                "em que <b>\\rho</b> é a resistividade elétrica do material, <b>L</b> é o comprimento do "
                "condutor e <b>S</b> é a seção transversal. Essa equação evidencia que, para um mesmo "
                "material e comprimento, o aumento da seção reduz a resistência elétrica. Como a "
                "dissipação térmica depende de <b>R</b>, condutores com maior seção tendem a operar com "
                "menor aquecimento para uma mesma corrente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A capacidade de condução de corrente, ou <b>ampacidade</b>, é o valor máximo de corrente "
                "que um cabo pode transportar continuamente sem que a temperatura do condutor e da "
                "isolação ultrapasse os limites estabelecidos para aquela construção e condição de uso. "
                "Desse modo, a corrente admissível resulta de um balanço entre o calor gerado "
                "internamente por efeito Joule e o calor dissipado para o meio externo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Do ponto de vista físico, a seção do condutor se relaciona à corrente admissível porque "
                "afeta simultaneamente a resistência elétrica e a densidade de corrente. A densidade de "
                "corrente pode ser expressa por:\n\n"
                "$$ J = \\frac{I}{S} $$\n\n"
                "em que <b>J</b> é a densidade de corrente. Se a seção <b>S</b> diminui para uma mesma "
                "corrente <b>I</b>, a densidade aumenta, intensificando a solicitação térmica no material. "
                "Por essa razão, condutores de menor seção tendem a suportar menores correntes admissíveis."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em aplicações de engenharia, a capacidade de condução de corrente não depende apenas da "
                "seção nominal do cabo. As condições de instalação alteram a dissipação de calor e, "
                "portanto, modificam a corrente admissível. Entre os fatores mais relevantes estão "
                "temperatura ambiente, agrupamento de cabos, método de instalação, tipo de isolação e "
                "material do condutor. Dois cabos com a mesma seção podem apresentar correntes "
                "admissíveis diferentes quando instalados em condições térmicas distintas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No contexto do motor de uma bomba, essa análise é essencial porque o circuito precisa "
                "fornecer energia continuamente sem provocar degradação térmica dos cabos. Se a corrente "
                "do motor for superior à capacidade admissível do condutor, podem ocorrer aquecimento "
                "excessivo, envelhecimento acelerado da isolação, perdas elétricas maiores e redução da "
                "confiabilidade operacional da instalação."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=-zCx4Y3I99o",
        },
        {
            "tipo": "lista",
            "itens": [
                "A corrente no cabo produz aquecimento por efeito Joule.",
                "A potência dissipada cresce com o quadrado da corrente: P_J = I²R.",
                "A resistência do condutor depende de resistividade, comprimento e seção: R = ρL/S.",
                "Maior seção tende a reduzir resistência, densidade de corrente e aquecimento.",
                "A ampacidade é um limite térmico de operação contínua do condutor.",
                "Método de instalação e temperatura ambiente alteram a corrente admissível do cabo.",
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
                "Ao analisar um cabo que alimenta um motor, qual grandeza física está mais diretamente "
                "associada ao limite térmico que define sua capacidade de condução de corrente?"
            ),
            "alternativas": {
                "a": "A frequência da rede elétrica",
                "b": "A potência dissipada por efeito Joule no condutor",
                "c": "A tensão nominal do sistema, isoladamente",
                "d": "O número de polos do motor",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Mantendo material, comprimento e condições de instalação, a substituição de um cabo por "
                "outro de maior seção tende a produzir qual efeito principal no circuito?"
            ),
            "alternativas": {
                "a": "Aumento da resistência elétrica e redução da corrente admissível",
                "b": "Eliminação completa da queda de tensão",
                "c": "Redução da resistência elétrica e aumento da corrente admissível",
                "d": "Nenhuma alteração elétrica relevante",
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