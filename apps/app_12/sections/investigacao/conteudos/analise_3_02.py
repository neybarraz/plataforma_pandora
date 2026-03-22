from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve organizar e comparar os dados já obtidos na execução da análise. "
                "O objetivo ainda não é apresentar a conclusão final, mas transformar os dados do motor "
                "e do circuito em evidências claras, comparáveis e úteis para a interpretação técnica."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Retome os valores levantados e os cálculos realizados anteriormente. "
                "Agora, compare as características elétricas do motor com as propriedades dos condutores "
                "e identifique o que indica compatibilidade, o que sugere limitação e quais evidências "
                "ajudam a avaliar o dimensionamento do circuito."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Seleção das evidências",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_001",
            "pergunta": (
                "Quais dados e resultados obtidos na execução você considera mais importantes para avaliar o dimensionamento dos condutores?"
            ),
            "placeholder": (
                "Indique quais dados do motor, do circuito e dos cálculos devem ser priorizados na análise..."
            ),
            "altura": 140,
        },
        {
            "tipo": "subtitulo",
            "texto": "Comparação entre corrente exigida e capacidade do condutor",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_002",
            "pergunta": (
                "Compare a corrente exigida pelo motor com a capacidade de condução de corrente dos condutores utilizados."
            ),
            "placeholder": (
                "Descreva se o cabo suporta a corrente do motor com folga, no limite ou de forma inadequada..."
            ),
            "altura": 140,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_003",
            "pergunta": (
                "Compare a seção dos condutores instalados com a seção que seria tecnicamente requerida para o circuito."
            ),
            "placeholder": (
                "Descreva se a seção instalada é compatível, superior ou inferior à necessária..."
            ),
            "altura": 140,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_004",
            "pergunta": (
                "Compare a queda de tensão estimada no circuito com os limites tecnicamente aceitáveis."
            ),
            "placeholder": (
                "Explique se a queda de tensão ficou dentro de limites adequados ou se indica problema no circuito..."
            ),
            "altura": 150,
        },
        {
            "tipo": "subtitulo",
            "texto": "Consistência do circuito analisado",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_005",
            "pergunta": (
                "Com base nos dados levantados, o circuito analisado apresenta coerência entre a demanda do motor e as características dos condutores?"
            ),
            "placeholder": (
                "Descreva se os elementos do circuito parecem compatíveis entre si ou se há indícios de inadequação..."
            ),
            "altura": 150,
        },
        {
            "tipo": "subtitulo",
            "texto": "Evidências do dimensionamento",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_006",
            "pergunta": (
                "Que evidências indicam que os condutores estão adequados para a operação do motor?"
            ),
            "placeholder": (
                "Explique quais resultados sustentam a adequação dos cabos, caso isso tenha sido observado..."
            ),
            "altura": 150,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_007",
            "pergunta": (
                "Que evidências indicam possível subdimensionamento ou limitação técnica dos condutores?"
            ),
            "placeholder": (
                "Explique quais resultados sugerem inadequação, operação no limite ou necessidade de redimensionamento..."
            ),
            "altura": 150,
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, é importante que você transforme os dados brutos em evidências comparáveis. "
                "Isso significa relacionar os valores obtidos, identificar compatibilidades e reconhecer "
                "limitações técnicas que ajudem a interpretar o comportamento do circuito."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "comparar a corrente exigida pelo motor com a corrente admissível do cabo",
                "comparar a seção instalada com a seção requerida",
                "verificar se a queda de tensão permanece em faixa aceitável",
                "identificar coerência entre motor, circuito e condutores",
                "reconhecer evidências de adequação ou inadequação do dimensionamento",
            ],
        },
        {
            "tipo": "subtitulo",
            "texto": "Síntese do registro de evidências",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_02_q_008",
            "pergunta": (
                "Organize, em um parágrafo, as principais evidências registradas durante a análise do circuito."
            ),
            "placeholder": (
                "Escreva um resumo claro das evidências obtidas a partir da comparação entre os dados do motor, dos condutores e dos cálculos realizados..."
            ),
            "altura": 220,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: nesta etapa, não repita apenas os valores obtidos. Mostre como eles se relacionam "
                "e o que revelam sobre a adequação dos condutores no circuito de alimentação do motor."
            ),
        },
    ]