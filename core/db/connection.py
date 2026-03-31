# core/db/connection.py

import os
import sqlite3
from contextlib import contextmanager
from config import DATABASE_PATH

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def using_postgres() -> bool:
    return bool(DATABASE_URL)

import streamlit as st
import os

st.write("DEBUG DATABASE_URL:", os.getenv("DATABASE_URL"))


def _ensure_db_dir():
    db_dir = os.path.dirname(DATABASE_PATH)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)


@contextmanager
def get_conn():

    # ---------- POSTGRES (Render) ----------
    if using_postgres():
        import psycopg

        conn = psycopg.connect(DATABASE_URL)
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    # ---------- SQLITE (Local) ----------
    else:
        _ensure_db_dir()
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row

        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
