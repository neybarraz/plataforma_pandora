from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "direcao_transformacoes_termicas"

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
                "De acordo com a Segunda Lei da Termodinâmica, o calor tende a se transferir "
                "espontaneamente:"
            ),
            "alternativas": {
                "a": "Da região mais fria para a mais quente",
                "b": "Da região mais quente para a mais fria",
                "c": "Apenas entre sistemas de mesma temperatura",
                "d": "Somente quando não há diferença de energia interna",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Em uma sala inicialmente com regiões a temperaturas diferentes, o que se espera ao longo do tempo, "
                "na ausência de novas entradas de energia?"
            ),
            "alternativas": {
                "a": "Os gradientes térmicos aumentam indefinidamente",
                "b": "A região mais fria se torna mais fria sem troca com o restante da sala",
                "c": "As diferenças de temperatura tendem a diminuir em direção ao equilíbrio",
                "d": "A entropia do sistema necessariamente diminui"
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
                "Você demonstrou domínio inicial sobre a direção das transformações térmicas. "
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
                    "Na questão 1, a resposta correta é **b**. A Segunda Lei da Termodinâmica "
                    "indica que o calor se transfere espontaneamente da região de maior temperatura "
                    "para a de menor temperatura. O sentido oposto não ocorre de forma natural sem "
                    "intervenção externa."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. Em um sistema sem novas entradas de energia, "
                    "as diferenças de temperatura tendem a diminuir ao longo do tempo. Esse processo expressa "
                    "a tendência do sistema ao equilíbrio térmico."
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
                "Depois de compreender o sistema térmico do ambiente e o balanço de energia, é necessário "
                "dar um passo além: entender **em que direção** os processos térmicos ocorrem. A termodinâmica "
                "não trata apenas da quantidade de energia presente em um sistema, mas também da forma como "
                "essa energia se distribui e da tendência natural das transformações."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esse aspecto é descrito pela **Segunda Lei da Termodinâmica**. Ela mostra que os processos "
                "térmicos possuem uma direção preferencial. Em particular, o calor tende a se transferir "
                "espontaneamente das regiões de maior temperatura para as de menor temperatura. Assim, não "
                "basta saber que existe energia térmica no sistema: é preciso analisar para onde essa energia "
                "tende a fluir."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa ideia está diretamente ligada à redução dos **gradientes térmicos**. Se duas regiões "
                "de um ambiente apresentam temperaturas diferentes, as trocas de calor entre elas tendem a "
                "diminuir essa diferença ao longo do tempo. Em outras palavras, o sistema evolui naturalmente "
                "em direção ao **equilíbrio térmico**, isto é, a uma condição em que não existe troca líquida "
                "de calor entre as partes em contato."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Outro conceito importante nesse contexto é a **irreversibilidade**. Muitos processos naturais "
                "ocorrem espontaneamente em um sentido, mas não retornam sozinhos ao estado inicial. Um corpo "
                "quente pode aquecer um corpo frio até que as temperaturas se aproximem, mas o processo inverso "
                "— o corpo frio aquecer espontaneamente o corpo quente — não ocorre sem ação externa. Isso mostra "
                "que os processos térmicos reais possuem um sentido preferencial."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A grandeza que ajuda a descrever essa tendência é a **entropia**. De forma qualitativa, a "
                "entropia está associada à dispersão da energia e à evolução do sistema para estados mais "
                "prováveis. Em processos reversíveis, a variação de entropia pode ser representada por:\n\n"
                "$$ \\Delta S = \\frac{Q_{rev}}{T} $$\n\n"
                "Neste contexto, o mais importante é interpretar seu significado físico: sistemas tendem a "
                "evoluir para estados em que a energia esteja mais distribuída, e não mais concentrada em "
                "diferenças térmicas intensas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Por isso, a Segunda Lei complementa a Primeira Lei. A Primeira Lei informa quanto a energia "
                "varia; a Segunda Lei indica como essa transformação acontece e qual é sua direção natural. "
                "Duas situações podem envolver a mesma quantidade de energia, mas apenas algumas delas são "
                "compatíveis com a evolução espontânea do sistema."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=YvsmfM2Vwmo",
        # },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=KcKj7NQK8mA",
        # },
        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, essa direção preferencial aparece de forma clara. "
                "Paredes aquecidas pela radiação solar tendem a transferir energia para o ar e para superfícies "
                "mais frias ao redor. Da mesma forma, regiões da sala com temperaturas mais elevadas tendem a "
                "ceder calor para regiões de menor temperatura, reduzindo gradientes térmicos com o passar do tempo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Entretanto, a sala nunca é perfeitamente uniforme, porque o sistema recebe continuamente novas "
                "entradas de energia. A radiação solar incidente, a presença de ocupantes, o funcionamento de "
                "equipamentos e a ventilação podem manter ou recriar desuniformidades térmicas. Assim, o ambiente "
                "tende ao equilíbrio, mas nem sempre o alcança completamente, pois as condições externas continuam "
                "alterando o sistema."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa leitura é essencial para compreender o conforto térmico. Quando diferentes regiões da sala "
                "apresentam temperaturas distintas, não se trata apenas de um estado momentâneo, mas da manifestação "
                "de processos térmicos em evolução. Observar onde o calor tende a se redistribuir ajuda a interpretar "
                "por que algumas zonas permanecem mais quentes, outras mais frias, e por que o ambiente pode manter "
                "gradientes térmicos mesmo ao longo de várias horas."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A Segunda Lei da Termodinâmica define a direção espontânea dos processos térmicos.",
                "O calor tende a fluir espontaneamente da região mais quente para a mais fria.",
                "Gradientes térmicos tendem a diminuir ao longo do tempo.",
                "Processos térmicos reais são, em geral, irreversíveis.",
                "A entropia está associada à dispersão da energia e à tendência ao equilíbrio.",
                "No ambiente interno, novas entradas de energia podem manter desuniformidades térmicas.",
                "A sala tende ao equilíbrio, mas nem sempre se torna perfeitamente uniforme.",
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
                "Em uma sala, uma parede aquecida transfere energia para o ar e para superfícies mais frias. "
                "Esse processo ilustra principalmente:"
            ),
            "alternativas": {
                "a": "A tendência do calor a fluir espontaneamente da região mais quente para a mais fria",
                "b": "A inexistência de gradientes térmicos em sistemas reais",
                "c": "A redução obrigatória da entropia em qualquer processo térmico",
                "d": "A impossibilidade de trocas de energia em ambientes internos",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Mesmo após algum tempo, uma sala pode continuar apresentando regiões com temperaturas diferentes. "
                "Qual explicação é mais adequada?"
            ),
            "alternativas": {
                "a": "A Segunda Lei impede qualquer tendência ao equilíbrio",
                "b": "A sala é incapaz de trocar energia com o meio externo",
                "c": "Novas entradas de energia, como radiação solar, podem manter desuniformidades térmicas",
                "d": "O calor flui espontaneamente da região mais fria para a mais quente",
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