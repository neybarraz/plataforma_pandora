# apps/app_05/renderer.py
import json
from typing import Any, Dict, List

import streamlit as st

from apps.app_05.config import QUESTIONS_DIR
from apps.app_05.sections.visao_geral.main import render_visao_geral as _render_visao_geral
from apps.app_05.storage import update_answer


def render_visao_geral() -> None:
    _render_visao_geral()


def load_questions(section: str) -> List[Dict[str, Any]]:
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


def render_question(
    username: str,
    section: str,
    question: Dict[str, Any],
    saved_answers: Dict[str, Any],
) -> None:
    qid = question.get("id", "")
    label = question.get("label", qid)
    qtype = question.get("type", "text")
    help_text = question.get("help", "")
    options = question.get("options", [])
    default_value = saved_answers.get(qid, question.get("default", ""))

    if not qid:
        st.warning("Questão ignorada porque está sem 'id'.")
        return

    st.markdown(f"**{label}**")
    if help_text:
        st.caption(help_text)

    widget_key = f"{section}_{qid}"

    if qtype == "text":
        value = st.text_input(
            label="",
            value=str(default_value),
            key=widget_key,
            label_visibility="collapsed",
        )
        update_answer(username, section, qid, value)

    elif qtype == "textarea":
        value = st.text_area(
            label="",
            value=str(default_value),
            key=widget_key,
            label_visibility="collapsed",
            height=140,
        )
        update_answer(username, section, qid, value)

    elif qtype == "select":
        if not options:
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
        update_answer(username, section, qid, value)

    elif qtype == "radio":
        if not options:
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
        update_answer(username, section, qid, value)

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
        update_answer(username, section, qid, value)

    elif qtype == "checkbox":
        value = st.checkbox(
            label=question.get("checkbox_label", "Selecionar"),
            value=bool(default_value),
            key=widget_key,
        )
        update_answer(username, section, qid, value)

    else:
        st.warning(f"Tipo de questão não suportado: {qtype}")

    st.divider()


def render_section(username: str, section: str, saved_data: Dict[str, Any]) -> None:
    questions = load_questions(section)
    answers = saved_data.get("responses", {}).get(section, {})

    if not questions:
        st.info(f"Nenhuma questão disponível para '{section}'.")
        return

    for question in questions:
        render_question(
            username=username,
            section=section,
            question=question,
            saved_answers=answers,
        )