from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Plano de Análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "Antes de executar a investigação, é necessário definir como o sistema elétrico será analisado. "
                "Nesta etapa, você deve observar o circuito de alimentação do motor da bomba e organizar um "
                "plano de análise que permita avaliar a relação entre a corrente exigida pelo motor e a capacidade "
                "dos condutores utilizados no circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo não é apresentar a conclusão do problema, mas construir um caminho de investigação. "
                "Para isso, observe como a energia elétrica percorre o circuito até o motor e quais fatores podem "
                "influenciar o comportamento elétrico do sistema. Pense também em quais grandezas precisam ser "
                "determinadas ou estimadas para que seja possível verificar se os condutores estão adequados para "
                "a operação do motor."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_01_q_0001",
            "pergunta": (
                "Ao analisar o sistema de alimentação do motor, quais condições ou aspectos do circuito precisam ser "
                "considerados para que a investigação faça sentido?"
            ),
            "placeholder": (
                "Descreva quais partes do sistema elétrico e quais condições devem ser consideradas na análise..."
            ),
            "altura": 140,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_01_q_0002",
            "pergunta": (
                "Quais grandezas elétricas, características do circuito ou propriedades dos condutores você considera "
                "importantes para observar ou determinar durante a análise?"
            ),
            "placeholder": (
                "Indique o que deve ser analisado, como corrente, tensão, potência, comprimento do circuito, seção dos cabos..."
            ),
            "altura": 160,
        },
        {
            "tipo": "texto",
            "texto": (
                "Um bom plano de análise costuma responder a três perguntas centrais: "
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Quais características do sistema elétrico serão consideradas?",
                "O que será calculado ou verificado em relação ao motor e aos condutores?",
                "Como os resultados poderão ser comparados para avaliar a adequação do circuito?",
            ],
        },
        {
            "tipo": "texto",
            "texto": (
                "No caso deste sistema, é importante considerar as características elétricas do motor, "
                "o tipo de alimentação, o comprimento do circuito e as propriedades dos condutores. "
                "A análise deve permitir comparar a corrente exigida pelo motor com a capacidade de condução "
                "dos cabos, além de verificar possíveis efeitos como queda de tensão no circuito."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_01_q_0003",
            "pergunta": (
                "Com base na sua análise do sistema, escreva seu plano de investigação. "
                "Explique como a análise será conduzida, quais parâmetros serão considerados, "
                "o que será calculado ou verificado e por que isso permite avaliar o dimensionamento dos condutores."
            ),
            "placeholder": (
                "Escreva aqui seu plano de análise..."
            ),
            "altura": 220,
        },
    ]