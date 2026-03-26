from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Hipótese de trabalho",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve antecipar o comportamento do sistema antes da análise completa. "
                "A hipótese de trabalho é uma previsão fundamentada: ela indica o que você espera observar "
                "em relação ao funcionamento elétrico do motor da bomba e qual explicação técnica você propõe "
                "para esse comportamento."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Para construir sua hipótese, retome o sistema analisado e o plano de análise que você elaborou. "
                "Observe especialmente a relação entre a corrente exigida pelo motor e a capacidade de condução "
                "dos condutores do circuito de alimentação."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Observe e antecipe o comportamento do sistema",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_02_q_0001",
            "pergunta": (
                "Considerando as características do motor e do circuito, o que você espera em relação à corrente elétrica "
                "exigida pelo motor durante sua operação?"
            ),
            "placeholder": (
                "Descreva como você espera que a corrente do motor se comporte em função de sua potência e tensão..."
            ),
            "altura": 140,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_02_q_0002",
            "pergunta": (
                "Com base nessa corrente, você acredita que os condutores do circuito estão adequados ou podem estar "
                "subdimensionados para a operação do motor?"
            ),
            "placeholder": (
                "Indique se os cabos parecem adequados ou não e justifique sua expectativa..."
            ),
            "altura": 140,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_02_q_0003",
            "pergunta": (
                "Quais conceitos elétricos (por exemplo: corrente elétrica, potência, resistência elétrica, queda de tensão) "
                "podem ajudar a explicar essa situação?"
            ),
            "placeholder": (
                "Relacione os conceitos que você considera importantes para explicar o comportamento do circuito..."
            ),
            "altura": 160,
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma hipótese bem formulada deve conter dois elementos: "
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "(1) uma previsão clara do comportamento do sistema e ",
                "(2) uma explicação baseada em conceitos elétricos.",
            ],
        },
        {
            "tipo": "subtitulo",
            "texto": "Formule sua hipótese",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_02_q_0004",
            "pergunta": (
                "Com base nas suas respostas anteriores, escreva sua hipótese de trabalho. "
                "Indique se você espera que os condutores estejam adequados ou subdimensionados "
                "e apresente uma explicação técnica para essa previsão."
            ),
            "placeholder": (
                "Escreva sua hipótese de trabalho de forma clara e fundamentada..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: evite respostas muito curtas. Sua hipótese deve relacionar as características do motor "
                "com o comportamento elétrico do circuito e os limites dos condutores."
            ),
        },
    ]