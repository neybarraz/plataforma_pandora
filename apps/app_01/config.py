# apps/app_01/config.py

from pathlib import Path

APP_ID = "app_01"

APP_TITLE = "Conforto Térmico na Sala"
APP_SUBTITLE = "Fenômenos Térmicos"

BASE_DIR = Path(__file__).resolve().parent

QUESTIONS_DIR = BASE_DIR / "questions"
RESPONSES_DIR = BASE_DIR / "data" / "responses"

# Ordem pedagógica do app
TABS = [
    {"key": "visao_geral", "label": "Disciplina"},
    {"key": "problema", "label": "Problema"},
    {"key": "investigacao", "label": "Investigação"},
    {"key": "solucao", "label": "Solução"},
    {"key": "memorial", "label": "Memorial Técnico"},
    {"key": "avaliacao", "label": "Avaliação"},
]
