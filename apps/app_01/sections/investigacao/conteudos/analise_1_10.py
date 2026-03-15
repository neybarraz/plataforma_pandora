from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "balanco_energia_termica"

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
    acerto_q2 = _acertou(Q_D_002, "b")
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
                "Pela Primeira Lei da Termodinâmica, a variação da energia interna de um sistema "
                "está associada a:"
            ),
            "alternativas": {
                "a": "Apenas à temperatura do meio externo",
                "b": "Apenas ao calor recebido pelo sistema",
                "c": "Ao calor trocado e ao trabalho realizado",
                "d": "Somente à massa total do sistema",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Um sistema recebe 600 J de calor e realiza 250 J de trabalho sobre o meio externo. "
                "Qual é a variação de sua energia interna?"
            ),
            "alternativas": {
                "a": "850 J",
                "b": "350 J",
                "c": "250 J",
                "d": "-350 J",
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
                "Você demonstrou domínio inicial sobre o balanço de energia térmica. "
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
                    "Na questão 1, a resposta correta é **c**. Pela Primeira Lei da Termodinâmica, "
                    "a variação da energia interna depende do calor trocado com o meio e do trabalho "
                    "realizado. A energia de um sistema pode aumentar ou diminuir conforme essas trocas."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **b**. Usando a relação "
                    "**$\\Delta U = Q - W$** com **$Q = 600\\,J$** e **$W = 250\\,J$**, obtemos "
                    "**$\\Delta U = 600 - 250 = 350\\,J$**."
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
                "Depois de definir o ambiente como um sistema térmico, o passo seguinte é compreender "
                "como sua energia pode variar. Em termodinâmica, essa análise é feita por meio do "
                "**balanço de energia**, que relaciona as trocas entre o sistema e o meio externo. "
                "No caso de uma sala, o ar interno, as superfícies e os objetos podem receber ou perder "
                "energia ao longo do dia, alterando o estado térmico do ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma grandeza central nesse contexto é a **energia interna**. Ela representa a energia "
                "associada ao estado microscópico do sistema, incluindo a agitação térmica das partículas "
                "e as interações entre elas. Em um ambiente interno, a energia interna do ar e das superfícies "
                "varia quando há aquecimento, resfriamento ou transformações associadas às trocas com o meio."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Duas formas principais de alterar a energia interna de um sistema são o **calor** e o "
                "**trabalho**. O calor corresponde à energia transferida devido a uma diferença de temperatura. "
                "Já o trabalho está associado à transferência de energia por ação de forças e deslocamentos. "
                "Em um gás, por exemplo, expansão e compressão podem envolver trabalho realizado pelo sistema "
                "ou sobre ele."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A relação entre essas grandezas é estabelecida pela **Primeira Lei da Termodinâmica**, "
                "que expressa a conservação da energia em sistemas térmicos. Em uma forma usual, essa lei "
                "é escrita como:\n\n"
                "$$ \\Delta U = Q - W $$\n\n"
                "onde **$\\Delta U$** é a variação da energia interna, **Q** é o calor recebido pelo sistema "
                "e **W** é o trabalho realizado pelo sistema sobre o meio externo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa equação mostra que a energia interna aumenta quando o sistema recebe calor e diminui "
                "quando ele realiza trabalho sobre o exterior. Em outras palavras, a energia do sistema não "
                "aparece nem desaparece espontaneamente: ela muda de forma ou é transferida através das "
                "interações com o meio."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Considere, por exemplo, uma situação em que o sistema recebe calor de uma superfície aquecida. "
                "Se parte dessa energia permanece no sistema, sua energia interna aumenta. Se, além disso, o "
                "sistema realiza trabalho, como no caso de expansão de um fluido, parte da energia recebida "
                "é transferida para fora. O balanço final depende justamente da diferença entre o calor "
                "recebido e o trabalho realizado."
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
                "No ambiente interno que estamos analisando, esse balanço de energia aparece de forma contínua. "
                "A radiação solar aquece paredes, piso e mobiliário; essas superfícies podem transferir calor "
                "para o ar; e o próprio ar pode trocar energia com janelas, objetos e ocupantes. Assim, a "
                "energia interna do ambiente não é constante, mas varia de acordo com as entradas e saídas de energia."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além disso, movimentos do ar e expansões locais do fluido podem estar associados a trabalho. "
                "Embora, em muitos problemas de conforto térmico, o calor seja o aspecto mais evidente, o "
                "raciocínio termodinâmico completo exige reconhecer que o estado energético do ambiente resulta "
                "da combinação entre calor trocado e trabalho realizado."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A energia interna representa a energia associada ao estado microscópico do sistema.",
                "Calor é energia transferida devido à diferença de temperatura.",
                "Trabalho é uma forma de transferência de energia associada a forças e deslocamentos.",
                "A Primeira Lei da Termodinâmica expressa a conservação da energia.",
                "A relação $\\Delta U = Q - W$ conecta calor, trabalho e energia interna.",
                "No ambiente interno, a energia térmica varia ao longo do dia devido às trocas com o meio.",
                "Radiação solar, superfícies aquecidas e movimentos do ar participam do balanço energético da sala.",
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
                "Em um ambiente interno, uma superfície aquecida transfere calor ao ar da sala. "
                "À luz da Primeira Lei da Termodinâmica, isso significa que:"
            ),
            "alternativas": {
                "a": "A energia interna do ar pode se alterar devido à troca de calor",
                "b": "A temperatura do ar não pode variar em sistema real",
                "c": "O calor recebido não interfere no estado energético do sistema",
                "d": "A energia interna depende apenas do volume da sala",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Um sistema recebe 900 J de calor e realiza 300 J de trabalho sobre o meio externo. "
                "Qual é a variação de energia interna do sistema?"
            ),
            "alternativas": {
                "a": "1200 J",
                "b": "900 J",
                "c": "600 J",
                "d": "-600 J",
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