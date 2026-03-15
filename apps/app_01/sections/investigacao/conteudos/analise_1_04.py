from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "transferencia_calor"

NUM_D_1 = 5
NUM_D_2 = 6
NUM_F_1 = 5
NUM_F_2 = 6

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
    acerto_q2 = _acertou(Q_D_002, "d")
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
                "A transferência de calor entre dois sistemas ocorre espontaneamente, em condições usuais, "
                "quando existe:"
            ),
            "alternativas": {
                "a": "Diferença de massa entre os corpos",
                "b": "Diferença de temperatura entre as regiões",
                "c": "Diferença de volume entre os materiais",
                "d": "Igualdade de energia interna total",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Uma parede plana recebe um fluxo de calor por condução. Se a taxa é de 120 W durante 5 s, "
                "qual quantidade de calor é transferida?"
            ),
            "alternativas": {
                "a": "24 J",
                "b": "60 J",
                "c": "125 J",
                "d": "600 J",
            },
            "alternativa_correta": "d",
        },
    ]


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre o conceito de transferência de calor. "
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
                    "Na questão 1, a resposta correta é **b**. A transferência de calor ocorre devido "
                    "à existência de uma diferença de temperatura. Essa diferença estabelece a direção "
                    "espontânea do fluxo energético, da região de maior temperatura para a de menor temperatura."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **d**. A quantidade de calor transferida é dada por "
                    "**$Q = \\dot{Q} \\cdot \\Delta t$**. Logo, **$Q = 120 \\cdot 5 = 600\\,J$**."
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
                "Transferência de calor é o processo de propagação de energia térmica entre regiões "
                "que apresentam temperaturas diferentes. Em física, calor não é algo armazenado em um "
                "corpo, mas energia em trânsito, transferida justamente por causa desse desnível térmico. "
                "Assim, quando dois sistemas interagem e possuem temperaturas distintas, surge um fluxo "
                "espontâneo de energia da região mais quente para a região mais fria, até que o equilíbrio "
                "térmico seja atingido."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esse processo pode ser analisado quantitativamente por duas grandezas principais. "
                "A quantidade total de energia transferida é representada por **Q**, medida em joules, "
                "enquanto a taxa temporal de transferência é dada por **$\\dot{Q}$**, medida em watts. "
                "Essa relação pode ser escrita como:\n\n"
                "$$ \\dot{Q} = \\frac{dQ}{dt} $$\n\n"
                "ou, em uma forma mais simples para taxa constante,\n\n"
                "$$ Q = \\dot{Q}\\,\\Delta t $$\n\n"
                "Essas expressões permitem interpretar quanto calor atravessa um sistema e com que "
                "intensidade esse processo ocorre ao longo do tempo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A diferença de temperatura é, portanto, a causa física da transferência de calor. "
                "Quanto maior esse desnível térmico, maior tende a ser o fluxo de energia, embora a "
                "intensidade real da transferência também dependa das propriedades do sistema, do tempo "
                "de interação e das condições do meio."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "É importante distinguir temperatura de calor. A temperatura descreve o estado térmico "
                "de um corpo, enquanto o calor descreve a energia que é transferida entre corpos ou "
                "regiões quando existe diferença de temperatura. Essa distinção é essencial para interpretar "
                "fenômenos térmicos corretamente."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=YvsmfM2Vwmo",
        # },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=0Z3M4x0V5MY",
        # },
        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, a transferência de calor ajuda a explicar "
                "por que a sala não apresenta temperatura uniforme. Quando uma superfície recebe radiação "
                "solar e se aquece mais do que o ar ao redor, ela passa a transferir energia para as regiões "
                "vizinhas. De forma análoga, superfícies mais frias podem receber energia do ar ou de outros "
                "elementos do ambiente. Assim, a distribuição térmica da sala depende do balanço contínuo "
                "de fluxos de calor entre superfícies, ar e ocupantes."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Calor é energia em trânsito, e não uma propriedade armazenada isoladamente.",
                "A transferência de calor ocorre devido à diferença de temperatura.",
                "O fluxo espontâneo de calor vai da região mais quente para a mais fria.",
                "A quantidade de calor pode ser representada por Q, em joules.",
                "A taxa de transferência de calor pode ser representada por Q̇, em watts.",
                "No ambiente interno, as trocas de calor entre superfícies e ar afetam diretamente o conforto térmico.",
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
                "Uma parede interna separa duas regiões a 32 °C e 28 °C. Considerando apenas a diferença "
                "de temperatura, qual afirmação é fisicamente correta?"
            ),
            "alternativas": {
                "a": "O calor tende a se transferir da região a 28 °C para a de 32 °C",
                "b": "Não há possibilidade de troca térmica porque ambas as temperaturas são positivas",
                "c": "O calor tende a se transferir da região a 32 °C para a de 28 °C",
                "d": "A direção da transferência depende apenas da massa de ar em cada lado",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Uma superfície transfere calor a uma taxa constante de 250 W durante 12 s. "
                "Qual é a quantidade total de calor transferida?"
            ),
            "alternativas": {
                "a": "20,8 J",
                "b": "262 J",
                "c": "2080 J",
                "d": "3000 J",
            },
            "alternativa_correta": "d",
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