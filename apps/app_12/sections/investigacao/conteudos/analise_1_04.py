from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_04"

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
            "Em um motor elétrico de bombeamento, a grandeza <b>potência nominal</b> indicada na placa "
            "deve ser interpretada, do ponto de vista do circuito, como:"
        ),
        "alternativas": {
            "a": "A energia total acumulada pelo motor ao longo do funcionamento",
            "b": "A taxa de conversão ou demanda de energia sob condições nominais de operação",
            "c": "A maior tensão transitória suportada pelos enrolamentos",
            "d": "A corrente de partida que ocorre no instante do acionamento",
        },
        "alternativa_correta": "b",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "No circuito de alimentação do motor da bomba, a <b>corrente nominal</b> deve ser entendida como:"
        ),
        "alternativas": {
            "a": "A corrente máxima possível em qualquer condição de falha",
            "b": "A corrente que independe da potência e da tensão do equipamento",
            "c": "A corrente requerida pelo motor em regime nominal, nas condições previstas de operação",
            "d": "A corrente que circula apenas nos dispositivos de proteção",
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
                "Você demonstrou domínio inicial sobre potência nominal, corrente nominal e suas "
                "relações com a análise da alimentação do motor. Este conteúdo pode ser considerado "
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
                    "Na questão 1, a resposta correta é <b>b</b>. A <b>potência nominal</b> de um motor "
                    "expressa a taxa com que a energia é convertida ou requerida em regime nominal de "
                    "operação. Em circuitos elétricos, potência não representa energia acumulada, mas uma "
                    "grandeza de taxa, usualmente expressa em watt. No estudo do motor da bomba, esse "
                    "parâmetro é central porque, em conjunto com a tensão de alimentação, o fator de "
                    "potência e o rendimento, permite estimar a corrente exigida pelo equipamento."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é <b>c</b>. A <b>corrente nominal</b> corresponde "
                    "à corrente absorvida pelo motor em regime nominal, sob as condições para as quais ele "
                    "foi especificado. Esse valor é essencial para o dimensionamento dos condutores, pois "
                    "a seção do cabo deve ser compatível com a corrente que circulará no circuito. Assim, "
                    "a corrente nominal funciona como uma das principais entradas para a análise da "
                    "capacidade de condução de corrente e da queda de tensão."
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
                "em que <b>P</b> é a potência elétrica, <b>V</b> é a tensão elétrica e <b>I</b> é a "
                "corrente elétrica. Embora motores reais em corrente alternada exijam um modelo "
                "mais completo, essa expressão constitui o ponto de partida conceitual para "
                "relacionar demanda de potência e solicitação de corrente no circuito."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Potência nominal do motor",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>potência nominal do motor</b> é o valor de potência associado à condição de "
                "operação para a qual o equipamento foi especificado. Em aplicações de bombeamento, "
                "esse parâmetro indica a ordem de grandeza da energia por unidade de tempo que o "
                "motor deve converter para manter o sistema em funcionamento. Em corrente alternada, "
                "a análise da potência ativa consumida por um motor monofásico pode ser expressa por:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "e, para sistemas trifásicos equilibrados, por:\n\n"
                "$$ P = \\sqrt{3}\\,V_L\\,I_L\\,\\cos\\varphi $$\n\n"
                "em que <b>\\cos\\varphi</b> é o fator de potência, <b>V_L</b> é a tensão de linha e "
                "<b>I_L</b> é a corrente de linha."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Tensão nominal de operação",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>tensão nominal de operação</b> é a diferença de potencial para a qual o motor "
                "foi projetado. Ela define a condição elétrica esperada nos terminais do equipamento "
                "durante o funcionamento adequado. Se a tensão disponível no circuito for inferior "
                "ou superior ao valor nominal, a corrente absorvida pelo motor e o seu comportamento "
                "térmico podem se alterar. Na prática, esse parâmetro é essencial porque conecta o "
                "equipamento à rede elétrica disponível e condiciona a interpretação correta das "
                "demais grandezas nominais do motor."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Corrente nominal",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>corrente nominal</b> representa a corrente que o motor exige quando opera nas "
                "condições previstas de carga, tensão e frequência. Em estudos de dimensionamento "
                "de condutores, essa grandeza é crítica porque indica a solicitação elétrica imposta "
                "ao cabo. Rearranjando as equações de potência, obtém-se, para o caso monofásico:\n\n"
                "$$ I = \\frac{P}{V\\,\\cos\\varphi} $$\n\n"
                "e, para o caso trifásico:\n\n"
                "$$ I_L = \\frac{P}{\\sqrt{3}\\,V_L\\,\\cos\\varphi} $$\n\n"
                "Quando se considera o rendimento do motor, a potência elétrica de entrada passa a "
                "se relacionar com a potência útil por meio de <b>\\eta</b>, refinando a estimativa da "
                "corrente nominal exigida pelo equipamento."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Para motores reais, a interpretação correta dessas grandezas evita erros de análise "
                "no circuito de alimentação. Um motor com maior potência nominal, para uma mesma tensão, "
                "tende a demandar maior corrente. Da mesma forma, para uma mesma potência, tensões mais "
                "elevadas tendem a reduzir a corrente requerida, o que impacta diretamente o dimensionamento "
                "dos condutores e a queda de tensão. Portanto, potência nominal, tensão nominal e corrente "
                "nominal não devem ser vistas como dados isolados da placa do motor, mas como grandezas "
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
            "tipo": "texto",
            "texto": (
                "<b>Síntese conceitual</b>\n\n"
                "A potência elétrica representa a taxa de conversão ou transferência de energia. "
                "A potência nominal define a demanda elétrica associada à operação do motor. A tensão "
                "nominal estabelece a condição elétrica prevista para funcionamento adequado. A corrente "
                "nominal expressa a solicitação elétrica efetiva imposta ao circuito. Em corrente alternada, "
                "fator de potência e rendimento influenciam a corrente requerida. Essas grandezas constituem "
                "a base para analisar a alimentação elétrica do motor da bomba."
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