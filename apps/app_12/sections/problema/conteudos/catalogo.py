# apps/app_01/sections/problema/conteudos/catalogo.py

from . import (
    conteudo_1_01,
    conteudo_1_02,
    conteudo_1_03,
    conteudo_1_04,
    conteudo_1_05,
    conteudo_1_06,
    conteudo_2_01,
    conteudo_2_02,
    conteudo_2_03,
    conteudo_3_01,
    conteudo_4_01,
    conteudo_4_02,
    conteudo_4_03,
)


SECTION_KEY = "problema"


def get_paginas():
    return [
        {
            "id": "problema_01",
            "section": SECTION_KEY,
            "numero": "01",
            "titulo_menu": "Contexto do Sistema",
            "conteudos": [
                {
                    "id": "problema_01_001",
                    "section": SECTION_KEY,
                    "pagina_numero": "01",
                    "numero": "001",
                    "titulo_menu": "Cenário do sistema",
                    "blocos": conteudo_1_01.get_blocos(),
                },
                {
                    "id": "problema_01_002",
                    "section": SECTION_KEY,
                    "pagina_numero": "01",
                    "numero": "002",
                    "titulo_menu": "O que é energia de reserva?",
                    "blocos": conteudo_1_02.get_blocos(),
                },
                {
                    "id": "problema_01_003",
                    "section": SECTION_KEY,
                    "pagina_numero": "01",
                    "numero": "003",
                    "titulo_menu": "Objetivo da investigação",
                    "blocos": conteudo_1_03.get_blocos(),
                },
                {
                    "id": "problema_01_004",
                    "section": SECTION_KEY,
                    "pagina_numero": "01",
                    "numero": "004",
                    "titulo_menu": "Componentes do sistema",
                    "blocos": conteudo_1_04.get_blocos(),
                },
                {
                    "id": "problema_01_005",
                    "section": SECTION_KEY,
                    "pagina_numero": "01",
                    "numero": "005",
                    "titulo_menu": "Parâmetros e funcionamento",
                    "blocos": conteudo_1_05.get_blocos(),
                },
                {
                    "id": "problema_01_006",
                    "section": SECTION_KEY,
                    "pagina_numero": "01",
                    "numero": "006",
                    "titulo_menu": "Instrumentos de medição",
                    "blocos": conteudo_1_06.get_blocos(),
                },
            ],
        },
        {
            "id": "problema_02",
            "section": SECTION_KEY,
            "numero": "02",
            "titulo_menu": "Recorte do Desafio",
            "conteudos": [
                {
                    "id": "problema_02_001",
                    "section": SECTION_KEY,
                    "pagina_numero": "02",
                    "numero": "001",
                    "titulo_menu": "Tensão central do sistema",
                    "blocos": conteudo_2_01.get_blocos(),
                },
                {
                    "id": "problema_02_002",
                    "section": SECTION_KEY,
                    "pagina_numero": "02",
                    "numero": "002",
                    "titulo_menu": "Foco da análise física",
                    "blocos": conteudo_2_02.get_blocos(),
                },
                {
                    "id": "problema_02_003",
                    "section": SECTION_KEY,
                    "pagina_numero": "02",
                    "numero": "003",
                    "titulo_menu": "Delimitação do estudo",
                    "blocos": conteudo_2_03.get_blocos(),
                },
            ],
        },
        {
            "id": "problema_03",
            "section": SECTION_KEY,
            "numero": "03",
            "titulo_menu": "Pergunta Central",
            "conteudos": [
                {
                    "id": "problema_03_001",
                    "section": SECTION_KEY,
                    "pagina_numero": "03",
                    "numero": "001",
                    "titulo_menu": "Pergunta central da análise",
                    "blocos": conteudo_3_01.get_blocos(),
                },
            ],
        },
        {
            "id": "problema_04",
            "section": SECTION_KEY,
            "numero": "04",
            "titulo_menu": "Como o Sistema Funciona",
            "conteudos": [
                {
                    "id": "problema_04_001",
                    "section": SECTION_KEY,
                    "pagina_numero": "04",
                    "numero": "001",
                    "titulo_menu": "Entradas do sistema",
                    "blocos": conteudo_4_01.get_blocos(),
                },
                {
                    "id": "problema_04_002",
                    "section": SECTION_KEY,
                    "pagina_numero": "04",
                    "numero": "002",
                    "titulo_menu": "Construção da análise elétrica",
                    "blocos": conteudo_4_02.get_blocos(),
                },
                {
                    "id": "problema_04_003",
                    "section": SECTION_KEY,
                    "pagina_numero": "04",
                    "numero": "003",
                    "titulo_menu": "Saídas e comportamento",
                    "blocos": conteudo_4_03.get_blocos(),
                },
            ],
        },
    ]


def get_conteudos():
    conteudos = []
    for pagina in get_paginas():
        conteudos.extend(pagina["conteudos"])
    return conteudos