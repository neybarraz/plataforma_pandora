from __future__ import annotations


def get_pagina() -> dict:
    return {
        "id": "memorial_04",
        "titulo": "Resultados e Análise",
        "titulo_menu": "Resultados e Análise",
        "conteudos": [
            {
                "id": "memorial_04_001",
                "titulo": "4. RESULTADOS E ANÁLISE",
                "titulo_menu": "Resultados",
                "blocos": [
                    {
                        "tipo": "texto",
                        "texto": (
                            "Nesta etapa, os dados devem ser apresentados e interpretados. "
                            "O aluno precisa transformar medições, observações e registros em entendimento técnico."
                        ),
                    },
                    {
                        "tipo": "alerta",
                        "nivel": "info",
                        "texto": (
                            "Não basta dizer o que foi medido. É preciso mostrar o que os dados significam."
                        ),
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "4.1 Dados obtidos",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_04_001_q_0001",
                        "pergunta": "Apresente os principais dados obtidos na investigação.",
                        "placeholder": (
                            "Cite medições, indicadores, diferenças observadas, tabelas, tendências ou resultados principais."
                        ),
                        "altura": 220,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "4.2 Identificação de padrões",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_04_001_q_0002",
                        "pergunta": "Que padrões, tendências ou diferenças relevantes apareceram nos dados?",
                        "placeholder": (
                            "Há diferença entre regiões, comportamentos repetidos, tendências ou contrastes importantes?"
                        ),
                        "altura": 180,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "4.3 Interpretação física",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_04_001_q_0003",
                        "pergunta": "Explique os resultados com base na teoria e no modelo adotado.",
                        "placeholder": (
                            "Por que os dados se comportaram assim? Que mecanismo físico ou técnico explica os resultados?"
                        ),
                        "altura": 220,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "4.4 Desvios e limitações",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_04_001_q_0004",
                        "pergunta": "Avalie desvios, limitações e possíveis fontes de erro.",
                        "placeholder": (
                            "Houve imprecisão, simplificações excessivas, limitação de amostragem ou restrições experimentais?"
                        ),
                        "altura": 200,
                    },
                ],
            }
        ],
    }