# core/db/init_db.py

import os
import sqlite3
from config import DATABASE_PATH

SCHEMA_SQL = """
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
"""

def ensure_db():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
    finally:

        conn.close()
