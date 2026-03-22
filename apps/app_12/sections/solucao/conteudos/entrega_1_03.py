from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Verificação da hipótese",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve comparar a hipótese formulada anteriormente com os resultados obtidos "
                "durante a investigação. O objetivo é verificar se a previsão inicial foi confirmada, refutada "
                "ou se precisa ser ajustada com base nas evidências produzidas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Verificar uma hipótese não significa apenas dizer se ela está certa ou errada. "
                "É necessário mostrar como os dados obtidos se relacionam com a previsão formulada "
                "e explicar por que a hipótese pode ser aceita, rejeitada ou reformulada."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_03_q_001",
            "pergunta": (
                "Retome a hipótese formulada anteriormente. O que você esperava observar no sistema?"
            ),
            "placeholder": (
                "Reescreva a hipótese inicial ou explique, com suas palavras, qual era a previsão formulada..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_03_q_002",
            "pergunta": (
                "Ao comparar a hipótese com os resultados do experimento, ela foi confirmada, refutada ou precisa ser ajustada?"
            ),
            "placeholder": (
                "Indique claramente se a hipótese foi confirmada, refutada ou ajustada..."
            ),
            "altura": 130,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_03_q_003",
            "pergunta": (
                "Quais resultados do experimento sustentam essa avaliação da hipótese?"
            ),
            "placeholder": (
                "Relacione os dados e observações que confirmam, contradizem ou exigem ajuste da hipótese..."
            ),
            "altura": 170,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_03_q_004",
            "pergunta": (
                "Explique por que esses resultados permitem avaliar a hipótese dessa maneira."
            ),
            "placeholder": (
                "Mostre como os dados se conectam à previsão formulada inicialmente..."
            ),
            "altura": 180,
        },
        {
            "tipo": "texto",
            "texto": (
                "Em uma investigação técnica, a hipótese deve ser avaliada com base em evidências. "
                "No caso deste estudo, é importante observar especialmente se a carga continuou funcionando, "
                "se a bateria manteve participação no sistema e se o conversor preservou a tensão de saída "
                "em nível compatível com o funcionamento da carga."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "continuidade ou interrupção do funcionamento da carga",
                "presença de tensão na bateria após a retirada da fonte externa",
                "manutenção da tensão de saída do conversor",
                "comparação entre o comportamento esperado e o comportamento observado",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_03_q_005",
            "pergunta": (
                "Escreva, em um parágrafo, a verificação final da hipótese de trabalho."
            ),
            "placeholder": (
                "Apresente de forma clara se a hipótese foi confirmada, refutada ou ajustada, e justifique com base nos resultados..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: não basta afirmar que a hipótese foi confirmada ou refutada. "
                "Mostre quais dados sustentam essa avaliação."
            ),
        },
    ]