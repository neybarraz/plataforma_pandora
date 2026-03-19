from __future__ import annotations

import streamlit as st

from .conteudos.avaliacao import render_avaliacao
from .conteudos.como_usar import render_como_usar
from .conteudos.problema_central import render_problema_central
from ...ui.layout import inject_menu_css, inject_topo_css, render_topo_html


def _inject_submenu_css() -> None:
    inject_topo_css("visao-geral-topo")
    inject_menu_css(submenu_key="visao_geral_submenu")


def _render_topo() -> None:
    render_topo_html(
        "visao-geral-topo",
        """
        Este menu, <strong>Disciplina</strong>, funciona como a principal porta de entrada da aplicação,
        reunindo de forma clara, organizada e intuitiva os elementos que direcionam toda a experiência
        do usuário. Nessa seção, é possível ter uma visão geral do sistema, com acesso estruturado aos
        conteúdos essenciais, incluindo orientações de uso, apresentação do problema central e critérios
        de avaliação.
        """,
    )


def render_visao_geral() -> None:
    _inject_submenu_css()

    opcoes = ["Como usar", "Problema central", "Avaliação"]

    if "visao_geral_secao" not in st.session_state:
        st.session_state.visao_geral_secao = opcoes[0]

    secao_atual = st.session_state.get("visao_geral_secao", opcoes[0])
    if secao_atual not in opcoes:
        st.session_state.visao_geral_secao = opcoes[0]

    _render_topo()

    with st.container(key="visao_geral_submenu"):
        cols = st.columns(len(opcoes), gap="small")

        for col, opcao in zip(cols, opcoes):
            with col:
                if st.button(
                    opcao,
                    key=f"visao_geral_btn_{opcao}",
                    type="primary" if st.session_state.visao_geral_secao == opcao else "secondary",
                    use_container_width=True,
                ):
                    st.session_state.visao_geral_secao = opcao
                    st.rerun()

    secao = st.session_state.visao_geral_secao

    if secao == "Como usar":
        render_como_usar()
    elif secao == "Problema central":
        render_problema_central()
    elif secao == "Avaliação":
        render_avaliacao()