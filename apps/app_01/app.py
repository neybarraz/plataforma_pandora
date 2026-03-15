# apps/app_01/app.py
import streamlit as st

from apps.app_01.config import APP_ID, APP_TITLE, APP_SUBTITLE, TABS
from apps.app_01.renderer import render_section, render_visao_geral
from apps.app_01.sections.problema.problema import render as render_problema
from apps.app_01.sections.investigacao.investigacao import render as render_investigacao
from apps.app_01.storage import load_user_data
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


def run() -> None:
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

    visible_tabs = [tab for tab in TABS if stage_access.get(tab["key"], False)]

    if not visible_tabs:
        st.warning("Você ainda não possui etapas liberadas neste aplicativo.")
        return

    tab_labels = [tab["label"] for tab in visible_tabs]
    tabs = st.tabs(tab_labels)

    for tab_ui, tab_cfg in zip(tabs, visible_tabs):
        section_key = tab_cfg["key"]
        section_label = tab_cfg["label"]

        with tab_ui:
            st.subheader(section_label)

            if section_key == "visao_geral":
                render_visao_geral()

            elif section_key == "problema":
                render_problema(
                    username=username,
                    saved_data=user_data,
                )

            elif section_key == "investigacao":
                render_investigacao(
                    {
                        "username": username,
                        "saved_data": user_data,
                    }
                )

            else:
                render_section(
                    username=username,
                    section=section_key,
                    saved_data=user_data,
                )
