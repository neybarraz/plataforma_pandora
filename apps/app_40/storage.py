from __future__ import annotations

from typing import Any, Dict
from .config import APP_ID
from core.app_data.repo import (
    load_app_user_data,
    save_app_user_data,
    update_app_user_question_payload,
)


# =========================
# BASE
# =========================

def _normalize_username(username: str) -> str:
    username = str(username).strip()
    if not username:
        raise ValueError("username é obrigatório.")
    return username


def _normalize_section(section: str) -> str:
    section = str(section).strip()
    if not section:
        raise ValueError("section é obrigatório.")
    return section


# =========================
# LOAD / SAVE
# =========================

def load_user_data(username: str) -> Dict[str, Any]:
    username = _normalize_username(username)

    data = load_app_user_data(username=username, app_id=APP_ID)

    if not isinstance(data, dict):
        data = {
            "app_id": APP_ID,
            "username": username,
            "responses": {},
        }
        save_app_user_data(username=username, app_id=APP_ID, payload=data)

    return data


def get_section_responses(username: str, section: str) -> Dict[str, Any]:
    username = _normalize_username(username)
    section = _normalize_section(section)

    data = load_user_data(username)
    responses = data.get("responses", {})

    if not isinstance(responses, dict):
        return {}

    return responses.get(section, {})


# =========================
# SAVE RESPOSTA
# =========================

def save_question_response(
    username: str,
    section: str,
    question_id: str,
    *,
    question_type: str,
    pergunta: str,
    resposta: Any = "",
    alternativas: dict[str, Any] | None = None,
) -> Dict[str, Any]:

    username = _normalize_username(username)
    section = _normalize_section(section)
    question_id = str(question_id).strip().lower()

    if not question_id:
        raise ValueError("question_id é obrigatório.")

    payload: Dict[str, Any] = {
        "question_id": question_id,
        "tipo": question_type,
        "pergunta": str(pergunta).strip(),
    }

    if question_type == "texto":
        payload["resposta"] = "" if resposta is None else str(resposta).strip()

    elif question_type == "multipla_escolha":
        payload["alternativas"] = alternativas or {}
        payload["resposta"] = "" if resposta is None else str(resposta).strip()

    else:
        raise ValueError(f"Tipo inválido: {question_type}")

    updated = update_app_user_question_payload(
        username=username,
        app_id=APP_ID,
        section=section,
        question_id=question_id,
        payload=payload,
    )

    return updated