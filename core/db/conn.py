# core/db/conn.py

import os
import sqlite3
from config import DATABASE_PATH

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def using_postgres() -> bool:
    return bool(DATABASE_URL)


def get_conn():
    if using_postgres():
        import psycopg
        from psycopg.rows import dict_row

        conn = psycopg.connect(
            DATABASE_URL,
            row_factory=dict_row
        )
        return conn

    conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
