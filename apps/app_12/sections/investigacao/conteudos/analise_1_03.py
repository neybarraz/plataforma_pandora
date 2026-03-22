from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_03"

Q_D_001 = f"{BASE_ID}_001"
Q_D_002 = f"{BASE_ID}_002"
Q_F_001 = f"{BASE_ID}_003"
Q_F_002 = f"{BASE_ID}_004"


DIAG_QUESTOES = (Q_D_001, Q_D_002)
DIAG_CORRETAS = {
    Q_D_001: "b",
    Q_D_002: "c",
}


def _get_widget_value(question_id: str):
    return st.session_state.get(f"analise_widget_{question_id}")


def _normalizar_resposta(valor) -> str:
    if valor is None:
        return ""
    return str(valor).strip().lower()


def _respostas_diagnostico() -> dict[str, str]:
    return {
        qid: _normalizar_resposta(_get_widget_value(qid))
        for qid in DIAG_QUESTOES
    }


def _questoes_pendentes() -> list[str]:
    respostas = _respostas_diagnostico()
    return [qid for qid in DIAG_QUESTOES if not respostas[qid]]


def _diagnostico_respondido() -> bool:
    return len(_questoes_pendentes()) == 0


def _resultado_diagnostico() -> dict:
    respostas = _respostas_diagnostico()
    pendentes = _questoes_pendentes()

    corretas: list[str] = []
    erradas: list[str] = []

    for qid in DIAG_QUESTOES:
        resposta = respostas[qid]
        if not resposta:
            continue

        if resposta == DIAG_CORRETAS[qid]:
            corretas.append(qid)
        else:
            erradas.append(qid)

    total_acertos = len(corretas)
    respondido = len(pendentes) == 0
    acertou_tudo = respondido and total_acertos == len(DIAG_QUESTOES)
    precisa_reforco = respondido and total_acertos < len(DIAG_QUESTOES)

    return {
        "respondido": respondido,
        "pendentes": pendentes,
        "respostas": respostas,
        "corretas": corretas,
        "erradas": erradas,
        "q1_correta": Q_D_001 in corretas,
        "q2_correta": Q_D_002 in corretas,
        "total_acertos": total_acertos,
        "acertou_tudo": acertou_tudo,
        "precisa_reforco": precisa_reforco,
    }


def _bloco_diagnostico_q1() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_001,
        "pergunta": (
            "Em uma instalação de bombeamento com motor monofásico, qual relação representa "
            "corretamente a potência ativa em função da tensão, da corrente e do fator de potência?"
        ),
        "alternativas": {
            "a": r"$P = V \,/\, (I\cos\varphi)$",
            "b": r"$P = V\,I\,\cos\varphi$",
            "c": r"$P = \sqrt{3}\,V\,I$",
            "d": r"$P = I^2 \,/\, R$",
        },
        "alternativa_correta": "b",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "No circuito de alimentação trifásico de um motor de bomba, usando tensão de linha "
            "e corrente de linha em regime equilibrado, qual expressão representa corretamente "
            "a potência ativa total do sistema?"
        ),
        "alternativas": {
            "a": r"$P = V\,I\,\cos\varphi$",
            "b": r"$P = 3\,V\,I$",
            "c": r"$P = \sqrt{3}\,V_L\,I_L\,\cos\varphi$",
            "d": r"$P = V_L\,I_L \,/\, \cos\varphi$",
        },
        "alternativa_correta": "c",
    }


def _mapa_blocos_diagnostico() -> dict[str, dict]:
    return {
        Q_D_001: _bloco_diagnostico_q1(),
        Q_D_002: _bloco_diagnostico_q2(),
    }


def _blocos_diagnostico_completo() -> list[dict]:
    return [
        _bloco_diagnostico_q1(),
        _bloco_diagnostico_q2(),
    ]


def _blocos_diagnostico_pendentes() -> list[dict]:
    resultado = _resultado_diagnostico()
    pendentes = resultado["pendentes"]
    mapa = _mapa_blocos_diagnostico()

    blocos: list[dict] = [
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Você já iniciou o diagnóstico. Responda apenas as questões que ainda estão pendentes."
            ),
        }
    ]

    for qid in pendentes:
        if qid in mapa:
            blocos.append(mapa[qid])

    return blocos


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre relações fundamentais de circuitos "
                "aplicadas a sistemas monofásicos e trifásicos no contexto de alimentação de motores. "
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
    resultado = _resultado_diagnostico()

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
                    "Na questão 1, a resposta correta é <b>b</b>. Em regime monofásico senoidal, "
                    "a potência ativa absorvida por uma carga é dada por:\n\n"
                    r"$$ P = V\,I\,\cos\varphi $$"
                    "\n\n"
                    "em que <b>V</b> é a tensão eficaz, <b>I</b> é a corrente eficaz e "
                    "<b>cosφ</b> é o fator de potência. Quando se deseja determinar a corrente, "
                    "a expressão pode ser reorganizada para:\n\n"
                    r"$$ I = \frac{P}{V\,\cos\varphi} $$"
                    "\n\n"
                    "Essa relação é central na análise de circuitos monofásicos, pois permite "
                    "estimar a corrente exigida pelo motor a partir dos dados nominais do sistema."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é <b>c</b>. Em um sistema trifásico equilibrado, "
                    "a potência ativa total pode ser escrita em função da tensão de linha e da corrente "
                    "de linha por:\n\n"
                    r"$$ P = \sqrt{3}\,V_L\,I_L\,\cos\varphi $$"
                    "\n\n"
                    "O fator <b>√3</b> decorre da relação entre grandezas de fase e grandezas de linha "
                    "no sistema trifásico. Reorganizando a equação, obtém-se:\n\n"
                    r"$$ I_L = \frac{P}{\sqrt{3}\,V_L\,\cos\varphi} $$"
                    "\n\n"
                    "Essa expressão é indispensável para calcular a corrente do circuito e verificar "
                    "as condições de alimentação do motor em instalações trifásicas."
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
                "Em circuitos elétricos de alimentação de motores, a relação entre tensão, corrente "
                "e potência constitui a base para interpretar a carga imposta ao sistema. No contexto "
                "do bombeamento, o motor converte energia elétrica em energia mecânica, mas essa "
                "conversão depende de uma alimentação capaz de fornecer a potência requerida sob "
                "condições adequadas de tensão e corrente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em regime monofásico senoidal, a potência ativa absorvida por uma carga é dada por:\n\n"
                r"$$ P = V\,I\,\cos\varphi $$"
                "\n\n"
                "em que <b>P</b> é a potência ativa, <b>V</b> é a tensão eficaz, <b>I</b> é a "
                "corrente eficaz e <b>cosφ</b> é o fator de potência. Para fins de dimensionamento, "
                "a expressão pode ser reescrita como:\n\n"
                r"$$ I = \frac{P}{V\,\cos\varphi} $$"
                "\n\n"
                "Essa forma é especialmente útil quando a potência e a tensão do motor são conhecidas "
                "e se deseja estimar a corrente que circulará nos condutores."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em sistemas trifásicos equilibrados, muito comuns em instalações de bombeamento, "
                "a potência ativa total é expressa por:\n\n"
                r"$$ P = \sqrt{3}\,V_L\,I_L\,\cos\varphi $$"
                "\n\n"
                "em que <b>V_L</b> é a tensão de linha e <b>I_L</b> é a corrente de linha. "
                "Assim, a corrente do circuito pode ser calculada por:\n\n"
                r"$$ I_L = \frac{P}{\sqrt{3}\,V_L\,\cos\varphi} $$"
                "\n\n"
                "A presença do fator <b>√3</b> diferencia a formulação trifásica da monofásica "
                "e expressa a estrutura elétrica do sistema de três fases."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando o motor é especificado em potência mecânica nominal, convém considerar "
                "também o rendimento <b>η</b>. Nesse caso, a potência elétrica de entrada é maior "
                "que a potência útil no eixo. Para um sistema monofásico, pode-se escrever:\n\n"
                r"$$ P_{in} = \frac{P_{out}}{\eta} $$"
                "\n\n"
                r"$$ I = \frac{P_{out}}{\eta\,V\,\cos\varphi} $$"
                "\n\n"
                "e, para um sistema trifásico equilibrado:\n\n"
                r"$$ I_L = \frac{P_{out}}{\sqrt{3}\,\eta\,V_L\,\cos\varphi} $$"
                "\n\n"
                "Essas expressões aproximam o cálculo das condições reais de operação do motor."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além do cálculo da corrente, essas relações são o ponto de partida para etapas "
                "posteriores do projeto elétrico, como verificação da capacidade de condução dos "
                "condutores, análise da queda de tensão e compatibilização entre o motor e a rede "
                "de alimentação. Compreender a diferença entre alimentação monofásica e trifásica "
                "é, portanto, uma exigência técnica para interpretar corretamente a solicitação "
                "elétrica do circuito."
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
            "tipo": "texto",
            "texto": (
                "No sistema estudado, essas relações permitem transformar os dados nominais do motor "
                "da bomba em uma corrente de projeto para o circuito de alimentação. A partir dela, "
                "torna-se possível avaliar se a seção dos condutores é compatível com a operação "
                "prevista e se a alimentação ocorrerá em condições tecnicamente adequadas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Se a alimentação for monofásica, a corrente tende a ser mais elevada para uma mesma "
                "potência, quando comparada a uma alimentação trifásica em tensão apropriada. Já em "
                "sistemas trifásicos, a distribuição de potência entre três fases tende a favorecer "
                "o fornecimento a motores de maior porte, o que influencia diretamente o dimensionamento "
                "dos cabos."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "<b>Síntese conceitual</b>\n\n"
                "Em rede monofásica, a potência ativa pode ser expressa por "
                r"$P = V\,I\,\cos\varphi$"
                ". Em rede trifásica equilibrada, utiliza-se "
                r"$P = \sqrt{3}\,V_L\,I_L\,\cos\varphi$"
                ". A corrente do circuito depende do tipo de alimentação adotado, e o uso de "
                "fator de potência e rendimento torna a análise mais próxima das condições reais "
                "de operação do motor. Essas relações constituem a base do dimensionamento da "
                "alimentação elétrica."
            ),
        },
    ]


def _blocos_reflexao_final() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Reflexão final",
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
                "Um motor monofásico opera sob tensão eficaz constante. Admitindo o mesmo fator "
                "de potência, o que ocorre com a corrente do circuito quando a potência ativa "
                "requerida aumenta?"
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
                "em rede monofásica e outro em rede trifásica equilibrada, a principal diferença "
                "no cálculo da corrente está em:"
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
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAG_QUESTOES):
            return _blocos_diagnostico_pendentes()
        return _blocos_diagnostico_completo()

    if resultado["acertou_tudo"]:
        return _blocos_sucesso_diagnostico()

    return (
        _blocos_correcao_diagnostico()
        + _blocos_reforco()
        + _blocos_reflexao_final()
    )


def render_controles_especiais() -> None:
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAG_QUESTOES):
            st.info("Diagnóstico em andamento. Responda apenas as questões pendentes.")
        else:
            st.info("Responda às duas questões iniciais. O reforço será liberado automaticamente se necessário.")
        return

    if resultado["acertou_tudo"]:
        st.success("Diagnóstico concluído com domínio.")
        return

    st.warning("Diagnóstico concluído. O bloco de reforço foi liberado com base nas suas respostas.")