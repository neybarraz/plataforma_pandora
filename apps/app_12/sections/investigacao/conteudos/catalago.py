from __future__ import annotations

from typing import Any

from . import (
    analise_1_01,
    analise_1_02,
    analise_1_03,
    analise_1_04,
    analise_1_05,
    analise_1_06,
    analise_1_07,
    analise_1_08,
    analise_1_09,
    analise_2_01,
    analise_2_02,
    analise_2_03,
    analise_2_04,
    analise_3_01,
    analise_3_02,
    analise_4_01,
    analise_4_02,
)


def _build_conteudo(
    content_id: str,
    titulo_menu: str,
    modulo: Any,
    *,
    flow_type: str = "normal",
) -> dict[str, Any]:
    return {
        "id": content_id,
        "titulo_menu": titulo_menu,
        "modulo": modulo,
        "flow_type": flow_type,
        "blocos": modulo.get_blocos(),
    }


def get_paginas() -> list[dict[str, Any]]:
    return [
        {
            "id": "pagina_1",
            "titulo_menu": "Base de Conhecimento",
            "conteudos": [
                _build_conteudo(
                    "analise_1_01",
                    "Grandezas Elétricas",
                    analise_1_01,
                    flow_type="diagnostico",
                ),
                _build_conteudo(
                    "analise_1_02",
                    "Relações Fundamentais",
                    analise_1_02,
                ),
                _build_conteudo(
                    "analise_1_03",
                    "Monofásicos e Trifásicos",
                    analise_1_03,
                ),
                _build_conteudo(
                    "analise_1_04",
                    "Grandezas nominais do motor",
                    analise_1_04,
                ),
                _build_conteudo(
                    "analise_1_05",
                    "Resistividade e Condutores",
                    analise_1_05,
                ),
                _build_conteudo(
                    "analise_1_06",
                    "Corrente e Seção do Condutor",
                    analise_1_06,
                ),
                _build_conteudo(
                    "analise_1_07",
                    "Queda de Tensão",
                    analise_1_07,
                ),
                _build_conteudo(
                    "analise_1_08",
                    "Comprimento do Circuito",
                    analise_1_08,
                ),
                _build_conteudo(
                    "analise_1_09",
                    "Dimensionamento de Condutores",
                    analise_1_09,
                ),
            ],
        },
        {
            "id": "pagina_2",
            "titulo_menu": "Formulação da Análise",
            "conteudos": [
                _build_conteudo(
                    "analise_2_01",
                    "Plano de Análise",
                    analise_2_01,
                ),
                _build_conteudo(
                    "analise_2_02",
                    "Hipótese de Trabalho",
                    analise_2_02,
                ),
                _build_conteudo(
                    "analise_2_03",
                    "Controle de Variáveis",
                    analise_2_03,
                ),
                _build_conteudo(
                    "analise_2_04",
                    "Método de Investigação",
                    analise_2_04,
                ),
            ],
        },
        {
            "id": "pagina_3",
            "titulo_menu": "Aplicação da Análise",
            "conteudos": [
                _build_conteudo(
                    "analise_3_01",
                    "Execução da Análise",
                    analise_3_01,
                ),
                _build_conteudo(
                    "analise_3_02",
                    "Registro de Evidências",
                    analise_3_02,
                ),
            ],
        },
        {
            "id": "pagina_4",
            "titulo_menu": "Avaliação Técnica",
            "conteudos": [
                _build_conteudo(
                    "analise_4_01",
                    "Leitura dos Resultados",
                    analise_4_01,
                ),
                _build_conteudo(
                    "analise_4_02",
                    "Desvios e Incertezas",
                    analise_4_02,
                ),
            ],
        },
    ]