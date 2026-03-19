from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "relacoes_fundamentais_circuitos_motor_bomba"

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
                "Em um motor elétrico de bombeamento, a **potência nominal** indicada na placa "
                "corresponde, do ponto de vista do circuito, a:"
            ),
            "alternativas": {
                "a": "A energia total consumida pelo motor ao longo de qualquer intervalo de tempo",
                "b": "A taxa de conversão ou demanda de energia sob condições nominais de operação",
                "c": "A tensão máxima suportada pelo isolamento dos enrolamentos",
                "d": "A corrente de partida medida no instante inicial de acionamento",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "A **tensão nominal de operação** de um motor deve ser interpretada como:"
            ),
            "alternativas": {
                "a": "A diferença de potencial que sempre permanece constante, independentemente da rede",
                "b": "O valor da queda de tensão interna no enrolamento durante a partida",
                "c": "O valor de tensão para o qual o motor foi projetado para operar adequadamente",
                "d": "A tensão instantânea máxima observada em regime transitório",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_003,
            "pergunta": (
                "A **corrente nominal** de um motor representa, em termos de circuito elétrico:"
            ),
            "alternativas": {
                "a": "A corrente requerida pelo motor em regime nominal, nas condições previstas de operação",
                "b": "A maior corrente possível em qualquer falha do sistema",
                "c": "A corrente que independe da potência e da tensão do equipamento",
                "d": "A corrente que circula apenas nos dispositivos de proteção",
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
                "Você demonstrou domínio inicial sobre potência nominal, tensão nominal e "
                "corrente nominal do motor no contexto das relações fundamentais de circuitos. "
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
                    "Na questão 1, a resposta correta é **b**. A potência nominal de um motor "
                    "expressa a taxa com que a energia é convertida ou requerida em regime "
                    "nominal. Em circuitos elétricos, potência não representa energia total "
                    "acumulada, mas sim uma grandeza de taxa, usualmente expressa em watt. "
                    "No estudo do motor da bomba, esse parâmetro é central porque, em conjunto "
                    "com a tensão de alimentação e com os parâmetros de desempenho, permite "
                    "estimar a corrente exigida pelo equipamento."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A tensão nominal é o valor de "
                    "diferença de potencial para o qual o motor foi projetado. Quando a tensão "
                    "de alimentação se afasta significativamente desse valor, o comportamento "
                    "elétrico e eletromecânico do motor também se altera, podendo afetar corrente, "
                    "torque, aquecimento e desempenho. Por isso, a tensão nominal não deve ser "
                    "interpretada como uma tensão transitória máxima, mas como referência de "
                    "operação adequada do equipamento."
                ),
            }
        )

    if not resultado.get("q3_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 3, a resposta correta é **a**. A corrente nominal corresponde à "
                    "corrente absorvida pelo motor em regime nominal, sob as condições para as "
                    "quais ele foi especificado. Esse valor é essencial para o dimensionamento "
                    "dos condutores, pois a seção do cabo deve ser compatível com a corrente "
                    "que circulará no circuito. Assim, a corrente nominal funciona como uma das "
                    "principais entradas para a análise da capacidade de condução de corrente e "
                    "da queda de tensão."
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
                "No circuito de alimentação do motor da bomba, as relações fundamentais entre "
                "tensão, corrente e potência fornecem a base para interpretar a carga elétrica "
                "imposta ao sistema. Em termos gerais, a potência elétrica pode ser entendida "
                "como a taxa de transferência ou conversão de energia no circuito. Para uma "
                "carga puramente resistiva em corrente contínua, a relação elementar é:\n\n"
                "$$ P = V\\,I $$\n\n"
                "em que **P** é a potência elétrica, **V** é a tensão elétrica e **I** é a "
                "corrente elétrica. Embora motores reais em corrente alternada exijam um modelo "
                "mais completo, essa expressão constitui o ponto de partida conceitual para "
                "relacionar demanda de potência e solicitação de corrente no circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **potência nominal do motor** é o valor de potência associado à condição de "
                "operação para a qual o equipamento foi especificado. Em aplicações de bombeamento, "
                "esse parâmetro indica a ordem de grandeza da energia por unidade de tempo que o "
                "motor deve converter para manter o sistema em funcionamento. Em corrente alternada, "
                "a análise da potência ativa consumida por um motor monofásico pode ser expressa por:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "e, para sistemas trifásicos equilibrados, por:\n\n"
                "$$ P = \\sqrt{3}\\,V_L\\,I_L\\,\\cos\\varphi $$\n\n"
                "em que **\\cos\\varphi** é o fator de potência, **V_L** é a tensão de linha e "
                "**I_L** é a corrente de linha."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **tensão nominal de operação** é a diferença de potencial para a qual o motor "
                "foi projetado. Ela define a condição elétrica esperada nos terminais do equipamento "
                "durante o funcionamento adequado. Se a tensão disponível no circuito for inferior "
                "ou superior ao valor nominal, a corrente absorvida pelo motor e o seu comportamento "
                "térmico podem se alterar. Na prática, esse parâmetro é essencial porque conecta o "
                "equipamento à rede elétrica disponível e condiciona a interpretação correta das "
                "demais grandezas nominais do motor."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A **corrente nominal** representa a corrente que o motor exige quando opera nas "
                "condições previstas de carga, tensão e frequência. Em estudos de dimensionamento "
                "de condutores, essa grandeza é crítica porque indica a solicitação elétrica imposta "
                "ao cabo. Rearranjando as equações de potência, obtém-se, para o caso monofásico:\n\n"
                "$$ I = \\frac{P}{V\\,\\cos\\varphi} $$\n\n"
                "e, para o caso trifásico:\n\n"
                "$$ I_L = \\frac{P}{\\sqrt{3}\\,V_L\\,\\cos\\varphi} $$\n\n"
                "Quando se considera o rendimento do motor, a potência elétrica de entrada passa a "
                "se relacionar com a potência útil por meio de **\\eta**, refinando a estimativa da "
                "corrente nominal exigida pelo equipamento."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Para motores reais, especialmente em engenharia ambiental e civil, a interpretação "
                "correta dessas grandezas evita erros de análise no circuito de alimentação. Um motor "
                "com maior potência nominal, para uma mesma tensão, tende a demandar maior corrente. "
                "Da mesma forma, para uma mesma potência, tensões mais elevadas tendem a reduzir a "
                "corrente requerida, o que impacta diretamente o dimensionamento dos condutores e a "
                "queda de tensão. Portanto, potência nominal, tensão nominal e corrente nominal não "
                "devem ser vistas como dados isolados da placa do motor, mas como grandezas "
                "fisicamente conectadas pela modelagem elétrica do circuito."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=KOaFVgU-yng",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema de bombeamento estudado, o motor constitui a carga principal do circuito "
                "de alimentação. A potência nominal informa a demanda elétrica associada à operação "
                "do equipamento, a tensão nominal define a compatibilidade com a rede, e a corrente "
                "nominal fornece a referência prática para avaliar se os condutores instalados podem "
                "alimentar o motor com segurança e desempenho adequado."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essas relações são decisivas no dimensionamento do circuito. A partir da potência "
                "nominal e da tensão de operação, estima-se a corrente exigida. Em seguida, compara-se "
                "essa corrente com a capacidade de condução do cabo e com os limites de queda de tensão. "
                "Assim, a teoria de circuitos deixa de ser apenas formalismo matemático e passa a "
                "funcionar como ferramenta objetiva de decisão técnica no projeto e na avaliação de "
                "instalações de bombeamento."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Potência elétrica relaciona taxa de conversão de energia com a operação do motor.",
                "Tensão nominal define a condição elétrica prevista para funcionamento adequado.",
                "Corrente nominal expressa a solicitação elétrica efetiva imposta ao circuito.",
                "Em corrente alternada, fator de potência e rendimento influenciam a corrente requerida.",
                "Essas grandezas são a base para avaliar cabos, perdas e queda de tensão no sistema.",
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
                "Para dois motores operando na mesma tensão e com fator de potência semelhante, "
                "aquele de maior potência nominal tenderá a exigir:"
            ),
            "alternativas": {
                "a": "Menor corrente nominal",
                "b": "Maior corrente nominal",
                "c": "A mesma corrente em qualquer condição",
                "d": "Corrente nula em regime nominal",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "No contexto do motor da bomba, a tensão nominal deve ser usada principalmente para:"
            ),
            "alternativas": {
                "a": "Substituir a corrente nominal no dimensionamento dos cabos",
                "b": "Definir a potência hidráulica da bomba",
                "c": "Verificar a compatibilidade do motor com a rede e interpretar a corrente requerida",
                "d": "Estimar diretamente a resistividade do cobre",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_003,
            "pergunta": (
                "A corrente nominal do motor é especialmente importante porque:"
            ),
            "alternativas": {
                "a": "Define a frequência da rede elétrica",
                "b": "Permite avaliar a seção dos condutores e a solicitação do circuito",
                "c": "Elimina a necessidade de considerar fator de potência",
                "d": "Torna irrelevante a queda de tensão",
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
        st.info("Responda as três questões para verificar o diagnóstico.")
        return

    if st.button(
        "Verificar diagnóstico",
        key=f"btn_verificar_diag_{CONTEUDO_ID}",
        use_container_width=False,
    ):
        _finalizar_diagnostico()