# apps/app_05/config.py

from pathlib import Path

APP_ID = "app_05"

APP_TITLE = "Sistemas de Bombeamento de Água"
APP_SUBTITLE = "Eletricidade Aplicada I"

BASE_DIR = Path(__file__).resolve().parent

QUESTIONS_DIR = BASE_DIR / "questions"
RESPONSES_DIR = BASE_DIR / "data" / "responses"

TABS = [
    {"key": "visao_geral", "label": "Disciplina"},
    {"key": "problema", "label": "Desafio"},
    {"key": "investigacao", "label": "Análise"},
    {"key": "solucao", "label": "Entrega"},
    {"key": "memorial", "label": "Memorial Técnico"},
]
