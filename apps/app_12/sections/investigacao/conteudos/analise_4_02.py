from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve avaliar a confiabilidade dos resultados obtidos. "
                "Toda análise técnica possui limitações, e é importante identificar "
                "quais fatores podem ter influenciado os dados levantados e os cálculos realizados."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo não é invalidar os resultados, mas compreender até que ponto eles são confiáveis "
                "e quais são os limites da análise realizada sobre o circuito de alimentação do motor."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Identificação de possíveis desvios",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_02_q_001",
            "pergunta": (
                "Quais fatores podem ter influenciado os dados e os resultados obtidos na análise do circuito?"
            ),
            "placeholder": (
                "Considere estimativas, dados nominais, condições reais de instalação e simplificações adotadas..."
            ),
            "altura": 150,
        },
        {
            "tipo": "subtitulo",
            "texto": "Limitações do método e das informações utilizadas",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_02_q_002",
            "pergunta": (
                "Há limitações associadas ao método adotado, aos dados disponíveis ou às condições consideradas na análise?"
            ),
            "placeholder": (
                "Explique possíveis limitações nos dados do motor, no comprimento do circuito, nas condições de instalação ou nos critérios adotados..."
            ),
            "altura": 150,
        },
        {
            "tipo": "subtitulo",
            "texto": "Impacto dos desvios nos resultados",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_02_q_003",
            "pergunta": (
                "De que forma esses fatores podem ter afetado os resultados obtidos?"
            ),
            "placeholder": (
                "Explique se essas limitações alteram significativamente a análise ou apenas introduzem pequenas incertezas..."
            ),
            "altura": 160,
        },
        {
            "tipo": "subtitulo",
            "texto": "Confiabilidade da análise",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_02_q_004",
            "pergunta": (
                "Considerando as limitações identificadas, até que ponto os resultados podem ser considerados confiáveis?"
            ),
            "placeholder": (
                "Indique o que pode ser afirmado com segurança sobre o dimensionamento dos condutores e o que deve ser interpretado com cautela..."
            ),
            "altura": 170,
        },
        {
            "tipo": "subtitulo",
            "texto": "Síntese dos limites da análise",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_4_02_q_005",
            "pergunta": (
                "Resuma, em um parágrafo, as principais limitações e o grau de confiabilidade da análise realizada."
            ),
            "placeholder": (
                "Apresente uma síntese clara das incertezas identificadas e do alcance da análise do circuito..."
            ),
            "altura": 200,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: identifique fatores concretos, explique seu impacto e indique se eles comprometem ou não "
                "a interpretação geral dos resultados sobre o circuito de alimentação do motor."
            ),
        },
    ]