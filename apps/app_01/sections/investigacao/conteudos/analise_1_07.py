from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "movimento_ar_ambiente"

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
                "Em uma sala com duas janelas abertas, o ar externo entra por uma abertura e sai por outra. "
                "Do ponto de vista físico, esse movimento do ar ocorre principalmente devido a:"
            ),
            "alternativas": {
                "a": "Igualdade de pressão em todas as regiões do ambiente",
                "b": "Diferenças de pressão que impulsionam o escoamento do ar",
                "c": "Ausência de interação entre o ar e as superfícies da sala",
                "d": "Impossibilidade de o ar ocupar todo o volume do ambiente",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Uma corrente de ar atravessa uma abertura de área 0,25 m² com velocidade média de 1,2 m/s. "
                "Qual é a vazão volumétrica aproximada desse escoamento?"
            ),
            "alternativas": {
                "a": "0,12 m³/s",
                "b": "0,20 m³/s",
                "c": "0,30 m³/s",
                "d": "1,45 m³/s",
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
                "Você demonstrou domínio inicial sobre o movimento do ar no ambiente. "
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
                    "Na questão 1, a resposta correta é **b**. O ar tende a se deslocar de regiões "
                    "de maior pressão para regiões de menor pressão. Em ambientes internos, essas diferenças "
                    "de pressão podem surgir por vento externo, aberturas, aquecimento desigual das superfícies "
                    "ou pela própria circulação já estabelecida no recinto."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A vazão volumétrica é dada por "
                    "**$Q_v = A\\,v$**. Logo, **$Q_v = 0,25 \\cdot 1,2 = 0,30\\,m^3/s$**."
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
                "Depois de compreender o ar como um fluido, o passo seguinte é analisar como ele se move "
                "dentro do ambiente. O movimento do ar depende da existência de diferenças de pressão e "
                "também das condições geométricas do espaço, como portas, janelas, corredores, móveis e "
                "obstáculos. Em uma sala, o ar não ocupa apenas um volume estático: ele pode entrar, sair, "
                "desviar, acelerar e redistribuir energia térmica pelo ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma das grandezas mais úteis para descrever esse processo é a **vazão volumétrica**, que "
                "representa o volume de ar que atravessa uma determinada seção por unidade de tempo. Ela pode "
                "ser expressa por:\n\n"
                "$$ Q_v = A\\,v $$\n\n"
                "em que **$Q_v$** é a vazão volumétrica, **A** é a área da abertura ou seção transversal e "
                "**v** é a velocidade média do ar. Essa relação ajuda a estimar quanto ar passa por uma janela, "
                "porta ou abertura de ventilação em um certo intervalo de tempo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Se a quantidade de ar que atravessa o sistema se conserva aproximadamente ao longo do escoamento, "
                "pode-se usar a **equação da continuidade**. Em uma forma simplificada, ela é escrita como:\n\n"
                "$$ A_1v_1 = A_2v_2 $$\n\n"
                "Essa expressão mostra que, quando o ar passa de uma região de maior área para outra de menor área, "
                "sua velocidade tende a aumentar. De forma análoga, ao entrar em uma região mais ampla, a velocidade "
                "tende a diminuir."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Outro conceito central é a **diferença de pressão**. Em termos físicos, o ar tende a se deslocar "
                "de regiões onde a pressão é maior para regiões onde a pressão é menor. Esse desnível de pressão "
                "pode ser produzido por vento externo, por diferenças de temperatura, pela posição e tamanho das "
                "aberturas ou pelo próprio desenho do ambiente. Assim, a pressão funciona como uma das causas do "
                "escoamento do ar."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esses três elementos — vazão, continuidade e diferença de pressão — ajudam a descrever como o "
                "ar circula no interior de uma sala. Se duas janelas estão abertas em lados diferentes, por exemplo, "
                "o ar pode atravessar o espaço interno de uma para outra. Se uma das aberturas for menor, a velocidade "
                "do escoamento nessa região pode aumentar. Ao mesmo tempo, móveis, divisórias e pessoas alteram o caminho "
                "do fluxo e tornam a distribuição do ar menos uniforme."
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
                "No ambiente interno que estamos analisando, o movimento do ar é importante porque ele interfere "
                "na forma como o calor se distribui dentro da sala. O ar pode entrar e sair por janelas e portas, "
                "acelerar ao atravessar passagens menores e mudar de direção ao encontrar paredes ou mobiliário. "
                "Por isso, regiões relativamente próximas podem apresentar velocidades de ar diferentes e, consequentemente, "
                "sensações térmicas distintas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa leitura ajuda a entender por que a geometria da sala influencia o conforto térmico. Uma abertura "
                "mal posicionada pode concentrar o escoamento em uma região específica, enquanto outra parte do ambiente "
                "permanece com pouca renovação de ar. Da mesma forma, obstáculos internos podem desviar o fluxo, criando "
                "zonas mais ventiladas e zonas mais estagnadas. Assim, estudar o movimento do ar no ambiente é estudar "
                "como o espaço construído controla a distribuição do ar e, com isso, modifica o conforto térmico."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A vazão volumétrica indica quanto ar atravessa uma abertura por unidade de tempo.",
                "A relação $Q_v = A\\,v$ conecta área de passagem e velocidade média do ar.",
                "A equação da continuidade expressa a conservação do escoamento em diferentes seções.",
                "Ao passar por aberturas menores, o ar tende a aumentar sua velocidade.",
                "Diferenças de pressão impulsionam o movimento do ar no ambiente.",
                "Portas, janelas, paredes e mobiliário alteram o caminho do escoamento.",
                "A distribuição do ar dentro da sala influencia diretamente o conforto térmico.",
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
                "Em uma sala, o ar atravessa uma abertura larga e depois passa por uma abertura mais estreita. "
                "Considerando a continuidade do escoamento, o que se espera que aconteça com a velocidade do ar "
                "na região mais estreita?"
            ),
            "alternativas": {
                "a": "A velocidade diminui, porque a área é menor",
                "b": "A velocidade permanece constante, independentemente da área",
                "c": "A velocidade aumenta, porque a área disponível é menor",
                "d": "A velocidade se anula ao atravessar a abertura",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "No contexto do movimento do ar em ambientes internos, qual afirmação descreve melhor o papel "
                "da diferença de pressão?"
            ),
            "alternativas": {
                "a": "A diferença de pressão pode impulsionar o escoamento do ar de uma região para outra",
                "b": "A diferença de pressão impede qualquer circulação dentro da sala",
                "c": "A pressão só atua em líquidos, não em gases",
                "d": "A pressão não interfere no trajeto do ar em portas e janelas",
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
        st.info("Responda as duas questões para verificar o diagnóstico.")
        return

    if st.button(
        "Verificar diagnóstico",
        key=f"btn_verificar_diag_{CONTEUDO_ID}",
        use_container_width=False,
    ):
        _finalizar_diagnostico()