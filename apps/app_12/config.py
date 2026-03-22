from __future__ import annotations

from pathlib import Path

APP_ID = "app_12"

APP_TITLE = "Sistemas de Bombeamento de Água"
APP_SUBTITLE = "Soluções em Dimensionamento de Fios"

BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_DIR = BASE_DIR / "questions"

# Mantido apenas por compatibilidade local.
# A persistência oficial é feita no PostgreSQL via core.app_data.repo.
RESPONSES_DIR = BASE_DIR / "data" / "responses"

TABS = [
    {"key": "visao_geral", "label": "Disciplina"},
    {"key": "problema", "label": "Desafio"},
    {"key": "investigacao", "label": "Análise"},
    {"key": "solucao", "label": "Entrega"},
    {"key": "memorial", "label": "Memorial Técnico"},
]

TAB_KEYS = [tab["key"] for tab in TABS]
TAB_LABELS = {tab["key"]: tab["label"] for tab in TABS}