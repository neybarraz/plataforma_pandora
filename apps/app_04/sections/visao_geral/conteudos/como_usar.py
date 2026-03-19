from __future__ import annotations

import streamlit as st

from ....ui.layout import render_texto_bloco, render_titulo_destaque


def render_como_usar() -> None:
    render_titulo_destaque("Como usar", nivel=1)

    render_texto_bloco(
        """
        Este aplicativo organiza o percurso de estudo da disciplina e
        acompanha as etapas do trabalho ao longo do semestre.
        """
    )

    render_titulo_destaque("Navegação", nivel=3)

    render_texto_bloco(
        """
        Cada etapa representa um momento do processo de aprendizagem.
        Algumas etapas podem ser liberadas progressivamente.
        """
    )

    render_titulo_destaque("Como estudar", nivel=3)

    render_texto_bloco(
        """
        Leia as orientações, registre suas respostas e utilize o ambiente
        para acompanhar seu desenvolvimento.
        """
    )

    st.info(
        "Use o aplicativo como guia de estudo e registro das atividades."
    )


def render(ctx=None) -> None:
    del ctx
    render_como_usar()