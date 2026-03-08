# core/app_data/repo.py

import json
import os
from datetime import datetime
from typing import Any, Dict

from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def _ph() -> str:
    """
    Retorna o placeholder correto para o banco atual.
    SQLite  -> ?
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

    finally:
        conn.close()


def save_app_user_data(username: str, app_id: str, payload: Dict[str, Any]) -> None:
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
            SELECT id
            FROM app_user_data
            WHERE username = {ph} AND app_id = {ph}
            LIMIT 1
            """,
            (username, app_id),
        )
        existing = cur.fetchone()

        if DATABASE_URL:
            # PostgreSQL: envia JSON serializado e faz cast para jsonb
            payload_json = _serialize_payload(payload)

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
            # SQLite: salva como texto JSON
            payload_json = _serialize_payload(payload)

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
