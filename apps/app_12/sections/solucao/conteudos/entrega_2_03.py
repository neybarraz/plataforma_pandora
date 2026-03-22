from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Condições de aplicação",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve indicar em que contexto a resposta técnica apresentada pode ser considerada válida. "
                "Toda conclusão possui um alcance e também limites, definidos pelas condições do experimento, "
                "pelo modelo adotado e pelas simplificações assumidas ao longo da investigação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo não é enfraquecer a conclusão, mas mostrar maturidade técnica: "
                "uma resposta bem fundamentada também precisa dizer onde ela se aplica e onde ela não deve ser generalizada."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_03_q_001",
            "pergunta": (
                "Em que condições ou contextos a sua resposta técnica pode ser considerada válida?"
            ),
            "placeholder": (
                "Indique para quais situações, sistemas ou condições experimentais sua resposta pode ser aplicada..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_03_q_002",
            "pergunta": (
                "Quais limites do experimento, do método ou do modelo adotado precisam ser considerados?"
            ),
            "placeholder": (
                "Aponte simplificações, restrições e aspectos que não foram analisados detalhadamente..."
            ),
            "altura": 170,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_03_q_003",
            "pergunta": (
                "Há situações em que essa conclusão não deve ser aplicada diretamente? Quais?"
            ),
            "placeholder": (
                "Explique em que casos a conclusão não deve ser generalizada sem cautela..."
            ),
            "altura": 160,
        },
        {
            "tipo": "texto",
            "texto": (
                "Em uma investigação técnica, definir condições de aplicação significa explicitar o alcance real da conclusão. "
                "Isso inclui reconhecer o contexto em que a análise foi realizada e evitar extrapolações que o estudo não sustenta."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "contexto em que a conclusão é válida",
                "limites do experimento e da montagem",
                "simplificações adotadas no estudo",
                "situações em que a conclusão não deve ser generalizada",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_2_03_q_004",
            "pergunta": (
                "Escreva, em um parágrafo, as condições de aplicação da sua conclusão técnica."
            ),
            "placeholder": (
                "Apresente de forma clara o alcance, os limites e as restrições da conclusão..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: não diga apenas que a conclusão 'vale para este caso'. "
                "Mostre em que contexto ela pode ser aplicada, quais limites existem e onde é necessário ter cautela."
            ),
        },
    ]