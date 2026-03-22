# apps/app_05/sections/solucao/conteudos/catalago.py

from . import (
    entrega_1_01,
    entrega_1_02,
    entrega_1_03,
    entrega_2_01,
    entrega_2_02,
    entrega_2_03,
    entrega_3_01,
    entrega_3_02,
    entrega_3_03,
)


def get_paginas():
    return [
        {
            "id": "pagina_1",
            "titulo_menu": "Síntese dos Resultados",
            "conteudos": [
                {
                    "id": "entrega_1_01",
                    "titulo_menu": "Pergunta Estratégica",
                    "modulo": entrega_1_01,
                    "blocos": entrega_1_01.get_blocos(),
                },
                {
                    "id": "entrega_1_02",
                    "titulo_menu": "Indicadores Críticos",
                    "modulo": entrega_1_02,
                    "blocos": entrega_1_02.get_blocos(),
                },
                {
                    "id": "entrega_1_03",
                    "titulo_menu": "Verificação da Hipótese",
                    "modulo": entrega_1_03,
                    "blocos": entrega_1_03.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_2",
            "titulo_menu": "Decisão Técnica",
            "conteudos": [
                {
                    "id": "entrega_2_01",
                    "titulo_menu": "Resposta objetiva",
                    "blocos": entrega_2_01.get_blocos(),
                },
                {
                    "id": "entrega_2_02",
                    "titulo_menu": "Justificativa baseada em evidências",
                    "blocos": entrega_2_02.get_blocos(),
                },
                {
                    "id": "entrega_2_03",
                    "titulo_menu": "Condições de Aplicação",
                    "blocos": entrega_2_03.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_3",
            "titulo_menu": "Validação da Conclusão",
            "conteudos": [
                {
                    "id": "entrega_3_01",
                    "titulo_menu": "Coerência",
                    "blocos": entrega_3_01.get_blocos(),
                },
                {
                    "id": "entrega_3_02",
                    "titulo_menu": "Suficiência de evidências",
                    "blocos": entrega_3_02.get_blocos(),
                },
                {
                    "id": "entrega_3_03",
                    "titulo_menu": "Robustez da decisão",
                    "blocos": entrega_3_03.get_blocos(),
                },
            ],
        },
       
    ]