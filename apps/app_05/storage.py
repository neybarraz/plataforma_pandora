# apps/app_05/storage.py

from copy import deepcopy
from typing import Any, Dict

from apps.app_05.config import APP_ID, TABS
from core.app_data.repo import (
    load_app_user_data,
    save_app_user_data,
    update_app_user_path,
    update_app_user_question_payload,
)


def empty_payload(username: str) -> Dict[str, Any]:
    return {
        "app_id": APP_ID,
        "username": username,
        "responses": {tab["key"]: {} for tab in TABS},
        "meta": {
            "status": "em_andamento"
        },
    }


def _normalize_payload(username: str, data: Dict[str, Any] | None) -> Dict[str, Any]:
    base = empty_payload(username)

    if not isinstance(data, dict):
        return base

    merged = deepcopy(base)

    meta = data.get("meta", {})
    if isinstance(meta, dict):
        merged["meta"] = meta

    responses = data.get("responses", {})
    if isinstance(responses, dict):
        merged["responses"] = base["responses"] | responses

    merged["app_id"] = APP_ID
    merged["username"] = username

    return merged


def load_user_data(username: str) -> Dict[str, Any]:
    data = load_app_user_data(username=username, app_id=APP_ID)

    if data is None:
        data = empty_payload(username)
        save_app_user_data(username=username, app_id=APP_ID, payload=data)
        return data

    normalized = _normalize_payload(username=username, data=data)

    # garante que a estrutura mínima esteja consistente no banco
    if normalized != data:
        save_app_user_data(username=username, app_id=APP_ID, payload=normalized)

    return normalized


def save_user_data(username: str, data: Dict[str, Any]) -> None:
    normalized = _normalize_payload(username=username, data=data)
    save_app_user_data(username=username, app_id=APP_ID, payload=normalized)


def update_answer(username: str, section: str, field_name: str, value: Any) -> Dict[str, Any]:
    section = str(section).strip()
    field_name = str(field_name).strip()

    if not section:
        raise ValueError("section é obrigatório.")
    if not field_name:
        raise ValueError("field_name é obrigatório.")

    updated = update_app_user_path(
        username=username,
        app_id=APP_ID,
        path=["responses", section, field_name],
        value=value,
    )

    return _normalize_payload(username=username, data=updated)


def update_question_payload(
    username: str,
    section: str,
    question_id: str,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    section = str(section).strip()
    question_id = str(question_id).strip()

    if not section:
        raise ValueError("section é obrigatório.")
    if not question_id:
        raise ValueError("question_id é obrigatório.")
    if not isinstance(payload, dict):
        raise ValueError("payload deve ser um dict.")

    updated = update_app_user_question_payload(
        username=username,
        app_id=APP_ID,
        section=section,
        question_id=question_id,
        payload=payload,
    )

    return _normalize_payload(username=username, data=updated)


def get_problem_stats(username: str) -> Dict[str, int]:
    data = load_user_data(username)
    problema = data.get("responses", {}).get("problema", {})

    if not isinstance(problema, dict):
        return {"total_questoes": 0, "respondidas": 0}

    total = 0
    respondidas = 0

    for _, item in problema.items():
        if not isinstance(item, dict):
            continue

        tipo = item.get("tipo")
        total += 1

        if tipo == "texto" and str(item.get("resposta", "")).strip():
            respondidas += 1
        elif tipo == "multipla_escolha" and str(item.get("resposta_escolhida", "")).strip():
            respondidas += 1

    return {
        "total_questoes": total,
        "respondidas": respondidas,
    }
