# admin/dashboard.py

import streamlit as st
from config import ADMIN_USERNAME
from core.auth.session import get_user
from admin.users_panel import users_panel
from admin.permissions_panel import permissions_panel
from admin.progress_panel import progress_panel
from admin.statistics_panel import statistics_panel
from admin.downloads_panel import downloads_panel

def admin_dashboard():
    username = get_user()
    if username != ADMIN_USERNAME:
        st.error("Acesso negado.")
        return

    st.markdown("## Painel do Admin")

    tab_users, tab_perms, tab_progress, tab_stats, tab_dl = st.tabs(
        ["Usuários", "Permissões", "Progressão", "Estatísticas", "Downloads"]
    )

    with tab_users:
        users_panel()

    with tab_perms:
        permissions_panel()

    with tab_progress:
        progress_panel()

    with tab_stats:
        statistics_panel()

    with tab_dl:
        downloads_panel()