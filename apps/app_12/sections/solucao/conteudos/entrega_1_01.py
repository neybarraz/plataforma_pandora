from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve organizar os elementos centrais da investigação realizada. "
                "O objetivo é retomar o problema, selecionar os dados mais relevantes e verificar "
                "se a hipótese formulada é compatível com os resultados obtidos."
            ),
        },

        # -------------------------
        # 1.1 Retomada da Pergunta
        # -------------------------
        {
            "tipo": "subtitulo",
            "texto": "Pergunta central do estudo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Antes de analisar os resultados finais, é importante retomar o problema que orientou a investigação. "
                "A pergunta central define o que está sendo explicado e deve guiar toda a interpretação."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_01_q_001",
            "pergunta": (
                "Reescreva, com suas próprias palavras, a pergunta central que orientou este estudo."
            ),
            "placeholder": (
                "Explique qual problema o estudo buscou responder..."
            ),
            "altura": 140,
        },

        # -------------------------
        # 1.2 Indicadores Críticos
        # -------------------------
        {
            "tipo": "subtitulo",
            "texto": "Indicadores críticos",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nem todos os dados obtidos têm o mesmo peso na análise. "
                "Nesta etapa, você deve selecionar apenas aqueles que são decisivos para interpretar o funcionamento do sistema."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_01_q_002",
            "pergunta": (
                "Quais foram os dados ou observações mais importantes para entender o comportamento do sistema?"
            ),
            "placeholder": (
                "Indique apenas os resultados que realmente influenciam a interpretação..."
            ),
            "altura": 160,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_01_q_003",
            "pergunta": (
                "Explique por que esses dados são decisivos para a análise."
            ),
            "placeholder": (
                "Relacione esses dados com o funcionamento do sistema observado..."
            ),
            "altura": 160,
        },

        # -------------------------
        # 1.3 Verificação da Hipótese
        # -------------------------
        {
            "tipo": "subtitulo",
            "texto": "Verificação da hipótese",
        },
        {
            "tipo": "texto",
            "texto": (
                "Agora, você deve comparar os resultados obtidos com a hipótese formulada anteriormente. "
                "Essa etapa é fundamental para verificar se a explicação proposta é consistente com os dados experimentais."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_01_q_004",
            "pergunta": (
                "Com base nos resultados obtidos, a hipótese formulada foi confirmada, refutada ou precisa ser ajustada?"
            ),
            "placeholder": (
                "Indique claramente sua avaliação da hipótese..."
            ),
            "altura": 140,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_01_q_005",
            "pergunta": (
                "Justifique sua resposta com base nos dados e evidências obtidas no experimento."
            ),
            "placeholder": (
                "Explique como os resultados sustentam ou contradizem a hipótese..."
            ),
            "altura": 180,
        },

        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: nesta etapa, seja objetivo. Retome o problema, selecione os dados mais relevantes "
                "e mostre claramente como eles se relacionam com a hipótese."
            ),
        },
    ]