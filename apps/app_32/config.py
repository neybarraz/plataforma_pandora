from __future__ import annotations

from pathlib import Path

APP_ID = "app_31"

APP_TITLE = "Física Clássica Aplicada"
APP_SUBTITLE = "Física II"

BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_DIR = BASE_DIR / "questions"

# Mantido apenas por compatibilidade local.
# A persistência oficial é feita no PostgreSQL via core.app_data.repo.
RESPONSES_DIR = BASE_DIR / "data" / "responses"

TABS = [
    {"key": "problema", "label": "Termodinâmica"},
    # {"key": "investigacao", "label": "Mecânica e Ondas"},
    {"key": "solucao", "label": "Fluidos"},
]

TAB_KEYS = [tab["key"] for tab in TABS]
TAB_LABELS = {tab["key"]: tab["label"] for tab in TABS}
