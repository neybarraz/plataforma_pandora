from __future__ import annotations
from typing import Any
from . import (
    b01_01_01, b01_01_02, b01_01_03, b01_01_04, b01_01_05, 
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
        {"id": "pagina_1", "titulo_menu": "Fluidos", "conteudos": [
            _build_conteudo("b01_01_01", "Lei de Bernoulli com garrafa e mangueira",      b01_01_01),
            # _build_conteudo("b01_01_02", "Viscosidade por queda de esfera",      b01_01_01),
            # _build_conteudo("b01_01_03", "Número de Reynolds em escoamento em tubo",      b01_01_01),
        ]},
        {"id": "pagina_2", "titulo_menu": "Termodinâmica", "conteudos": [
            # _build_conteudo("b01_02_01", "Lei dos Gases Ideais com seringa aquecida",      b01_01_01),
            # _build_conteudo("b01_02_02", "Calor específico de metais por calorimetria",      b01_01_01),
            # _build_conteudo("b01_02_03", "Eficiência de um aquecedor elétrico",      b01_01_01),
            _build_conteudo("b01_02_04", "Dilatação térmica",      b01_01_01),
        ]},
        {"id": "pagina_3", "titulo_menu": "Eletricidade", "conteudos": [
            # _build_conteudo("b01_03_01", "Resistividade de um fio",      b01_01_01),
            # _build_conteudo("b01_03_02", "Resistência e Potência",      b01_01_01),
            _build_conteudo("b01_03_03", "Resistência Ôhmica e Não Ôhmica",      b01_01_01),
            # _build_conteudo("b01_03_04", "Lei de Ohm e resistividade de um fio",      b01_01_01),
            # _build_conteudo("b01_03_05", "Divisor de tensão com carga (Teorema de Thévenin)",      b01_01_01),
            # _build_conteudo("b01_03_06", "Circuito RC transitório",      b01_01_01),
        ]},
        {"id": "pagina_4", "titulo_menu": "Magnetismo", "conteudos": [
            # _build_conteudo("b01_04_01", "Campo magnético de um ímã com sensor Hall",      b01_01_01),
            _build_conteudo("b01_04_02", "Lei de Faraday e Transformadores",      b01_01_01),
            # _build_conteudo("b01_04_03", "Força magnética entre fios paralelos",      b01_01_01),
        ]},
        {"id": "pagina_5", "titulo_menu": "Ótica", "conteudos": [
            _build_conteudo("b01_05_01", "Reflexão e Refração da Luz",      b01_01_01),
            # _build_conteudo("b01_05_02", "Difração por fenda única e dupla",      b01_01_01),
            # _build_conteudo("b01_05_03", "Lei de Snell e índice de refração",      b01_01_01),
            # _build_conteudo("b01_05_04", "Comprimento focal de lentes (método de Bessel)",      b01_01_01),
        ]},
        {"id": "pagina_6", "titulo_menu": "Física Moderna", "conteudos": [
            _build_conteudo("b01_06_01", "Efeito fotoelétrico (simulado com LED e multímetro)",      b01_01_01),
            # _build_conteudo("b01_06_02", "Quantização de energia com espectroscopia de LED",      b01_01_01),
            # _build_conteudo("b01_06_03", "Absorção de radiação gama (simulado com fontes de baixa atividade)",      b01_01_01),
        ]},

    ]
