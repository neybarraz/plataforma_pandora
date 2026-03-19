from __future__ import annotations


def get_pagina() -> dict:
    return {
        "id": "memorial_02",
        "titulo": "Fundamentação e Modelo",
        "titulo_menu": "Fundamentação e Modelo",
        "conteudos": [
            {
                "id": "memorial_02_001",
                "titulo": "2. MODELO E FUNDAMENTAÇÃO",
                "titulo_menu": "Modelo e fundamentos",
                "blocos": [
                    {
                        "tipo": "texto",
                        "texto": (
                            "Nesta parte, o aluno deve mostrar que compreende o fenômeno analisado. "
                            "O memorial não deve trazer definições soltas, mas sim conceitos articulados com o problema real."
                        ),
                    },
                    {
                        "tipo": "alerta",
                        "nivel": "info",
                        "texto": (
                            "Explique a teoria sempre em relação ao caso estudado."
                        ),
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "2.1 Conceitos físicos relevantes",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_02_001_q_0001",
                        "pergunta": "Quais conceitos físicos ou técnicos sustentam a análise?",
                        "placeholder": (
                            "Liste e explique os conceitos usados, relacionando-os ao problema. "
                            "Ex.: condução, convecção, radiação, corrente, potência, gradiente térmico..."
                        ),
                        "altura": 220,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "2.2 Modelo do sistema",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_02_001_q_0002",
                        "pergunta": "Descreva o sistema como estrutura analítica.",
                        "placeholder": (
                            "Apresente entradas, processos e saídas. "
                            "Ex.: Entradas: calor/energia. Processos: trocas, fluxos, conversões. Saídas: temperatura, tensão, corrente..."
                        ),
                        "altura": 220,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "2.3 Hipóteses e simplificações",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_02_001_q_0003",
                        "pergunta": "Quais hipóteses e simplificações foram assumidas?",
                        "placeholder": (
                            "Ex.: regime estacionário, desprezo de perdas, análise bidimensional, ausência de climatização ativa..."
                        ),
                        "altura": 180,
                    },
                ],
            }
        ],
    }