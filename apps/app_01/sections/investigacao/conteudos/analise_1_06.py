from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "ar_como_fluido"

NUM_D_1 = 1
NUM_D_2 = 2
NUM_F_1 = 1
NUM_F_2 = 2

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
                "Em uma sala fechada, uma parede recebe radiação solar direta e aquece o ar próximo a ela. "
                "Após algum tempo, observa-se que o ar próximo à parede sobe enquanto ar mais frio ocupa a "
                "região inferior. Qual é a explicação física mais adequada para esse fenômeno?"
            ),
            "alternativas": {
                "a": "O aquecimento aumenta a pressão do ar, fazendo com que ele desça",
                "b": "O ar aquecido torna-se mais denso e tende a subir devido à gravidade",
                "c": "O ar aquecido expande-se, reduz sua densidade e sofre empuxo ascendente",
                "d": "A radiação solar gera movimento do ar independentemente da temperatura",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Considere duas regiões de uma sala: uma próxima a uma janela iluminada pelo Sol e outra "
                "mais afastada, onde o ar está mais frio. Qual das afirmações descreve corretamente o "
                "comportamento esperado do ar nesse ambiente?"
            ),
            "alternativas": {
                "a": "O ar mais frio sobe porque possui maior densidade",
                "b": "O ar aquecido tende a subir e o ar mais frio tende a descer, formando correntes convectivas",
                "c": "O ar permanece imóvel porque a pressão atmosférica é constante no ambiente",
                "d": "O movimento do ar depende apenas da geometria da sala e não da temperatura",
            },
            "alternativa_correta": "b",
        },
    ]


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre dinâmica de fluidos aplicada à circulação de ar. "
                "Este conteúdo pode ser considerado concluído nesta etapa."
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
                    "Na questão 1, a resposta correta é **c**. Quando o ar é aquecido, ele se expande e sua "
                    "densidade diminui. Em um campo gravitacional, regiões menos densas tendem a subir, "
                    "enquanto regiões mais densas descem. Esse processo está associado ao empuxo e "
                    "dá origem às correntes convectivas naturais no ambiente."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **b**. Diferenças de temperatura produzem diferenças "
                    "de densidade no ar. O ar aquecido torna-se menos denso e tende a subir, enquanto o ar "
                    "mais frio e mais denso tende a descer. Esse processo estabelece correntes convectivas "
                    "que contribuem para a circulação de ar dentro do ambiente."
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
                "Para compreender a circulação de ar dentro de um ambiente, é necessário primeiro "
                "entender a natureza física do ar. Na física, o ar é tratado como um **fluido**. "
                "Fluidos são substâncias que não possuem forma própria e que podem se deformar "
                "continuamente quando submetidas a forças. Em vez de manter uma forma fixa como "
                "os sólidos, os fluidos escoam e se adaptam ao espaço que ocupam."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Os fluidos podem ser classificados em dois grandes grupos: **líquidos** e **gases**. "
                "Essa classificação está relacionada principalmente ao comportamento do fluido em relação "
                "ao volume que ocupa e à distância média entre suas moléculas. "
                
                "Os **líquidos** possuem volume praticamente constante e baixa compressibilidade, ou seja, "
                "seu volume varia muito pouco quando submetidos a pressão. Embora não mantenham forma própria, "
                "eles ocupam apenas a parte inferior do recipiente e apresentam moléculas relativamente próximas "
                "entre si. "
                
                "Já os **gases**, como o ar, são altamente compressíveis e não possuem volume nem forma definidos. "
                "Eles tendem a se expandir até ocupar todo o espaço disponível no ambiente. Isso ocorre porque as "
                "moléculas em um gás estão muito mais afastadas umas das outras e se movem livremente no espaço."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Uma característica importante dos gases é que eles exercem **pressão** sobre as "
                "superfícies ao seu redor. Em termos físicos, pressão é definida como a força "
                "aplicada por unidade de área:\n\n"
                "$$ P = \\frac{F}{A} $$\n\n"
                "No caso do ar, essa pressão surge das colisões constantes das moléculas do gás "
                "contra as superfícies do ambiente, como paredes, piso e teto. Mesmo quando não "
                "percebemos, o ar está continuamente exercendo pressão em todas as direções."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Outra grandeza fundamental é a **densidade**, que representa a quantidade de massa "
                "presente em um determinado volume de fluido:\n\n"
                "$$ \\rho = \\frac{m}{V} $$\n\n"
                "No ar, a densidade varia com a temperatura. Quando o ar é aquecido, ele tende a se "
                "expandir e sua densidade diminui. Por outro lado, quando o ar esfria, ele se torna "
                "mais denso. Essa relação entre temperatura e densidade é essencial para compreender "
                "como o ar se movimenta dentro de ambientes."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Diferenças de densidade em um fluido podem gerar uma força chamada **empuxo**. "
                "Esse fenômeno ocorre porque regiões menos densas tendem a subir sob a ação da "
                "gravidade, enquanto regiões mais densas tendem a descer. No caso do ar aquecido, "
                "isso significa que parcelas de ar mais quentes tendem a subir, enquanto o ar mais "
                "frio se desloca para ocupar a região inferior."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Esse comportamento explica por que o ar em um ambiente raramente permanece parado. "
                "Superfícies aquecidas, como paredes atingidas pela radiação solar ou equipamentos "
                "eletrônicos, podem aquecer o ar próximo a elas. À medida que esse ar se torna menos "
                "denso, ele tende a subir, enquanto ar mais frio se desloca para preencher o espaço "
                "deixado. Esse processo dá origem às chamadas **correntes convectivas naturais**."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=-texYqRJ4Es",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=raBp9dY__WE",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=gH1AP6gj0yo",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=W_BWQqUy4mI",
        },

        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, tratar o ar como um fluido permite "
                "interpretar como ele circula dentro da sala. Diferenças de temperatura entre "
                "superfícies — como paredes aquecidas pelo Sol, regiões sombreadas ou áreas próximas "
                "a janelas — podem gerar variações locais de densidade no ar. Essas diferenças "
                "produzem movimentos ascendentes e descendentes que contribuem para a circulação "
                "do ar no ambiente."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Assim, mesmo em uma sala aparentemente tranquila, o ar pode estar em constante "
                "movimento devido à interação entre temperatura, densidade e pressão. Essas "
                "circulações influenciam a forma como o calor é redistribuído no espaço e ajudam "
                "a explicar por que diferentes pontos da sala podem apresentar sensações térmicas "
                "distintas."
            ),
        },

        {
            "tipo": "lista",
            "itens": [
                "Fluidos são substâncias que se deformam continuamente quando submetidas a forças.",
                "Líquidos e gases são os dois grandes tipos de fluidos.",
                "O ar é um fluido gasoso que ocupa todo o volume disponível.",
                "A pressão do ar resulta das colisões das moléculas contra as superfícies.",
                "A densidade do ar depende da temperatura.",
                "Ar aquecido torna-se menos denso e tende a subir.",
                "Diferenças de densidade geram movimentos convectivos no ambiente.",
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
                "Considere duas regiões de uma sala: uma próxima a uma parede aquecida pelo Sol "
                "e outra em uma região sombreada. Qual fenômeno físico explica o fato de o ar "
                "próximo à parede aquecida tender a subir?"
            ),
            "alternativas": {
                "a": "O ar aquecido torna-se mais denso e desce",
                "b": "O aquecimento reduz a densidade do ar, produzindo movimento ascendente",
                "c": "O aumento da pressão força o ar a permanecer imóvel",
                "d": "O ar aquecido deixa de exercer pressão sobre as superfícies",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Em um ambiente fechado, uma janela aberta permite a entrada de ar externo. "
                "Considerando o ar como um fluido gasoso, qual característica física permite "
                "que ele ocupe todo o espaço disponível dentro da sala?"
            ),
            "alternativas": {
                "a": "Os gases possuem volume próprio e permanecem concentrados em uma região",
                "b": "Os gases são altamente compressíveis e se expandem para ocupar o espaço disponível",
                "c": "Os gases não exercem pressão sobre as superfícies",
                "d": "As moléculas do gás permanecem fixas em posições definidas",
            },
            "alternativa_correta": "b",
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