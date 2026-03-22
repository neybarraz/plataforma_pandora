from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Resposta objetiva",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve apresentar uma resposta direta ao problema investigado. "
                "A resposta objetiva deve ser clara, concisa e baseada na análise realizada, "
                "sem necessidade de explicações longas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Considere a pergunta central do estudo e formule uma resposta técnica que sintetize "
                "o funcionamento do sistema observado."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_01_q_001",
            "pergunta": (
                "Qual é a resposta técnica para o problema investigado?"
            ),
            "placeholder": (
                "Responda de forma direta, em uma ou duas frases, sem explicações longas..."
            ),
            "altura": 140,
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma resposta objetiva deve expressar o essencial: o que foi observado e como isso resolve "
                "o problema investigado."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "responder diretamente ao problema",
                "ser clara e objetiva",
                "não incluir explicações detalhadas",
                "refletir o resultado da análise realizada",
            ],
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: imagine que você precisa responder ao problema em poucas palavras. "
                "Se a resposta estiver longa demais, tente simplificar mantendo apenas o essencial."
            ),
        },
    ]