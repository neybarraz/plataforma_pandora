# core/users/repo.py

import os
from typing import Tuple, List, Dict
from datetime import datetime

from core.db.conn import get_conn
from core.users.username_generator import normalize_display_name, generate_base_username

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def _ph() -> str:
    """
    Retorna o placeholder correto para o banco atual.
    SQLite  -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _order_by_nome() -> str:
    """
    SQLite aceita COLLATE NOCASE.
    Para Postgres, usamos ORDER BY nome simples por enquanto.
    """
    return "nome" if DATABASE_URL else "nome COLLATE NOCASE"


def _now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def username_exists(username: str) -> bool:
    conn = get_conn()
    ph = _ph()

    try:
        cur = conn.cursor()
        cur.execute(
            f"SELECT 1 FROM users WHERE username = {ph} LIMIT 1",
            (username,),
        )
        row = cur.fetchone()
        return bool(row)
    finally:
        conn.close()


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
    Cria usuário com first_login=1 e password_hash NULL.
    Retorna (created, username, message)
    """
    display = normalize_display_name(display_name)
    base = generate_base_username(display)

    if not base:
        return (False, "", "Nome inválido (não foi possível gerar username).")

    username = make_unique_username(base)
    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()

        cur.execute(
            f"SELECT id FROM users WHERE username = {ph}",
            (username,),
        )
        existing = cur.fetchone()

        if existing:
            return (False, username, "Username já existe.")

        cur.execute(
            f"""
            INSERT INTO users (nome, username, password_hash, first_login, last_login)
            VALUES ({ph}, {ph}, NULL, 1, NULL)
            """,
            (display, username),
        )
        conn.commit()
        return (True, username, "Usuário criado.")
    finally:
        conn.close()


def list_users(limit: int = 500) -> List[Dict]:
    ph = _ph()
    order_by = _order_by_nome()
    conn = get_conn()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT id, nome, username, first_login, last_login
            FROM users
            ORDER BY {order_by}
            LIMIT {ph}
            """,
            (limit,),
        )
        rows = cur.fetchall()

        result = []
        for r in rows:
            if isinstance(r, dict):
                result.append(r)
            else:
                try:
                    result.append(dict(r))
                except Exception:
                    result.append(
                        {
                            "id": r[0],
                            "nome": r[1],
                            "username": r[2],
                            "first_login": r[3],
                            "last_login": r[4],
                        }
                    )
        return result
    finally:
        conn.close()


def reset_password(username: str) -> None:
    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            UPDATE users
            SET password_hash = NULL, first_login = 1
            WHERE username = {ph}
            """,
            (username,),
        )
        conn.commit()
    finally:
        conn.close()


def delete_user(username: str) -> None:
    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM answers WHERE username = {ph}", (username,))
        cur.execute(f"DELETE FROM app_access WHERE username = {ph}", (username,))
        cur.execute(f"DELETE FROM stage_unlock WHERE username = {ph}", (username,))
        cur.execute(f"DELETE FROM users WHERE username = {ph}", (username,))
        conn.commit()
    finally:
        conn.close()
