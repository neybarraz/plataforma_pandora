from __future__ import annotations

import streamlit as st

from .config import APP_ID, APP_TITLE, APP_SUBTITLE, TABS
from .renderer import render_section
from .storage import load_user_data
from .ui.layout import inject_menu_css
from core.permissions.stage_unlock import get_stage_unlocks_for_app

def _inject_tabs_css() -> None:
    inject_menu_css(main_menu_key="main_tabs")

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
    username = str(username).strip()
    allowed = {
        str(tab.get("key", "")).strip(): False
        for tab in TABS
        if isinstance(tab, dict) and str(tab.get("key", "")).strip()
    }

    if not username:
        return allowed

    unlock_map = get_stage_unlocks_for_app(APP_ID)
    if not isinstance(unlock_map, dict):
        return allowed

    unlocked_stages = unlock_map.get(username)
    if not isinstance(unlocked_stages, (set, list, tuple)):
        return allowed

    for stage in set(unlocked_stages):
        stage = str(stage).strip()
        if stage in allowed:
            allowed[stage] = True

    return allowed


def _get_visible_tabs(stage_access: dict[str, bool]) -> list[dict]:
    visible_tabs: list[dict] = []

    for tab in TABS:
        if not isinstance(tab, dict):
            continue

        key = str(tab.get("key", "")).strip()
        if not key:
            continue

        if stage_access.get(key, False):
            visible_tabs.append(tab)

    return visible_tabs


def _ensure_active_tab(visible_tabs: list[dict]) -> str:
    visible_keys = {
        str(tab.get("key", "")).strip()
        for tab in visible_tabs
        if isinstance(tab, dict)
    }

    current_main_tab = st.session_state.get("main_tab")

    if current_main_tab not in visible_keys:
        st.session_state.main_tab = visible_tabs[0]["key"]

    return str(st.session_state.main_tab).strip()

def _render_main_tabs(visible_tabs: list[dict]) -> None:
    with st.container(key="main_tabs"):
        cols = st.columns(len(visible_tabs), gap="small")

        for col, tab_cfg in zip(cols, visible_tabs):
            key = str(tab_cfg.get("key", "")).strip()
            label = str(tab_cfg.get("label", key)).strip()

            with col:
                if st.button(
                    label,
                    key=f"tab_{key}",
                    type="primary" if st.session_state.main_tab == key else "secondary",
                    use_container_width=True,
                ):
                    st.session_state.main_tab = key
                    st.rerun()



def _render_active_section(
    section_key: str,
    username: str,
    user_data: dict,
) -> None:
    render_section(
        username=username,
        section=section_key,
        saved_data=user_data,
    )


def run() -> None:
    _inject_tabs_css()

    try:
        username = get_logged_username()
    except RuntimeError as exc:
        st.error(str(exc))
        return

    user_data = load_user_data(username)
    stage_access = get_stage_access(username)

    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.markdown(f"**Usuário:** `{username}`")

    if not TABS:
        st.warning("Nenhuma etapa foi configurada para este app.")
        return

    visible_tabs = _get_visible_tabs(stage_access)

    if not visible_tabs:
        st.warning("Você ainda não possui etapas liberadas neste aplicativo.")
        return

    active_tab = _ensure_active_tab(visible_tabs)
    _render_main_tabs(visible_tabs)

    _render_active_section(
        section_key=active_tab,
        username=username,
        user_data=user_data,
    )