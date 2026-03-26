from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_01"

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
    }


def _bloco_diagnostico_q2() -> dict:
    return {
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
                "Você demonstrou domínio inicial sobre tensão elétrica, corrente elétrica e suas "
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
                    "Na questão 1, a resposta correta é <b>b</b>. A <b>tensão elétrica</b> é a "
                    "<b>diferença de potencial</b> entre dois pontos do circuito. Ela representa a "
                    "energia potencial elétrica disponível por unidade de carga para impulsionar o "
                    "movimento das cargas. Em termos gerais:\n\n"
                    "$$ V = \\frac{W}{q} $$\n\n"
                    "em que <b>V</b> é a tensão, <b>W</b> é o trabalho ou energia transferida e "
                    "<b>q</b> é a carga elétrica. No circuito de alimentação do motor, a tensão "
                    "fornecida pela rede estabelece a condição energética necessária para a circulação "
                    "de corrente."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é <b>c</b>. A <b>corrente elétrica</b> expressa "
                    "a taxa de escoamento de carga elétrica através de uma seção transversal do condutor. "
                    "Sua definição fundamental é:\n\n"
                    "$$ I = \\frac{\\Delta q}{\\Delta t} $$\n\n"
                    "em que <b>I</b> é a corrente, <b>Δq</b> é a quantidade de carga transportada e "
                    "<b>Δt</b> é o intervalo de tempo. No circuito do motor, a corrente indica a "
                    "intensidade da solicitação elétrica imposta aos cabos e está diretamente ligada "
                    "à análise de aquecimento, perdas e dimensionamento."
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
                "A análise do circuito de alimentação de um motor de bombeamento começa pela "
                "compreensão de três grandezas elétricas fundamentais: <b>tensão elétrica</b>, "
                "<b>corrente elétrica</b> e <b>potência elétrica</b>. Essas grandezas estruturam "
                "a descrição física do sistema e permitem relacionar a fonte de alimentação, "
                "os condutores e a carga representada pelo motor."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Tensão elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>tensão elétrica</b> representa a diferença de potencial entre dois pontos "
                "do circuito. Fisicamente, ela expressa a energia disponível por unidade de carga "
                "para promover o deslocamento dos portadores elétricos. Sua definição geral pode "
                "ser escrita como:\n\n"
                "$$ V = \\frac{W}{q} $$\n\n"
                "em que <b>V</b> é a tensão, <b>W</b> é a energia transferida e <b>q</b> é a carga "
                "elétrica. No sistema de alimentação do motor, a tensão fornecida pela rede estabelece "
                "a condição energética necessária para que haja circulação de corrente elétrica."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Corrente elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>corrente elétrica</b> corresponde à taxa de passagem de carga elétrica por uma "
                "seção do condutor. Ela é descrita por:\n\n"
                "$$ I = \\frac{\\Delta q}{\\Delta t} $$\n\n"
                "em que <b>I</b> é a corrente, <b>Δq</b> é a quantidade de carga e <b>Δt</b> é o "
                "intervalo de tempo. Do ponto de vista da instalação, a corrente é uma das variáveis "
                "mais relevantes, pois determina o esforço elétrico imposto aos condutores e influencia "
                "diretamente aquecimento, perdas e critérios de dimensionamento."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Potência elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>potência elétrica</b> expressa a taxa com que a energia elétrica é transferida "
                "ou convertida. Em formulações básicas, pode ser escrita como:\n\n"
                "$$ P = V\\,I $$\n\n"
                "Em elementos resistivos, também podem ser utilizadas as formas:\n\n"
                "$$ P = R\\,I^2 $$\n\n"
                "$$ P = \\frac{V^2}{R} $$\n\n"
                "Já em sistemas de corrente alternada aplicados a motores, a potência ativa absorvida "
                "é mais adequadamente representada por:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "para sistemas monofásicos, e por:\n\n"
                "$$ P = \\sqrt{3}\\,V\\,I\\,\\cos\\varphi $$\n\n"
                "para sistemas trifásicos equilibrados, em que <b>cosφ</b> é o fator de potência."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No caso do motor da bomba, essas relações permitem determinar a corrente exigida "
                "pelo equipamento a partir da potência nominal, da tensão de alimentação e das "
                "características operacionais do sistema. Para uma análise mais realista, especialmente "
                "em engenharia, é comum considerar também o rendimento do motor. Assim, em um sistema "
                "monofásico:\n\n"
                "$$ I = \\frac{P}{V\\,\\cos\\varphi\\,\\eta} $$\n\n"
                "e, em um sistema trifásico:\n\n"
                "$$ I = \\frac{P}{\\sqrt{3}\\,V\\,\\cos\\varphi\\,\\eta} $$\n\n"
                "em que <b>η</b> representa o rendimento."
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
                "Essas grandezas não devem ser estudadas de forma isolada. No circuito de alimentação "
                "do motor, a tensão imposta pela rede produz a circulação de corrente, e essa corrente, "
                "combinada com a tensão e com as características da carga, define a potência elétrica "
                "absorvida pelo sistema. É essa corrente que será comparada com a capacidade admissível "
                "dos condutores no dimensionamento do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Portanto, compreender tensão, corrente e potência é o primeiro passo para interpretar "
                "tecnicamente o funcionamento do sistema de bombeamento. Sem esse bloco conceitual, "
                "não é possível avaliar com rigor se os cabos instalados são suficientes para alimentar "
                "o motor com segurança e desempenho adequado."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "<b>Síntese conceitual</b>\n\n"
                "A tensão elétrica representa diferença de potencial e energia por unidade de carga. "
                "A corrente elétrica mede a taxa de escoamento de cargas no circuito. A potência elétrica "
                "expressa a taxa de transferência ou conversão de energia. Em motores, a corrente depende "
                "de tensão, potência, fator de potência e rendimento. Essas grandezas constituem a base "
                "para analisar a alimentação elétrica do motor da bomba."
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