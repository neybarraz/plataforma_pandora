from . import (
    conteudo_1_01,
    conteudo_2_01,
    conteudo_3_01,
)

SECTION_KEY = "problema"
def get_paginas():
    return [
        {"id": "problema_01", "section": SECTION_KEY, "titulo_menu": "Situação real",
         "conteudos": [{"id": "problema_01_001", "section": SECTION_KEY, "titulo_menu": "", "blocos": conteudo_1_01.get_blocos()}]},

        {"id": "problema_02", "section": SECTION_KEY, "titulo_menu": "Limitações da análise",
         "conteudos": [{"id": "problema_02_001", "section": SECTION_KEY, "titulo_menu": "", "blocos": conteudo_2_01.get_blocos()}]},

        {"id": "problema_03", "section": SECTION_KEY, "titulo_menu": "Pergunta técnica",
         "conteudos": [{"id": "problema_03_001", "section": SECTION_KEY, "titulo_menu": "", "blocos": conteudo_3_01.get_blocos()}]},
    ]


def get_conteudos():
    conteudos = []
    for pagina in get_paginas():
        conteudos.extend(pagina["pro_conteudo"])
    return conteudos