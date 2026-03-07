import importlib
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

from config import ADMIN_USERNAME
from core.db.init_db import ensure_db
from core.permissions.app_access import user_has_access
from ui.layouts.home_layout import render_home
from ui.layouts.admin_layout import render_admin

ensure_db()


def get_logged_username() -> str | None:
    """
    Normaliza o usuário autenticado da plataforma.

    Casos aceitos:
    - st.session_state["auth_user"] como string
    - st.session_state["auth_user"] como dict contendo "username"
    """
    auth_user = st.session_state.get("auth_user")

    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        username = auth_user.get("username")
        if isinstance(username, str) and username.strip():
            return username.strip()

    return None


def reset_to_home() -> None:
    st.session_state["current_view"] = "home"
    st.session_state["current_app"] = None
    st.rerun()


def main() -> None:
    st.set_page_config(page_title="Plataforma", layout="wide")

    st.session_state.setdefault("current_view", "home")
    st.session_state.setdefault("current_app", None)

    view = st.session_state["current_view"]

    if view == "home":
        render_home()
        return

    if view == "admin":
        render_admin()

        if st.button("Voltar para Home"):
            reset_to_home()
        return

    if view == "app":
        username = get_logged_username()
        current_app = st.session_state.get("current_app")

        if not username:
            st.error("Você precisa estar logado para acessar um app.")
            reset_to_home()
            return

        if not current_app:
            st.error("Nenhum app foi selecionado.")
            reset_to_home()
            return

        # Admin pode acessar qualquer app
        if username != ADMIN_USERNAME and not user_has_access(username, current_app):
            st.error("Você não tem acesso a este app.")
            reset_to_home()
            return

        try:
            module = importlib.import_module(f"apps.{current_app}.app")
            module.run()

        except ModuleNotFoundError as e:
            st.warning(f"O módulo do app '{current_app}' ainda não foi implementado.")
            st.caption(f"Detalhe técnico: {e}")

        except AttributeError:
            st.error(f"O app '{current_app}' não possui uma função run().")

        except Exception as e:
            st.error(f"Erro ao carregar o app '{current_app}'.")
            st.caption(f"Detalhe técnico: {e}")

        if st.button("Voltar para Home"):
            reset_to_home()
        return

    reset_to_home()


if __name__ == "__main__":
    main()