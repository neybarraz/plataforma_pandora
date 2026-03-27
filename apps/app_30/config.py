from __future__ import annotations

from pathlib import Path

APP_ID = "app_30"

APP_TITLE = "Backup de Energia em Circuitos Eletrônicos"
APP_SUBTITLE = "Energia de Reserva na Prática"

BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_DIR = BASE_DIR / "questions"

# Mantido apenas por compatibilidade local.
# A persistência oficial é feita no PostgreSQL via core.app_data.repo.
RESPONSES_DIR = BASE_DIR / "data" / "responses"

TABS = [
    # {"key": "visao_geral", "label": "Disciplina"},
    # {"key": "problema", "label": "Elétrico"},
    {"key": "investigacao", "label": "Circuitos"},
    # {"key": "solucao", "label": "Magnetismo"},
]

TAB_KEYS = [tab["key"] for tab in TABS]
TAB_LABELS = {tab["key"]: tab["label"] for tab in TABS}
