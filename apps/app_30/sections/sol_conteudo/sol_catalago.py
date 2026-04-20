from __future__ import annotations
from typing import Any 
from . import (
    b3_1_01, b3_1_02, b3_1_03, b3_1_04, 
    b3_2_01, b3_2_02, b3_2_03, 
    b3_3_01, b3_3_02, b3_3_03, b3_3_04,  
    b3_4_01, b3_4_02, b3_4_03, b3_4_04, 
    b3_5_01, b3_5_02, b3_5_03, b3_5_04, b3_5_05,
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
        # {"id": "pagina_1", "titulo_menu": "Força magnética", "conteudos": [
        #     _build_conteudo("b3_1_01", "Fundamentos",           b3_1_01),
        #     _build_conteudo("b3_1_02", "Carga puntiforme",      b3_1_02),
        #     _build_conteudo("b3_1_03", "Movimento circular",    b3_1_03),
        #     _build_conteudo("b3_1_04", "Força em fio",        b3_1_04),
        # ],},
        # {"id": "pagina_2", "titulo_menu": "Campo magnético", "conteudos": [
        #     _build_conteudo("b3_2_01", "Conceitos básicos",   b3_2_01),
        #     _build_conteudo("b3_2_02", "Fontes de campo",       b3_2_02),
        #     _build_conteudo("b3_2_03", "Fios e espiras",        b3_2_03),
        # ],},
        # Contexto → Fenômeno → Lei → Aplicação
        {"id": "pagina_3", "titulo_menu": "Lei de Ampère", "conteudos": [
            _build_conteudo("b3_3_01", "🌱 Das descobertas aos motores", b3_3_01),
            _build_conteudo("b3_3_02", "🔧 Desafio de engenharia", b3_3_02),
            _build_conteudo("b3_3_03", "📐 A matemática por trás", b3_3_03),
            _build_conteudo("b3_3_04", "✏️ Mão na massa", b3_3_04),
        ],},
        {"id": "pagina_4", "titulo_menu": "Lei de Faraday", "conteudos": [
            _build_conteudo("b3_4_01", "🌱 Das descobertas aos geradores", b3_4_01),
            _build_conteudo("b3_4_02", "🔧 Desafio de engenharia", b3_4_02),
            _build_conteudo("b3_4_03", "📐 A matemática por trás", b3_4_03),
            _build_conteudo("b3_4_04", "✏️ Mão na massa", b3_4_04),
        ],},
        # {"id": "pagina_5", "titulo_menu": "Ondas eletromagnéticas", "conteudos": [
        #     _build_conteudo("b3_5_01", "Conceitos fundamentais", b3_5_01),
        #     _build_conteudo("b3_5_02", "Propriedades das ondas EM", b3_5_02),
        #     _build_conteudo("b3_5_03", "Espectro eletromagnético", b3_5_03),
        #     _build_conteudo("b3_5_04", "Propagação e velocidade", b3_5_04),
        #     _build_conteudo("b3_5_05", "Aplicações e exemplos", b3_5_05),
        # ],},
    ]
