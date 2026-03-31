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
# PAYLOAD BASE
# =========================

def _empty_payload(username: str) -> Dict[str, Any]:
    return {
        "app_id": APP_ID,
        "username": username,
        "responses": {},  # dinâmico agora
    }


# =========================
# LOAD / SAVE
# =========================

def load_user_data(username: str) -> Dict[str, Any]:
    username = _normalize_username(username)

    data = load_app_user_data(username=username, app_id=APP_ID)

    # 🔴 se não existe → cria
    if not isinstance(data, dict):
        data = _empty_payload(username)
        save_app_user_data(username=username, app_id=APP_ID, payload=data)
        return data

    # 🔴 garantir estrutura mínima
    if "responses" not in data or not isinstance(data["responses"], dict):
        data["responses"] = {}

    return data


def get_section_responses(username: str, section: str) -> Dict[str, Any]:
    username = _normalize_username(username)
    section = _normalize_section(section)

    data = load_user_data(username)
    responses = data.get("responses", {})

    if not isinstance(responses, dict):
        return {}

    section_data = responses.get(section, {})

    return section_data if isinstance(section_data, dict) else {}


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
    alternativa_correta: str = "",
) -> Dict[str, Any]:

    username = _normalize_username(username)
    section = _normalize_section(section)
    question_id = str(question_id).strip().lower()

    if not question_id:
        raise ValueError("question_id é obrigatório.")

    if not pergunta:
        pergunta = ""

    # =========================
    # PAYLOAD
    # =========================

    payload: Dict[str, Any] = {
        "tipo": str(question_type).strip().lower(),
        "pergunta": str(pergunta).strip(),
    }

    # -------------------------
    # TEXTO
    # -------------------------
    if question_type == "texto":
        payload["resposta"] = "" if resposta is None else str(resposta).strip()

    # -------------------------
    # MÚLTIPLA ESCOLHA
    # -------------------------
    elif question_type == "multipla_escolha":
        if not isinstance(alternativas, dict):
            alternativas = {}
        payload["alternativas"] = alternativas
        payload["resposta_escolhida"] = (
            "" if resposta is None else str(resposta).strip()
        )
        payload["alternativa_correta"] = str(alternativa_correta).strip()

    else:
        raise ValueError(f"Tipo inválido: {question_type}")

    # =========================
    # SAVE (CORE)
    # =========================

    updated = update_app_user_question_payload(
        username=username,
        app_id=APP_ID,
        section=section,
        question_id=question_id,
        payload=payload,
    )

    # 🔴 garantir estrutura consistente no retorno
    if not isinstance(updated, dict):
        updated = load_user_data(username)

    return updated
