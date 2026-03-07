# apps/app_02/storage.py
import json
import os
import time
import uuid
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict

from apps.app_02.config import APP_ID, RESPONSES_DIR, TABS


def ensure_response_dir() -> None:
    RESPONSES_DIR.mkdir(parents=True, exist_ok=True)


def build_filename(username: str) -> str:
    safe_username = str(username).strip().lower().replace(" ", "_")
    return f"{safe_username}_{APP_ID}.json"


def build_filepath(username: str) -> Path:
    ensure_response_dir()
    return RESPONSES_DIR / build_filename(username)


def empty_payload(username: str) -> Dict[str, Any]:
    return {
        "app_id": APP_ID,
        "username": username,
        "responses": {tab["key"]: {} for tab in TABS},
        "meta": {
            "status": "em_andamento"
        }
    }


def load_user_data(username: str) -> Dict[str, Any]:
    path = build_filepath(username)

    if not path.exists():
        data = empty_payload(username)
        save_user_data(username, data)
        return data

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        data = empty_payload(username)
        save_user_data(username, data)
        return data

    base = empty_payload(username)
    merged = deepcopy(base)
    merged["meta"] = data.get("meta", base["meta"])
    merged["responses"] = base["responses"] | data.get("responses", {})
    return merged


def save_user_data(username: str, data: Dict[str, Any]) -> None:
    path = build_filepath(username)
    ensure_response_dir()

    tmp_path = path.with_suffix(f".{uuid.uuid4().hex}.tmp")

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())

    last_error = None
    for attempt in range(6):
        try:
            os.replace(tmp_path, path)
            return
        except PermissionError as exc:
            last_error = exc
            time.sleep(0.08 * (attempt + 1))

    try:
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
    except Exception:
        pass

    raise last_error


def update_answer(username: str, section: str, field_name: str, value: Any) -> Dict[str, Any]:
    data = load_user_data(username)
    data["responses"].setdefault(section, {})
    data["responses"][section][field_name] = value
    save_user_data(username, data)
    return data


def update_question_payload(
    username: str,
    section: str,
    question_id: str,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    data = load_user_data(username)
    data["responses"].setdefault(section, {})
    data["responses"][section][question_id] = payload
    save_user_data(username, data)
    return data


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