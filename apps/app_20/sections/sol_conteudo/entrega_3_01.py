from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Coerência problema–análise–decisão",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve verificar se a investigação manteve alinhamento lógico entre o problema formulado, "
                "o caminho de análise adotado, os dados registrados e a resposta técnica apresentada."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo é avaliar se a decisão final realmente responde à pergunta do estudo e se ela foi construída "
                "a partir de procedimentos e evidências compatíveis com o problema investigado."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_01_q_001",
            "pergunta": (
                "A resposta técnica apresentada está diretamente relacionada à pergunta central do estudo? Explique."
            ),
            "placeholder": (
                "Mostre como a resposta formulada retoma o problema investigado..."
            ),
            "altura": 150,
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_01_q_002",
            "pergunta": (
                "Os procedimentos adotados durante a análise foram adequados para produzir dados relevantes ao problema?"
            ),
            "placeholder": (
                "Explique se o método e as observações escolhidas fazem sentido para responder à pergunta do estudo..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_01_q_003",
            "pergunta": (
                "Os dados obtidos e organizados ao longo da investigação sustentam a resposta técnica formulada?"
            ),
            "placeholder": (
                "Relacione os dados produzidos com a resposta final apresentada..."
            ),
            "altura": 160,
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando há coerência problema–análise–decisão, a investigação apresenta um encadeamento lógico: "
                "a pergunta orienta o método, o método produz dados relevantes e os dados sustentam a decisão."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "a resposta deve retomar o problema formulado",
                "os procedimentos devem ser compatíveis com a pergunta do estudo",
                "os dados precisam sustentar a resposta apresentada",
                "não deve haver salto lógico entre análise e decisão",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_01_q_004",
            "pergunta": (
                "Escreva, em um parágrafo, sua avaliação sobre a coerência entre problema, análise e decisão."
            ),
            "placeholder": (
                "Apresente uma síntese mostrando se a investigação manteve alinhamento lógico entre suas etapas..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: não basta dizer que 'está coerente'. Explique como a pergunta, o método, os dados e a resposta final "
                "se conectam ao longo da investigação."
            ),
        },
    ]