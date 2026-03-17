from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "relacoes_fundamentais_circuito"

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
                "Em um trecho do circuito de alimentação de um motor de bomba, mede-se uma tensão de 24 V "
                "aplicada a um condutor equivalente cuja resistência total é 6 Ω. De acordo com a Lei de Ohm, "
                "a corrente elétrica nesse trecho é:"
            ),
            "alternativas": {
                "a": "0,25 A",
                "b": "4 A",
                "c": "18 A",
                "d": "144 A",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Um equipamento elétrico opera em corrente contínua com potência de 2200 W sob tensão de 220 V. "
                "Desprezando perdas adicionais, a corrente elétrica requerida é:"
            ),
            "alternativas": {
                "a": "0,1 A",
                "b": "4,5 A",
                "c": "10 A",
                "d": "484 A",
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
                "Você demonstrou domínio inicial sobre Lei de Ohm e sobre a relação entre potência, "
                "tensão e corrente em circuitos elétricos. Este conteúdo pode ser considerado concluído "
                "nesta etapa."
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
                    "Na questão 1, a resposta correta é **b**. Pela **Lei de Ohm**, a relação entre "
                    "tensão, resistência e corrente é dada por:\n\n"
                    "$$ V = R\\,I $$\n\n"
                    "Logo:\n\n"
                    "$$ I = \\frac{V}{R} = \\frac{24}{6} = 4\\ \\text{A} $$\n\n"
                    "Isso mostra que, para uma mesma resistência, a corrente cresce linearmente com a tensão "
                    "aplicada. Em circuitos reais, essa relação é essencial para interpretar o comportamento "
                    "elétrico de trechos resistivos e para estimar solicitações elétricas sobre condutores."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A relação fundamental entre potência, "
                    "tensão e corrente, para esse caso simplificado, é:\n\n"
                    "$$ P = V\\,I $$\n\n"
                    "Isolando a corrente:\n\n"
                    "$$ I = \\frac{P}{V} = \\frac{2200}{220} = 10\\ \\text{A} $$\n\n"
                    "Essa equação é central na análise de circuitos de alimentação, pois permite estimar a "
                    "corrente exigida por uma carga a partir de sua potência elétrica e da tensão de operação. "
                    "No dimensionamento de condutores, essa corrente calculada é um parâmetro básico."
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
                "A interpretação de circuitos elétricos em aplicações de engenharia depende da compreensão "
                "das relações matemáticas que conectam as grandezas fundamentais do sistema. No caso de um "
                "circuito de alimentação de motor, as relações entre tensão, corrente, resistência e potência "
                "permitem estimar a solicitação elétrica imposta aos condutores e avaliar se a instalação está "
                "operando em condições compatíveis com o projeto."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **Lei de Ohm** descreve a relação básica entre tensão elétrica, corrente elétrica e "
                "resistência em um elemento resistivo:\n\n"
                "$$ V = R\\,I $$\n\n"
                "em que **V** é a diferença de potencial, **R** é a resistência elétrica e **I** é a corrente. "
                "Essa expressão também pode ser escrita como:\n\n"
                "$$ I = \\frac{V}{R} $$\n\n"
                "ou\n\n"
                "$$ R = \\frac{V}{I} $$\n\n"
                "Essas formas são úteis quando se deseja calcular a corrente que atravessa um trecho do circuito "
                "ou a resistência equivalente associada à passagem de corrente elétrica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em condutores elétricos, a resistência depende do material, do comprimento e da seção "
                "transversal. Para análise de engenharia, essa dependência pode ser representada por:\n\n"
                "$$ R = \\rho\\,\\frac{L}{A} $$\n\n"
                "em que **ρ** é a resistividade elétrica do material, **L** é o comprimento do condutor e "
                "**A** é a área da seção transversal. Essa equação é particularmente importante em instalações "
                "elétricas, porque mostra que cabos mais longos ou com menor seção apresentam maior resistência, "
                "o que afeta a corrente, as perdas e a queda de tensão."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Outra relação fundamental conecta **potência elétrica**, **tensão** e **corrente**. "
                "Em sua forma elementar, tem-se:\n\n"
                "$$ P = V\\,I $$\n\n"
                "em que **P** é a potência elétrica ativa fornecida à carga em uma formulação simplificada. "
                "Essa expressão permite obter:\n\n"
                "$$ I = \\frac{P}{V} $$\n\n"
                "e também:\n\n"
                "$$ V = \\frac{P}{I} $$\n\n"
                "No contexto do circuito de alimentação de um motor, essa relação é usada para estimar a corrente "
                "requerida a partir da potência nominal e da tensão de operação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em problemas de engenharia elétrica aplicada, especialmente em motores, a análise pode exigir "
                "formas mais completas da potência. Em sistemas monofásicos com fator de potência, utiliza-se:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "e, em sistemas trifásicos equilibrados:\n\n"
                "$$ P = \\sqrt{3}\\,V_L\\,I_L\\,\\cos\\varphi $$\n\n"
                "quando se consideram grandezas de linha. Para motores reais, o rendimento também interfere, "
                "pois a potência elétrica absorvida não coincide exatamente com a potência mecânica útil."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essas relações são essenciais em cursos de engenharia civil e ambiental quando se analisam "
                "sistemas prediais, estações elevatórias, recalque de água, automação de reservatórios e outros "
                "sistemas eletromecânicos de infraestrutura. A partir delas, torna-se possível estimar correntes, "
                "avaliar perdas por efeito Joule, prever queda de tensão e estabelecer critérios técnicos para "
                "dimensionamento de cabos e verificação de desempenho do circuito."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=aFrag-RGDhQ",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=jzGOUszBHEU",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=rqZKL8vGDBA",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, o motor da bomba constitui a carga principal do circuito. A tensão fornecida "
                "pela rede e a potência exigida pelo motor determinam a corrente elétrica que circulará nos "
                "condutores. Essa corrente, ao atravessar cabos com resistência não nula, produz dissipação de "
                "energia e queda de tensão ao longo do percurso."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Assim, a Lei de Ohm ajuda a interpretar o efeito da resistência dos condutores no comportamento "
                "do circuito, enquanto a relação entre potência, tensão e corrente permite calcular a solicitação "
                "elétrica imposta pela carga. Em conjunto, essas duas bases fornecem o ponto de partida para "
                "avaliar se os condutores de alimentação do motor estão adequadamente dimensionados."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A Lei de Ohm relaciona tensão, corrente e resistência: V = RI.",
                "A resistência do condutor depende do material, do comprimento e da seção transversal.",
                "A potência elétrica, em forma simplificada, pode ser expressa por P = VI.",
                "A corrente requerida por uma carga pode ser estimada por I = P/V.",
                "Em motores, fator de potência e rendimento podem precisar ser considerados.",
                "Essas relações são a base para analisar o circuito de alimentação da bomba.",
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
                "A resistência elétrica equivalente de um trecho de circuito é 8 Ω e a corrente que o atravessa "
                "é 3 A. A tensão elétrica nesse trecho vale:"
            ),
            "alternativas": {
                "a": "11 V",
                "b": "24 V",
                "c": "5 V",
                "d": "0,375 V",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Um equipamento opera com potência de 1500 W em uma tensão de 127 V, em análise simplificada. "
                "A corrente aproximada exigida é:"
            ),
            "alternativas": {
                "a": "0,085 A",
                "b": "8,5 A",
                "c": "11,8 A",
                "d": "190,5 A",
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