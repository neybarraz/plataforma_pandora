# apps/app_05/app.py
import streamlit as st

from apps.app_05.config import (
    APP_ID,
    APP_SUBTITLE,
    APP_TITLE,
    TABS,
)
from apps.app_05.renderer import render_section, render_visao_geral
from apps.app_05.sections.problema.problema import render as render_problema
from apps.app_05.storage import load_user_data
from core.permissions.stage_unlock import get_stage_unlocks_for_app


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


def get_stage_access(username: str) -> dict[str, bool]:
    allowed = {tab["key"]: False for tab in TABS}

    unlock_map = get_stage_unlocks_for_app(APP_ID)
    if not isinstance(unlock_map, dict):
        return allowed

    unlocked_stages = unlock_map.get(username)
    if not isinstance(unlocked_stages, (set, list, tuple)):
        return allowed

    unlocked_stages = set(unlocked_stages)

    for stage in unlocked_stages:
        if stage in allowed:
            allowed[stage] = True

    return allowed


def _render_active_stage(
    *,
    username: str,
    section_key: str,
    saved_data: dict,
) -> None:
    section_cfg = next((tab for tab in TABS if tab["key"] == section_key), None)

    if not section_cfg:
        st.error("Etapa selecionada inválida.")
        return

    st.subheader(section_cfg["label"])

    if section_key == "visao_geral":
        render_visao_geral()
        return

    if section_key == "problema":
        render_problema(
            username=username,
            saved_data=saved_data,
        )
        return

    render_section(
        username=username,
        section=section_key,
        saved_data=saved_data,
    )


def run() -> None:
    try:
        username = get_logged_username()
    except RuntimeError as exc:
        st.error(str(exc))
        return

    user_data = load_user_data(username) or {}
    stage_access = get_stage_access(username)

    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.markdown(f"**Usuário:** `{username}`")

    if not TABS:
        st.warning("Nenhuma etapa foi configurada para este app.")
        return

    visible_tabs = [tab for tab in TABS if stage_access.get(tab["key"], False)]

    if not visible_tabs:
        st.warning("Você ainda não possui etapas liberadas neste aplicativo.")
        return

    tab_labels = [tab["label"] for tab in visible_tabs]
    tabs = st.tabs(tab_labels)

    for tab_ui, tab_cfg in zip(tabs, visible_tabs):
        with tab_ui:
            _render_active_stage(
                username=username,
                section_key=tab_cfg["key"],
                saved_data=user_data,
            )