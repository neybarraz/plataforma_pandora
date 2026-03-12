# apps/app_05/config.py
from pathlib import Path

APP_ID = "app_05"

APP_TITLE = "Sistema de Backup: como funciona?"
APP_SUBTITLE = "Energia de Reserva na Prática"

BASE_DIR = Path(__file__).resolve().parent

QUESTIONS_DIR = BASE_DIR / "questions"
RESPONSES_DIR = BASE_DIR / "data" / "responses"

DEFAULT_STAGE_KEY = "visao_geral"

# Ordem pedagógica do app
TABS = [
    {"key": "visao_geral", "label": "Disciplina"},
    {"key": "problema", "label": "Desafio"},
    {"key": "investigacao", "label": "Análise"},
    {"key": "solucao", "label": "Explicação"},
    {"key": "memorial", "label": "Memorial Técnico"},
]