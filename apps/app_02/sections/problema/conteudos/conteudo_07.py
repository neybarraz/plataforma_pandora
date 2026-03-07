from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Foco de análise do sistema elétrico",
        },
        {
            "tipo": "texto",
            "texto": (
                "Com o problema elétrico definido, é necessário identificar quais "
                "aspectos do funcionamento do motor serão analisados ao longo da "
                "investigação. Em um sistema de bombeamento acionado por motor elétrico, "
                "o comportamento do circuito depende de diferentes grandezas elétricas "
                "relacionadas à operação do equipamento.\n\n"
                "Entre os principais elementos que influenciam a alimentação elétrica "
                "do motor estão a corrente de operação, a corrente de partida, o "
                "dimensionamento adequado dos condutores, o tipo de ligação elétrica "
                "do motor e a queda de tensão ao longo do circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_021",
            "pergunta": (
                "Qual conjunto de aspectos representa corretamente o foco de análise "
                "do sistema elétrico neste estudo?"
            ),
            "alternativas": {
                "a": "Volume do reservatório, altura da caixa d’água e tipo de tubulação",
                "b": "Corrente de operação, corrente de partida, condutores, ligação do motor e queda de tensão",
                "c": "Temperatura da água, pressão hidráulica e tipo de válvula",
                "d": "Quantidade de moradores do prédio e consumo diário de água",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Cada um desses elementos está diretamente relacionado ao "
                "comportamento elétrico do motor no circuito. A corrente de "
                "operação representa a corrente consumida durante o funcionamento "
                "normal do equipamento, enquanto a corrente de partida indica o "
                "valor momentâneo necessário para iniciar o movimento do motor.\n\n"
                "Além disso, o dimensionamento dos condutores precisa garantir que "
                "os cabos suportem a corrente do circuito, o tipo de ligação do "
                "motor define como ele deve ser conectado à rede elétrica e a "
                "queda de tensão permite avaliar as perdas elétricas ao longo do "
                "circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao analisar o sistema elétrico da motobomba, procure identificar "
                "como cada um desses fatores influencia o funcionamento do motor "
                "e quais deles precisam ser considerados para garantir uma "
                "alimentação elétrica adequada."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_022",
            "pergunta": (
                "Explique, com suas palavras, por que a corrente de operação, "
                "a corrente de partida, o dimensionamento dos condutores, o tipo "
                "de ligação do motor e a queda de tensão são aspectos importantes "
                "na análise da alimentação elétrica de um motor."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]