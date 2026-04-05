from __future__ import annotations
from typing import Any
from . import (
    analise_1_00, analise_1_01, analise_1_02, analise_1_03, analise_1_04, analise_1_05, analise_1_06,
    analise_2_00, analise_2_01, analise_2_02, analise_2_03, analise_2_04, analise_2_05, analise_2_06,
    analise_3_00, analise_3_01, analise_3_02, analise_3_03, analise_3_04, analise_3_05, analise_3_06,
)

def _build_conteudo(content_id: str, titulo_menu: str, 
    modulo: Any, *, flow_type: str = "normal",) -> dict[str, Any]:
    return {
        "id": content_id,
        "titulo_menu": titulo_menu,
        "modulo": modulo,
        "flow_type": flow_type,
        "blocos": modulo.get_blocos(),
    }


def get_paginas() -> list[dict[str, Any]]:
    return [
        # {"id": "pagina_1", "titulo_menu": "Corrente elétrica", "conteudos": [
        #     _build_conteudo("analise_1_00", "Situação real: circuito ligado a uma fonte", analise_1_00, flow_type="diagnostico",),
        #     _build_conteudo("analise_1_01", "O que está fluindo no circuito?", analise_1_01, flow_type="diagnostico",),
        #     _build_conteudo("analise_1_02", "Por que a corrente surge?", analise_1_02, flow_type="diagnostico",),
        #     _build_conteudo("analise_1_03", "O que afeta a intensidade?", analise_1_03, flow_type="diagnostico",),
        #     _build_conteudo("analise_1_04", "Como modelar matematicamente a corrente?", analise_1_04, flow_type="diagnostico",),
        #     _build_conteudo("analise_1_05", "Quando o modelo simples de corrente não é suficiente?", analise_1_05, flow_type="diagnostico",),
        #     _build_conteudo("analise_1_06", "Como prever o comportamento da corrente?", analise_1_06, flow_type="diagnostico",),
        # ]},
        # {"id": "pagina_2", "titulo_menu": "Resistência elétrica", "conteudos": [
        #     _build_conteudo("analise_2_00", "Situação real: aquecimento em um condutor", analise_2_00, flow_type="diagnostico",),
        #     _build_conteudo("analise_2_01", "Por que a corrente encontra resistência?", analise_2_01, flow_type="diagnostico",),
        #     _build_conteudo("analise_2_02", "O que aumenta ou reduz resistência?", analise_2_02, flow_type="diagnostico",),
        #     _build_conteudo("analise_2_03", "Como o material influencia?", analise_2_03, flow_type="diagnostico",),
        #     _build_conteudo("analise_2_04", "Como modelar a resistência elétrica?", analise_2_04, flow_type="diagnostico",),
        #     _build_conteudo("analise_2_05", "Quando a lei de Ohm falha?", analise_2_05, flow_type="diagnostico",),
        #     _build_conteudo("analise_2_06", "Como controlar a corrente em um circuito?", analise_2_06, flow_type="diagnostico",),
        # ]},
        {"id": "pagina_3", "titulo_menu": "Circuitos", "conteudos": [
            _build_conteudo("analise_3_00", "Verificação de Carga com o TP4056",    analise_3_00,),
            _build_conteudo("analise_3_01", "O que está acontecendo?",              analise_3_01,),
            _build_conteudo("analise_3_02", "Como o carregador funciona?",          analise_3_02,),
            _build_conteudo("analise_3_03", "Como modelar a carga?",                analise_3_03,),
            _build_conteudo("analise_3_04", "Como verificar se está carregando corretamente?",  analise_3_04,),
            _build_conteudo("analise_3_05", "Quando o modelo deixa de funcionar?", analise_3_05,),
            _build_conteudo("analise_3_06", "Procedimento estruturado de diagnóstico", analise_3_06,),
        ]},
    ]
