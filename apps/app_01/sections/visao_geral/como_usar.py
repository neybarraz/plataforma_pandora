# apps/app_01/sections/visao_geral/como_usar.py
import streamlit as st


def render_como_usar() -> None:
    st.markdown("### Como usar")
    st.write(
        "Este aplicativo organiza o percurso de estudo da disciplina e será "
        "utilizado para acompanhar as etapas do trabalho."
    )

    st.markdown("#### Navegação")
    st.write(
        "As abas do aplicativo representam etapas do processo de aprendizagem. "
        "Algumas etapas podem ser liberadas progressivamente ao longo da disciplina."
    )

    st.markdown("#### Como estudar por aqui")
    st.write(
        "Leia as orientações de cada etapa, registre suas respostas com atenção "
        "e utilize o ambiente para acompanhar seu desenvolvimento."
    )

    st.markdown("#### Importante")
    st.write(
        "Nem todas as etapas estarão disponíveis ao mesmo tempo. "
        "O avanço depende da organização da disciplina e das liberações realizadas pelo professor."
    )

    st.info(
        "Em resumo: use o app como guia de estudo, registro das atividades "
        "e acompanhamento do seu percurso na disciplina."
    )