# core/permissions/app_access.py

import os

from config import ADMIN_USERNAME, APP_CATALOG
from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def _ph() -> str:
    """
    SQLite  -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _row_value(row, key: str, index: int = 0):
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


def _as_username(username) -> str:
    """
    Extrai o username sem alterar caixa.
    """
    if username is None:
        return ""

    if isinstance(username, str):
        return username.strip()

    if isinstance(username, dict):
        value = username.get("username")
        if isinstance(value, str):
            return value.strip()

    return str(username).strip()


def _normalized(value: str) -> str:
    """
    Normalização apenas para comparações lógicas.
    """
    return (value or "").strip().lower()


def _is_admin(username) -> bool:
    return _normalized(_as_username(username)) == _normalized(ADMIN_USERNAME)


def get_allowed_apps(username: str) -> set[str]:
    username = _as_username(username)

    if not username:
        return set()

    if _is_admin(username):
        return {app["app_id"] for app in APP_CATALOG}

    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT app_id
            FROM app_access
            WHERE username = {ph} AND access = 1
            """,
            (username,),
        )
        rows = cur.fetchall()
        return {_row_value(r, "app_id", 0) for r in rows if _row_value(r, "app_id", 0)}
    finally:
        conn.close()


def get_users_with_access(app_id: str) -> set[str]:
    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT username
            FROM app_access
            WHERE app_id = {ph} AND access = 1
            """,
            (app_id,),
        )
        rows = cur.fetchall()
        return {_row_value(r, "username", 0) for r in rows if _row_value(r, "username", 0)}
    finally:
        conn.close()


def set_app_access(username: str, app_id: str, access: bool) -> None:
    username = _as_username(username)

    if not username:
        return

    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()

        cur.execute(
            f"SELECT 1 FROM app_access WHERE username = {ph} AND app_id = {ph}",
            (username, app_id),
        )
        exists = cur.fetchone()

        if exists:
            cur.execute(
                f"UPDATE app_access SET access = {ph} WHERE username = {ph} AND app_id = {ph}",
                (1 if access else 0, username, app_id),
            )
        else:
            cur.execute(
                f"INSERT INTO app_access (username, app_id, access) VALUES ({ph}, {ph}, {ph})",
                (username, app_id, 1 if access else 0),
            )

        conn.commit()
    finally:
        conn.close()


def bulk_set_access_for_app(app_id: str, user_access_map: dict[str, bool]) -> None:
    """
    user_access_map: { "maiconmarcal": True, "anacosta": False, ... }
    """
    if not user_access_map:
        return

    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()

        for username, allowed in user_access_map.items():
            username = _as_username(username)

            if not username:
                continue

            cur.execute(
                f"SELECT 1 FROM app_access WHERE username = {ph} AND app_id = {ph}",
                (username, app_id),
            )
            exists = cur.fetchone()

            if exists:
                cur.execute(
                    f"UPDATE app_access SET access = {ph} WHERE username = {ph} AND app_id = {ph}",
                    (1 if allowed else 0, username, app_id),
                )
            else:
                cur.execute(
                    f"INSERT INTO app_access (username, app_id, access) VALUES ({ph}, {ph}, {ph})",
                    (username, app_id, 1 if allowed else 0),
                )

        conn.commit()
    finally:
        conn.close()


def user_has_access(username: str, app_id: str) -> bool:
    username = _as_username(username)

    if not username:
        return False

    if _is_admin(username):
        return True

    return app_id in get_allowed_apps(username)
