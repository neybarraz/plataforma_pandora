# core/users/auth_repo.py

from core.db.conn import get_conn


def get_user(username: str):
    conn = get_conn()
    try:
        row = conn.execute(
            """
            SELECT id, nome, username, password_hash, first_login, last_login
            FROM users
            WHERE username = ?
            """,
            (username,),
        ).fetchone()
        return row
    finally:
        conn.close()


def set_password_and_activate(username: str, password_hash: str) -> None:
    conn = get_conn()
    try:
        conn.execute(
            """
            UPDATE users
            SET password_hash = ?,
                first_login = 0
            WHERE username = ?
            """,
            (password_hash, username),
        )
        conn.commit()
    finally:
        conn.close()


def update_last_login(username: str, last_login: str) -> None:
    conn = get_conn()
    try:
        conn.execute(
            """
            UPDATE users
            SET last_login = ?
            WHERE username = ?
            """,
            (last_login, username),
        )
        conn.commit()
    finally:
        conn.close()