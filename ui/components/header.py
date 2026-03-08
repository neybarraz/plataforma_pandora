# ui/components/header.py

import streamlit as st
from datetime import datetime

from config import ADMIN_USERNAME, ADMIN_PASSWORD, APP_CATALOG
from core.permissions.app_access import get_allowed_apps
from core.users.auth_repo import get_user, set_password_and_activate, update_last_login
from core.auth.password import hash_password, verify_password


def _init_session():
    st.session_state.setdefault("auth_user", None)
    st.session_state.setdefault("last_login", None)
    st.session_state.setdefault("progress_overall", 0)

    st.session_state.setdefault("current_view", "home")
    st.session_state.setdefault("current_app", None)

    st.session_state.setdefault("auth_mode", "login")
    st.session_state.setdefault("pending_username", None)


def _logout():
    st.session_state["auth_user"] = None
    st.session_state["last_login"] = None
    st.session_state["progress_overall"] = 0
    st.session_state["current_view"] = "home"
    st.session_state["current_app"] = None
    st.session_state["auth_mode"] = "login"
    st.session_state["pending_username"] = None


def _finish_login(username: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    st.session_state["auth_user"] = username
    st.session_state["last_login"] = now
    st.session_state["progress_overall"] = 0
    st.session_state["auth_mode"] = "login"
    st.session_state["pending_username"] = None

    update_last_login(username, now)


def render_header():
    _init_session()

    col1, col2 = st.columns([3, 2])

    with col1:
        st.title("Pandora Learning Platform")

    with col2:
        user = st.session_state["auth_user"]

        if user:
            st.write(
                f"Usuário: **{user}** | Último acesso: {st.session_state['last_login']} | Progresso: {st.session_state['progress_overall']}%"
            )

            if user == ADMIN_USERNAME:
                c1, c2 = st.columns(2)

                with c1:
                    if st.button("Admin", key="btn_admin", use_container_width=True):
                        st.session_state["current_view"] = "admin"
                        st.session_state["current_app"] = None
                        st.rerun()

                with c2:
                    if st.button("Sair", key="btn_logout_admin", use_container_width=True):
                        _logout()
                        st.rerun()
            else:
                if st.button("Sair", key="btn_logout_user"):
                    _logout()
                    st.rerun()

            return

        if st.session_state["auth_mode"] == "set_password":
            username = st.session_state.get("pending_username")

            if not username:
                st.session_state["auth_mode"] = "login"
                st.error("Fluxo de primeiro acesso inválido. Tente novamente.")
                st.rerun()
                return

            st.info(f"Primeiro acesso detectado para **{username}**")

            p1 = st.text_input("Nova senha", type="password", key="first_pass_1")
            p2 = st.text_input("Confirmar senha", type="password", key="first_pass_2")

            c1, c2 = st.columns(2)

            with c1:
                if st.button("Salvar senha", key="btn_save_first_password", use_container_width=True):
                    if not p1 or not p2:
                        st.error("Preencha os dois campos.")
                        return

                    if p1 != p2:
                        st.error("As senhas não coincidem.")
                        return

                    user_data = get_user(username)
                    if not user_data:
                        st.error("Usuário não encontrado para criação de senha.")
                        return

                    set_password_and_activate(username, hash_password(p1))
                    _finish_login(username)

                    st.session_state.pop("first_pass_1", None)
                    st.session_state.pop("first_pass_2", None)

                    st.success("Senha criada com sucesso.")
                    st.rerun()

            with c2:
                if st.button("Cancelar", key="btn_cancel_first_password", use_container_width=True):
                    st.session_state["auth_mode"] = "login"
                    st.session_state["pending_username"] = None
                    st.session_state.pop("first_pass_1", None)
                    st.session_state.pop("first_pass_2", None)
                    st.rerun()

            return

        username = st.text_input("Username", key="login_username").strip().lower()
        password = st.text_input("Senha", type="password", key="login_password")

        if st.button("Entrar", key="btn_login"):

            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                _finish_login(username)
                st.success("Login admin realizado")
                st.rerun()
                return

            user_data = get_user(username)

            if not user_data:
                st.error("Usuário não encontrado.")
                return

            if user_data["first_login"] == 1 or not user_data["password_hash"]:
                st.session_state["auth_mode"] = "set_password"
                st.session_state["pending_username"] = username
                st.rerun()
                return

            if not verify_password(password, user_data["password_hash"]):
                st.error("Senha incorreta.")
                return

            _finish_login(username)
            st.success("Login realizado.")
            st.rerun()


def get_allowed_apps_for_current_user():
    _init_session()

    user = st.session_state.get("auth_user")
    if not user:
        return {app["app_id"] for app in APP_CATALOG}

    return get_allowed_apps(user)
