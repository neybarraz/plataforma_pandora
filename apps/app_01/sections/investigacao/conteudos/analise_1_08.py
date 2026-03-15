from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "circulacao_mistura_ar"

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
                "Em uma sala, uma parede aquecida pelo Sol faz o ar próximo a ela subir, enquanto o ar "
                "mais frio desce em outra região. Esse padrão de circulação é explicado principalmente por:"
            ),
            "alternativas": {
                "a": "Anulação das diferenças de densidade no ambiente",
                "b": "Convecção natural gerada por gradientes de temperatura",
                "c": "Ausência de interação entre o ar e as superfícies",
                "d": "Movimento aleatório do ar sem relação com a temperatura",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Em uma sala com móveis, pessoas e superfícies aquecidas, o escoamento do ar tende a apresentar "
                "mistura intensa e variações locais de velocidade. Qual conceito é mais adequado para descrever "
                "esse comportamento menos ordenado do fluxo?"
            ),
            "alternativas": {
                "a": "Equilíbrio térmico estático",
                "b": "Escoamento puramente laminar",
                "c": "Escoamento turbulento",
                "d": "Ausência de gradientes de temperatura",
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
                "Você demonstrou domínio inicial sobre circulação e mistura do ar no ambiente. "
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
                    "Na questão 1, a resposta correta é **b**. Quando existem diferenças de temperatura "
                    "no ambiente, o ar aquecido tende a ficar menos denso e subir, enquanto o ar mais frio "
                    "desce. Esse processo gera correntes convectivas naturais e ajuda a explicar a circulação "
                    "do ar dentro da sala."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. Em ambientes reais, a presença de obstáculos, "
                    "diferenças de temperatura e mudanças de direção do escoamento favorece a formação de um "
                    "fluxo turbulento, com mistura intensa e variações locais de velocidade."
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
                "O ar dentro de uma sala não se move de forma perfeitamente uniforme. Mesmo quando não há "
                "ventilação mecânica, diferenças de temperatura entre paredes, piso, teto, janelas e ocupantes "
                "podem gerar movimentos ascendentes e descendentes do ar. Além disso, a presença de móveis, "
                "pessoas e obstáculos modifica o trajeto do escoamento, produzindo regiões de mistura e de "
                "recirculação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Um dos mecanismos mais importantes nesse processo é a **convecção natural**. Ela ocorre quando "
                "diferenças de temperatura geram diferenças de densidade no ar. O ar aquecido, por se tornar "
                "menos denso, tende a subir; o ar mais frio, relativamente mais denso, tende a descer. Esse "
                "movimento estabelece correntes internas que redistribuem energia térmica dentro do ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essas correntes estão diretamente ligadas aos **gradientes de temperatura**, isto é, às variações "
                "espaciais da temperatura dentro da sala. Quando uma parede recebe radiação solar, por exemplo, o ar "
                "próximo a ela pode se aquecer mais do que o ar em regiões sombreadas. Esse desnível térmico não "
                "apenas altera a temperatura local, mas também impulsiona o movimento do ar."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Para caracterizar o tipo de escoamento, utiliza-se frequentemente o **número de Reynolds**, dado por:\n\n"
                "$$ Re = \\frac{\\rho v L}{\\mu} $$\n\n"
                "em que **$\\rho$** é a densidade do fluido, **v** é a velocidade característica do escoamento, "
                "**L** é uma dimensão característica do problema e **$\\mu$** é a viscosidade dinâmica. Essa grandeza "
                "permite comparar os efeitos das forças inerciais com os efeitos viscosos no fluido."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando o número de Reynolds é relativamente baixo, o escoamento tende a ser mais **laminar**, "
                "ou seja, mais organizado e com trajetórias mais regulares. Quando o número de Reynolds é maior, "
                "o escoamento tende a se tornar **turbulento**, com flutuações de velocidade, formação de vórtices "
                "e mistura mais intensa entre diferentes regiões do ar."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em ambientes internos reais, o ar raramente apresenta um movimento completamente ordenado. "
                "A geometria da sala, a presença de mesas, cadeiras, pessoas, portas e janelas, além do "
                "aquecimento desigual das superfícies, favorece o surgimento de regiões em que o escoamento "
                "muda de direção, desacelera, acelera ou recircula. Por isso, a distribuição do ar no ambiente "
                "é geralmente heterogênea."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=V4PpQf4Wf2Q",
        # },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=1L2ef1CP-yw",
        # },
        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, a circulação e a mistura do ar ajudam a explicar "
                "por que diferentes pontos da sala podem apresentar temperaturas distintas. Paredes aquecidas "
                "fazem o ar subir, enquanto regiões mais frias favorecem movimentos descendentes. Ao mesmo tempo, "
                "móveis, pessoas e paredes desviam o escoamento e podem gerar pequenas regiões de recirculação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Como resultado, o calor não se distribui de forma uniforme no espaço. Algumas regiões podem "
                "receber mais ar aquecido, enquanto outras permanecem relativamente menos ventiladas ou mais frias. "
                "Essa mistura desigual do ar está diretamente relacionada à sensação térmica dos ocupantes e ao "
                "conforto térmico dentro da sala."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A convecção natural surge quando diferenças de temperatura produzem diferenças de densidade no ar.",
                "Gradientes de temperatura impulsionam movimentos ascendentes e descendentes dentro da sala.",
                "O número de Reynolds ajuda a caracterizar o regime do escoamento.",
                "Escoamentos laminares tendem a ser mais organizados; escoamentos turbulentos apresentam mistura intensa.",
                "Móveis, pessoas, paredes e aberturas alteram o caminho do ar e favorecem recirculações.",
                "A circulação e a mistura do ar explicam por que diferentes regiões da sala têm temperaturas diferentes.",
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
                "Em uma sala com uma parede aquecida e outra região mais fria, qual processo ajuda a explicar "
                "a formação de correntes de ar que sobem e descem no ambiente?"
            ),
            "alternativas": {
                "a": "Convecção natural associada a diferenças de temperatura",
                "b": "Ausência de gradientes térmicos no ambiente",
                "c": "Equilíbrio térmico completo em toda a sala",
                "d": "Movimento do ar independente da densidade",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Quando o ar de uma sala encontra móveis, pessoas e mudanças de direção do escoamento, é comum "
                "surgirem regiões de mistura intensa. Esse comportamento está mais associado a:"
            ),
            "alternativas": {
                "a": "Escoamento perfeitamente laminar",
                "b": "Ausência de interação entre o fluido e o ambiente",
                "c": "Escoamento turbulento",
                "d": "Velocidade nula em todo o recinto",
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