from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Indicadores críticos",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve selecionar apenas os dados e observações que foram realmente decisivos "
                "para a interpretação do problema. Nem toda informação coletada tem o mesmo peso na análise: "
                "alguns resultados são centrais porque ajudam diretamente a explicar o funcionamento do sistema."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo aqui é identificar quais evidências têm maior valor explicativo. "
                "Procure destacar os resultados que mostram continuidade ou mudança no comportamento do sistema, "
                "especialmente aqueles que ajudam a entender o papel da bateria, do conversor e da carga."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_02_q_001",
            "pergunta": (
                "Quais dados e observações do experimento você considera mais importantes para interpretar o funcionamento do sistema?"
            ),
            "placeholder": (
                "Selecione apenas os resultados mais relevantes para explicar o fenômeno observado..."
            ),
            "altura": 170,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_02_q_002",
            "pergunta": (
                "Entre os resultados obtidos, quais indicam que a carga continuou sendo alimentada após a remoção da fonte externa?"
            ),
            "placeholder": (
                "Descreva quais evidências mostram continuidade de funcionamento da carga..."
            ),
            "altura": 150,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_02_q_003",
            "pergunta": (
                "Quais resultados ajudam a perceber o papel da bateria e do conversor no comportamento observado?"
            ),
            "placeholder": (
                "Indique os dados que revelam a participação da bateria e a atuação do conversor..."
            ),
            "altura": 160,
        },
        {
            "tipo": "texto",
            "texto": (
                "Em uma investigação técnica, indicadores críticos são aqueles que permitem sustentar a interpretação. "
                "No caso deste estudo, vale observar especialmente resultados ligados à alimentação da carga, à tensão "
                "na bateria e à tensão de saída do conversor."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "presença de tensão na bateria",
                "presença de tensão na saída do conversor",
                "continuidade de funcionamento da carga",
                "estabilidade ou mudança durante a troca de fonte",
                "diferença entre tensão da bateria e tensão fornecida à carga",
            ],
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_02_q_004",
            "pergunta": (
                "Explique por que os dados que você selecionou são decisivos para a interpretação do problema."
            ),
            "placeholder": (
                "Justifique por que esses resultados são os mais importantes para entender o sistema..."
            ),
            "altura": 180,
        },
        {
            "tipo": "questao_texto",
            "id": "entrega_1_02_q_005",
            "pergunta": (
                "Organize, em um único parágrafo, os principais indicadores críticos do estudo."
            ),
            "placeholder": (
                "Escreva uma síntese dos dados decisivos para a análise..."
            ),
            "altura": 200,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: não repita todos os resultados do experimento. Selecione apenas aqueles que realmente ajudam "
                "a explicar o funcionamento do sistema e a sustentar a análise."
            ),
        },
    ]