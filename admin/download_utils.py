# admin/download_utils.py

from __future__ import annotations

import io
import json
import os
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


@dataclass
class ResponseFileInfo:
    app_id: str
    username: str
    filename: str
    relative_path: str
    size_bytes: int
    modified_at: str
    absolute_path: Path | None


def _ph() -> str:
    """
    Retorna o placeholder correto para o banco atual.
    SQLite  -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _parse_datetime(value: Any) -> str:
    if value is None:
        return "-"

    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    text = str(value).strip()
    if not text:
        return "-"

    # remove fração de segundos e timezone, se vierem
    text = text.replace("T", " ")
    if "." in text:
        text = text.split(".", 1)[0]
    if "+" in text:
        text = text.split("+", 1)[0]

    return text


def _build_filename(username: str, app_id: str) -> str:
    safe_username = str(username).strip().lower().replace(" ", "_")
    return f"{safe_username}_{app_id}.json"


def _virtual_relative_path(app_id: str, username: str) -> str:
    """
    Identificador virtual para a camada de download.
    Não aponta para filesystem; identifica um registro do banco.
    """
    return f"db::{app_id}::{username}"


def _serialize_payload(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)


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


def get_responses_dir(app_id: str | None) -> Path:
    """
    Mantido por compatibilidade com o painel de downloads.
    Agora é apenas um rótulo lógico, não uma pasta real.
    """
    if not app_id:
        return Path("db") / "app_user_data"
    return Path("db") / "app_user_data" / app_id


def list_response_files(app_id: str) -> tuple[Path, list[ResponseFileInfo]]:
    logical_dir = get_responses_dir(app_id)
    conn = get_conn()
    ph = _ph()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT username, payload, created_at, updated_at
            FROM app_user_data
            WHERE app_id = {ph}
            ORDER BY username
            """,
            (app_id,),
        )
        rows = cur.fetchall()

        files: list[ResponseFileInfo] = []

        for row in rows:
            username = str(_row_value(row, "username", 0) or "").strip()
            raw_payload = _row_value(row, "payload", 1)
            created_at = _row_value(row, "created_at", 2)
            updated_at = _row_value(row, "updated_at", 3)

            if not username:
                continue

            payload = _deserialize_payload(raw_payload)
            if payload is None:
                continue

            json_text = _serialize_payload(payload)
            size_bytes = len(json_text.encode("utf-8"))

            files.append(
                ResponseFileInfo(
                    app_id=app_id,
                    username=username,
                    filename=_build_filename(username, app_id),
                    relative_path=_virtual_relative_path(app_id, username),
                    size_bytes=size_bytes,
                    modified_at=_parse_datetime(updated_at or created_at),
                    absolute_path=None,
                )
            )

        return logical_dir, files

    finally:
        conn.close()


def _load_payload_from_virtual_path(relative_path: str) -> tuple[str, str, dict[str, Any]] | None:
    """
    Interpreta um path virtual no formato:
        db::<app_id>::<username>
    e carrega o payload correspondente do banco.
    """
    text = str(relative_path).strip()

    parts = text.split("::")
    if len(parts) != 3 or parts[0] != "db":
        return None

    _, app_id, username = parts
    app_id = app_id.strip()
    username = username.strip()

    if not app_id or not username:
        return None

    conn = get_conn()
    ph = _ph()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT payload
            FROM app_user_data
            WHERE app_id = {ph} AND username = {ph}
            LIMIT 1
            """,
            (app_id, username),
        )
        row = cur.fetchone()

        if not row:
            return None

        raw_payload = _row_value(row, "payload", 0)
        payload = _deserialize_payload(raw_payload)

        if payload is None:
            return None

        return app_id, username, payload

    finally:
        conn.close()


def build_zip_bytes(app_id: str, selected_relative_paths: list[str]) -> bytes:
    buffer = io.BytesIO()

    with zipfile.ZipFile(
        buffer,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=1,
    ) as zf:
        for relative_path in selected_relative_paths:
            loaded = _load_payload_from_virtual_path(relative_path)
            if not loaded:
                continue

            loaded_app_id, username, payload = loaded
            filename = _build_filename(username, loaded_app_id)
            json_text = _serialize_payload(payload)

            arcname = f"{loaded_app_id}/{filename}"
            zf.writestr(arcname, json_text)

    buffer.seek(0)
    return buffer.getvalue()


def format_size(num_bytes: int) -> str:
    if num_bytes < 1024:
        return f"{num_bytes} B"
    if num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"

    return f"{num_bytes / (1024 * 1024):.2f} MB"
