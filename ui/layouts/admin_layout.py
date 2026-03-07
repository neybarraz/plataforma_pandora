# ui/layouts/admin_layout.py

import streamlit as st
from config import ADMIN_USERNAME

from admin.users_panel import users_panel
from admin.permissions_panel import permissions_panel
from admin.progress_panel import progress_panel
from admin.statistics_panel import statistics_panel
from admin.downloads_panel import downloads_panel


def _get_logged_username() -> str:
    auth_user = st.session_state.get("auth_user")

    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        username = auth_user.get("username")
        if isinstance(username, str) and username.strip():
            return username.strip()

    return ""


def render_admin() -> None:
    username = _get_logged_username()

    if username != ADMIN_USERNAME:
        st.error("Acesso negado.")
        st.session_state["current_view"] = "home"
        st.rerun()
        return

    st.subheader("Painel Admin")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Usuários", "Permissões", "Progressão", "Estatísticas", "Downloads"]
    )

    with tab1:
        users_panel()

    with tab2:
        permissions_panel()

    with tab3:
        progress_panel()

    with tab4:
        statistics_panel()

    with tab5:
        downloads_panel()