# apps/app_01/sections/problema/conteudos/catalogo.py

from apps.app_05.sections.problema.conteudos import (
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


def get_paginas():
    return [

        {
            "id": "pagina_1",
            "titulo_menu": "Contexto do Sistema",
            "conteudos": [
                {
                    "id": "conteudo_1_01",
                    "titulo_menu": "Cenário do sistema",
                    "blocos": conteudo_1_01.get_blocos(),
                },
                {
                    "id": "conteudo_1_02",
                    "titulo_menu": "O que é energia de reserva?",
                    "blocos": conteudo_1_02.get_blocos(),
                },
                {
                    "id": "conteudo_1_03",
                    "titulo_menu": "Objetivo da investigação",
                    "blocos": conteudo_1_03.get_blocos(),
                },
                {
                    "id": "conteudo_1_04",
                    "titulo_menu": "Componentes do sistema",
                    "blocos": conteudo_1_04.get_blocos(),
                },
                {
                    "id": "conteudo_1_05",
                    "titulo_menu": "Parâmetros e funcionamento observado",
                    "blocos": conteudo_1_05.get_blocos(),
                },
                {
                    "id": "conteudo_1_06",
                    "titulo_menu": "Instrumentos de medição",
                    "blocos": conteudo_1_06.get_blocos(),
                },
            ],
        },

        {
            "id": "pagina_2",
            "titulo_menu": "Recorte do Desafio",
            "conteudos": [
                {
                    "id": "conteudo_2_01",
                    "titulo_menu": "Tensão central do sistema",
                    "blocos": conteudo_2_01.get_blocos(),
                },
                {
                    "id": "conteudo_2_02",
                    "titulo_menu": "Foco da análise física",
                    "blocos": conteudo_2_02.get_blocos(),
                },
                {
                    "id": "conteudo_2_03",
                    "titulo_menu": "Delimitação do estudo",
                    "blocos": conteudo_2_03.get_blocos(),
                },
            ],
        },

        {
            "id": "pagina_3",
            "titulo_menu": "Pergunta Central",
            "conteudos": [
                {
                    "id": "conteudo_3_01",
                    "titulo_menu": "Pergunta central da investigação",
                    "blocos": conteudo_3_01.get_blocos(),
                },
            ],
        },

        {
            "id": "pagina_4",
            "titulo_menu": "Como o Sistema Funciona",
            "conteudos": [
                {
                    "id": "conteudo_4_01",
                    "titulo_menu": "Entradas do sistema",
                    "blocos": conteudo_4_01.get_blocos(),
                },
                {
                    "id": "conteudo_4_02",
                    "titulo_menu": "Processos elétricos e magnéticos",
                    "blocos": conteudo_4_02.get_blocos(),
                },
                {
                    "id": "conteudo_4_03",
                    "titulo_menu": "Saídas e comportamento da carga",
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