# admin/downloads_panel.py

from __future__ import annotations

from datetime import datetime

import pandas as pd
import streamlit as st
from core.db.conn import get_conn
import json

from config import ADMIN_USERNAME, APP_CATALOG
from admin.download_utils import (
    build_zip_bytes,
    format_size,
    get_responses_dir,
    list_response_files,
)


def get_app_data_from_db(app_id: str):
    conn = get_conn()
    cur = conn.cursor()

    if "psycopg" in str(type(conn)):
        cur.execute(
            "SELECT username, payload FROM app_user_data WHERE app_id = %s",
            (app_id,)
        )
        rows = cur.fetchall()
    else:
        cur.execute(
            "SELECT username, payload FROM app_user_data WHERE app_id = ?",
            (app_id,)
        )
        rows = cur.fetchall()

    result = []

    for row in rows:
        username = row["username"] if isinstance(row, dict) else row[0]
        payload = row["payload"] if isinstance(row, dict) else row[1]

        result.append({
            "username": username,
            "data": payload
        })

    conn.close()
    return result

def _get_auth_username() -> str | None:
    auth_user = st.session_state.get("auth_user")

    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        username = auth_user.get("username")
        if isinstance(username, str) and username.strip():
            return username.strip()

    return None


def _init_state() -> None:
    st.session_state.setdefault("downloads_selected_app", None)
    st.session_state.setdefault("downloads_table_df", None)
    st.session_state.setdefault("downloads_zip_bytes", None)
    st.session_state.setdefault("downloads_zip_name", None)
    st.session_state.setdefault("downloads_last_loaded_app", None)
    st.session_state.setdefault("downloads_responses_dir_label", None)


def _select_download_app(app_id: str) -> None:
    st.session_state["downloads_selected_app"] = app_id
    st.session_state["downloads_table_df"] = None
    st.session_state["downloads_zip_bytes"] = None
    st.session_state["downloads_zip_name"] = None
    st.session_state["downloads_last_loaded_app"] = None
    st.session_state["downloads_responses_dir_label"] = None


def _clear_checkbox_state_for_app(app_id: str) -> None:
    prefix = f"downloads_select_{app_id}_"
    keys_to_remove = [k for k in st.session_state.keys() if k.startswith(prefix)]
    for key in keys_to_remove:
        st.session_state.pop(key, None)


def _load_files_for_app(app_id: str) -> None:
    responses_dir, files = list_response_files(app_id)

    rows = []
    for item in files:
        rows.append(
            {
                "Selecionar": False,
                "Username": item.username,
                "Arquivo": item.filename,
                "Tamanho": format_size(item.size_bytes),
                "Modificado em": item.modified_at,
                "Caminho": item.relative_path,
            }
        )

    df = pd.DataFrame(rows)

    _clear_checkbox_state_for_app(app_id)

    st.session_state["downloads_table_df"] = df
    st.session_state["downloads_last_loaded_app"] = app_id
    st.session_state["downloads_zip_bytes"] = None
    st.session_state["downloads_zip_name"] = None
    st.session_state["downloads_responses_dir_label"] = str(responses_dir)


def downloads_panel() -> None:
    current_username = _get_auth_username()

    if current_username != ADMIN_USERNAME:
        st.error("Acesso negado.")
        return

    _init_state()

    st.subheader("Downloads")
    st.caption("1) Clique em um app. 2) Carregue os registros. 3) Selecione. 4) Baixe o ZIP.")

    if not APP_CATALOG:
        st.warning("APP_CATALOG está vazio no config.py.")
        return

    # ---------- GRID DE APPS ----------
    st.markdown("### Apps")
    col_left, col_right = st.columns(2, gap="large")

    for i, app in enumerate(APP_CATALOG):
        app_id = app["app_id"]
        title = app.get("title", app_id)
        subtitle = app.get("subtitle", "")

        target_col = col_left if (i % 2 == 0) else col_right
        with target_col:
            is_selected = (st.session_state["downloads_selected_app"] == app_id)
            label = f"✅ {title}" if is_selected else title

            st.button(
                label,
                key=f"downloads_pick_{app_id}",
                use_container_width=True,
                help=subtitle or app_id,
                on_click=_select_download_app,
                args=(app_id,),
            )
            st.caption(app_id)

    st.divider()

    # ---------- APP SELECIONADO ----------
    app_id = st.session_state.get("downloads_selected_app")
    if not app_id:
        st.info("Clique em um app acima para listar os registros disponíveis.")
        return

    st.markdown(f"### App selecionado: `{app_id}`")
    # NOVO: leitura direto do banco
    data_db = get_app_data_from_db(app_id)

    if data_db:
        json_str = json.dumps(data_db, indent=2, ensure_ascii=False)

        st.download_button(
            label="⬇️ Baixar dados do banco (JSON)",
            data=json_str,
            file_name=f"{app_id}_dados.json",
            mime="application/json",
            use_container_width=True,
        )
    else:
        st.warning("Nenhum registro encontrado no banco para este app.")
    col_a, col_b = st.columns([1, 1])

    with col_a:
        if st.button("Carregar arquivos", use_container_width=True, key=f"downloads_load_{app_id}"):
            _load_files_for_app(app_id)
            st.rerun()

    with col_b:
        if st.button("Limpar seleção", use_container_width=True, key=f"downloads_clear_{app_id}"):
            df = st.session_state.get("downloads_table_df")
            if isinstance(df, pd.DataFrame) and not df.empty:
                df["Selecionar"] = False
                st.session_state["downloads_table_df"] = df

            _clear_checkbox_state_for_app(app_id)
            st.session_state["downloads_zip_bytes"] = None
            st.session_state["downloads_zip_name"] = None
            st.rerun()

    if st.session_state.get("downloads_last_loaded_app") != app_id:
        st.info("Clique em **Carregar arquivos** para listar os registros do app selecionado.")
        return

    responses_dir = st.session_state.get("downloads_responses_dir_label") or str(get_responses_dir(app_id))
    st.caption(f"Fonte de dados: `{responses_dir}`")

    df = st.session_state.get("downloads_table_df")

    if not isinstance(df, pd.DataFrame) or df.empty:
        st.warning("Nenhum registro encontrado para este app.")
        return

    st.markdown("### Arquivos disponíveis")

    selected_paths: list[str] = []

    header_cols = st.columns([0.7, 1.2, 2.0, 0.9, 1.3])
    header_cols[0].markdown("**Sel.**")
    header_cols[1].markdown("**Username**")
    header_cols[2].markdown("**Arquivo**")
    header_cols[3].markdown("**Tamanho**")
    header_cols[4].markdown("**Modificado em**")

    st.markdown("---")

    for i, row in df.iterrows():
        path_value = str(row["Caminho"])
        checkbox_key = f"downloads_select_{app_id}_{i}"

        cols = st.columns([0.7, 1.2, 2.0, 0.9, 1.3])

        checked = cols[0].checkbox(
            label="Selecionar",
            value=st.session_state.get(checkbox_key, False),
            key=checkbox_key,
            label_visibility="collapsed",
        )

        cols[1].write(str(row["Username"]))
        cols[2].write(str(row["Arquivo"]))
        cols[3].write(str(row["Tamanho"]))
        cols[4].write(str(row["Modificado em"]))

        if checked:
            selected_paths.append(path_value)

    total_selected = len(selected_paths)
    st.caption(f"Arquivos selecionados: {total_selected}")

    if total_selected == 0:
        st.info("Selecione pelo menos um arquivo para preparar o download.")
        return

    if st.button(
        "Compactar selecionados em ZIP",
        type="primary",
        use_container_width=True,
        key=f"downloads_zip_{app_id}",
    ):
        zip_bytes = build_zip_bytes(
            app_id=app_id,
            selected_relative_paths=selected_paths,
        )

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        zip_name = f"{app_id}_downloads_{timestamp}.zip"

        st.session_state["downloads_zip_bytes"] = zip_bytes
        st.session_state["downloads_zip_name"] = zip_name
        st.rerun()

    zip_bytes = st.session_state.get("downloads_zip_bytes")
    zip_name = st.session_state.get("downloads_zip_name")

    if zip_bytes and zip_name:
        st.download_button(
            label="Baixar pacote ZIP",
            data=zip_bytes,
            file_name=zip_name,
            mime="application/zip",
            use_container_width=True,
            key=f"downloads_button_{app_id}",
        )
