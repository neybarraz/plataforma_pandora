from __future__ import annotations


def get_pagina() -> dict:
    return {
        "id": "metodologia",
        "titulo": "Metodologia",
        "titulo_menu": "METODOLOGIA",
        "conteudos": [
            {
                "id": "estrategia_investigacao",
                "titulo": "3. ESTRATÉGIA DE INVESTIGAÇÃO",
                "titulo_menu": "Estratégia",
                "blocos": [
                    {
                        "tipo": "texto",
                        "texto": (
                            "A metodologia deve mostrar como o problema foi atacado. "
                            "O leitor precisa entender como a investigação foi planejada, executada e validada."
                        ),
                    },
                    {
                        "tipo": "alerta",
                        "nivel": "info",
                        "texto": (
                            "Descreva os procedimentos de modo que outra pessoa possa reproduzir o estudo."
                        ),
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "3.1 Planejamento",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "m_met_planejamento_001",
                        "pergunta": "Explique como a investigação foi planejada.",
                        "placeholder": (
                            "Por que esse método foi escolhido? O que seria medido, comparado ou observado?"
                        ),
                        "altura": 180,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "3.2 Procedimentos",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "m_met_procedimentos_001",
                        "pergunta": "Descreva os procedimentos realizados.",
                        "placeholder": (
                            "Onde mediu? Quantos pontos? Como registrou? Que etapas foram executadas?"
                        ),
                        "altura": 220,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "3.3 Controle de variáveis",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "m_met_controle_variaveis_001",
                        "pergunta": "Explique quais variáveis foram controladas ou observadas.",
                        "placeholder": (
                            "Quais condições foram mantidas? Quais fatores externos poderiam influenciar o resultado?"
                        ),
                        "altura": 180,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "3.4 Critérios de validação",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "m_met_criterios_validacao_001",
                        "pergunta": "Como a confiabilidade da investigação foi avaliada?",
                        "placeholder": (
                            "Houve repetição, comparação, coerência física, análise crítica de consistência?"
                        ),
                        "altura": 180,
                    },
                ],
            }
        ],
    }