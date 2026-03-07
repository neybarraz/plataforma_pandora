# core/db/conn.py

import sqlite3
from config import DATABASE_PATH


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn