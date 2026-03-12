# apps/app_05/sections/visao_geral/como_usar.py

import streamlit as st


def render_como_usar():

    st.title("Como usar")

    st.write(
        """
Este aplicativo organiza o percurso de estudo da disciplina e
acompanha as etapas do trabalho ao longo do semestre.
"""
    )

    st.subheader("Navegação")

    st.write(
        """
Cada etapa representa um momento do processo de aprendizagem.
Algumas etapas podem ser liberadas progressivamente.
"""
    )

    st.subheader("Como estudar")

    st.write(
        """
Leia as orientações, registre suas respostas e utilize o ambiente
para acompanhar seu desenvolvimento.
"""
    )

    st.info(
        "Use o aplicativo como guia de estudo e registro das atividades."
    )