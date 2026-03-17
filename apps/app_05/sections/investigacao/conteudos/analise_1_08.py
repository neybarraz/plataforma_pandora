from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "relacoes_circuito_comprimento_circuito"

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
                "Em um circuito de alimentação de motor, dois cabos possuem o mesmo material e "
                "a mesma seção transversal, mas um deles possui comprimento significativamente "
                "maior. Considerando o comportamento elétrico do circuito, conclui-se que:"
            ),
            "alternativas": {
                "a": "O comprimento não influencia o circuito se a seção do cabo for a mesma",
                "b": "O aumento do comprimento eleva a resistência elétrica do condutor e pode aumentar a queda de tensão",
                "c": "O comprimento reduz a corrente elétrica do motor independentemente da tensão",
                "d": "O comprimento apenas influencia o aquecimento do motor, não do condutor",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Ao calcular a resistência elétrica de um circuito monofásico que alimenta um "
                "motor localizado a certa distância do quadro elétrico, como deve ser considerado "
                "o comprimento do percurso elétrico no cálculo da resistência do circuito?"
            ),
            "alternativas": {
                "a": "Considera-se apenas o comprimento físico entre o quadro e o motor",
                "b": "Considera-se apenas o comprimento do condutor de fase",
                "c": "Considera-se o percurso completo de ida e retorno da corrente no circuito",
                "d": "O comprimento não é necessário para o cálculo da resistência elétrica",
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
                "Você demonstrou domínio inicial sobre a influência do comprimento do circuito "
                "no comportamento elétrico de condutores e na queda de tensão em instalações elétricas."
            ),
        }
    ]


def _blocos_correcao_diagnostico() -> list[dict]:
    resultado = _get_diag_result()

    blocos: list[dict] = [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": (
                "Uma ou mais respostas do diagnóstico não estavam corretas. "
                "Revise os conceitos fundamentais abaixo."
            ),
        }
    ]

    if not resultado.get("q1_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "A resistência elétrica de um condutor depende diretamente de seu comprimento. "
                    "Essa relação é descrita pela expressão:\n\n"
                    "$$ R = \\rho \\frac{L}{A} $$\n\n"
                    "onde **R** é a resistência elétrica do condutor, **ρ** é a resistividade do material, "
                    "**L** é o comprimento do condutor e **A** é a área de sua seção transversal. "
                    "Assim, quanto maior o comprimento do cabo, maior será sua resistência elétrica."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Em um circuito real, a corrente elétrica percorre um caminho completo entre "
                    "a fonte e a carga. Em sistemas monofásicos, isso significa que a corrente "
                    "circula pelo condutor de ida e retorna pelo condutor de retorno. "
                    "Portanto, o comprimento elétrico considerado no cálculo deve incluir "
                    "o percurso total do circuito (ida + retorno)."
                ),
            }
        )

    return blocos


def _blocos_reforco() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Comprimento do circuito e resistência elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência elétrica de um condutor depende das propriedades físicas do "
                "material e da geometria do cabo. A relação fundamental que descreve esse "
                "comportamento é dada por:\n\n"
                "$$ R = \\rho \\frac{L}{A} $$\n\n"
                "onde **ρ** representa a resistividade elétrica do material, **L** o comprimento "
                "do condutor e **A** a área da seção transversal. Essa equação mostra que o "
                "aumento do comprimento do cabo provoca aumento proporcional da resistência elétrica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência do condutor influencia diretamente a queda de tensão ao longo "
                "do circuito. Utilizando a Lei de Ohm, a queda de tensão pode ser estimada por:\n\n"
                "$$ \\Delta V = I R $$\n\n"
                "onde **I** é a corrente elétrica do circuito e **R** é a resistência total do "
                "percurso elétrico."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em circuitos monofásicos utilizados para alimentação de motores, a corrente "
                "percorre o trajeto completo entre fonte e carga, retornando pelo condutor de "
                "retorno. Assim, o comprimento elétrico considerado no cálculo deve incluir "
                "o percurso total do circuito. Dessa forma, a queda de tensão pode ser "
                "aproximada por:\n\n"
                "$$ \\Delta V = 2 I R $$\n\n"
                "em que o fator **2** representa o percurso completo da corrente elétrica "
                "no circuito (ida e retorno)."
            ),
        },
    ]


def _blocos_verificacao_final() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Verificação final",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_001,
            "pergunta": (
                "Em um circuito que alimenta um motor localizado a grande distância do "
                "quadro elétrico, qual efeito físico tende a se tornar mais relevante "
                "devido ao aumento do comprimento dos condutores?"
            ),
            "alternativas": {
                "a": "Redução da resistividade do material",
                "b": "Aumento da resistência elétrica e da queda de tensão",
                "c": "Eliminação da corrente elétrica",
                "d": "Aumento da potência nominal do motor",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "No cálculo da queda de tensão em um circuito monofásico que alimenta um motor, "
                "o comprimento considerado deve representar:"
            ),
            "alternativas": {
                "a": "Somente o trecho entre o quadro e o motor",
                "b": "Apenas o condutor de fase",
                "c": "O percurso completo de ida e retorno da corrente no circuito",
                "d": "Apenas o trecho onde ocorre maior corrente",
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