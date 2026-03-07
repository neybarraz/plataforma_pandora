# apps/app_02/sections/problema/conteudos/catalogo.py

from apps.app_02.sections.problema.conteudos import (
    conteudo_00,
    conteudo_01,
    conteudo_02,
    conteudo_03,
    conteudo_04,
    conteudo_05,
    conteudo_06,
    conteudo_07,
    conteudo_08,
    conteudo_09,
    conteudo_10,
    conteudo_11,
    conteudo_12,
    conteudo_13,
)


def get_conteudos():
    return [
        {
            "id": "conteudo_00",
            "titulo_menu": "Formalização",
            "blocos": conteudo_00.get_blocos(),
        },
        {
            "id": "conteudo_01",
            "titulo_menu": "Finalidade",
            "blocos": conteudo_01.get_blocos(),
        },
        {
            "id": "conteudo_02",
            "titulo_menu": "Placa do motor",
            "blocos": conteudo_02.get_blocos(),
        },
        {
            "id": "conteudo_03",
            "titulo_menu": "Incertezas",
            "blocos": conteudo_03.get_blocos(),
        },
        {
            "id": "conteudo_04",
            "titulo_menu": "Alimentação elétrica",
            "blocos": conteudo_04.get_blocos(),
        },
        {
            "id": "conteudo_05",
            "titulo_menu": "Instalação física",
            "blocos": conteudo_05.get_blocos(),
        },
        {
            "id": "conteudo_06",
            "titulo_menu": "Foco do problema",
            "blocos": conteudo_06.get_blocos(),
        },
        {
            "id": "conteudo_07",
            "titulo_menu": "Foco da análise",
            "blocos": conteudo_07.get_blocos(),
        },
        {
            "id": "conteudo_08",
            "titulo_menu": "Escopo do estudo",
            "blocos": conteudo_08.get_blocos(),
        },
        {
            "id": "conteudo_09",
            "titulo_menu": "Pergunta norteadora",
            "blocos": conteudo_09.get_blocos(),
        },
        {
            "id": "conteudo_10",
            "titulo_menu": "Entradas do sistema",
            "blocos": conteudo_10.get_blocos(),
        },
        {
            "id": "conteudo_11",
            "titulo_menu": "Processamento",
            "blocos": conteudo_11.get_blocos(),
        },
        {
            "id": "conteudo_12",
            "titulo_menu": "Saídas do sistema",
            "blocos": conteudo_12.get_blocos(),
        },
        {
            "id": "conteudo_13",
            "titulo_menu": "Validação",
            "blocos": conteudo_13.get_blocos(),
        },
    ]