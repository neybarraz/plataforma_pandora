from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "calor_capacidade_calorifica_mudanca_fase"

NUM_D_1 = 13
NUM_D_2 = 14
NUM_F_1 = 13
NUM_F_2 = 14

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
                "Em uma análise térmica de ambiente interno, considere duas placas maciças, A e B, "
                "inicialmente à mesma temperatura. A placa A tem capacidade calorífica total maior que a placa B. "
                "Se ambas receberem a mesma quantidade de calor e não houver mudança de fase, conclui-se que:"
            ),
            "alternativas": {
                "a": "A placa A sofrerá maior variação de temperatura porque armazena mais energia",
                "b": "As duas placas sofrerão a mesma variação de temperatura porque receberam o mesmo calor",
                "c": "A placa A sofrerá menor variação de temperatura porque precisa de mais energia para variar 1 °C",
                "d": "Não é possível comparar, porque capacidade calorífica não se relaciona à variação de temperatura",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "Durante um processo de fusão de gelo presente em um reservatório usado para resfriamento local, "
                "observa-se que a mistura permanece a 0 °C enquanto ainda coexistem gelo e água. "
                "Do ponto de vista físico, isso significa que o calor recebido pelo sistema está sendo usado principalmente para:"
            ),
            "alternativas": {
                "a": "Aumentar a temperatura da água líquida já formada",
                "b": "Romper a estrutura da fase sólida, promovendo mudança de fase sem elevar a temperatura",
                "c": "Diminuir a energia interna total do sistema",
                "d": "Anular a capacidade calorífica da mistura",
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
                "Você demonstrou domínio inicial sobre calor, capacidade calorífica, calor específico, "
                "calor latente, calor de fusão e mudança de fase. Este conteúdo pode ser considerado "
                "concluído nesta etapa."
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
                    "Na questão 1, a resposta correta é **c**. A capacidade calorífica total de um corpo "
                    "mede quanto calor ele precisa trocar para variar sua temperatura em 1 °C. "
                    "Matematicamente, **C = Q/ΔT**, de modo que **ΔT = Q/C**. Portanto, para a mesma "
                    "quantidade de calor recebida, o corpo com maior capacidade calorífica sofre menor "
                    "variação de temperatura."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **b**. Durante a fusão, o sistema recebe energia, "
                    "mas essa energia não se converte imediatamente em aumento de temperatura. Ela é empregada "
                    "na reorganização microscópica da matéria, rompendo a estrutura mais rígida do sólido. "
                    "Por isso, enquanto coexistem as duas fases, a temperatura permanece constante."
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
                "Calor é a energia transferida entre sistemas devido a uma diferença de temperatura. "
                "Sempre que dois corpos estão a temperaturas diferentes, ocorre transferência de "
                "energia térmica entre eles até que essa diferença diminua. Diferentemente da "
                "temperatura, que descreve o estado térmico de um sistema, o calor representa "
                "energia em trânsito durante esse processo de troca."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a troca de calor provoca apenas variação de temperatura, sem mudança de fase, "
                "utiliza-se o modelo conhecido como **calor sensível**:\n\n"
                "$$ Q = m\\,c\\,\\Delta T $$\n\n"
                "em que **Q** é o calor trocado, **m** é a massa do corpo, **c** é o calor específico "
                "do material e **ΔT** é a variação de temperatura. O calor específico indica quanta "
                "energia é necessária, por unidade de massa, para elevar a temperatura de um material "
                "em 1 °C. Por isso, materiais diferentes respondem de maneiras distintas ao mesmo "
                "ganho ou perda de energia térmica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A capacidade calorífica está relacionada a essa ideia, mas se refere ao corpo "
                "inteiro, e não apenas a uma unidade de massa. Ela pode ser expressa por:\n\n"
                "$$ C = m\\,c $$\n\n"
                "ou, de forma equivalente:\n\n"
                "$$ Q = C\\,\\Delta T $$\n\n"
                "Assim, a capacidade calorífica depende tanto da massa quanto do material do corpo. "
                "Elementos mais massivos ou feitos de materiais com maior calor específico podem "
                "armazenar mais energia térmica antes de apresentar grandes variações de temperatura."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além das trocas de calor associadas à variação de temperatura, existem processos "
                "em que a energia térmica é transferida sem alterar a temperatura do material. "
                "Isso ocorre durante as **mudanças de fase**, como fusão, evaporação ou "
                "condensação. Nesses casos, utiliza-se a relação:\n\n"
                "$$ Q = m\\,L $$\n\n"
                "em que **L** é o calor latente. O calor latente representa a quantidade de energia "
                "necessária por unidade de massa para que uma substância mude de estado físico "
                "sem variar sua temperatura."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a mudança ocorre do estado sólido para o líquido, utiliza-se o termo "
                "**calor latente de fusão**. Durante esse processo, a energia recebida não aumenta "
                "a temperatura do material, mas é empregada na reorganização microscópica da "
                "matéria, enfraquecendo as ligações que mantêm as partículas em uma estrutura "
                "mais rígida."
            ),
        },

        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=XABOuQhXwSo",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=r7z2DsWl8C4",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=lDKHu5knA8I",
        },
        {
            "tipo": "texto",
            "texto": (
                "No ambiente interno que estamos analisando, essas propriedades ajudam a explicar "
                "o comportamento térmico das superfícies. Paredes, piso, janelas, mobiliário e o "
                "próprio ar trocam energia continuamente sempre que existem diferenças de temperatura."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Por exemplo, em uma sala com forte incidência solar, parte da radiação que entra "
                "pelas janelas é absorvida pelas superfícies internas, como paredes, piso e "
                "mobiliário. Se esses elementos possuem grande massa e alta capacidade calorífica, "
                "eles podem armazenar energia térmica ao longo do dia enquanto sua temperatura "
                "aumenta gradualmente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a intensidade da radiação solar diminui ou durante a noite, essas superfícies "
                "passam a liberar parte da energia acumulada para o ar do ambiente por convecção e "
                "radiação térmica. Esse processo ajuda a explicar por que alguns ambientes permanecem "
                "quentes mesmo após a redução da incidência solar: o calor armazenado nas superfícies "
                "continua sendo transferido para o interior do espaço."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além disso, processos de mudança de fase da água presentes no ambiente — como "
                "condensação em superfícies frias ou evaporação de pequenas quantidades de água — "
                "também podem absorver ou liberar energia térmica, contribuindo para o balanço "
                "energético do ambiente interno."
            ),
        },

        {
            "tipo": "lista",
            "itens": [
                "Calor é energia em trânsito causada por diferença de temperatura.",
                "O calor sensível está associado à variação de temperatura (Q = mcΔT).",
                "Capacidade calorífica depende da massa total e do material do corpo.",
                "Superfícies mais massivas tendem a aquecer e resfriar mais lentamente.",
                "Mudanças de fase envolvem calor latente e ocorrem sem variação de temperatura.",
                "Esses processos ajudam a interpretar o comportamento térmico do ambiente interno.",
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
                "Duas superfícies internas recebem a mesma quantidade de calor ao longo de uma hora. "
                "A superfície X apresenta pequena variação de temperatura, enquanto a superfície Y aquece rapidamente. "
                "A interpretação mais adequada é que:"
            ),
            "alternativas": {
                "a": "A superfície X provavelmente possui maior capacidade calorífica total que a Y",
                "b": "A superfície Y possui maior calor específico que a X",
                "c": "As duas necessariamente têm a mesma massa",
                "d": "A superfície X não trocou calor com o ambiente",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Em um ponto do ambiente, gelo derrete sem variação de temperatura enquanto recebe energia. "
                "Esse processo ilustra principalmente:"
            ),
            "alternativas": {
                "a": "Apenas aumento de calor específico",
                "b": "Transferência de calor com redução da energia interna",
                "c": "Uso de calor latente de fusão durante a mudança de fase",
                "d": "Ausência de troca térmica por equilíbrio térmico",
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