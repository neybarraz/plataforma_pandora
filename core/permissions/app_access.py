# core/permissions/app_access.py

from config import ADMIN_USERNAME, APP_CATALOG
from core.db.conn import get_conn


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

    # admin sempre acessa todos os apps cadastrados no catálogo
    if _is_admin(username):
        return {app["app_id"] for app in APP_CATALOG}

    conn = get_conn()
    try:
        rows = conn.execute(
            """
            SELECT app_id
            FROM app_access
            WHERE username = ? AND access = 1
            """,
            (username,),
        ).fetchall()

        return {r["app_id"] for r in rows}
    finally:
        conn.close()


def get_users_with_access(app_id: str) -> set[str]:
    conn = get_conn()
    try:
        rows = conn.execute(
            """
            SELECT username
            FROM app_access
            WHERE app_id = ? AND access = 1
            """,
            (app_id,),
        ).fetchall()

        return {r["username"] for r in rows}
    finally:
        conn.close()


def set_app_access(username: str, app_id: str, access: bool) -> None:
    username = _as_username(username)

    if not username:
        return

    conn = get_conn()
    try:
        exists = conn.execute(
            "SELECT 1 FROM app_access WHERE username = ? AND app_id = ?",
            (username, app_id),
        ).fetchone()

        if exists:
            conn.execute(
                "UPDATE app_access SET access = ? WHERE username = ? AND app_id = ?",
                (1 if access else 0, username, app_id),
            )
        else:
            conn.execute(
                "INSERT INTO app_access (username, app_id, access) VALUES (?, ?, ?)",
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

    conn = get_conn()
    try:
        for username, allowed in user_access_map.items():
            username = _as_username(username)

            if not username:
                continue

            exists = conn.execute(
                "SELECT 1 FROM app_access WHERE username = ? AND app_id = ?",
                (username, app_id),
            ).fetchone()

            if exists:
                conn.execute(
                    "UPDATE app_access SET access = ? WHERE username = ? AND app_id = ?",
                    (1 if allowed else 0, username, app_id),
                )
            else:
                conn.execute(
                    "INSERT INTO app_access (username, app_id, access) VALUES (?, ?, ?)",
                    (username, app_id, 1 if allowed else 0),
                )

        conn.commit()
    finally:
        conn.close()


def user_has_access(username: str, app_id: str) -> bool:
    username = _as_username(username)

    if not username:
        return False

    # admin sempre acessa qualquer app do catálogo
    if _is_admin(username):
        return True

    return app_id in get_allowed_apps(username)