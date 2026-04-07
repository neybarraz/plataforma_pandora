from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict
from .config import APP_ID, TABS
from core.app_data.repo import (
    load_app_user_data,
    save_app_user_data,
    update_app_user_path,
    update_app_user_question_payload,
)
import re

QUESTION_TYPE_TEXTO = "texto"
QUESTION_TYPE_MULTIPLA_ESCOLHA = "multipla_escolha"

VALID_QUESTION_TYPES = {
    QUESTION_TYPE_TEXTO,
    QUESTION_TYPE_MULTIPLA_ESCOLHA,
}

QUESTION_ID_RE = re.compile(
    r"^(?P<etapa>[a-z0-9-]+)\.(?P<pagina>\d{2})\.(?P<conteudo>\d{3})\.(?P<numero>\d{4})$"
)

def _normalize_username(username: str) -> str:
    username = str(username).strip()
    if not username:
        raise ValueError("username é obrigatório.")
    return username


def _section_keys() -> set[str]:
    keys: set[str] = set()

    for tab in TABS:
        if not isinstance(tab, dict):
            continue

        key = str(tab.get("key", "")).strip()
        if key:
            keys.add(key)

    return keys


def _validate_section(section: str) -> str:
    section = str(section).strip()
    if not section:
        raise ValueError("section é obrigatório.")

    valid_sections = _section_keys()
    if valid_sections and section not in valid_sections:
        raise ValueError(
            f"section inválido: '{section}'. Válidos: {sorted(valid_sections)}"
        )

    return section


def build_question_id(
    etapa: str,
    pagina: int | str,
    conteudo: int | str,
    tipo: str,
    numero: int | str,
) -> str:
    """
    Padrão oficial do question_id:

        <etapa>.<pagina>.<conteudo>.<numero>

    Exemplos:
        problema.01.003.0001
        investigacao.02.001.0004
        visao-geral.01.002.0003

    Observações:
    - o parâmetro `tipo` foi mantido na assinatura apenas por compatibilidade
      com chamadas existentes, mas ele não entra mais no ID;
    - a etapa é normalizada para slug com hífen.
    """
    etapa = str(etapa).strip().lower()

    etapa_slug = etapa.replace("_", "-").replace(" ", "-")
    etapa_slug = re.sub(r"-+", "-", etapa_slug).strip("-")

    if not etapa_slug:
        raise ValueError("etapa inválida para build_question_id.")

    pagina_str = str(pagina).strip().zfill(2)
    conteudo_str = str(conteudo).strip().zfill(3)
    numero_str = str(numero).strip().zfill(4)

    if not pagina_str.isdigit():
        raise ValueError("pagina deve ser numérica.")
    if not conteudo_str.isdigit():
        raise ValueError("conteudo deve ser numérico.")
    if not numero_str.isdigit():
        raise ValueError("numero deve ser numérico.")

    return f"{etapa_slug}.{pagina_str}.{conteudo_str}.{numero_str}"

def _normalize_question_id(question_id: str) -> str:
    question_id = str(question_id).strip()
    if not question_id:
        raise ValueError("question_id é obrigatório.")
    return question_id.lower()

def _normalize_question_type(question_type: str) -> str:
    question_type = str(question_type).strip()

    if question_type not in VALID_QUESTION_TYPES:
        raise ValueError(
            f"question_type inválido: '{question_type}'. "
            f"Válidos: {sorted(VALID_QUESTION_TYPES)}"
        )

    return question_type


def _normalize_pergunta(pergunta: str) -> str:
    pergunta = str(pergunta).strip()
    if not pergunta:
        raise ValueError("pergunta é obrigatória.")
    return pergunta


def _normalize_meta(meta: dict[str, Any] | None) -> dict[str, Any]:
    return deepcopy(meta) if isinstance(meta, dict) else {}



def parse_question_id(question_id: str) -> dict[str, str]:
    question_id = _normalize_question_id(question_id)
    match = QUESTION_ID_RE.match(question_id)

    if not match:
        return {
            "raw": question_id,
            "etapa": "",
            "pagina": "",
            "conteudo": "",
            "tipo_id": "",
            "numero": "",
            "valido": "0",
        }

    parts = match.groupdict()

    return {
        "raw": question_id,
        "etapa": parts["etapa"],
        "pagina": parts["pagina"],
        "conteudo": parts["conteudo"],
        "tipo_id": "",
        "numero": parts["numero"],
        "valido": "1",
    }

def empty_payload(username: str) -> Dict[str, Any]:
    username = _normalize_username(username)

    return {
        "app_id": APP_ID,
        "username": username,
        "responses": {
            tab["key"]: {}
            for tab in TABS
            if isinstance(tab, dict) and tab.get("key")
        },
        "meta": {
            "status": "em_andamento",
        },
    }


def _normalize_payload(
    username: str,
    data: Dict[str, Any] | None,
) -> Dict[str, Any]:
    username = _normalize_username(username)
    base = empty_payload(username)

    if not isinstance(data, dict):
        return base

    merged = deepcopy(base)

    incoming_meta = data.get("meta", {})
    if isinstance(incoming_meta, dict):
        merged["meta"] = deepcopy(incoming_meta)

    incoming_responses = data.get("responses", {})
    if isinstance(incoming_responses, dict):
        for section_key, section_value in incoming_responses.items():
            if section_key not in merged["responses"]:
                merged["responses"][section_key] = {}

            if isinstance(section_value, dict):
                merged["responses"][section_key] = deepcopy(section_value)

    merged["app_id"] = APP_ID
    merged["username"] = username

    return merged


def _persist_if_changed(
    username: str,
    data: Dict[str, Any],
    original: Any,
) -> Dict[str, Any]:
    if data != original:
        save_app_user_data(username=username, app_id=APP_ID, payload=data)
    return data


def load_user_data(username: str) -> Dict[str, Any]:
    username = _normalize_username(username)

    data = load_app_user_data(username=username, app_id=APP_ID)

    if data is None:
        created = empty_payload(username)
        save_app_user_data(username=username, app_id=APP_ID, payload=created)
        return created

    normalized = _normalize_payload(username=username, data=data)
    return _persist_if_changed(username=username, data=normalized, original=data)


def save_user_data(username: str, data: Dict[str, Any]) -> None:
    username = _normalize_username(username)
    normalized = _normalize_payload(username=username, data=data)
    save_app_user_data(username=username, app_id=APP_ID, payload=normalized)


def get_all_responses(username: str) -> Dict[str, Any]:
    username = _normalize_username(username)
    data = load_user_data(username)

    responses = data.get("responses", {})
    return responses if isinstance(responses, dict) else {}


def get_section_responses(username: str, section: str) -> Dict[str, Any]:
    username = _normalize_username(username)
    section = _validate_section(section)

    responses = get_all_responses(username)
    section_data = responses.get(section, {})
    return section_data if isinstance(section_data, dict) else {}


def get_question_payload(
    username: str,
    section: str,
    question_id: str,
) -> Dict[str, Any]:
    username = _normalize_username(username)
    section = _validate_section(section)
    question_id = _normalize_question_id(question_id)

    section_data = get_section_responses(username, section)
    item = section_data.get(question_id, {})
    return item if isinstance(item, dict) else {}


def update_answer(
    username: str,
    section: str,
    field_name: str,
    value: Any,
) -> Dict[str, Any]:
    """
    Compatibilidade com campos simples/legados.
    """
    username = _normalize_username(username)
    section = _validate_section(section)
    field_name = str(field_name).strip()

    if not field_name:
        raise ValueError("field_name é obrigatório.")

    updated = update_app_user_path(
        username=username,
        app_id=APP_ID,
        path=["responses", section, field_name],
        value=value,
    )

    normalized = _normalize_payload(username=username, data=updated)
    return _persist_if_changed(username=username, data=normalized, original=updated)


def normalize_question_payload(
    question_id: str,
    payload: Dict[str, Any],
    *,
    section: str | None = None,
) -> Dict[str, Any]:
    question_id = _normalize_question_id(question_id)

    if not isinstance(payload, dict):
        raise ValueError("payload deve ser um dict.")

    tipo = _normalize_question_type(payload.get("tipo", ""))
    pergunta = _normalize_pergunta(payload.get("pergunta", ""))
    meta = _normalize_meta(payload.get("meta"))

    parsed_id = parse_question_id(question_id)

    normalized: Dict[str, Any] = {
        "question_id": question_id,
        "tipo": tipo,
        "pergunta": pergunta,
        "meta": {
            **meta,
            "app_id": APP_ID,
            "section": section or meta.get("section", ""),
            "id_info": parsed_id,
        },
    }

    if tipo == QUESTION_TYPE_TEXTO:
        normalized["resposta"] = str(payload.get("resposta", "")).strip()
        return normalized

    if tipo == QUESTION_TYPE_MULTIPLA_ESCOLHA:
        alternativas = payload.get("alternativas", {})
        if not isinstance(alternativas, dict):
            alternativas = {}

        resposta_escolhida = payload.get("resposta_escolhida", "")

        if isinstance(resposta_escolhida, list):
            resposta_normalizada = [
                str(item).strip()
                for item in resposta_escolhida
                if str(item).strip()
            ]
        else:
            resposta_normalizada = str(resposta_escolhida).strip()

        normalized["alternativas"] = deepcopy(alternativas)
        normalized["resposta_escolhida"] = resposta_normalizada
        normalized["alternativa_correta"] = str(
            payload.get("alternativa_correta", "")
        ).strip()
        return normalized

    raise ValueError(f"Tipo de payload não suportado: {tipo}")


def update_question_payload(
    username: str,
    section: str,
    question_id: str,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Compatível com a chamada atual, mas agora já normaliza o payload
    no padrão universal antes de persistir.
    """
    username = _normalize_username(username)
    section = _validate_section(section)
    question_id = _normalize_question_id(question_id)

    normalized_payload = normalize_question_payload(
        question_id=question_id,
        payload=payload,
        section=section,
    )

    updated = update_app_user_question_payload(
        username=username,
        app_id=APP_ID,
        section=section,
        question_id=question_id,
        payload=normalized_payload,
    )

    normalized = _normalize_payload(username=username, data=updated)
    return _persist_if_changed(username=username, data=normalized, original=updated)


def save_text_question(
    username: str,
    section: str,
    question_id: str,
    pergunta: str,
    resposta: Any,
    *,
    meta: dict[str, Any] | None = None,
) -> Dict[str, Any]:
    payload = {
        "tipo": QUESTION_TYPE_TEXTO,
        "pergunta": pergunta,
        "resposta": "" if resposta is None else str(resposta).strip(),
        "meta": _normalize_meta(meta),
    }

    return update_question_payload(
        username=username,
        section=section,
        question_id=question_id,
        payload=payload,
    )

def save_mcq_question(
    username: str,
    section: str,
    question_id: str,
    pergunta: str,
    alternativas: dict[str, Any],
    resposta_escolhida: Any,
    *,
    alternativa_correta: str = "",
    meta: dict[str, Any] | None = None,
) -> Dict[str, Any]:
    if isinstance(resposta_escolhida, list):
        resposta_normalizada = [
            str(item).strip()
            for item in resposta_escolhida
            if str(item).strip()
        ]
    else:
        resposta_normalizada = (
            "" if resposta_escolhida is None else str(resposta_escolhida).strip()
        )

    payload = {
        "tipo": QUESTION_TYPE_MULTIPLA_ESCOLHA,
        "pergunta": pergunta,
        "alternativas": deepcopy(alternativas) if isinstance(alternativas, dict) else {},
        "resposta_escolhida": resposta_normalizada,
        "alternativa_correta": str(alternativa_correta).strip(),
        "meta": _normalize_meta(meta),
    }

    return update_question_payload(
        username=username,
        section=section,
        question_id=question_id,
        payload=payload,
    )


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
    meta: dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Porta única para qualquer módulo chamar o salvamento estruturado.
    """
    question_type = _normalize_question_type(question_type)

    if question_type == QUESTION_TYPE_TEXTO:
        return save_text_question(
            username=username,
            section=section,
            question_id=question_id,
            pergunta=pergunta,
            resposta=resposta,
            meta=meta,
        )

    if question_type == QUESTION_TYPE_MULTIPLA_ESCOLHA:
        return save_mcq_question(
            username=username,
            section=section,
            question_id=question_id,
            pergunta=pergunta,
            alternativas=alternativas or {},
            resposta_escolhida=resposta,
            alternativa_correta=alternativa_correta,
            meta=meta,
        )

    raise ValueError(f"Tipo de questão não suportado: {question_type}")

def _is_answered_question_payload(item: Any) -> bool:
    if not isinstance(item, dict):
        return False

    tipo = str(item.get("tipo", "")).strip()

    if tipo == QUESTION_TYPE_TEXTO:
        return bool(str(item.get("resposta", "")).strip())

    if tipo == QUESTION_TYPE_MULTIPLA_ESCOLHA:
        resposta = item.get("resposta_escolhida", "")

        if isinstance(resposta, list):
            return any(str(op).strip() for op in resposta)

        return bool(str(resposta).strip())

    return False


def get_section_stats(username: str, section: str) -> Dict[str, int]:
    username = _normalize_username(username)
    section = _validate_section(section)

    section_data = get_section_responses(username, section)

    total = 0
    respondidas = 0

    for _, item in section_data.items():
        if not isinstance(item, dict):
            continue

        total += 1

        if _is_answered_question_payload(item):
            respondidas += 1

    return {
        "total_questoes": total,
        "respondidas": respondidas,
    }


def get_problem_stats(username: str) -> Dict[str, int]:
    return get_section_stats(username, "problema")


def get_investigacao_stats(username: str) -> Dict[str, int]:
    return get_section_stats(username, "investigacao")


def get_solucao_stats(username: str) -> Dict[str, int]:
    return get_section_stats(username, "solucao")
