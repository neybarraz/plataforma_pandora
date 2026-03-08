# core/users/auth_repo.py

import os
from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def _ph():
    """
    Retorna o placeholder correto:
    SQLite -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _row_to_dict(row):
    if row is None:
        return None

    if isinstance(row, dict):
        return row

    if hasattr(row, "keys"):
        return {key: row[key] for key in row.keys()}

    return {
        "id": row[0],
        "nome": row[1],
        "username": row[2],
        "password_hash": row[3],
        "first_login": row[4],
        "last_login": row[5],
    }


def get_user(username: str):
    conn = get_conn()
    ph = _ph()

    try:
        sql = f"""
        SELECT id, nome, username, password_hash, first_login, last_login
        FROM users
        WHERE username = {ph}
        """

        cur = conn.cursor()
        cur.execute(sql, (username,))
        row = cur.fetchone()
        return _row_to_dict(row)

    finally:
        conn.close()


def set_password_and_activate(username: str, password_hash: str) -> None:
    conn = get_conn()
    ph = _ph()

    try:
        sql = f"""
        UPDATE users
        SET password_hash = {ph},
            first_login = 0
        WHERE username = {ph}
        """

        cur = conn.cursor()
        cur.execute(sql, (password_hash, username))
        conn.commit()

    finally:
        conn.close()


def update_last_login(username: str, last_login: str) -> None:
    conn = get_conn()
    ph = _ph()

    try:
        sql = f"""
        UPDATE users
        SET last_login = {ph}
        WHERE username = {ph}
        """

        cur = conn.cursor()
        cur.execute(sql, (last_login, username))
        conn.commit()

    finally:
        conn.close()
