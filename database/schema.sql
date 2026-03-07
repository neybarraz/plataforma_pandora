-- database/schema.sql

PRAGMA foreign_keys = ON;

-- =========================
-- USERS
-- =========================
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT,
    first_login INTEGER NOT NULL DEFAULT 1 CHECK (first_login IN (0,1)),
    last_login TEXT
);

CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);

-- =========================
-- APP ACCESS
-- =========================
CREATE TABLE IF NOT EXISTS app_access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    access INTEGER NOT NULL DEFAULT 0 CHECK (access IN (0,1)),
    UNIQUE(username, app_id)
);

CREATE INDEX IF NOT EXISTS idx_app_access_user ON app_access(username);
CREATE INDEX IF NOT EXISTS idx_app_access_app ON app_access(app_id);

-- =========================
-- ANSWERS
-- =========================
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    stage TEXT NOT NULL CHECK (stage IN ('problema','investigacao','solucao','memorial','avaliacao')),
    question_id TEXT NOT NULL,
    answer TEXT,
    correct INTEGER NOT NULL DEFAULT 0 CHECK (correct IN (0,1)),
    timestamp TEXT NOT NULL,
    UNIQUE(username, app_id, stage, question_id)
);

CREATE INDEX IF NOT EXISTS idx_answers_user_app ON answers(username, app_id);
CREATE INDEX IF NOT EXISTS idx_answers_app_stage ON answers(app_id, stage);
CREATE INDEX IF NOT EXISTS idx_answers_question ON answers(app_id, stage, question_id);

-- =========================
-- STAGE UNLOCK
-- =========================
CREATE TABLE IF NOT EXISTS stage_unlock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    app_id TEXT NOT NULL,
    stage TEXT NOT NULL CHECK (stage IN ('problema','investigacao','solucao','memorial','avaliacao')),
    unlocked INTEGER NOT NULL DEFAULT 0 CHECK (unlocked IN (0,1)),
    UNIQUE(username, app_id, stage)
);

CREATE INDEX IF NOT EXISTS idx_stage_unlock_user_app ON stage_unlock(username, app_id);
CREATE INDEX IF NOT EXISTS idx_stage_unlock_app_stage ON stage_unlock(app_id, stage);