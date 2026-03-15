from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "temperatura"

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

    acerto_q1 = _acertou(Q_D_001, "c")
    acerto_q2 = _acertou(Q_D_002, "a")
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
                "Do ponto de vista microscópico, a temperatura de um sistema está mais "
                "diretamente associada a qual grandeza física?"
            ),
            "alternativas": {
                "a": "Quantidade total de energia interna armazenada no sistema",
                "b": "Quantidade de calor contida no corpo",
                "c": "Agitação térmica média das partículas do sistema",
                "d": "Capacidade térmica total do material",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Um termômetro em Celsius registra 25 °C em uma superfície. "
                "Qual é o valor correspondente dessa temperatura na escala Kelvin?"
            ),
            "alternativas": {
                "a": "298 K",
                "b": "248 K",
                "c": "273 K",
                "d": "310 K",
            },
            "alternativa_correta": "a",
        },
    ]


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre o conceito de temperatura. "
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
                    "Na questão 1, a resposta correta é **c**. "
                    "A temperatura está associada ao estado térmico do sistema e se relaciona, "
                    "em nível microscópico, à agitação térmica média de suas partículas. "
                    "Ela não é sinônimo de calor nem corresponde, sozinha, à energia interna total."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **a**. "
                    "A conversão entre Celsius e Kelvin é dada por **T(K) = T(°C) + 273,15**. "
                    "Assim, para 25 °C, obtém-se aproximadamente **298 K**."
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
                "Temperatura é a grandeza física que expressa o estado térmico de um sistema e "
                "permite comparar quão quente ou frio ele está em relação a outro. Em termos "
                "microscópicos, ela está associada à energia cinética média das partículas, isto é, "
                "ao grau de agitação térmica presente no material. Por isso, dois corpos podem ter a "
                "mesma temperatura mesmo possuindo massas, volumes e energias internas diferentes."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A teoria cinética dos gases fornece uma leitura microscópica mais precisa desse conceito. "
                "Em um gás, as moléculas se movem continuamente de forma desordenada, colidindo entre si "
                "e com as superfícies do ambiente. Nessa perspectiva, a temperatura mede a energia cinética "
                "média das moléculas. Para um gás ideal, essa relação pode ser expressa por:\n\n"
                "$$ \\langle E_c \\rangle = \\frac{3}{2} k_B T $$\n\n"
                "onde **$\\langle E_c \\rangle$** é a energia cinética média por molécula, "
                "**$k_B$** é a constante de Boltzmann e **$T$** é a temperatura absoluta em Kelvin. "
                "Assim, elevar a temperatura significa aumentar, em média, a agitação molecular do ar."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Um princípio fundamental que sustenta o conceito de temperatura é a **Lei Zero da "
                "Termodinâmica**. Ela afirma que, se dois sistemas estão em equilíbrio térmico com um "
                "terceiro sistema, então eles também estão em equilíbrio térmico entre si. Em termos "
                "práticos, isso significa que todos esses sistemas possuem a mesma temperatura."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esse princípio é essencial porque permite definir a temperatura como uma grandeza "
                "mensurável. Quando um termômetro entra em contato com um corpo e atinge equilíbrio "
                "térmico com ele, assume-se que ambos possuem a mesma temperatura. Assim, a Lei Zero "
                "fundamenta o funcionamento dos instrumentos de medição e torna possível comparar o "
                "estado térmico de diferentes sistemas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Na física, a escala absoluta é a Kelvin, pois ela se conecta diretamente aos modelos "
                "termodinâmicos e à descrição microscópica da matéria. A relação entre as escalas pode ser "
                "escrita como:\n\n"
                "$$ T(K) = T(°C) + 273,15 $$\n\n"
                "Uma forma comparativa entre Celsius, Fahrenheit e Kelvin é:\n\n"
                "$$ \\frac{T_C}{100} = \\frac{T_F - 32}{180} = \\frac{T_K - 273,15}{100} $$\n\n"
                "Essas transformações são lineares: as escalas diferem por deslocamentos de origem e por "
                "fatores de escala, mas preservam a proporcionalidade entre variações de temperatura. "
                "Por isso, em muitos problemas físicos, as diferenças de temperatura **($\\Delta T$)** "
                "são mais relevantes do que os valores absolutos, pois ajudam a analisar a intensidade e "
                "a direção das trocas de energia térmica."
            ),
        },

        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=8fo8_m-qP9M",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=02HqOFprQoc",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=QnNk82CX2Es",
        },

        {
            "tipo": "texto",
            "texto": (
                "No diagnóstico térmico de um ambiente, a temperatura não deve ser interpretada como um valor "
                "isolado, mas como parte de um balanço de trocas. Quando se mede a temperatura do ar em "
                "diferentes pontos de uma sala, não se está medindo calor armazenado, mas uma grandeza capaz "
                "de indicar como o estado térmico varia espacialmente no ambiente. Essas diferenças ajudam a "
                "identificar regiões com maior ou menor agitação molecular média e, portanto, regiões com "
                "potencial distinto de troca térmica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, a temperatura do ar e a temperatura das superfícies ajudam a "
                "explicar por que alguns pontos da sala parecem mais quentes ou mais frios. Uma parede "
                "atingida por radiação solar pode apresentar temperatura superior à do restante do ambiente, "
                "alterando a sensação térmica nas regiões próximas. Sob a ótica microscópica, isso significa "
                "que, nessas regiões, as moléculas do ar tendem a apresentar maior energia cinética média, "
                "enquanto em áreas mais frias essa agitação é menor. Ao medir esses valores em vários pontos, "
                "torna-se possível interpretar o campo térmico da sala e reconhecer gradientes espaciais "
                "relevantes para a análise de conforto térmico."
            ),
        },

        {
            "tipo": "lista",
            "itens": [
                "Temperatura não é sinônimo de calor.",
                "A temperatura está ligada à agitação térmica média das partículas.",
                "A Lei Zero da Termodinâmica define o conceito de equilíbrio térmico.",
                "A teoria cinética dos gases relaciona temperatura à energia cinética média molecular.",
                "A escala Kelvin é a escala absoluta usada em termodinâmica.",
                "Diferenças de temperatura indicam possibilidade de trocas de energia térmica.",
                "Mapear temperaturas em uma sala permite identificar regiões termicamente distintas.",
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
                "Dois pontos de uma sala apresentam 24 °C e 30 °C. Essa diferença indica, do ponto "
                "de vista físico, que:"
            ),
            "alternativas": {
                "a": "Os dois pontos possuem necessariamente a mesma energia interna",
                "b": "Não pode haver troca térmica entre regiões do ambiente",
                "c": "Existe uma desuniformidade térmica que pode favorecer trocas de calor",
                "d": "As superfícies próximas a esses pontos têm obrigatoriamente a mesma temperatura",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Em um experimento, uma região da sala foi medida em 31 °C. "
                "Qual é o valor correspondente, aproximadamente, em Kelvin?"
            ),
            "alternativas": {
                "a": "242 K",
                "b": "304 K",
                "c": "273 K",
                "d": "331 K",
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
