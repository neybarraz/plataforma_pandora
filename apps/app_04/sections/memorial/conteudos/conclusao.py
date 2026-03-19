from __future__ import annotations


def get_pagina() -> dict:
    return {
        "id": "memorial_05",
        "titulo": "Conclusão",
        "titulo_menu": "Conclusão",
        "conteudos": [
            {
                "id": "memorial_05_001",
                "titulo": "5. DECISÃO TÉCNICA",
                "titulo_menu": "Decisão",
                "blocos": [
                    {
                        "tipo": "texto",
                        "texto": (
                            "A conclusão deve fechar o raciocínio do memorial. "
                            "Ela precisa responder à pergunta técnica, justificar a decisão e indicar as condições de validade."
                        ),
                    },
                    {
                        "tipo": "alerta",
                        "nivel": "info",
                        "texto": (
                            "Conclusão técnica não é opinião pessoal. Ela deve ser derivada dos dados e da análise."
                        ),
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "5.1 Resposta à pergunta",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_05_001_q_0001",
                        "pergunta": "Responda diretamente à pergunta técnica do trabalho.",
                        "placeholder": (
                            "Ex.: Sim, foi identificada diferença significativa de temperatura entre regiões do ambiente..."
                        ),
                        "altura": 150,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "5.2 Justificativa técnica",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_05_001_q_0002",
                        "pergunta": "Justifique a conclusão com base nos dados e na análise.",
                        "placeholder": (
                            "Conecte dados → análise → conclusão. Mostre por que a resposta final é tecnicamente defensável."
                        ),
                        "altura": 220,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "5.3 Condições de validade",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_05_001_q_0003",
                        "pergunta": "Em que condições essa conclusão é válida?",
                        "placeholder": (
                            "A conclusão vale apenas neste ambiente? Depende de condições específicas? Quais limites precisam ser respeitados?"
                        ),
                        "altura": 180,
                    },
                ],
            }
        ],
    }