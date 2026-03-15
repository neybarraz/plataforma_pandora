# apps/app_01/sections/investigacao/conteudos/catalago.py

from apps.app_01.sections.investigacao.conteudos import (
    analise_1_01,
    analise_1_02,
    analise_1_03,
    analise_1_04,
    analise_1_05,
    analise_1_06,
    analise_1_07,
    analise_1_08,
    analise_1_09,
    analise_1_10,
    analise_1_11,
    analise_2_01,
    analise_2_02,
    analise_2_03,
    analise_2_04,
    analise_3_01,
    analise_3_02,
    analise_3_03,
    analise_3_04,
)


def get_paginas():
    return [
        {
            "id": "pagina_1",
            "titulo_menu": "Base de Conhecimento",
            "conteudos": [
                {
                    "id": "analise_1_01",
                    "titulo_menu": "Distribuição de temperatura na sala",
                    "modulo": analise_1_01,
                    "blocos": analise_1_01.get_blocos(),
                },
                {
                    "id": "analise_1_02",
                    "titulo_menu": "Trocas de calor no ambiente",
                    "modulo": analise_1_02,
                    "blocos": analise_1_02.get_blocos(),
                },
                {
                    "id": "analise_1_03",
                    "titulo_menu": "Equilíbrio térmico do ambiente",
                    "modulo": analise_1_03,
                    "blocos": analise_1_03.get_blocos(),
                },
                {
                    "id": "analise_1_04",
                    "titulo_menu": "Transferência de calor nas superfícies",
                    "modulo": analise_1_04,
                    "blocos": analise_1_04.get_blocos(),
                },
                {
                    "id": "analise_1_05",
                    "titulo_menu": "Mecanismos de transferência de calor na sala",
                    "modulo": analise_1_05,
                    "blocos": analise_1_05.get_blocos(),
                },
                {
                    "id": "analise_1_06",
                    "titulo_menu": "Propriedades do ar no ambiente",
                    "modulo": analise_1_06,
                    "blocos": analise_1_06.get_blocos(),
                },
                {
                    "id": "analise_1_07",
                    "titulo_menu": "Circulação do ar na sala",
                    "modulo": analise_1_07,
                    "blocos": analise_1_07.get_blocos(),
                },
                {
                    "id": "analise_1_08",
                    "titulo_menu": "Mistura e recirculação do ar",
                    "modulo": analise_1_08,
                    "blocos": analise_1_08.get_blocos(),
                },
                {
                    "id": "analise_1_09",
                    "titulo_menu": "Sistema térmico do ambiente",
                    "modulo": analise_1_09,
                    "blocos": analise_1_09.get_blocos(),
                },
                {
                    "id": "analise_1_10",
                    "titulo_menu": "Balanço de energia térmica",
                    "modulo": analise_1_10,
                    "blocos": analise_1_10.get_blocos(),
                },
                {
                    "id": "analise_1_11",
                    "titulo_menu": "Direção das transformações térmicas",
                    "modulo": analise_1_11,
                    "blocos": analise_1_11.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_2",
            "titulo_menu": "Plano de Análise",
            "conteudos": [
                {
                    "id": "analise_2_01",
                    "titulo_menu": "Hipótese de Trabalho",
                    "blocos": analise_2_01.get_blocos(),
                },
                {
                    "id": "analise_2_02",
                    "titulo_menu": "Método de análise",
                    "blocos": analise_2_02.get_blocos(),
                },
                {
                    "id": "analise_2_03",
                    "titulo_menu": "Variáveis do sistema",
                    "blocos": analise_2_03.get_blocos(),
                },
                {
                    "id": "analise_2_04",
                    "titulo_menu": "Critérios de validação",
                    "blocos": analise_2_04.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_3",
            "titulo_menu": "Execução da Análise",
            "conteudos": [
                {
                    "id": "analise_3_01",
                    "titulo_menu": "Registro de Evidências",
                    "blocos": analise_3_01.get_blocos(),
                },
                {
                    "id": "analise_3_02",
                    "titulo_menu": "Leitura dos Resultados",
                    "blocos": analise_3_02.get_blocos(),
                },
                {
                    "id": "analise_3_03",
                    "titulo_menu": "Tratamento de Desvios e Incertezas",
                    "blocos": analise_3_03.get_blocos(),
                },
                {
                    "id": "analise_3_04",
                    "titulo_menu": "Iterações",
                    "blocos": analise_3_04.get_blocos(),
                },
            ],
        },
    ]