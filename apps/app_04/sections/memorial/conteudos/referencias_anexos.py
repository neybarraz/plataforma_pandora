from __future__ import annotations


def get_pagina() -> dict:
    return {
        "id": "memorial_06",
        "titulo": "Referências e Anexos",
        "titulo_menu": "Referências e Anexos",
        "conteudos": [
            {
                "id": "memorial_06_001",
                "titulo": "6. REFERÊNCIAS E ANEXOS",
                "titulo_menu": "Apoio documental",
                "blocos": [
                    {
                        "tipo": "texto",
                        "texto": (
                            "Esta última parte reúne as fontes utilizadas e os materiais que complementam o memorial."
                        ),
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "6.1 Referências",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_06_001_q_0001",
                        "pergunta": "Liste as referências utilizadas.",
                        "placeholder": (
                            "Livros, apostilas, normas, materiais complementares, referências técnicas ou científicas."
                        ),
                        "altura": 180,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "6.2 Anexos",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_06_001_q_0002",
                        "pergunta": "Indique os anexos que acompanham o memorial.",
                        "placeholder": (
                            "Fotos, tabelas completas, registros experimentais, croquis, gráficos, imagens do sistema..."
                        ),
                        "altura": 180,
                    },
                ],
            }
        ],
    }