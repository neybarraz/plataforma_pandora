from . import (
    entrega_1_01,
    entrega_1_02,
    entrega_1_03,
)


def get_paginas():
    return [
        {"id": "pagina_1", "titulo_menu": "Diagnóstico",
         "conteudos": [{"id": "entrega_1_01", "titulo_menu": "", "blocos": entrega_1_01.get_blocos()}]},

        {"id": "pagina_2", "titulo_menu": "Proposta de Solução",
         "conteudos": [{"id": "entrega_2_01", "titulo_menu": "", "blocos": entrega_1_02.get_blocos()}]},

        {"id": "pagina_3", "titulo_menu": "Validade",
         "conteudos": [{"id": "entrega_3_01", "titulo_menu": "", "blocos": entrega_1_03.get_blocos()}]},
    ]