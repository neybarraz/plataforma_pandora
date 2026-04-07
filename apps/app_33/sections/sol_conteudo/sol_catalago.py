from __future__ import annotations
from typing import Any 
from . import (
    entrega_1_01, entrega_1_02, entrega_1_03, entrega_1_04, entrega_1_05, entrega_1_06,
)

def _build_conteudo(content_id: str, titulo_menu: str, modulo: Any, *, flow_type: str = "normal") -> dict[str, Any]:
    return {
        "id": content_id,
        "titulo_menu": titulo_menu,
        "modulo": modulo,
        "flow_type": flow_type,
        "blocos": modulo.get_blocos(),
    }

def get_paginas() -> list[dict[str, Any]]:
    return [
       {"id": "pagina_1", "titulo_menu": "Força magnética", "conteudos": [
            _build_conteudo("entrega_1_01", "O que acontece com a carga no campo?", entrega_1_01),
            _build_conteudo("entrega_1_02", "Por que a trajetória muda?", entrega_1_02),
            _build_conteudo("entrega_1_03", "Como depende da velocidade?", entrega_1_03),
            _build_conteudo("entrega_1_04", "Qual o tipo de movimento?", entrega_1_04),
        ],},
        # {"id": "pagina_2", "titulo_menu": "Campo magnético", "conteudos": [
        #     _build_conteudo("entrega_2_01", "O que surge ao redor de um fio?", entrega_2_01),
        #     _build_conteudo("entrega_2_02", "Por que a corrente gera campo?", entrega_2_02),
        #     _build_conteudo("entrega_2_03", "Onde o campo é mais intenso?", entrega_2_03),
        #     _build_conteudo("entrega_2_04", "Qual a direção do campo?", entrega_2_04),
        # ],},
        # {"id": "pagina_3", "titulo_menu": "Lei de Ampère", "conteudos": [
        #     _build_conteudo("entrega_3_01", "Como calcular o campo magnético?", entrega_3_01),
        #     _build_conteudo("entrega_3_02", "Quando a simetria ajuda?", entrega_3_02),
        #     _build_conteudo("entrega_3_03", "Qual caminho escolher?", entrega_3_03),
        #     _build_conteudo("entrega_3_04", "Quando a lei deixa de ser simples?", entrega_3_04),
        # ],},
        # {"id": "pagina_4", "titulo_menu": "Lei de Faraday", "conteudos": [
        #     _build_conteudo("entrega_4_01", "Quando surge corrente sem bateria?", entrega_4_01),
        #     _build_conteudo("entrega_4_02", "O que é fluxo magnético?", entrega_4_02),
        #     _build_conteudo("entrega_4_03", "O que aumenta a indução?", entrega_4_03),
        #     _build_conteudo("entrega_4_04", "Como prever a corrente induzida?", entrega_4_04),
        # ],},
        # {"id": "pagina_5", "titulo_menu": "Ondas eletromagnéticas", "conteudos": [
        #     _build_conteudo("entrega_5_01", "O que está oscilando?", entrega_5_01),
        #     _build_conteudo("entrega_5_02", "Como a onda se propaga?", entrega_5_02),
        #     _build_conteudo("entrega_5_03", "O que define frequência e comprimento?", entrega_5_03),
        #     _build_conteudo("entrega_5_04", "Onde isso aparece no mundo real?", entrega_5_04),
        # ],},
    ]