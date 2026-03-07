# apps/app_02/sections/problema/problema.py

from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st

from apps.app_02.sections.problema.conteudos.catalogo import get_conteudos
from apps.app_02.storage import (
    get_problem_stats,
    load_user_data,
    update_question_payload,
)


AUTOSAVE_INTERVAL_S = 20
APP_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = APP_DIR / "assets"


# -----------------------------
# UTILIDADES VISUAIS
# -----------------------------

def _titulo_destaque(texto: str, nivel: int = 2) -> None:
    tamanhos = {1: "2.2rem", 2: "1.8rem", 3: "1.35rem", 4: "1.1rem"}
    tamanho = tamanhos.get(nivel, "1.2rem")

    st.markdown(
        f"""
        <div style="
            font-size:{tamanho};
            font-weight:700;
            color:#14B8A6;
            margin-top:0.6rem;
            margin-bottom:0.8rem;
        ">
            {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _texto_justificado(texto: str) -> None:
    st.markdown(
        f"""
        <div style="text-align:justify; line-height:1.65;">
            {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _status_salvamento() -> None:
    ultimo = st.session_state.get("problema_last_save_label", "Ainda não salvo")
    dirty = st.session_state.get("problema_dirty", False)

    if dirty:
        msg = "● Alterações pendentes"
        cor = "#f59e0b"
    else:
        msg = f"✓ {ultimo}"
        cor = "#22c55e"

    st.markdown(
        f"""
        <div style="
            margin-top:1rem;
            padding:0.55rem 0.8rem;
            border:1px solid #e5e7eb;
            border-radius:10px;
            font-size:0.92rem;
            color:{cor};
            background:#fafafa;
        ">
            {msg}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _flash_style(saved_ids: set[str]) -> None:
    return


def _menu_conteudos_style() -> None:
    st.markdown(
        """
        <style>
        div[data-testid="stButton"] > button {
            text-align: left !important;
            justify-content: flex-start !important;
            white-space: normal !important;
            word-break: break-word !important;
            padding: 0.40rem 0.40rem 0.40rem 0.40rem !important;
            border-radius: 10px !important;
            min-height: auto !important;
        }

        div[data-testid="stButton"] > button p {
            font-size: 0.68rem !important;
            line-height: 1.15 !important;
            margin: 0 !important;
            text-align: left !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _show_image(filename: str, caption: str = "") -> None:
    image_path = ASSETS_DIR / filename

    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: {image_path}")


# -----------------------------
# ESTADO / DADOS
# -----------------------------

def _resolve_username(
    username: str | None = None,
    ctx: dict[str, Any] | None = None,
) -> str:
    if isinstance(username, str) and username.strip():
        return username.strip()

    if ctx and ctx.get("username"):
        return str(ctx["username"]).strip()

    auth_user = st.session_state.get("auth_user")
    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        auth_username = auth_user.get("username")
        if isinstance(auth_username, str) and auth_username.strip():
            return auth_username.strip()

    return "anonimo"


def _extract_problema_answers(data: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(data, dict):
        return {}

    responses = data.get("responses", {})
    if not isinstance(responses, dict):
        return {}

    problema = responses.get("problema", {})
    if not isinstance(problema, dict):
        return {}

    return problema


def _get_saved_widget_value(item: Any) -> Any:
    if isinstance(item, dict):
        if item.get("tipo") == "texto":
            return item.get("resposta", "")
        if item.get("tipo") == "multipla_escolha":
            return item.get("resposta_escolhida", "")
        if "value" in item:
            return item.get("value", "")
    return item if item is not None else ""


def _ensure_state(username: str) -> None:
    if "problema_username" not in st.session_state:
        st.session_state.problema_username = username

    if "problema_dirty" not in st.session_state:
        st.session_state.problema_dirty = False

    if "problema_saved_ids" not in st.session_state:
        st.session_state.problema_saved_ids = set()

    if "problema_last_save_label" not in st.session_state:
        st.session_state.problema_last_save_label = "Ainda não salvo"

    data = load_user_data(username)
    st.session_state.problema_data_cache = data


def _hydrate_widgets_from_file(username: str, conteudo: dict[str, Any], *, overwrite: bool = False) -> None:
    data = load_user_data(username)
    st.session_state.problema_data_cache = data
    problema_answers = _extract_problema_answers(data)

    for bloco in conteudo["blocos"]:
        if bloco["tipo"] not in {"questao_texto", "questao_multipla_escolha"}:
            continue

        qid = bloco["id"]
        widget_key = f"widget_{qid}"

        if qid not in problema_answers:
            continue

        if (not overwrite) and (widget_key in st.session_state):
            continue

        valor = _get_saved_widget_value(problema_answers[qid])

        if bloco["tipo"] == "questao_multipla_escolha":
            opcoes = list(bloco["alternativas"].keys())
            if valor not in opcoes:
                valor = None

        st.session_state[widget_key] = valor


def _mark_dirty() -> None:
    st.session_state.problema_dirty = True


def _get_widget_value(questao_id: str, default: Any = "") -> Any:
    return st.session_state.get(f"widget_{questao_id}", default)


# -----------------------------
# SALVAMENTO
# -----------------------------

def _save_question(username: str, bloco: dict[str, Any]) -> None:
    questao_id = bloco["id"]

    if bloco["tipo"] == "questao_texto":
        resposta = str(_get_widget_value(questao_id, "")).strip()
        payload = {
            "tipo": "texto",
            "pergunta": bloco["pergunta"],
            "resposta": resposta,
        }
        update_question_payload(
            username=username,
            section="problema",
            question_id=questao_id,
            payload=payload,
        )

    elif bloco["tipo"] == "questao_multipla_escolha":
        resposta = _get_widget_value(questao_id, None)
        resposta = "" if resposta is None else str(resposta).strip()

        payload = {
            "tipo": "multipla_escolha",
            "pergunta": bloco["pergunta"],
            "alternativas": deepcopy(bloco["alternativas"]),
            "resposta_escolhida": resposta,
            "alternativa_correta": bloco["alternativa_correta"],
        }
        update_question_payload(
            username=username,
            section="problema",
            question_id=questao_id,
            payload=payload,
        )


def _question_blocks_from_conteudo(conteudo: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        bloco
        for bloco in conteudo["blocos"]
        if bloco["tipo"] in {"questao_texto", "questao_multipla_escolha"}
    ]


def _save_conteudo_if_dirty(username: str, conteudo: dict[str, Any]) -> None:
    if not st.session_state.get("problema_dirty", False):
        return

    saved_ids = set()

    for bloco in _question_blocks_from_conteudo(conteudo):
        _save_question(username, bloco)
        saved_ids.add(bloco["id"])

    st.session_state.problema_dirty = False
    st.session_state.problema_saved_ids = saved_ids
    st.session_state.problema_last_save_label = (
        f"Salvo às {datetime.now().strftime('%H:%M:%S')}"
    )
    st.session_state.problema_data_cache = load_user_data(username)


# -----------------------------
# AUTOSAVE
# -----------------------------

@st.fragment(run_every=f"{AUTOSAVE_INTERVAL_S}s")
def _autosave_fragment(username: str, conteudo: dict[str, Any]) -> None:
    _save_conteudo_if_dirty(username, conteudo)


# -----------------------------
# RENDER DE BLOCOS
# -----------------------------

def _render_bloco(bloco: dict[str, Any]) -> None:
    tipo = bloco["tipo"]

    if tipo == "titulo":
        _titulo_destaque(bloco["texto"], nivel=2)
        return

    if tipo == "subtitulo":
        _titulo_destaque(bloco["texto"], nivel=3)
        return

    if tipo == "texto":
        _texto_justificado(bloco["texto"])
        return

    if tipo == "video":
        st.video(bloco["url"])
        if bloco.get("caption"):
            st.caption(bloco["caption"])
        return

    if tipo == "imagem":
        _show_image(
            filename=bloco["arquivo"],
            caption=bloco.get("caption", ""),
        )
        return

    if tipo == "questao_texto":
        questao_id = bloco["id"]

        st.markdown(f"{bloco['pergunta']}")

        st.text_area(
            label="Sua resposta",
            key=f"widget_{questao_id}",
            height=bloco.get("altura", 160),
            placeholder=bloco.get("placeholder", ""),
            on_change=_mark_dirty,
            label_visibility="visible",
        )
        return

    if tipo == "questao_multipla_escolha":
        questao_id = bloco["id"]
        alternativas = bloco["alternativas"]
        opcoes = list(alternativas.keys())
        widget_key = f"widget_{questao_id}"

        valor_atual = st.session_state.get(widget_key, None)
        if valor_atual not in opcoes:
            st.session_state[widget_key] = None

        st.markdown(f"{bloco['pergunta']}")

        def _fmt(x: str) -> str:
            return f"{x}) {alternativas[x]}"

        st.radio(
            label="Escolha uma alternativa",
            options=opcoes,
            format_func=_fmt,
            key=widget_key,
            index=None,
            horizontal=False,
            on_change=_mark_dirty,
            label_visibility="visible",
        )
        return


def _render_conteudo(conteudo: dict[str, Any]) -> None:
    for bloco in conteudo["blocos"]:
        _render_bloco(bloco)
        st.markdown("<div style='margin-bottom:0.8rem;'></div>", unsafe_allow_html=True)


def _barra_resumo(username: str) -> None:
    stats = get_problem_stats(username)
    total = stats.get("total_questoes", 0)
    respondidas = stats.get("respondidas", 0)
    progresso = 0.0 if total == 0 else respondidas / total

    st.progress(progresso)
    st.caption(f"Questões respondidas: {respondidas}/{total}")


# -----------------------------
# RENDER PRINCIPAL
# -----------------------------

def render(
    username: str | None = None,
    saved_data: dict[str, Any] | None = None,
    ctx: dict[str, Any] | None = None,
) -> None:
    del saved_data

    username = _resolve_username(username=username, ctx=ctx)
    _ensure_state(username)

    conteudos = get_conteudos()

    if not conteudos:
        st.info("Nenhum conteúdo foi configurado para a etapa Problema.")
        return

    if "problema_conteudo_idx" not in st.session_state:
        st.session_state.problema_conteudo_idx = 0

    idx = st.session_state.problema_conteudo_idx
    idx = max(0, min(idx, len(conteudos) - 1))
    st.session_state.problema_conteudo_idx = idx

    conteudo_atual = conteudos[idx]

    # lê o arquivo primeiro e hidrata o conteúdo atual
    _hydrate_widgets_from_file(username, conteudo_atual, overwrite=False)

    _autosave_fragment(username, conteudo_atual)

    _barra_resumo(username)
    st.markdown("---")

    col_menu, col_main = st.columns([0.9, 2.55], gap="small")

    with col_menu:
        _menu_conteudos_style()
        st.markdown("**Conteúdos**")

        for i, item in enumerate(conteudos):
            label = item.get("titulo_menu", item.get("titulo", item["id"]))

            if st.button(
                label,
                key=f"problema_menu_{item['id']}",
                use_container_width=True,
                type="primary" if i == idx else "secondary",
            ):
                _save_conteudo_if_dirty(username, conteudo_atual)
                st.session_state.problema_conteudo_idx = i
                _hydrate_widgets_from_file(username, conteudos[i], overwrite=True)
                st.rerun()

    with col_main:
        _flash_style(st.session_state.get("problema_saved_ids", set()))
        _render_conteudo(conteudo_atual)
        _status_salvamento()

        # st.markdown("---")
        # if st.button(
        #     "Salvar respostas deste conteúdo",
        #     type="primary",
        #     use_container_width=True,
        #     key=f"salvar_conteudo_{conteudo_atual['id']}",
        # ):
        #     _save_conteudo_if_dirty(username, conteudo_atual)
        #     st.rerun()

        # _status_salvamento()
        