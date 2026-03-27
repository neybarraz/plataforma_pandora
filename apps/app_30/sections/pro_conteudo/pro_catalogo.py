from __future__ import annotations
from typing import Any
from . import (
    conteudo_1_01, conteudo_1_02, conteudo_1_03, conteudo_1_04,
    conteudo_2_01, conteudo_2_02, conteudo_2_03, conteudo_2_04,
    conteudo_3_01, conteudo_3_02, conteudo_3_03, conteudo_3_04,
    conteudo_4_01, conteudo_4_02, conteudo_4_03, conteudo_4_04,
    conteudo_5_01, conteudo_5_02, conteudo_5_03, conteudo_5_04,
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
        {"id": "pagina_1", "titulo_menu": "Força elétrica", "conteudos": [
            _build_conteudo("conteudo_1_01", "O que acontece entre cargas?", conteudo_1_01, flow_type="diagnostico"),
            _build_conteudo("conteudo_1_02", "Por que elas se atraem ou repelem?", conteudo_1_02),
            _build_conteudo("conteudo_1_03", "Onde a força é mais intensa?", conteudo_1_03),
            _build_conteudo("conteudo_1_04", "Como prever o movimento?", conteudo_1_04),
        ]},
        {"id": "pagina_2", "titulo_menu": "Campo elétrico", "conteudos": [
            _build_conteudo("conteudo_2_01", "O que existe no espaço ao redor da carga?", conteudo_2_01),
            _build_conteudo("conteudo_2_02", "Preciso de outra carga para medir?", conteudo_2_02),
            _build_conteudo("conteudo_2_03", "Onde o campo é mais intenso?", conteudo_2_02),
            _build_conteudo("conteudo_2_04", "Como representar o campo?", conteudo_2_02),
        ]},
        {"id": "pagina_3", "titulo_menu": "Lei de Gauss", "conteudos": [
            _build_conteudo("conteudo_3_01", "Como medir o efeito total do campo?", conteudo_3_01),
            _build_conteudo("conteudo_3_02", "Por que a simetria importa?", conteudo_3_02),
            _build_conteudo("conteudo_3_03", "Qual superfície escolher?", conteudo_3_03),
            _build_conteudo("conteudo_3_04", "Quando Gauss funciona melhor?", conteudo_3_04),
        ]},
        {"id": "pagina_4", "titulo_menu": "Potencial elétrico", "conteudos": [
            _build_conteudo("conteudo_4_01", "O que faz a carga se mover?", conteudo_4_01),
            _build_conteudo("conteudo_4_02", "Qual a diferença entre campo e potencial?", conteudo_4_02),
            _build_conteudo("conteudo_4_03", "Onde a energia é maior?", conteudo_4_03),
            _build_conteudo("conteudo_4_04", "Como prever o movimento?", conteudo_4_04),
        ]},

        {"id": "pagina_5", "titulo_menu": "Capacitância", "conteudos": [
            _build_conteudo("conteudo_5_01", "O que um capacitor faz?", conteudo_5_01),
            _build_conteudo("conteudo_5_02", "Do que depende a capacitância?", conteudo_5_02),
            _build_conteudo("conteudo_5_03", "Onde a energia está armazenada?", conteudo_5_03),
            _build_conteudo("conteudo_5_04", "Quando o modelo deixa de funcionar?", conteudo_5_04),
        ]},
    ]