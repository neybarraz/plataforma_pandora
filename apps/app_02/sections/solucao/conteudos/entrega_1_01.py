from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "grandezas_eletricas_fundamentais"

NUM_D_1 = 1
NUM_D_2 = 2
NUM_D_3 = 3
NUM_F_1 = 4
NUM_F_2 = 5
NUM_F_3 = 6

Q_D_001 = f"q_d_{CONTEUDO_ID}_{NUM_D_1:03d}"
Q_D_002 = f"q_d_{CONTEUDO_ID}_{NUM_D_2:03d}"
Q_D_003 = f"q_d_{CONTEUDO_ID}_{NUM_D_3:03d}"
Q_F_001 = f"q_f_{CONTEUDO_ID}_{NUM_F_1:03d}"
Q_F_002 = f"q_f_{CONTEUDO_ID}_{NUM_F_2:03d}"
Q_F_003 = f"q_f_{CONTEUDO_ID}_{NUM_F_3:03d}"

DIAG_STATUS_KEY = f"analise_diag_status_{CONTEUDO_ID}"
DIAG_RESULT_KEY = f"analise_diag_result_{CONTEUDO_ID}"


def _get_widget_value(question_id: str):
    return st.session_state.get(f"analise_widget_{question_id}")


def _diagnostico_respondido() -> bool:
    return (
        _get_widget_value(Q_D_001) is not None
        and _get_widget_value(Q_D_002) is not None
        and _get_widget_value(Q_D_003) is not None
    )


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
    acerto_q3 = _acertou(Q_D_003, "a")
    total_acertos = int(acerto_q1) + int(acerto_q2) + int(acerto_q3)

    resultado = {
        "resposta_q1": _get_widget_value(Q_D_001),
        "resposta_q2": _get_widget_value(Q_D_002),
        "resposta_q3": _get_widget_value(Q_D_003),
        "q1_correta": acerto_q1,
        "q2_correta": acerto_q2,
        "q3_correta": acerto_q3,
        "total_acertos": total_acertos,
        "acertou_tudo": total_acertos == 3,
    }

    _set_diag_result(resultado)

    if total_acertos == 3:
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
                "No circuito de alimentação de um motor de bomba, a grandeza tensão elétrica pode ser "
                "interpretada fisicamente como:"
            ),
            "alternativas": {
                "a": "A quantidade de carga que atravessa o condutor por segundo",
                "b": "A diferença de potencial elétrico que impulsiona o movimento de cargas no circuito",
                "c": "A resistência oferecida pelo motor à passagem de corrente",
                "d": "A energia dissipada exclusivamente na forma de calor nos cabos",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Em regime de operação, a corrente elétrica que circula no circuito de alimentação do motor "
                "representa principalmente:"
            ),
            "alternativas": {
                "a": "A tensão nominal aplicada entre os terminais do motor",
                "b": "A potência mecânica útil já convertida no eixo",
                "c": "A taxa de escoamento de carga elétrica através dos condutores",
                "d": "A oposição elétrica do isolamento do cabo ao campo elétrico",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_003,
            "pergunta": (
                "Ao analisar a alimentação elétrica de um motor, a potência elétrica absorvida pelo sistema "
                "está associada, de forma fundamental, à relação entre:"
            ),
            "alternativas": {
                "a": "Tensão elétrica e corrente elétrica",
                "b": "Resistividade e comprimento do condutor",
                "c": "Frequência e fator de potência apenas",
                "d": "Corrente elétrica e temperatura ambiente apenas",
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
                "Você demonstrou domínio inicial sobre tensão elétrica, corrente elétrica e potência elétrica. "
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
                    "Na questão 1, a resposta correta é **b**. A tensão elétrica é a **diferença de potencial** "
                    "entre dois pontos do circuito. Ela representa a energia potencial elétrica disponível por unidade "
                    "de carga para impulsionar o deslocamento das cargas. Em termos formais:\n\n"
                    "$$ V = \\frac{W}{q} $$\n\n"
                    "em que **V** é a tensão, **W** é o trabalho ou energia transferida e **q** é a carga elétrica."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A corrente elétrica expressa a taxa de escoamento "
                    "de carga elétrica através de uma seção transversal do condutor. Sua definição fundamental é:\n\n"
                    "$$ I = \\frac{\\Delta q}{\\Delta t} $$\n\n"
                    "em que **I** é a corrente, **Δq** é a quantidade de carga transportada e **Δt** é o intervalo de tempo. "
                    "No circuito do motor, a corrente indica a intensidade da solicitação elétrica imposta aos cabos."
                ),
            }
        )

    if not resultado.get("q3_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 3, a resposta correta é **a**. A potência elétrica corresponde à taxa de transferência "
                    "ou conversão de energia elétrica. Em sua forma básica, ela pode ser expressa por:\n\n"
                    "$$ P = V\\,I $$\n\n"
                    "em que **P** é a potência, **V** é a tensão elétrica e **I** é a corrente elétrica. "
                    "No caso de motores em corrente alternada, a análise prática também pode envolver fator de potência "
                    "e rendimento, mas a relação entre tensão e corrente continua sendo central."
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
                "A análise do circuito de alimentação de um motor de bombeamento começa pelo entendimento de três "
                "grandezas elétricas fundamentais: **tensão elétrica**, **corrente elétrica** e **potência elétrica**. "
                "Essas grandezas estruturam a descrição física do sistema e permitem relacionar a fonte de alimentação, "
                "os condutores e a carga representada pelo motor."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **tensão elétrica** representa a diferença de potencial entre dois pontos do circuito. "
                "Fisicamente, ela expressa a energia disponível por unidade de carga para promover o deslocamento "
                "de portadores elétricos. Sua definição geral pode ser escrita como:\n\n"
                "$$ V = \\frac{W}{q} $$\n\n"
                "em que **V** é a tensão, **W** é a energia transferida e **q** é a carga elétrica. "
                "No sistema de alimentação do motor, a tensão fornecida pela rede estabelece a condição energética "
                "necessária para que haja circulação de corrente elétrica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **corrente elétrica** corresponde à taxa de passagem de carga elétrica por uma seção do condutor. "
                "Ela é descrita por:\n\n"
                "$$ I = \\frac{\\Delta q}{\\Delta t} $$\n\n"
                "em que **I** é a corrente, **Δq** é a quantidade de carga e **Δt** é o intervalo de tempo. "
                "Do ponto de vista da instalação, a corrente é uma das variáveis mais relevantes, pois determina "
                "o esforço elétrico imposto aos condutores e influencia diretamente aquecimento, perdas e critérios "
                "de dimensionamento."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **potência elétrica** expressa a taxa com que a energia elétrica é transferida ou convertida. "
                "Em corrente contínua e em formulações básicas, pode ser escrita como:\n\n"
                "$$ P = V\\,I $$\n\n"
                "Em elementos resistivos, também podem ser utilizadas as formas:\n\n"
                "$$ P = R\\,I^2 $$\n\n"
                "$$ P = \\frac{V^2}{R} $$\n\n"
                "Já em sistemas de corrente alternada aplicados a motores, a potência ativa absorvida é mais adequadamente "
                "representada por:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "para sistemas monofásicos, e por:\n\n"
                "$$ P = \\sqrt{3}\\,V\\,I\\,\\cos\\varphi $$\n\n"
                "para sistemas trifásicos equilibrados, em que **cosφ** é o fator de potência."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No caso do motor da bomba, essas relações permitem determinar a corrente exigida pelo equipamento "
                "a partir da potência nominal, da tensão de alimentação e das características operacionais do sistema. "
                "Para uma análise mais realista, especialmente em engenharia, é comum considerar também o rendimento "
                "do motor. Assim, em um sistema monofásico:\n\n"
                "$$ I = \\frac{P}{V\\,\\cos\\varphi\\,\\eta} $$\n\n"
                "e, em um sistema trifásico:\n\n"
                "$$ I = \\frac{P}{\\sqrt{3}\\,V\\,\\cos\\varphi\\,\\eta} $$\n\n"
                "em que **η** representa o rendimento."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=dYM-azGeQhM",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=xcdhLBymAqI",
        },
        {
            "tipo": "texto",
            "texto": (
                "Essas grandezas não devem ser estudadas de forma isolada. No circuito de alimentação do motor, "
                "a tensão imposta pela rede produz a circulação de corrente, e essa corrente, combinada com a tensão "
                "e com as características da carga, define a potência elétrica absorvida pelo sistema. É essa corrente "
                "que será comparada com a capacidade admissível dos condutores no dimensionamento do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Portanto, compreender tensão, corrente e potência é o primeiro passo para interpretar tecnicamente "
                "o funcionamento do sistema de bombeamento. Sem esse bloco conceitual, não é possível avaliar com rigor "
                "se os cabos instalados são suficientes para alimentar o motor com segurança e desempenho adequado."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Tensão elétrica representa diferença de potencial e energia por unidade de carga.",
                "Corrente elétrica mede a taxa de escoamento de cargas no circuito.",
                "Potência elétrica expressa a taxa de transferência ou conversão de energia.",
                "Em motores, corrente depende de tensão, potência, fator de potência e rendimento.",
                "Essas grandezas são a base para analisar a alimentação elétrica do motor da bomba.",
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
                "Em um circuito que alimenta um motor, a tensão elétrica é mais corretamente interpretada como:"
            ),
            "alternativas": {
                "a": "A taxa de transporte de carga no condutor",
                "b": "A energia potencial elétrica disponível por unidade de carga entre dois pontos",
                "c": "A potência dissipada em regime permanente",
                "d": "A resistência total equivalente do sistema",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Se a corrente elétrica em um cabo aumenta, isso indica que:"
            ),
            "alternativas": {
                "a": "A diferença de potencial desapareceu",
                "b": "A resistência elétrica tornou-se nula",
                "c": "A taxa de passagem de carga elétrica pelo condutor aumentou",
                "d": "A potência elétrica necessariamente diminuiu",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_003,
            "pergunta": (
                "Na análise de um motor trifásico, a potência ativa elétrica absorvida é associada principalmente à relação:"
            ),
            "alternativas": {
                "a": "$$P = \\sqrt{3}\\,V\\,I\\,\\cos\\varphi$$",
                "b": "$$P = \\frac{V}{I}$$",
                "c": "$$P = R\\,V$$",
                "d": "$$P = \\frac{I}{R}$$",
            },
            "alternativa_correta": "a",
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
        st.info("Responda as três questões para verificar o diagnóstico.")
        return

    if st.button(
        "Verificar diagnóstico",
        key=f"btn_verificar_diag_{CONTEUDO_ID}",
        use_container_width=False,
    ):
        _finalizar_diagnostico()