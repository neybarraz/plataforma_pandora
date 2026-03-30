from __future__ import annotations

import json
from typing import Any, Dict, List

import streamlit as st

from .config import QUESTIONS_DIR
from .sections.visao_geral.main import render_visao_geral as _render_visao_geral
from .sections.pro import render as render_problema
from .sections.inv import render as render_investigacao
from .sections.sol import render as render_solucao
from .storage import load_user_data, update_answer


def render_visao_geral() -> None:
    _render_visao_geral()


def load_questions(section: str) -> List[Dict[str, Any]]:
    section = str(section).strip()
    path = QUESTIONS_DIR / f"{section}.json"

    if not path.exists():
        st.warning(f"Arquivo de questões não encontrado: {path.name}")
        return []

    try:
        content = path.read_text(encoding="utf-8").strip()

        if not content:
            st.warning(f"O arquivo {path.name} está vazio.")
            return []

        data = json.loads(content)

        if not isinstance(data, list):
            st.warning(f"O arquivo {path.name} deve conter uma lista JSON.")
            return []

        return data

    except json.JSONDecodeError as e:
        st.error(f"JSON inválido em {path.name}: {e}")
        return []

    except Exception as e:
        st.error(f"Erro ao carregar {path.name}: {e}")
        return []


def _widget_key(section: str, qid: str) -> str:
    return f"{section}_{qid}"


def _saved_default(saved_answers: Dict[str, Any], question: Dict[str, Any]) -> Any:
    qid = str(question.get("id", "")).strip()
    if not qid:
        return question.get("default", "")

    if qid in saved_answers:
        return saved_answers.get(qid)

    return question.get("default", "")


def _save_if_changed(
    username: str,
    section: str,
    qid: str,
    value: Any,
    saved_answers: Dict[str, Any],
) -> None:
    previous = saved_answers.get(qid)

    if previous != value:
        update_answer(username, section, qid, value)
        saved_answers[qid] = value


def render_question(
    username: str,
    section: str,
    question: Dict[str, Any],
    saved_answers: Dict[str, Any],
) -> None:
    qid = str(question.get("id", "")).strip()
    label = str(question.get("label", qid)).strip()
    qtype = str(question.get("type", "text")).strip().lower()
    help_text = str(question.get("help", "")).strip()
    options = question.get("options", [])
    default_value = _saved_default(saved_answers, question)

    if not qid:
        st.warning("Questão ignorada porque está sem 'id'.")
        return

    st.markdown(f"**{label}**")
    if help_text:
        st.caption(help_text)

    widget_key = _widget_key(section, qid)

    if qtype == "text":
        value = st.text_input(
            label="",
            value=str(default_value) if default_value is not None else "",
            key=widget_key,
            label_visibility="collapsed",
        )
        _save_if_changed(username, section, qid, value, saved_answers)

    elif qtype == "textarea":
        value = st.text_area(
            label="",
            value=str(default_value) if default_value is not None else "",
            key=widget_key,
            label_visibility="collapsed",
            height=int(question.get("height", 140)),
        )
        _save_if_changed(username, section, qid, value, saved_answers)

    elif qtype == "select":
        if not isinstance(options, list) or not options:
            st.warning(f"A questão '{qid}' não possui opções.")
            return

        index = options.index(default_value) if default_value in options else 0

        value = st.selectbox(
            label="",
            options=options,
            index=index,
            key=widget_key,
            label_visibility="collapsed",
        )
        _save_if_changed(username, section, qid, value, saved_answers)

    elif qtype == "radio":
        if not isinstance(options, list) or not options:
            st.warning(f"A questão '{qid}' não possui opções.")
            return

        index = options.index(default_value) if default_value in options else 0

        value = st.radio(
            label="",
            options=options,
            index=index,
            key=widget_key,
            label_visibility="collapsed",
        )
        _save_if_changed(username, section, qid, value, saved_answers)

    elif qtype == "number":
        try:
            numeric_default = float(default_value)
        except (TypeError, ValueError):
            try:
                numeric_default = float(question.get("default", 0))
            except (TypeError, ValueError):
                numeric_default = 0.0

        value = st.number_input(
            label="",
            value=numeric_default,
            key=widget_key,
            label_visibility="collapsed",
        )
        _save_if_changed(username, section, qid, value, saved_answers)

    elif qtype == "checkbox":
        value = st.checkbox(
            label=question.get("checkbox_label", "Selecionar"),
            value=bool(default_value),
            key=widget_key,
        )
        _save_if_changed(username, section, qid, value, saved_answers)

    else:
        st.warning(f"Tipo de questão não suportado: {qtype}")

    st.divider()


def render_section(
    username: str,
    section: str,
    saved_data: Dict[str, Any] | None = None,
) -> None:
    section = str(section).strip()

    if section == "visao_geral":
        render_visao_geral()
        return

    if section == "problema":
        render_problema(username=username, saved_data=saved_data)
        return

    if section == "investigacao":
        render_investigacao(username=username, saved_data=saved_data)
        return

    if section == "solucao":
        render_solucao(username=username, saved_data=saved_data)
        return

    if not isinstance(saved_data, dict):
        saved_data = load_user_data(username)

    questions = load_questions(section)
    answers = saved_data.get("responses", {}).get(section, {})

    if not isinstance(answers, dict):
        answers = {}

    if not questions:
        st.info(f"Nenhuma questão disponível para '{section}'.")
        return

    for question in questions:
        if not isinstance(question, dict):
            continue

        render_question(
            username=username,
            section=section,
            question=question,
            saved_answers=answers,
        )