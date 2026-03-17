from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "manutencao_tecnica"


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": (
                "Este módulo está temporariamente em **manutenção técnica**. "
                "Estamos realizando ajustes na estrutura da plataforma para "
                "melhorar a estabilidade e o registro das respostas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Durante este período, algumas atividades interativas podem "
                "não estar disponíveis. O conteúdo será restabelecido em breve."
            ),
        },
    ]


def render_controles_especiais() -> None:
    st.warning(
        """
        **Manutenção técnica em andamento**

        Esta atividade está temporariamente indisponível enquanto realizamos
        atualizações no sistema da plataforma.
        """
    )

    st.info(
        """
        O conteúdo será reativado assim que a atualização for concluída.
        """
    )