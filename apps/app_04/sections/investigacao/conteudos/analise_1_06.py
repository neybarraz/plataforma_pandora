from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "relacoes_fundamentais_circuitos_capacidade_conducao_corrente"

NUM_D_1 = 1
NUM_D_2 = 2
NUM_F_1 = 3
NUM_F_2 = 4

Q_D_001 = f"q_d_{CONTEUDO_ID}_{NUM_D_1:03d}"
Q_D_002 = f"q_d_{CONTEUDO_ID}_{NUM_D_2:03d}"
Q_F_001 = f"q_f_{CONTEUDO_ID}_{NUM_F_1:03d}"
Q_F_002 = f"q_f_{CONTEUDO_ID}_{NUM_F_2:03d}"

DIAG_STATUS_KEY = f"analise_diag_status_{CONTEUDO_ID}"
DIAG_RESULT_KEY = f"analise_diag_result_{CONTEUDO_ID}"


def _get_widget_value(question_id: str):
    return st.session_state.get(f"analise_widget_{question_id}")


def _diagnostico_respondido() -> bool:
    return _get_widget_value(Q_D_001) is not None and _get_widget_value(Q_D_002) is not None


def _acertou(question_id: str, correta: str) -> bool:
    valor = _get_widget_value(question_id)
    return valor is not None and str(valor).strip().lower() == correta.strip().lower()


def _get_diag_status() -> str:
    return str(st.session_state.get(DIAG_STATUS_KEY, "nao_iniciado"))


def _set_diag_status(status: str) -> None:
    st.session_state[DIAG_STATUS_KEY] = status


def _get_diag_result() -> dict:
    valor = st.session_state.get(DIAG_RESULT_KEY, {})
    return valor if isinstance(valor, dict) else {}


def _set_diag_result(resultado: dict) -> None:
    st.session_state[DIAG_RESULT_KEY] = resultado


def _finalizar_diagnostico() -> None:
    if not _diagnostico_respondido():
        return

    acerto_q1 = _acertou(Q_D_001, "b")
    acerto_q2 = _acertou(Q_D_002, "c")
    total_acertos = int(acerto_q1) + int(acerto_q2)

    resultado = {
        "resposta_q1": _get_widget_value(Q_D_001),
        "resposta_q2": _get_widget_value(Q_D_002),
        "q1_correta": acerto_q1,
        "q2_correta": acerto_q2,
        "total_acertos": total_acertos,
        "acertou_tudo": total_acertos == 2,
    }

    _set_diag_result(resultado)

    if total_acertos == 2:
        _set_diag_status("concluido_com_dominio")
    else:
        _set_diag_status("concluido_com_reforco")

    st.rerun()


def _blocos_diagnostico() -> list[dict]:
    return [
        {
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
        },
        {
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
        },
    ]


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
    resultado = _get_diag_result()

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
                    "Na questão 1, a resposta correta é **b**. A capacidade de condução de corrente, "
                    "também chamada de ampacidade, corresponde à corrente máxima que o condutor pode "
                    "transportar em regime permanente sem que sua temperatura ultrapasse o limite "
                    "admissível para a isolação e para as condições de instalação. Portanto, não se trata "
                    "de ausência de queda de tensão nem de corrente de curto-circuito, mas de um limite "
                    "térmico operacional do circuito."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. Para uma mesma corrente elétrica, um "
                    "condutor com maior seção transversal apresenta menor densidade de corrente e, em "
                    "geral, menor resistência elétrica por unidade de comprimento. Isso reduz a potência "
                    "dissipada por efeito Joule, expressa por **P_J = I²R**, o que favorece a operação "
                    "dentro de limites térmicos seguros. Assim, a seção do condutor influencia "
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
                "em que **I** é a corrente elétrica e **R** é a resistência do trecho condutor. "
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
                "em que **\\rho** é a resistividade elétrica do material, **L** é o comprimento do "
                "condutor e **S** é a seção transversal. Essa equação evidencia que, para um mesmo "
                "material e comprimento, o aumento da seção reduz a resistência elétrica. Como a "
                "dissipação térmica depende de **R**, condutores com maior seção tendem a operar com "
                "menor aquecimento para uma mesma corrente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A capacidade de condução de corrente, ou **ampacidade**, é o valor máximo de corrente "
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
                "em que **J** é a densidade de corrente. Se a seção **S** diminui para uma mesma "
                "corrente **I**, a densidade aumenta, intensificando a solicitação térmica no material. "
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


def _blocos_verificacao_final() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Verificação final",
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
    blocos: list[dict] = []
    status = _get_diag_status()

    if status == "nao_iniciado":
        blocos.extend(_blocos_diagnostico())
        return blocos

    if status == "concluido_com_dominio":
        blocos.extend(_blocos_sucesso_diagnostico())
        return blocos

    if status == "concluido_com_reforco":
        blocos.extend(_blocos_correcao_diagnostico())
        blocos.extend(_blocos_reforco())
        blocos.extend(_blocos_verificacao_final())
        return blocos

    return blocos


def render_controles_especiais() -> None:
    status = _get_diag_status()

    if status != "nao_iniciado":
        return

    if not _diagnostico_respondido():
        st.info("Responda as duas questões para verificar o diagnóstico.")
        return

    if st.button(
        "Verificar diagnóstico",
        key=f"btn_verificar_diag_{CONTEUDO_ID}",
        use_container_width=False,
    ):
        _finalizar_diagnostico()