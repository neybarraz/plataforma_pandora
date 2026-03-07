import streamlit as st

from apps.app_02.sections.visao_geral.avaliacao import render_avaliacao
from apps.app_02.sections.visao_geral.como_usar import render_como_usar
from apps.app_02.sections.visao_geral.problema_central import render_problema_central


def render_visao_geral() -> None:
    tab_como_usar, tab_problema_central, tab_avaliacao = st.tabs(
        ["Como usar", "Problema central", "Avaliação"]
    )

    with tab_como_usar:
        render_como_usar()

    with tab_problema_central:
        render_problema_central()

    with tab_avaliacao:
        render_avaliacao()