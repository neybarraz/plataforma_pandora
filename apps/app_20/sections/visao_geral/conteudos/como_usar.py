from __future__ import annotations

import streamlit as st

from ....ui.layout import render_texto_bloco, render_titulo_destaque


def render_como_usar() -> None:
    render_titulo_destaque("Como usar", nivel=1)

    render_texto_bloco(
        """
        Este aplicativo organiza o percurso de aprendizagem da disciplina 
        com base no método DAE (Desafio, Análise e Entrega), estruturando 
        as etapas do trabalho e acompanhando o desenvolvimento técnico ao longo do semestre.
        """
    )

    render_titulo_destaque("Navegação", nivel=3)

    render_texto_bloco(
        """
        Cada etapa corresponde a uma fase do método DAE, orientando o 
        avanço desde a compreensão do desafio até a entrega da solução. 
        O acesso às etapas pode ser liberado progressivamente, conforme a 
        evolução do trabalho.
        """
    )

    render_titulo_destaque("Como estudar", nivel=3)

    render_texto_bloco(
        """
        Siga as orientações de cada etapa, registre suas análises de forma estruturada 
        e utilize o ambiente para acompanhar seu progresso, consolidar o raciocínio 
        técnico e organizar o memorial ao longo do processo.
        """
    )

    st.info(
        "Utilize o aplicativo como ferramenta de apoio ao estudo, organização da investigação e registro estruturado das atividades desenvolvidas."
    )


def render(ctx=None) -> None:
    del ctx
    render_como_usar()