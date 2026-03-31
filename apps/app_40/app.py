from __future__ import annotations

import streamlit as st

from .config import APP_ID, APP_TITLE, APP_SUBTITLE
from .engine.entrypoint import run_engine


def get_logged_username() -> str:
    auth_user = st.session_state.get("auth_user")

    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        username = auth_user.get("username")
        if isinstance(username, str) and username.strip():
            return username.strip()

    raise RuntimeError(
        "Usuário autenticado não encontrado em session_state['auth_user']."
    )

def run() -> None:
    try:
        username = get_logged_username()
    except RuntimeError as exc:
        st.error(str(exc))
        return

    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.markdown(f"**Usuário:** `{username}`")

    run_engine(username)
