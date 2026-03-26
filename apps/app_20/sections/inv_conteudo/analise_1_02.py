from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_02"

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
            "Em um trecho do circuito de alimentação de um motor de bomba, mede-se uma tensão de 24 V "
            "aplicada a um condutor equivalente cuja resistência total é 6 Ω. De acordo com a Lei de Ohm, "
            "a corrente elétrica nesse trecho é:"
        ),
        "alternativas": {
            "a": "0,25 A",
            "b": "4 A",
            "c": "18 A",
            "d": "144 A",
        },
        "alternativa_correta": "b",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "Um equipamento elétrico opera em corrente contínua com potência de 2200 W sob tensão de 220 V. "
            "Desprezando perdas adicionais, a corrente elétrica requerida é:"
        ),
        "alternativas": {
            "a": "0,1 A",
            "b": "4,5 A",
            "c": "10 A",
            "d": "484 A",
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
                "Você demonstrou domínio inicial sobre Lei de Ohm e sobre as relações entre "
                "potência, tensão e corrente em circuitos elétricos. Este conteúdo pode ser "
                "considerado concluído nesta etapa."
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
                    "Na questão 1, a resposta correta é <b>b</b>. Pela <b>Lei de Ohm</b>, a relação entre "
                    "tensão, resistência e corrente é dada por:\n\n"
                    "$$ V = R\\,I $$\n\n"
                    "Logo:\n\n"
                    "$$ I = \\frac{V}{R} = \\frac{24}{6} = 4\\ \\text{A} $$\n\n"
                    "Essa relação mostra que, em um trecho resistivo do circuito, a corrente elétrica "
                    "depende diretamente da tensão aplicada e da resistência equivalente associada à passagem "
                    "de cargas. Em análises de engenharia, essa equação é fundamental para interpretar "
                    "solicitações elétricas em condutores e cargas."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é <b>c</b>. Em uma formulação simplificada, a relação "
                    "entre potência, tensão e corrente é:\n\n"
                    "$$ P = V\\,I $$\n\n"
                    "Isolando a corrente:\n\n"
                    "$$ I = \\frac{P}{V} = \\frac{2200}{220} = 10\\ \\text{A} $$\n\n"
                    "Essa equação é central na análise de circuitos de alimentação, pois permite estimar a "
                    "corrente exigida por uma carga a partir de sua potência elétrica e da tensão de operação. "
                    "No dimensionamento de condutores, essa corrente calculada constitui um parâmetro básico."
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
                "A interpretação de circuitos elétricos em aplicações de engenharia depende da compreensão "
                "das relações matemáticas que conectam as grandezas fundamentais do sistema. No caso de um "
                "circuito de alimentação de motor, as relações entre tensão, corrente, resistência e potência "
                "permitem estimar a solicitação elétrica imposta aos condutores e avaliar se a instalação "
                "opera em condições compatíveis com o problema analisado."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Lei de Ohm",
        },
        {
            "tipo": "texto",
            "texto": (
                "A <b>Lei de Ohm</b> descreve a relação básica entre tensão elétrica, corrente elétrica e "
                "resistência em um elemento resistivo:\n\n"
                "$$ V = R\\,I $$\n\n"
                "em que <b>V</b> é a diferença de potencial, <b>R</b> é a resistência elétrica e <b>I</b> é "
                "a corrente. Essa expressão também pode ser escrita como:\n\n"
                "$$ I = \\frac{V}{R} $$\n\n"
                "ou\n\n"
                "$$ R = \\frac{V}{I} $$\n\n"
                "Essas formas são úteis quando se deseja calcular a corrente que atravessa um trecho do circuito "
                "ou a resistência equivalente associada à passagem de corrente elétrica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em condutores elétricos, a resistência depende do material, do comprimento e da seção "
                "transversal. Para análise de engenharia, essa dependência pode ser representada por:\n\n"
                "$$ R = \\rho\\,\\frac{L}{A} $$\n\n"
                "em que <b>ρ</b> é a resistividade elétrica do material, <b>L</b> é o comprimento do condutor "
                "e <b>A</b> é a área da seção transversal. Essa equação é importante em instalações elétricas "
                "porque mostra que cabos mais longos ou com menor seção apresentam maior resistência, o que "
                "afeta a corrente, as perdas e a queda de tensão."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Relação entre potência, tensão e corrente",
        },
        {
            "tipo": "texto",
            "texto": (
                "Outra relação fundamental conecta <b>potência elétrica</b>, <b>tensão</b> e <b>corrente</b>. "
                "Em sua forma elementar, tem-se:\n\n"
                "$$ P = V\\,I $$\n\n"
                "em que <b>P</b> é a potência elétrica ativa fornecida à carga em uma formulação simplificada. "
                "Essa expressão permite obter:\n\n"
                "$$ I = \\frac{P}{V} $$\n\n"
                "e também:\n\n"
                "$$ V = \\frac{P}{I} $$\n\n"
                "No contexto do circuito de alimentação de um motor, essa relação é usada para estimar a corrente "
                "requerida a partir da potência nominal e da tensão de operação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em problemas de engenharia elétrica aplicada, especialmente em motores, a análise pode exigir "
                "formas mais completas da potência. Em sistemas monofásicos com fator de potência, utiliza-se:\n\n"
                "$$ P = V\\,I\\,\\cos\\varphi $$\n\n"
                "e, em sistemas trifásicos equilibrados:\n\n"
                "$$ P = \\sqrt{3}\\,V\\,I\\,\\cos\\varphi $$\n\n"
                "Para motores reais, o rendimento também interfere, pois a potência elétrica absorvida não coincide "
                "exatamente com a potência mecânica útil. Por isso, em análises mais completas, fator de potência "
                "e rendimento precisam ser considerados."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=aFrag-RGDhQ",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=jzGOUszBHEU",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, o motor da bomba constitui a carga principal do circuito. A tensão fornecida "
                "pela rede e a potência exigida pelo motor determinam a corrente elétrica que circulará nos "
                "condutores. Essa corrente, ao atravessar cabos com resistência não nula, produz dissipação de "
                "energia e queda de tensão ao longo do percurso."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Assim, a Lei de Ohm ajuda a interpretar o efeito da resistência dos condutores no comportamento "
                "do circuito, enquanto a relação entre potência, tensão e corrente permite calcular a solicitação "
                "elétrica imposta pela carga. Em conjunto, essas duas bases fornecem o ponto de partida para "
                "avaliar se os condutores de alimentação do motor estão adequadamente dimensionados."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "<b>Síntese conceitual</b>\n\n"
                "A Lei de Ohm relaciona tensão, corrente e resistência. A resistência do condutor depende do "
                "material, do comprimento e da seção transversal. A potência elétrica, em forma simplificada, "
                "pode ser expressa por P = VI, permitindo estimar a corrente requerida por uma carga. Em motores, "
                "fator de potência e rendimento podem precisar ser considerados. Essas relações são a base para "
                "analisar o circuito de alimentação da bomba."
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
                "A resistência elétrica equivalente de um trecho de circuito é 8 Ω e a corrente que o atravessa "
                "é 3 A. A tensão elétrica nesse trecho vale:"
            ),
            "alternativas": {
                "a": "11 V",
                "b": "24 V",
                "c": "5 V",
                "d": "0,375 V",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Um equipamento opera com potência de 1500 W em uma tensão de 127 V, em análise simplificada. "
                "A corrente aproximada exigida é:"
            ),
            "alternativas": {
                "a": "0,085 A",
                "b": "8,5 A",
                "c": "11,8 A",
                "d": "190,5 A",
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