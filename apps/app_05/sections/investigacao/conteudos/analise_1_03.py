from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "relacoes_fundamentais_circuitos_sistemas_mono_trifasicos"

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
                "Em uma instalação de bombeamento com motor monofásico, deseja-se estimar a corrente "
                "absorvida a partir da potência elétrica ativa do circuito. Desprezando perdas adicionais, "
                "qual relação representa corretamente a ligação fundamental entre potência, tensão, "
                "corrente e fator de potência em regime monofásico senoidal?"
            ),
            "alternativas": {
                "a": r"$P = V \,/\, (I\cos\varphi)$",
                "b": r"$P = V\,I\,\cos\varphi$",
                "c": r"$P = \sqrt{3}\,V\,I$",
                "d": r"$P = I^2 \,/\, R$",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "No circuito de alimentação trifásico de um motor de bomba, usando tensão de linha e "
                "corrente de linha em regime balanceado, qual expressão representa corretamente a "
                "potência ativa total do sistema?"
            ),
            "alternativas": {
                "a": r"$P = V\,I\,\cos\varphi$",
                "b": r"$P = 3\,V\,I$",
                "c": r"$P = \sqrt{3}\,V_L\,I_L\,\cos\varphi$",
                "d": r"$P = V_L\,I_L \,/\, \cos\varphi$",
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
                "Você demonstrou domínio inicial sobre relações fundamentais de circuitos "
                "aplicadas a redes monofásicas e trifásicas no contexto de alimentação de motores."
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
                    "Na questão 1, a resposta correta é **b**. Em regime monofásico senoidal, "
                    "a potência ativa absorvida por uma carga é dada por:\n\n"
                    r"$$ P = V\,I\,\cos\varphi $$"
                    "\n\n"
                    "em que **V** é a tensão eficaz, **I** é a corrente eficaz e "
                    "**cosφ** é o fator de potência. Logo, quando se deseja determinar a corrente, "
                    "pode-se reorganizar a expressão para:\n\n"
                    r"$$ I = \frac{P}{V\,\cos\varphi} $$"
                    "\n\n"
                    "Essa relação é central no dimensionamento de circuitos monofásicos, pois permite "
                    "estimar a solicitação elétrica imposta aos condutores a partir dos dados nominais "
                    "do equipamento."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. Para um sistema trifásico equilibrado, "
                    "a potência ativa total pode ser escrita em função da tensão de linha e da corrente "
                    "de linha por:\n\n"
                    r"$$ P = \sqrt{3}\,V_L\,I_L\,\cos\varphi $$"
                    "\n\n"
                    "O fator **√3** surge da relação geométrica entre grandezas de fase e grandezas de linha "
                    "no sistema trifásico. Reorganizando a equação, obtém-se a corrente de linha:\n\n"
                    r"$$ I_L = \frac{P}{\sqrt{3}\,V_L\,\cos\varphi} $$"
                    "\n\n"
                    "Essa expressão é indispensável para avaliar a corrente exigida pelo motor e verificar "
                    "se os condutores do circuito de alimentação estão adequadamente dimensionados."
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
                "Em circuitos elétricos de alimentação de motores, a relação entre tensão, corrente e "
                "potência constitui a base para interpretar a carga imposta ao sistema. No contexto do "
                "bombeamento, o motor converte energia elétrica em energia mecânica, mas essa conversão "
                "depende de um circuito capaz de fornecer a potência requerida sob condições adequadas "
                "de tensão e corrente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em regime monofásico senoidal, a potência ativa absorvida por uma carga é dada por:\n\n"
                r"$$ P = V\,I\,\cos\varphi $$"
                "\n\n"
                "em que **P** é a potência ativa, **V** é a tensão eficaz, **I** é a corrente eficaz e "
                "**cosφ** é o fator de potência. Para fins de dimensionamento, a expressão pode ser "
                "reescrita como:\n\n"
                r"$$ I = \frac{P}{V\,\cos\varphi} $$"
                "\n\n"
                "Essa forma é especialmente útil quando a potência e a tensão de alimentação do motor são "
                "conhecidas e se deseja estimar a corrente que circulará nos condutores."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em sistemas trifásicos equilibrados, muito comuns em instalações de bombeamento, a potência "
                "ativa total é expressa por:\n\n"
                r"$$ P = \sqrt{3}\,V_L\,I_L\,\cos\varphi $$"
                "\n\n"
                "em que **V_L** é a tensão de linha e **I_L** é a corrente de linha. Assim, a corrente do "
                "circuito pode ser calculada por:\n\n"
                r"$$ I_L = \frac{P}{\sqrt{3}\,V_L\,\cos\varphi} $$"
                "\n\n"
                "A presença do fator **√3** diferencia o modelo trifásico do monofásico e reflete a própria "
                "estrutura geométrica do sistema de três fases defasadas eletricamente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando o motor é especificado em potência mecânica nominal, convém ainda considerar o "
                "rendimento **η**. Nesse caso, a potência elétrica de entrada é maior que a potência útil "
                "no eixo. Para um modelo monofásico, pode-se escrever:\n\n"
                r"$$ P_{in} = \frac{P_{out}}{\eta} $$"
                "\n\n"
                r"$$ I = \frac{P_{out}}{\eta\,V\,\cos\varphi} $$"
                "\n\n"
                "e, para um sistema trifásico equilibrado:\n\n"
                r"$$ I_L = \frac{P_{out}}{\sqrt{3}\,\eta\,V_L\,\cos\varphi} $$"
                "\n\n"
                "Essas expressões são mais adequadas para engenharia, pois aproximam o cálculo da condição "
                "real de operação do motor."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além do cálculo da corrente, essas relações são o ponto de partida para etapas posteriores "
                "do projeto elétrico, como verificação da ampacidade dos condutores, análise da queda de "
                "tensão e compatibilização entre o motor e a rede de alimentação. Portanto, compreender "
                "a distinção entre rede monofásica e trifásica não é apenas uma questão classificatória, "
                "mas uma exigência técnica para calcular corretamente a solicitação elétrica do circuito."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=K7s0VPYdtPI",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=r3LMjN7AUJg",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=AaotM_xbemU",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, essas relações permitem transformar os dados nominais do motor da bomba "
                "em uma corrente de projeto para o circuito de alimentação. A partir dela, torna-se possível "
                "avaliar se a seção dos condutores é compatível com a operação prevista e se a alimentação "
                "elétrica do motor ocorrerá em condições seguras e tecnicamente adequadas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Se a alimentação for monofásica, a corrente tende a ser mais elevada para uma mesma potência, "
                "quando comparada a uma alimentação trifásica em tensão apropriada. Já em sistemas trifásicos, "
                "a distribuição de potência entre três fases tende a tornar o fornecimento mais eficiente para "
                "motores de maior porte, o que influencia diretamente o dimensionamento dos cabos."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                r"Em rede monofásica: $P = V\,I\,\cos\varphi$.",
                r"Em rede trifásica equilibrada: $P = \sqrt{3}\,V_L\,I_L\,\cos\varphi$.",
                "A corrente do circuito depende do tipo de alimentação elétrica adotado.",
                "Rendimento e fator de potência refinam o cálculo da corrente real exigida pelo motor.",
                "Essas relações são a base do dimensionamento dos condutores de alimentação.",
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
                "Um motor monofásico opera sob tensão eficaz constante. Admitindo mesmo fator de potência, "
                "o que ocorre com a corrente do circuito quando a potência ativa requerida aumenta?"
            ),
            "alternativas": {
                "a": "A corrente diminui proporcionalmente",
                "b": "A corrente permanece constante",
                "c": "A corrente aumenta, pois em regime monofásico vale $I = P/(V\\cos\\varphi)$",
                "d": "A corrente só depende da resistência do cabo",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Para dois motores com mesma potência ativa e mesmo fator de potência, um alimentado "
                "em rede monofásica e outro em rede trifásica equilibrada, a principal diferença no "
                "cálculo da corrente está em:"
            ),
            "alternativas": {
                "a": "No uso da resistividade do condutor na equação de potência",
                "b": "Na presença do fator $\\sqrt{3}$ na expressão trifásica com grandezas de linha",
                "c": "Na eliminação do fator de potência no caso trifásico",
                "d": "No fato de a corrente trifásica independer da tensão",
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