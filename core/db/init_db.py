# core/db/init_db.py

import os
import sqlite3
from config import DATABASE_PATH

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()

SQLITE_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT,
    first_login INTEGER DEFAULT 1,
    last_login TEXT
);

CREATE TABLE IF NOT EXISTS app_access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    access INTEGER DEFAULT 0,
    UNIQUE(username, app_id)
);

CREATE TABLE IF NOT EXISTS stage_unlock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    unlocked INTEGER DEFAULT 0,
    UNIQUE(username, app_id, stage)
);

CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    question_id TEXT NOT NULL,
    answer_index INTEGER,
    is_correct INTEGER,
    answered_at TEXT
);

CREATE TABLE IF NOT EXISTS app_user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    payload TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(username, app_id)
);

CREATE INDEX IF NOT EXISTS idx_app_user_data_username_app
ON app_user_data (username, app_id);
"""

POSTGRES_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT,
    first_login INTEGER DEFAULT 1,
    last_login TEXT
);

CREATE TABLE IF NOT EXISTS app_access (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    access INTEGER DEFAULT 0,
    UNIQUE(username, app_id)
);

CREATE TABLE IF NOT EXISTS stage_unlock (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    unlocked INTEGER DEFAULT 0,
    UNIQUE(username, app_id, stage)
);

CREATE TABLE IF NOT EXISTS answers (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    question_id TEXT NOT NULL,
    answer_index INTEGER,
    is_correct INTEGER,
    answered_at TEXT
);

CREATE TABLE IF NOT EXISTS app_user_data (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(username, app_id)
);

CREATE INDEX IF NOT EXISTS idx_app_user_data_username_app
ON app_user_data (username, app_id);
"""


def using_postgres() -> bool:
    return bool(DATABASE_URL)


def ensure_sqlite_db() -> None:
    db_dir = os.path.dirname(DATABASE_PATH)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    try:
        conn.executescript(SQLITE_SCHEMA_SQL)
        conn.commit()
    finally:
        conn.close()


def ensure_postgres_db() -> None:
    import psycopg

    conn = psycopg.connect(DATABASE_URL)
    try:
        with conn.cursor() as cur:
            cur.execute(POSTGRES_SCHEMA_SQL)
        conn.commit()
    finally:
        conn.close()


def ensure_db() -> None:
    if using_postgres():
        ensure_postgres_db()
    else:
        ensure_sqlite_db()
