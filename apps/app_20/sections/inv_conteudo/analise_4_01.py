from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve interpretar os resultados obtidos a partir da análise do circuito. "
                "O objetivo é identificar o que os dados mostram quando analisados em conjunto, "
                "relacionando as características do motor, dos condutores e dos cálculos realizados."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Evite apenas repetir os valores obtidos. Procure comparar, identificar relações entre os parâmetros "
                "do sistema, reconhecer o que indica compatibilidade e perceber o que sugere limitação técnica no circuito."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Seleção dos resultados relevantes",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_01_q_001",
            "pergunta": (
                "Quais dados e resultados obtidos na análise são mais relevantes para entender o comportamento elétrico do circuito?"
            ),
            "placeholder": (
                "Indique os principais dados do motor, dos condutores e dos cálculos realizados..."
            ),
            "altura": 140,
        },
        {
            "tipo": "subtitulo",
            "texto": "Comparação entre parâmetros do sistema",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_01_q_002",
            "pergunta": (
                "Compare a demanda elétrica do motor com a capacidade técnica dos condutores analisados."
            ),
            "placeholder": (
                "Descreva como a corrente exigida, a seção dos cabos e a queda de tensão se relacionam..."
            ),
            "altura": 160,
        },
        {
            "tipo": "subtitulo",
            "texto": "Identificação de padrões",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_01_q_003",
            "pergunta": (
                "A partir da comparação realizada, há algum padrão, tendência ou relação recorrente nos resultados?"
            ),
            "placeholder": (
                "Explique se os resultados indicam coerência, limite de operação, folga técnica ou outra tendência relevante..."
            ),
            "altura": 150,
        },
        {
            "tipo": "subtitulo",
            "texto": "Coerência dos resultados",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_01_q_004",
            "pergunta": (
                "Os resultados obtidos são coerentes entre si e com o comportamento esperado de um circuito de alimentação de motor?"
            ),
            "placeholder": (
                "Explique se os dados fazem sentido quando analisados em conjunto e se são compatíveis com os princípios elétricos envolvidos..."
            ),
            "altura": 150,
        },
        {
            "tipo": "subtitulo",
            "texto": "Síntese da leitura dos resultados",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_01_q_005",
            "pergunta": (
                "Com base na análise realizada, descreva de forma integrada o que os resultados mostram sobre o circuito de alimentação do motor."
            ),
            "placeholder": (
                "Escreva um parágrafo sintetizando a leitura dos resultados..."
            ),
            "altura": 200,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: primeiro relacione os dados do motor com os dados dos condutores, depois identifique padrões "
                "e, por fim, descreva o que os resultados revelam sobre o circuito. Evite antecipar a conclusão final nesta etapa."
            ),
        },
    ]