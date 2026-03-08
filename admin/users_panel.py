# admin/users_panel.py

import streamlit as st

from core.users.repo import list_users, create_user, reset_password, delete_user
from core.users.import_csv import import_users_from_csv_bytes
from config import ADMIN_USERNAME


def users_panel():
    user = st.session_state.get("auth_user")
    if user != ADMIN_USERNAME:
        st.error("Acesso negado.")
        return

    st.subheader("Usuários")

    # ---------- Criar usuário manual ----------
    with st.expander("Criar usuário manualmente", expanded=False):
        nome = st.text_input("Nome completo (ex.: MAICON MARÇAL)", key="adm_create_nome")
        senha_inicial = st.text_input(
            "Senha inicial (opcional)",
            type="password",
            key="adm_create_password"
        )

        if st.button("Criar usuário", key="adm_create_btn"):
            senha = senha_inicial.strip() if senha_inicial else None
            ok, username, msg = create_user(nome, senha)

            if ok:
                if senha:
                    st.success(f"{msg} username: {username} | senha inicial definida.")
                else:
                    st.success(f"{msg} username: {username}")
                st.rerun()
            else:
                st.warning(f"{msg} (username sugerido: {username})")

    # ---------- Importar CSV ----------
    with st.expander("Importar CSV (1 coluna: NOME_COMPLETO)", expanded=True):
        up = st.file_uploader("Selecione o CSV", type=["csv"], key="adm_csv")
        if up is not None:
            if st.button("Importar agora", key="adm_csv_import_btn"):
                res = import_users_from_csv_bytes(up.getvalue())
                st.success(f"Criados: {res['created']} | Ignorados: {res['skipped']} | Erros: {res['errors']}")
                st.dataframe(res["details"], use_container_width=True)

    st.divider()

    # ---------- Lista ----------
    st.caption("Lista de usuários. Se o usuário estiver com first_login = SIM, ele precisará criar senha no próximo acesso.")

    all_users = list_users()
    query = st.text_input("Buscar (nome ou username)", key="adm_user_search").strip().lower()

    if query:
        all_users = [
            u for u in all_users
            if query in (u["nome"] or "").lower() or query in (u["username"] or "").lower()
        ]

    st.dataframe(
        [
            {
                "nome": u["nome"],
                "username": u["username"],
                "first_login": "SIM" if u["first_login"] else "NÃO",
                "last_login": u["last_login"] or "-",
            }
            for u in all_users
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.write("Ações rápidas")

    # mensagens persistentes
    st.session_state.setdefault("adm_msg_reset", None)
    st.session_state.setdefault("adm_msg_delete", None)

    def _render_msg(msg):
        if not msg:
            return
        kind, text = msg
        if kind == "success":
            st.success(text)
        elif kind == "warning":
            st.warning(text)
        else:
            st.error(text)

    # =========================
    # RESETAR SENHA
    # =========================
    st.markdown("### Resetar senha")

    c_inp, c_pass, c_btn = st.columns([3.2, 3.2, 1.8])

    with c_inp:
        target_reset = st.text_input(
            "reset_username",
            key="adm_reset_username",
            label_visibility="collapsed",
            placeholder="username (ex.: maiconmarcal)",
        ).strip().lower()

    with c_pass:
        new_password = st.text_input(
            "Nova senha (opcional)",
            key="adm_reset_new_password",
            type="password",
            label_visibility="collapsed",
            placeholder="nova senha (deixe vazio para forçar primeiro acesso)",
        )

    with c_btn:
        if st.button("Resetar senha", key="adm_reset_btn", use_container_width=True):
            if not target_reset:
                st.session_state["adm_msg_reset"] = ("warning", "Informe um username.")
            else:
                senha = new_password.strip() if new_password else None
                reset_password(target_reset, senha)

                if senha:
                    st.session_state["adm_msg_reset"] = (
                        "success",
                        f"Senha redefinida para {target_reset} com senha inicial."
                    )
                else:
                    st.session_state["adm_msg_reset"] = (
                        "success",
                        f"Senha resetada para {target_reset}. O usuário criará nova senha no próximo login."
                    )
            st.rerun()

    _render_msg(st.session_state.get("adm_msg_reset"))

    # =========================
    # REMOVER USUÁRIO
    # =========================
    st.markdown("### Remover usuário")

    c_inp, c_btn = st.columns([4, 1.8])

    with c_inp:
        target_del = st.text_input(
            "delete_username",
            key="adm_delete_username",
            label_visibility="collapsed",
            placeholder="username (ex.: maiconmarcal)",
        ).strip().lower()

    with c_btn:
        if st.button("Remover usuário", key="adm_delete_btn", use_container_width=True):
            confirm = bool(st.session_state.get("adm_delete_confirm"))
            if not target_del:
                st.session_state["adm_msg_delete"] = ("warning", "Informe um username.")
            elif not confirm:
                st.session_state["adm_msg_delete"] = ("warning", "Marque a confirmação para remover.")
            else:
                delete_user(target_del)
                st.session_state["adm_delete_confirm"] = False
                st.session_state["adm_msg_delete"] = ("success", f"Usuário {target_del} removido.")
            st.rerun()

    st.checkbox(
        "Confirmo que quero remover (irreversível)",
        key="adm_delete_confirm",
    )

    _render_msg(st.session_state.get("adm_msg_delete"))

    st.divider()
