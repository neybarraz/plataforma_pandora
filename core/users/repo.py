# core/users/repo.py

from typing import Iterable, Optional, Tuple, List, Dict
from datetime import datetime

from core.db.connection import get_conn
from core.db.conn import get_conn
from core.users.username_generator import normalize_display_name, generate_base_username


def list_users():
    """
    Retorna lista de dicts: [{"username":..., "nome":...}, ...]
    """
    conn = get_conn()
    try:
        rows = conn.execute(
            "SELECT username, nome FROM users ORDER BY nome COLLATE NOCASE"
        ).fetchall()
        return [{"username": r["username"], "nome": r["nome"]} for r in rows]
    finally:
        conn.close()

def _now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def username_exists(username: str) -> bool:
    with get_conn() as conn:
        row = conn.execute("SELECT 1 FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
        return bool(row)


def make_unique_username(base: str) -> str:
    base = (base or "").strip().lower()
    if not base:
        return ""
    if not username_exists(base):
        return base
    i = 2
    while True:
        candidate = f"{base}{i}"
        if not username_exists(candidate):
            return candidate
        i += 1


def create_user(display_name: str) -> Tuple[bool, str, str]:
    """
    Cria usuário com first_login=1 e password_hash NULL (primeiro login cria senha).
    Retorna (created, username, message)
    """
    display = normalize_display_name(display_name)
    base = generate_base_username(display)
    if not base:
        return (False, "", "Nome inválido (não foi possível gerar username).")

    username = make_unique_username(base)

    with get_conn() as conn:
        existing = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        if existing:
            return (False, username, "Username já existe.")

        conn.execute(
            """
            INSERT INTO users (nome, username, password_hash, first_login, last_login)
            VALUES (?, ?, NULL, 1, NULL)
            """,
            (display, username),
        )
    return (True, username, "Usuário criado.")


def list_users(limit: int = 500) -> List[Dict]:
    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT id, nome, username, first_login, last_login
            FROM users
            ORDER BY nome COLLATE NOCASE
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]


def reset_password(username: str) -> None:
    with get_conn() as conn:
        conn.execute(
            """
            UPDATE users
            SET password_hash = NULL, first_login = 1
            WHERE username = ?
            """,
            (username,),
        )


def delete_user(username: str) -> None:
    # remove também dados vinculados
    with get_conn() as conn:
        conn.execute("DELETE FROM answers WHERE username = ?", (username,))
        conn.execute("DELETE FROM app_access WHERE username = ?", (username,))
        conn.execute("DELETE FROM stage_unlock WHERE username = ?", (username,))
        conn.execute("DELETE FROM users WHERE username = ?", (username,))