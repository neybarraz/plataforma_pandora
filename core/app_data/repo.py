# core/app_data/repo.py

import json
import os
from datetime import datetime
from typing import Any, Dict, Iterable, List

from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def _ph() -> str:
    """
    Retorna o placeholder correto para o banco atual.
    SQLite   -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _serialize_payload(payload: Dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False)


def _deserialize_payload(value: Any) -> Dict[str, Any] | None:
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


def _deep_merge_dicts(base: Dict[str, Any], incoming: Dict[str, Any]) -> Dict[str, Any]:
    """
    Faz merge profundo entre dois dicts.
    - chaves ausentes no incoming são preservadas do base
    - dicts aninhados são mesclados recursivamente
    - valores não-dict do incoming sobrescrevem o base
    """
    merged = dict(base)

    for key, incoming_value in incoming.items():
        base_value = merged.get(key)

        if isinstance(base_value, dict) and isinstance(incoming_value, dict):
            merged[key] = _deep_merge_dicts(base_value, incoming_value)
        else:
            merged[key] = incoming_value

    return merged


def _set_nested_value(target: Dict[str, Any], path: Iterable[str], value: Any) -> Dict[str, Any]:
    """
    Define um valor em um caminho aninhado dentro de um dict.
    Exemplo:
        _set_nested_value(data, ["responses", "problema", "q_001"], {...})
    """
    keys = [str(k).strip() for k in path if str(k).strip()]
    if not keys:
        raise ValueError("path deve conter pelo menos uma chave válida.")

    current = target
    for key in keys[:-1]:
        node = current.get(key)
        if not isinstance(node, dict):
            node = {}
            current[key] = node
        current = node

    current[keys[-1]] = value
    return target


def _empty_record_payload(username: str, app_id: str) -> Dict[str, Any]:
    return {
        "app_id": app_id,
        "username": username,
        "responses": {},
        "meta": {},
    }


def _extract_row_payload(row: Any) -> Dict[str, Any] | None:
    if not row:
        return None

    if isinstance(row, dict):
        raw_payload = row.get("payload")
    else:
        try:
            raw_payload = row["payload"]
        except Exception:
            raw_payload = row[0]

    return _deserialize_payload(raw_payload)


def load_app_user_data(username: str, app_id: str) -> Dict[str, Any] | None:
    username = str(username).strip()
    app_id = str(app_id).strip()

    if not username or not app_id:
        return None

    conn = get_conn()
    ph = _ph()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT payload
            FROM app_user_data
            WHERE username = {ph} AND app_id = {ph}
            LIMIT 1
            """,
            (username, app_id),
        )
        row = cur.fetchone()
        return _extract_row_payload(row)

    finally:
        conn.close()


def save_app_user_data(username: str, app_id: str, payload: Dict[str, Any]) -> None:
    """
    Salva o payload completo do app.

    Importante:
    - no UPDATE, não sobrescreve cegamente o documento salvo;
    - primeiro lê o payload atual e faz merge profundo em Python;
    - isso preserva chaves já existentes que não vieram no payload novo.
    """
    username = str(username).strip()
    app_id = str(app_id).strip()

    if not username or not app_id:
        raise ValueError("username e app_id são obrigatórios.")

    if not isinstance(payload, dict):
        raise ValueError("payload deve ser um dict.")

    conn = get_conn()
    ph = _ph()
    now = _now_iso()

    try:
        cur = conn.cursor()

        cur.execute(
            f"""
            SELECT payload
            FROM app_user_data
            WHERE username = {ph} AND app_id = {ph}
            LIMIT 1
            """,
            (username, app_id),
        )
        existing = cur.fetchone()
        current_payload = _extract_row_payload(existing) or {}

        merged_payload = _deep_merge_dicts(current_payload, payload)
        payload_json = _serialize_payload(merged_payload)

        if DATABASE_URL:
            if existing:
                cur.execute(
                    f"""
                    UPDATE app_user_data
                    SET payload = {ph}::jsonb,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE username = {ph} AND app_id = {ph}
                    """,
                    (payload_json, username, app_id),
                )
            else:
                cur.execute(
                    f"""
                    INSERT INTO app_user_data (
                        username,
                        app_id,
                        payload,
                        created_at,
                        updated_at
                    )
                    VALUES ({ph}, {ph}, {ph}::jsonb, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """,
                    (username, app_id, payload_json),
                )
        else:
            if existing:
                cur.execute(
                    f"""
                    UPDATE app_user_data
                    SET payload = {ph},
                        updated_at = {ph}
                    WHERE username = {ph} AND app_id = {ph}
                    """,
                    (payload_json, now, username, app_id),
                )
            else:
                cur.execute(
                    f"""
                    INSERT INTO app_user_data (
                        username,
                        app_id,
                        payload,
                        created_at,
                        updated_at
                    )
                    VALUES ({ph}, {ph}, {ph}, {ph}, {ph})
                    """,
                    (username, app_id, payload_json, now, now),
                )

        conn.commit()

    finally:
        conn.close()


def update_app_user_path(
    username: str,
    app_id: str,
    path: List[str],
    value: Any,
) -> Dict[str, Any]:
    """
    Atualiza apenas um caminho específico do payload.

    Exemplo de path:
        ["responses", "problema", "q_001"]

    No PostgreSQL:
    - usa jsonb_set para atualizar apenas o trecho alterado

    No SQLite:
    - carrega o payload atual, altera em Python e salva de volta
    """
    username = str(username).strip()
    app_id = str(app_id).strip()
    clean_path = [str(p).strip() for p in path if str(p).strip()]

    if not username or not app_id:
        raise ValueError("username e app_id são obrigatórios.")

    if not clean_path:
        raise ValueError("path deve conter pelo menos uma chave válida.")

    conn = get_conn()
    ph = _ph()
    now = _now_iso()

    try:
        cur = conn.cursor()

        cur.execute(
            f"""
            SELECT payload
            FROM app_user_data
            WHERE username = {ph} AND app_id = {ph}
            LIMIT 1
            """,
            (username, app_id),
        )
        existing = cur.fetchone()
        current_payload = _extract_row_payload(existing)

        if current_payload is None:
            current_payload = _empty_record_payload(username=username, app_id=app_id)

        updated_payload = _set_nested_value(dict(current_payload), clean_path, value)

        if DATABASE_URL:
            value_json = json.dumps(value, ensure_ascii=False)
            path_pg = clean_path

            if existing:
                cur.execute(
                    f"""
                    UPDATE app_user_data
                    SET payload = jsonb_set(
                        COALESCE(payload, '{{}}'::jsonb),
                        {ph}::text[],
                        {ph}::jsonb,
                        true
                    ),
                    updated_at = CURRENT_TIMESTAMP
                    WHERE username = {ph} AND app_id = {ph}
                    """,
                    (path_pg, value_json, username, app_id),
                )
            else:
                payload_json = _serialize_payload(updated_payload)
                cur.execute(
                    f"""
                    INSERT INTO app_user_data (
                        username,
                        app_id,
                        payload,
                        created_at,
                        updated_at
                    )
                    VALUES ({ph}, {ph}, {ph}::jsonb, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """,
                    (username, app_id, payload_json),
                )
        else:
            payload_json = _serialize_payload(updated_payload)

            if existing:
                cur.execute(
                    f"""
                    UPDATE app_user_data
                    SET payload = {ph},
                        updated_at = {ph}
                    WHERE username = {ph} AND app_id = {ph}
                    """,
                    (payload_json, now, username, app_id),
                )
            else:
                cur.execute(
                    f"""
                    INSERT INTO app_user_data (
                        username,
                        app_id,
                        payload,
                        created_at,
                        updated_at
                    )
                    VALUES ({ph}, {ph}, {ph}, {ph}, {ph})
                    """,
                    (username, app_id, payload_json, now, now),
                )

        conn.commit()
        return updated_payload

    finally:
        conn.close()


def update_app_user_question_payload(
    username: str,
    app_id: str,
    section: str,
    question_id: str,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Atalho para gravar respostas no caminho:
        responses -> section -> question_id
    """
    section = str(section).strip()
    question_id = str(question_id).strip()

    if not section or not question_id:
        raise ValueError("section e question_id são obrigatórios.")

    if not isinstance(payload, dict):
        raise ValueError("payload deve ser um dict.")

    return update_app_user_path(
        username=username,
        app_id=app_id,
        path=["responses", section, question_id],
        value=payload,
    )


def delete_app_user_data(username: str, app_id: str | None = None) -> None:
    username = str(username).strip()

    if not username:
        return

    conn = get_conn()
    ph = _ph()

    try:
        cur = conn.cursor()

        if app_id is None:
            cur.execute(
                f"DELETE FROM app_user_data WHERE username = {ph}",
                (username,),
            )
        else:
            app_id = str(app_id).strip()
            cur.execute(
                f"DELETE FROM app_user_data WHERE username = {ph} AND app_id = {ph}",
                (username, app_id),
            )

        conn.commit()

    finally:
        conn.close()
