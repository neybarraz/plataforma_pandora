# admin/statistics_panel.py

from __future__ import annotations

import json
import os
from typing import Any

import pandas as pd
import streamlit as st

from config import ADMIN_USERNAME, APP_CATALOG
from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def _ph() -> str:
    """
    Retorna o placeholder correto para o banco atual.
    SQLite  -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _row_value(row: Any, key: str, index: int = 0) -> Any:
    if row is None:
        return None

    if isinstance(row, dict):
        return row.get(key)

    try:
        return row[key]
    except Exception:
        pass

    try:
        return row[index]
    except Exception:
        return None


def _deserialize_payload(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None

    if isinstance(value, dict):
        return value

    if isinstance(value, str):
        try:
            data = json.loads(value)
            return data if isinstance(data, dict) else None
        except json.JSONDecodeError:
            return None

    try:
        data = json.loads(value)
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _get_auth_username() -> str | None:
    auth_user = st.session_state.get("auth_user")

    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        username = auth_user.get("username")
        if isinstance(username, str) and username.strip():
            return username.strip()

    return None


def _init_stats_state() -> None:
    st.session_state.setdefault("stats_selected_app", None)
    st.session_state.setdefault("stats_force_reload", None)
    st.session_state.setdefault("stats_table_df", None)
    st.session_state.setdefault("stats_total_files", 0)
    st.session_state.setdefault("stats_loaded_app", None)


def _select_stats_app(app_id: str) -> None:
    st.session_state["stats_selected_app"] = app_id
    st.session_state["stats_force_reload"] = app_id
    st.session_state["stats_table_df"] = None
    st.session_state["stats_total_files"] = 0
    st.session_state["stats_loaded_app"] = None


def _get_responses_dir_label(app_id: str) -> str:
    return f"db/app_user_data/{app_id}"


def _normalize_tipo(raw_tipo: Any) -> str:
    raw = str(raw_tipo or "").strip().lower()

    if raw in {"multipla_escolha", "multipla-escolha", "multiple_choice", "radio", "select", "abcd"}:
        return "abcd"

    if raw in {"texto", "text", "textarea"}:
        return "texto"

    return raw or "desconhecido"


def _is_answered_text(item: dict[str, Any]) -> bool:
    resposta = str(item.get("resposta", "")).strip()
    return bool(resposta)


def _is_answered_abcd(item: dict[str, Any]) -> bool:
    resposta = str(item.get("resposta_escolhida", "")).strip()
    return bool(resposta)


def _is_correct_abcd(item: dict[str, Any]) -> bool:
    resposta = str(item.get("resposta_escolhida", "")).strip()
    correta = str(item.get("alternativa_correta", "")).strip()

    if not resposta or not correta:
        return False

    return resposta == correta


def _load_payloads_for_app(app_id: str) -> list[dict[str, Any]]:
    conn = get_conn()
    ph = _ph()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT payload
            FROM app_user_data
            WHERE app_id = {ph}
            """,
            (app_id,),
        )
        rows = cur.fetchall()

        payloads: list[dict[str, Any]] = []

        for row in rows:
            raw_payload = _row_value(row, "payload", 0)
            payload = _deserialize_payload(raw_payload)

            if isinstance(payload, dict):
                payloads.append(payload)

        return payloads

    finally:
        conn.close()


def _collect_question_stats(app_id: str) -> tuple[int, pd.DataFrame]:
    payloads = _load_payloads_for_app(app_id)
    total_files = len(payloads)

    if total_files == 0:
        return 0, pd.DataFrame(columns=["ID", "TIPO", "% RESPONDIDAS", "% ERRO"])

    aggregated: dict[str, dict[str, Any]] = {}

    for payload in payloads:
        responses = payload.get("responses", {})
        if not isinstance(responses, dict):
            continue

        for _, section_payload in responses.items():
            if not isinstance(section_payload, dict):
                continue

            for qid, item in section_payload.items():
                if not isinstance(item, dict):
                    continue

                if "tipo" not in item:
                    continue

                tipo = _normalize_tipo(item.get("tipo"))

                if tipo not in {"abcd", "texto"}:
                    continue

                if qid not in aggregated:
                    aggregated[qid] = {
                        "id": qid,
                        "tipo": tipo,
                        "respondidas": 0,
                        "erros": 0,
                    }

                if tipo == "texto":
                    if _is_answered_text(item):
                        aggregated[qid]["respondidas"] += 1

                elif tipo == "abcd":
                    if _is_answered_abcd(item):
                        aggregated[qid]["respondidas"] += 1
                        if not _is_correct_abcd(item):
                            aggregated[qid]["erros"] += 1

    rows: list[dict[str, Any]] = []

    for qid in sorted(
        aggregated.keys(),
        key=lambda x: int(x.split("_")[-1]) if "_" in x and x.split("_")[-1].isdigit() else x
    ):
        item = aggregated[qid]
        respondidas = item["respondidas"]
        erros = item["erros"]
        tipo = item["tipo"]

        pct_respondidas = (respondidas / total_files * 100) if total_files > 0 else 0

        if tipo == "abcd":
            pct_erro = (erros / total_files * 100) if total_files > 0 else 0
            pct_erro_display = f"{pct_erro:.0f}%"
        else:
            pct_erro_display = "—"

        rows.append(
            {
                "ID": qid,
                "TIPO": tipo,
                "% RESPONDIDAS": f"{pct_respondidas:.0f}%",
                "% ERRO": pct_erro_display,
            }
        )

    df = pd.DataFrame(rows, columns=["ID", "TIPO", "% RESPONDIDAS", "% ERRO"])
    return total_files, df


def statistics_panel() -> None:
    current_username = _get_auth_username()

    if current_username != ADMIN_USERNAME:
        st.error("Acesso negado.")
        return

    _init_stats_state()

    st.subheader("Estatísticas")
    st.caption("1) Clique em um app. 2) Carregue as estatísticas. 3) Veja a tabela por questão.")

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
            is_selected = (st.session_state["stats_selected_app"] == app_id)
            label = f"✅ {title}" if is_selected else title

            st.button(
                label,
                key=f"stats_pick_{app_id}",
                use_container_width=True,
                help=subtitle or app_id,
                on_click=_select_stats_app,
                args=(app_id,),
            )
            st.caption(app_id)

    st.divider()

    # ---------- APP SELECIONADO ----------
    app_id = st.session_state.get("stats_selected_app")
    if not app_id:
        st.info("Clique em um app acima para analisar as estatísticas.")
        return

    st.markdown(f"### App selecionado: `{app_id}`")

    c1, c2 = st.columns([1, 1])

    with c1:
        if st.button("Carregar estatísticas", use_container_width=True, key=f"stats_load_{app_id}"):
            total_files, df = _collect_question_stats(app_id)
            st.session_state["stats_total_files"] = total_files
            st.session_state["stats_table_df"] = df
            st.session_state["stats_loaded_app"] = app_id
            st.rerun()

    with c2:
        if st.button("Recarregar", use_container_width=True, key=f"stats_reload_{app_id}"):
            total_files, df = _collect_question_stats(app_id)
            st.session_state["stats_total_files"] = total_files
            st.session_state["stats_table_df"] = df
            st.session_state["stats_loaded_app"] = app_id
            st.rerun()

    if st.session_state.get("stats_loaded_app") != app_id:
        st.info("Clique em **Carregar estatísticas** para montar a tabela do app selecionado.")
        return

    responses_label = _get_responses_dir_label(app_id)
    total_files = int(st.session_state.get("stats_total_files", 0))
    df = st.session_state.get("stats_table_df")

    st.caption(f"Fonte analisada: `{responses_label}`")
    st.caption(f"Registros analisados: {total_files}")

    if total_files == 0:
        st.warning("Nenhum registro encontrado para este app.")
        return

    if not isinstance(df, pd.DataFrame) or df.empty:
        st.warning("Nenhuma questão estatística foi encontrada nos registros deste app.")
        return

    st.markdown("### Estatísticas por tipo de questão")

    df_abcd = df[df["TIPO"] == "abcd"]
    df_texto = df[df["TIPO"] == "texto"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Questões de múltipla escolha (abcd)**")
        if df_abcd.empty:
            st.info("Nenhuma questão de múltipla escolha encontrada.")
        else:
            st.dataframe(
                df_abcd,
                use_container_width=True,
                hide_index=True,
            )

    with col2:
        st.markdown("**Questões discursivas (texto)**")
        if df_texto.empty:
            st.info("Nenhuma questão de texto encontrada.")
        else:
            st.dataframe(
                df_texto,
                use_container_width=True,
                hide_index=True,
            )
