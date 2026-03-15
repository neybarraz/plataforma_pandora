from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "equilibrio_termico"

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
                "Dois corpos colocados em contato térmico tendem ao equilíbrio térmico quando:"
            ),
            "alternativas": {
                "a": "Passam a possuir a mesma quantidade de calor",
                "b": "Atingem a mesma temperatura e cessa a troca líquida de calor entre eles",
                "c": "Apresentam a mesma massa e o mesmo material",
                "d": "Suas energias internas totais tornam-se iguais",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Um corpo a 80 °C é colocado em contato com outro a 20 °C, em um sistema isolado. "
                "Se ambos possuem mesma massa e mesmo calor específico, a temperatura de equilíbrio será:"
            ),
            "alternativas": {
                "a": "20 °C",
                "b": "30 °C",
                "c": "40 °C",
                "d": "50 °C",
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
                "Você demonstrou domínio inicial sobre o conceito de equilíbrio térmico. "
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
                    "Na questão 1, a resposta correta é **b**. O equilíbrio térmico ocorre quando os sistemas "
                    "atingem a mesma temperatura. Nessa condição, deixa de existir fluxo líquido de calor entre eles, "
                    "embora as interações microscópicas continuem ocorrendo."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **d**. Em um sistema isolado, com corpos de mesma massa e "
                    "mesmo calor específico, a temperatura de equilíbrio é a média aritmética: "
                    "**$T_eq = (80 + 20)/2 = 50 °C$**."
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
                "Equilíbrio térmico é o estado em que dois ou mais sistemas, após interagirem termicamente, "
                "atingem a mesma temperatura e deixam de apresentar troca líquida de calor entre si. Esse conceito "
                "é central na termodinâmica porque define a condição em que o desnível térmico desaparece. Enquanto "
                "existir diferença de temperatura, haverá tendência de transferência de energia térmica da região "
                "mais quente para a mais fria."
            ),
        },
        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "A formulação conceitual desse processo está associada à **Lei Zero da Termodinâmica**. "
        #         "Ela estabelece que, se um sistema A está em equilíbrio térmico com um sistema B, e B está em "
        #         "equilíbrio térmico com um sistema C, então A também está em equilíbrio térmico com C. Essa ideia "
        #         "permite definir a temperatura como uma grandeza física mensurável e comparável entre sistemas."
        #     ),
        # },
        {
            "tipo": "texto",
            "texto": (
                "Em problemas simples de troca de calor, a condição de equilíbrio pode ser escrita impondo que a "
                "soma algébrica das quantidades de calor trocadas seja nula:\n\n"
                "$$ \\sum Q = 0 $$\n\n"
                "Quando não há perdas para o ambiente, o calor cedido pelos corpos mais quentes é igual, em módulo, "
                "ao calor recebido pelos corpos mais frios. Em muitos casos, usa-se também a relação:\n\n"
                "$$ Q = mc\\Delta T $$\n\n"
                "onde **m** é a massa, **c** o calor específico e **$\\Delta T$** a variação de temperatura. "
                "Essa equação permite calcular a temperatura final de equilíbrio a partir do balanço energético."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Microscopicamente, o equilíbrio térmico corresponde a uma situação em que, apesar de as partículas "
                "continuarem em movimento e colisão, não existe mais tendência líquida de redistribuição de energia "
                "entre os sistemas em contato. O estado macroscópico torna-se estável em relação à temperatura. "
                "Por isso, equilíbrio térmico não significa ausência de movimento molecular, mas ausência de fluxo "
                "líquido de calor causado por diferença de temperatura."
            ),
        },
        # {
        #     "tipo": "imagem",
        #     "arquivo": "equilibrio_termico_esquema.png",
        #     "legenda": (
        #         "Esquema de dois corpos em contato térmico evoluindo para a mesma temperatura."
        #     ),
        #     "fonte": "Material do projeto",
        # },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=pCqBui3RhqI",
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=KcKj7NQK8mA",
        # },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, o equilíbrio térmico ajuda a interpretar por que a sala de aula raramente "
                "permanece em condição térmica uniforme. Superfícies expostas ao Sol, regiões próximas às janelas "
                "e zonas com maior circulação de ar podem apresentar temperaturas diferentes, indicando que o ambiente "
                "ainda não atingiu equilíbrio térmico interno. Se as trocas de energia entre ar, paredes, piso, teto "
                "e mobiliário continuarem ocorrendo, haverá gradientes térmicos espaciais mensuráveis."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando as medições mostram temperaturas distintas em diferentes pontos da sala, isso evidencia que "
                "o sistema está apenas em equilíbrio parcial ou fora do equilíbrio térmico global. Essa leitura é "
                "fundamental para o experimento, porque permite relacionar os dados medidos com o comportamento físico "
                "do ambiente: onde ainda há desnível térmico, ainda há potencial de troca de calor e possibilidade de "
                "desconforto térmico para os ocupantes."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Equilíbrio térmico ocorre quando os sistemas atingem a mesma temperatura.",
                "No equilíbrio, a troca líquida de calor entre os corpos é nula.",
                # "A Lei Zero da Termodinâmica fundamenta o conceito de temperatura.",
                "Em sistema isolado, o calor cedido é igual ao calor recebido.",
                "A equação Q = mcΔT é usada para analisar trocas de calor em direção ao equilíbrio.",
                "Equilíbrio térmico não significa ausência de agitação microscópica.",
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
                "Em uma sala de aula, duas regiões apresentam 27 °C e 27 °C, sem influência relevante de radiação "
                "local ou correntes de ar entre elas. A interpretação mais adequada é:"
            ),
            "alternativas": {
                "a": "As duas regiões necessariamente possuem a mesma energia interna total",
                "b": "As duas regiões podem estar em equilíbrio térmico entre si",
                "c": "Não pode haver equilíbrio térmico em um ambiente aberto",
                "d": "As superfícies próximas devem ter obrigatoriamente temperatura maior que 27 °C",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Dois corpos, de mesma massa e mesmo calor específico, estão inicialmente a 60 °C e 30 °C, "
                "isolados do ambiente e colocados em contato. Qual será a temperatura de equilíbrio?"
            ),
            "alternativas": {
                "a": "35 °C",
                "b": "40 °C",
                "c": "45 °C",
                "d": "50 °C",
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