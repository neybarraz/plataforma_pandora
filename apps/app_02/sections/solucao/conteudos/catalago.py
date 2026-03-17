# apps/app_02/sections/solucao/conteudos/catalago.py

from apps.app_02.sections.solucao.conteudos import (
    entrega_1_01,
    entrega_1_02,
    entrega_1_03,
    entrega_2_01,
    entrega_2_02,
)


def get_paginas():
    return [
        {
            "id": "pagina_1",
            "titulo_menu": "Resumo dos Resultados",
            "conteudos": [
                {
                    "id": "entrega_1_01",
                    "titulo_menu": "Pergunta Central do Estudo",
                    "modulo": entrega_1_01,
                    "blocos": entrega_1_01.get_blocos(),
                },
                {
                    "id": "entrega_1_02",
                    "titulo_menu": "Dados-Chave para Decisão",
                    "modulo": entrega_1_02,
                    "blocos": entrega_1_02.get_blocos(),
                },
                {
                    "id": "entrega_1_03",
                    "titulo_menu": "Avaliação da Hipótese",
                    "modulo": entrega_1_03,
                    "blocos": entrega_1_03.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_2",
            "titulo_menu": "Conclusão Técnica",
            "conteudos": [
                {
                    "id": "entrega_2_01",
                    "titulo_menu": "Evidências que Sustentam a Conclusão",
                    "blocos": entrega_2_01.get_blocos(),
                },
                {
                    "id": "entrega_2_02",
                    "titulo_menu": "Limites e Condições de Aplicação",
                    "blocos": entrega_2_02.get_blocos(),
                },
            ],
        },
       
    ]