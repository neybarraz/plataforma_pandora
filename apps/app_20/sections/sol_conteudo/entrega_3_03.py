from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Robustez da decisão",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve avaliar se a decisão técnica apresentada é logicamente defensável, "
                "considerando os dados obtidos, a análise realizada e as limitações reconhecidas ao longo da investigação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma decisão robusta não depende de um único dado isolado nem desconsidera as limitações do estudo. "
                "Ela se mantém consistente porque está apoiada em evidências relevantes, em interpretação coerente "
                "e em conceitos consolidados."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_03_q_001",
            "pergunta": (
                "A decisão técnica formulada pode ser considerada logicamente defensável? Explique."
            ),
            "placeholder": (
                "Explique por que a decisão final pode ou não ser sustentada com base na investigação realizada..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_03_q_002",
            "pergunta": (
                "Mesmo considerando as limitações experimentais, quais elementos tornam essa decisão consistente?"
            ),
            "placeholder": (
                "Indique os aspectos que mantêm a força da decisão, mesmo com restrições do experimento..."
            ),
            "altura": 170,
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_03_q_003",
            "pergunta": (
                "Há algum ponto da decisão que deve ser sustentado com mais cautela? Qual?"
            ),
            "placeholder": (
                "Explique se existe algum aspecto da decisão que exige formulação mais cuidadosa..."
            ),
            "altura": 160,
        },
        {
            "tipo": "texto",
            "texto": (
                "Avaliar a robustez da decisão significa verificar se ela continua válida quando confrontada com os "
                "dados obtidos, com a lógica da investigação e com os limites reconhecidos no estudo."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "a decisão deve se apoiar em mais de uma evidência relevante",
                "a interpretação deve ser coerente com os dados e com o modelo adotado",
                "as limitações não devem invalidar a resposta principal",
                "a formulação final deve ser defensável do ponto de vista lógico e técnico",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "validacao_3_03_q_004",
            "pergunta": (
                "Escreva, em um parágrafo, sua avaliação sobre a robustez da decisão técnica."
            ),
            "placeholder": (
                "Apresente uma síntese explicando por que a decisão pode ser considerada robusta — ou em que medida ela exige cautela..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: robustez não significa perfeição. Significa que a decisão se sustenta de forma coerente, "
                "mesmo reconhecendo os limites da investigação."
            ),
        },
    ]