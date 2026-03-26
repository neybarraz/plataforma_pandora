from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Suficiência de evidências",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve avaliar se as evidências obtidas ao longo da investigação foram suficientes "
                "para responder à pergunta do estudo. O foco aqui não é verificar se os dados são perfeitos, "
                "mas se eles oferecem base adequada para sustentar a interpretação e a decisão técnica formulada."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma evidência é considerada suficiente quando permite responder ao problema com base em observações, "
                "medições e relações conceituais consistentes com o objetivo do estudo."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_02_q_001",
            "pergunta": (
                "Os dados e observações obtidos foram suficientes para responder à pergunta central do estudo? Explique."
            ),
            "placeholder": (
                "Explique se as evidências produzidas permitem responder ao problema investigado..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_02_q_002",
            "pergunta": (
                "Quais evidências foram mais importantes para sustentar a resposta final apresentada?"
            ),
            "placeholder": (
                "Indique os dados e observações que tiveram maior peso na construção da resposta técnica..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_02_q_003",
            "pergunta": (
                "Houve alguma informação importante que não foi obtida, mas que poderia tornar a análise mais forte?"
            ),
            "placeholder": (
                "Explique se faltou algum dado complementar e como ele poderia contribuir para a investigação..."
            ),
            "altura": 170,
        },
        {
            "tipo": "texto",
            "texto": (
                "Avaliar a suficiência das evidências não significa exigir exatidão absoluta. "
                "Em muitos estudos didáticos, a questão principal é verificar se o conjunto de dados produzido "
                "já é suficiente para sustentar a resposta em nível compatível com o escopo da investigação."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "os dados devem ser relevantes para o problema formulado",
                "as observações devem permitir interpretar o comportamento do sistema",
                "as evidências precisam sustentar a resposta final",
                "pode haver limites, desde que eles não inviabilizem a interpretação principal",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_02_q_004",
            "pergunta": (
                "Escreva, em um parágrafo, sua avaliação sobre a suficiência das evidências obtidas."
            ),
            "placeholder": (
                "Apresente uma síntese explicando se as evidências foram suficientes para sustentar a conclusão..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: não diga apenas que as evidências foram 'suficientes' ou 'insuficientes'. "
                "Mostre por que elas são adequadas — ou por que seriam necessárias evidências complementares."
            ),
        },
    ]