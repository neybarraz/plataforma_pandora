# apps/app_02/config.py

from pathlib import Path

APP_ID = "app_02"

APP_TITLE = "Sistemas de Bombeamento de Água"
APP_SUBTITLE = "Eletricidade Aplicada I"

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
