from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "sistema_termico_ambiente"

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
                "Em termodinâmica, quando escolhemos a sala de aula como objeto de estudo, "
                "o ar, as paredes e os elementos internos podem ser tratados como:"
            ),
            "alternativas": {
                "a": "Meio externo do problema",
                "b": "Sistema termodinâmico em análise",
                "c": "Fronteira rígida do sistema",
                "d": "Apenas fontes de calor independentes",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "A Lei Zero da Termodinâmica permite afirmar que, se dois sistemas estão em "
                "equilíbrio térmico com um terceiro, então:"
            ),
            "alternativas": {
                "a": "Eles têm necessariamente o mesmo volume",
                "b": "Eles trocam trabalho entre si",
                "c": "Eles estão em equilíbrio térmico entre si",
                "d": "Eles possuem a mesma energia interna total",
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
                "Você demonstrou domínio inicial sobre sistema térmico do ambiente. "
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
                    "Na questão 1, a resposta correta é **b**. Em termodinâmica, o sistema é a "
                    "parte do universo escolhida para análise. Em um estudo de conforto térmico, "
                    "a sala pode ser tratada como sistema, incluindo o ar interno, as superfícies, "
                    "o mobiliário e até os ocupantes, dependendo do recorte adotado."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A Lei Zero da Termodinâmica estabelece "
                    "que, se dois sistemas estão separadamente em equilíbrio térmico com um terceiro, "
                    "então eles também estão em equilíbrio térmico entre si. Esse princípio fundamenta "
                    "o conceito de temperatura e o uso de termômetros."
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
                "Para aplicar a termodinâmica a um ambiente interno, o primeiro passo é definir "
                "qual porção da realidade será estudada. Em física, essa porção recebe o nome de "
                "**sistema termodinâmico**. Tudo aquilo que está fora do sistema é chamado de "
                "**meio externo** ou vizinhança. Essa separação é importante porque a análise "
                "termodinâmica depende de identificar onde ocorrem as trocas de energia e quais "
                "elementos pertencem ao objeto de estudo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Entre o sistema e o meio externo existe a **fronteira**, que é o limite real ou "
                "imaginário que separa essas duas regiões. A fronteira pode permitir ou impedir "
                "trocas de calor, matéria ou trabalho, dependendo do tipo de problema analisado. "
                "No caso de uma sala, as paredes, janelas, portas e superfícies que delimitam o "
                "ambiente podem ser interpretadas como partes dessa fronteira, pois separam o "
                "interior do espaço do meio externo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma vez definido o sistema, passa a ser possível descrever seu **estado térmico**. "
                "Esse estado corresponde à condição física do sistema em um dado momento, podendo ser "
                "caracterizado por grandezas como temperatura, pressão e distribuição de energia. "
                "Quando analisamos uma sala de aula, por exemplo, estamos interessados em como esse "
                "estado varia de um ponto para outro e como ele evolui ao longo do tempo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Um conceito central nesse contexto é o de **equilíbrio térmico**. Dizemos que dois "
                "sistemas ou duas regiões estão em equilíbrio térmico quando, ao serem colocados em "
                "contato, não há troca líquida de calor entre eles. Isso significa que possuem a "
                "mesma temperatura. O equilíbrio térmico é importante porque define a condição em que "
                "não existe tendência espontânea de mudança térmica entre as partes em contato."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A base formal dessa ideia é dada pela **Lei Zero da Termodinâmica**. Ela afirma que, "
                "se dois sistemas estão separadamente em equilíbrio térmico com um terceiro sistema, "
                "então eles também estão em equilíbrio térmico entre si. Esse princípio parece simples, "
                "mas é fundamental porque permite tratar a temperatura como uma grandeza mensurável e "
                "comparável entre diferentes corpos."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "É justamente por causa da Lei Zero que os instrumentos de medição de temperatura fazem "
                "sentido. Quando um sensor ou termômetro entra em contato com uma superfície ou com o ar "
                "de uma sala, ele tende a atingir equilíbrio térmico com aquele ponto. A leitura obtida "
                "passa, então, a representar o estado térmico local do sistema analisado."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=8fo8_m-qP9M",
        # },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=02HqOFprQoc",
        # },
        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, a sala pode ser tratada como um sistema "
                "térmico. O ar interno, as paredes, o piso, o teto, o mobiliário e os ocupantes podem "
                "compor esse sistema, dependendo do recorte escolhido para a análise. Já o ambiente "
                "externo, a radiação solar incidente e as trocas com o exterior podem ser tratados como "
                "parte do meio externo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa forma de organizar o problema ajuda a interpretar corretamente as medições feitas "
                "no ambiente. Quando sensores registram temperaturas diferentes em pontos distintos da "
                "sala, isso indica que o sistema não está em equilíbrio térmico uniforme. Assim, o estudo "
                "do conforto térmico passa a ser uma análise do estado térmico do ambiente, de sua "
                "fronteira e das interações que ele mantém com o meio ao redor."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Sistema termodinâmico é a parte do universo escolhida para análise.",
                "Tudo o que está fora do sistema constitui o meio externo.",
                "A fronteira separa o sistema do meio externo.",
                "O estado térmico descreve a condição física do sistema em determinado instante.",
                "Equilíbrio térmico ocorre quando não há troca líquida de calor entre regiões em contato.",
                "A Lei Zero da Termodinâmica fundamenta o conceito de temperatura.",
                "A sala pode ser tratada como um sistema térmico na análise de conforto.",
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
                "Em um estudo de conforto térmico, tratar a sala como sistema termodinâmico significa:"
            ),
            "alternativas": {
                "a": "Ignorar a existência do ambiente externo",
                "b": "Considerar que apenas o termômetro faz parte da análise",
                "c": "Definir a sala como a porção do universo escolhida para estudo",
                "d": "Assumir que não existem trocas pela fronteira",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Do ponto de vista da Lei Zero da Termodinâmica, qual afirmação é correta?"
            ),
            "alternativas": {
                "a": "Dois sistemas em equilíbrio com um terceiro possuem necessariamente o mesmo volume",
                "b": "Dois sistemas em equilíbrio térmico com um terceiro estão em equilíbrio térmico entre si",
                "c": "A temperatura depende apenas da massa do sistema",
                "d": "Equilíbrio térmico significa ausência total de energia interna",
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