# apps/app_05/sections/investigacao/conteudos/catalago.py

from apps.app_05.sections.investigacao.conteudos import (
    analise_1_01,
    analise_1_02,
    analise_1_03,
    analise_1_04,
    analise_1_05,
    analise_1_06,
    analise_1_07,
    analise_1_08,
    analise_1_09,
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
                    "titulo_menu": "Grandezas elétricas fundamentais",
                    "modulo": analise_1_01,
                    "blocos": analise_1_01.get_blocos(),
                },
                {
                    "id": "analise_1_02",
                    "titulo_menu": "Relações fundamentais de circuito",
                    "modulo": analise_1_02,
                    "blocos": analise_1_02.get_blocos(),
                },
                {
                    "id": "analise_1_03",
                    "titulo_menu": "Sistemas monofásicos e trifásicos",
                    "modulo": analise_1_03,
                    "blocos": analise_1_03.get_blocos(),
                },
                {
                    "id": "analise_1_04",
                    "titulo_menu": "Características elétricas do motor",
                    "modulo": analise_1_04,
                    "blocos": analise_1_04.get_blocos(),
                },
                {
                    "id": "analise_1_05",
                    "titulo_menu": "Propriedades elétricas dos condutores",
                    "modulo": analise_1_05,
                    "blocos": analise_1_05.get_blocos(),
                },
                {
                    "id": "analise_1_06",
                    "titulo_menu": "Capacidade de condução de corrente",
                    "modulo": analise_1_06,
                    "blocos": analise_1_06.get_blocos(),
                },
                {
                    "id": "analise_1_07",
                    "titulo_menu": "Queda de tensão em condutores",
                    "modulo": analise_1_07,
                    "blocos": analise_1_07.get_blocos(),
                },
                {
                    "id": "analise_1_08",
                    "titulo_menu": "Comprimento do circuito elétrico",
                    "modulo": analise_1_08,
                    "blocos": analise_1_08.get_blocos(),
                },
                {
                    "id": "analise_1_09",
                    "titulo_menu": "Critérios técnicos de dimensionamento de condutores",
                    "modulo": analise_1_09,
                    "blocos": analise_1_09.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_2",
            "titulo_menu": "Formulação da Análise",
            "conteudos": [
                {
                    "id": "analise_2_01",
                    "titulo_menu": "Plano de Análise",
                    "blocos": analise_2_01.get_blocos(),
                },
                {
                    "id": "analise_2_02",
                    "titulo_menu": "Hipótese de Trabalho",
                    "blocos": analise_2_02.get_blocos(),
                },
                {
                    "id": "analise_2_03",
                    "titulo_menu": "Controle de Variáveis",
                    "blocos": analise_2_03.get_blocos(),
                },
                {
                    "id": "analise_2_04",
                    "titulo_menu": "Método de Investigação",
                    "blocos": analise_2_04.get_blocos(),
                },
            ],
        },
        {
            "id": "pagina_3",
            "titulo_menu": "Aplicação da Análise",
            "conteudos": [
                {
                    "id": "analise_3_01",
                    "titulo_menu": "Execução da Análise",
                    "blocos": analise_3_01.get_blocos(),
                },
                {
                    "id": "analise_3_02",
                    "titulo_menu": "Registro de Evidências",
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
        {
            "id": "pagina_4",
            "titulo_menu": "Avaliação Técnica",
            "conteudos": [
                {
                    "id": "analise_3_01",
                    "titulo_menu": "Leitura dos Resultados",
                    "blocos": analise_3_01.get_blocos(),
                },
                {
                    "id": "analise_3_02",
                    "titulo_menu": "Tratamento de Desvios e Incertezas",
                    "blocos": analise_3_02.get_blocos(),
                },
            ],
        },
    ]