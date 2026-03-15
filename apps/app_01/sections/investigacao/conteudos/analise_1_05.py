from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "mecanismo_de_transferencia_calor"

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
                "Uma parede externa de concreto recebe radiação solar direta durante a tarde. "
                "Após algum tempo, observa-se que a face interna da parede também se aquece, "
                "mesmo sem incidência direta de radiação. Qual mecanismo explica principalmente "
                "a propagação da energia térmica através da espessura da parede?"
            ),
            "alternativas": {
                "a": "Convecção do ar através da parede",
                "b": "Condução térmica no interior do material",
                "c": "Radiação eletromagnética atravessando o sólido",
                "d": "Movimento macroscópico de partículas do material",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Em uma sala aquecida pelo Sol, o ar próximo a uma janela iluminada torna-se mais quente "
                "e sobe lentamente, enquanto ar mais frio desce para ocupar seu lugar. Esse movimento "
                "estabelece uma circulação de ar no ambiente. Qual mecanismo de transferência de calor "
                "está principalmente associado a esse fenômeno?"
            ),
            "alternativas": {
                "a": "Condução térmica no ar",
                "b": "Radiação térmica entre as superfícies",
                "c": "Convecção natural do fluido",
                "d": "Difusão térmica independente do movimento do fluido",
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
                "A transferência de calor pode ocorrer por três mecanismos clássicos: **condução**, "
                "**convecção** e **radiação**. Esses mecanismos descrevem diferentes formas de "
                "propagação da energia térmica quando existe diferença de temperatura entre regiões "
                "de um sistema. Em ambientes reais, como uma sala de aula ou um espaço interno, esses "
                "processos geralmente atuam ao mesmo tempo e determinam como a energia térmica se "
                "distribui no ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Na **condução**, a energia se propaga por interação microscópica entre partículas "
                "vizinhas, sem que haja transporte macroscópico de matéria. Esse mecanismo é "
                "especialmente importante em sólidos, como paredes, pisos, coberturas e mobiliário. "
                "Quando uma face de um material está mais quente que outra, a energia térmica tende "
                "a se propagar internamente através do corpo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A condução térmica é descrita pela **Lei de Fourier**, segundo a qual o fluxo de "
                "calor é proporcional ao gradiente de temperatura presente no material. Em sua forma "
                "vetorial, essa lei pode ser escrita como:\n\n"
                "$$ \\vec{q} = -k\\,\\nabla T $$\n\n"
                "em que **$\\vec{q}$** representa o fluxo de calor por unidade de área, **k** é a "
                "condutividade térmica do material e **$\\nabla T$** é o gradiente de temperatura. "
                "O sinal negativo indica que o calor se propaga no sentido de temperaturas menores."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em uma parede plana, por exemplo, a condução pode ser aproximada por:\n\n"
                "$$ \\dot{Q} = kA\\frac{\\Delta T}{L} $$\n\n"
                "onde **k** é a condutividade térmica do material, **A** é a área da superfície, "
                "**$\\Delta T$** é a diferença de temperatura entre as faces e **L** é a espessura "
                "da parede. Esse modelo ajuda a entender como o calor atravessa paredes e divisórias "
                "quando existe diferença de temperatura entre ambientes ou entre o interior e o exterior."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Na **convecção**, a transferência de calor ocorre com o movimento do fluido. Em um "
                "ambiente interno, esse fluido é geralmente o ar. Quando o ar em contato com uma "
                "superfície aquecida recebe energia térmica, ele tende a se expandir, tornando-se "
                "menos denso e subindo. Ao mesmo tempo, regiões de ar mais frio descem para ocupar "
                "seu lugar, estabelecendo correntes de circulação no ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esse processo pode ser modelado, em primeira aproximação, pela relação:\n\n"
                "$$ \\dot{Q} = hA\\,(T_s - T_f) $$\n\n"
                "em que **h** é o coeficiente convectivo, **A** é a área da superfície, **$T_s$** "
                "é a temperatura da superfície e **$T_f$** é a temperatura do fluido. Esse mecanismo "
                "é responsável pela troca de calor entre paredes, piso, teto e o ar do ambiente, "
                "influenciando diretamente a distribuição de temperatura dentro da sala."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Na **radiação**, a transferência de energia ocorre por meio de ondas eletromagnéticas "
                "e não requer um meio material. Toda superfície com temperatura acima do zero absoluto "
                "emite radiação térmica. No ambiente interno, esse mecanismo aparece tanto na entrada "
                "de radiação solar pelas janelas quanto na troca radiativa entre superfícies internas, "
                "objetos e ocupantes."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=R8xvZQ7zkUE",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=nKUjAKkAnkU",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=8ra9SD-8xJc",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=DHgtlKhH0ok",
        },

        
        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, os três mecanismos atuam de forma "
                "combinada. A radiação solar pode aquecer uma parede ou o piso próximo à janela. "
                "Esse aquecimento se propaga pelo interior do material por condução e, em seguida, "
                "parte dessa energia é transferida para o ar do ambiente por convecção."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O aquecimento das superfícies também pode gerar movimentos de ar no interior da "
                "sala. Quando o ar próximo a uma parede aquecida se torna mais quente, ele tende "
                "a subir, enquanto ar mais frio se desloca para ocupar a região inferior. Esse "
                "processo cria correntes convectivas que redistribuem energia térmica pelo espaço."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Assim, a temperatura medida em diferentes pontos do ambiente resulta da interação "
                "entre radiação, condução e convecção. As propriedades térmicas das paredes, a "
                "incidência de radiação solar e o movimento do ar influenciam diretamente o campo "
                "de temperatura da sala e, consequentemente, o conforto térmico dos ocupantes."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A transferência de calor ocorre por condução, convecção e radiação.",
                "A condução descreve a propagação de calor dentro de sólidos, como paredes e pisos.",
                "A Lei de Fourier modela matematicamente o fluxo de calor em materiais sólidos.",
                "A convecção envolve o movimento do fluido, como o ar dentro de uma sala.",
                "A radiação permite transferência de energia sem necessidade de meio material.",
                "Em ambientes internos, os três mecanismos atuam simultaneamente e determinam o conforto térmico.",
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
                "Durante a tarde, a radiação solar atravessa a janela e aquece o piso próximo a ela. "
                "Depois de algum tempo, a região do piso permanece quente e o calor se propaga "
                "gradualmente para outras partes do material. Qual mecanismo de transferência de "
                "calor explica principalmente essa propagação dentro do piso?"
            ),
            "alternativas": {
                "a": "Convecção do ar sobre a superfície",
                "b": "Condução térmica no material sólido",
                "c": "Radiação térmica emitida pelo piso",
                "d": "Movimento macroscópico do material do piso",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Em uma sala aquecida pelo Sol, o ar próximo a uma parede aquecida sobe enquanto "
                "o ar mais frio desce para ocupar seu lugar, formando correntes de circulação "
                "no ambiente. Esse processo está associado principalmente a qual mecanismo "
                "de transferência de calor?"
            ),
            "alternativas": {
                "a": "Condução térmica no ar",
                "b": "Radiação entre superfícies",
                "c": "Convecção natural do ar",
                "d": "Difusão molecular independente da temperatura",
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