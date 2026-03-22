from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Justificativa baseada em evidências",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve sustentar sua resposta objetiva com base nos dados obtidos, "
                "nas observações registradas e nos conceitos utilizados ao longo da investigação. "
                "A justificativa deve mostrar por que a resposta apresentada pode ser considerada tecnicamente válida."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Não basta afirmar que o sistema funciona ou que a hipótese foi confirmada. "
                "É necessário indicar quais evidências sustentam essa interpretação e como elas se relacionam "
                "com o modelo físico adotado no estudo."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_02_q_001",
            "pergunta": (
                "Quais evidências experimentais sustentam a resposta técnica apresentada?"
            ),
            "placeholder": (
                "Indique os dados e observações mais importantes para sustentar sua resposta..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_02_q_002",
            "pergunta": (
                "Como essas evidências se relacionam com o funcionamento do sistema observado?"
            ),
            "placeholder": (
                "Explique o que os dados revelam sobre o comportamento do sistema..."
            ),
            "altura": 170,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_02_q_003",
            "pergunta": (
                "Que conceitos físicos ajudam a explicar as evidências obtidas?"
            ),
            "placeholder": (
                "Relacione os dados observados com os conceitos físicos mobilizados na investigação..."
            ),
            "altura": 170,
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma justificativa técnica consistente costuma articular três elementos: "
                "os dados obtidos, o comportamento observado e os conceitos que explicam esse comportamento."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "dados experimentais relevantes",
                "observações do comportamento do sistema",
                "conexão entre evidências e conceitos",
                "encadeamento lógico entre resultado e resposta",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_02_q_004",
            "pergunta": (
                "Escreva, em um parágrafo, a justificativa baseada em evidências da sua resposta técnica."
            ),
            "placeholder": (
                "Apresente uma justificativa clara, articulando dados, observações e conceitos..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: uma boa justificativa não repete apenas os resultados. "
                "Ela mostra como os dados sustentam a resposta e por que eles podem ser interpretados dessa maneira."
            ),
        },
    ]