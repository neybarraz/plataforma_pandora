# apps/app_01/sections/problema/problema.py

from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st

from apps.app_01.sections.problema.conteudos.catalogo import get_paginas
from apps.app_01.storage import (
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


def _barra_paginas(etapa: int, total: int) -> None:
    cores = []

    for i in range(total):
        if i < etapa:
            cores.append("#22c55e")
        elif i == etapa:
            cores.append("#f59e0b")
        else:
            cores.append("#e5e7eb")

    barras = "".join(
        f'<div style="flex:1;height:10px;background:{cor};border-radius:5px"></div>'
        for cor in cores
    )

    st.markdown(
        f"""
        <div style="display:flex; gap:8px; margin-bottom:10px;">
            {barras}
        </div>
        """,
        unsafe_allow_html=True,
    )


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

    if "problema_pagina_idx" not in st.session_state:
        st.session_state.problema_pagina_idx = 0

    if "problema_conteudo_idx_por_pagina" not in st.session_state:
        st.session_state.problema_conteudo_idx_por_pagina = {}

    if "problema_total_questoes" not in st.session_state:
        st.session_state.problema_total_questoes = 0

    if "problema_respondidas" not in st.session_state:
        st.session_state.problema_respondidas = 0

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
# CONTAGEM DE QUESTÕES
# -----------------------------

def _is_catalog_question_block(bloco: dict[str, Any]) -> bool:
    if not isinstance(bloco, dict):
        return False

    bloco_id = str(bloco.get("id", "")).strip()
    bloco_tipo = str(bloco.get("tipo", "")).strip()

    return (
        bloco_id.startswith("q_")
        and bloco_tipo in {"questao_texto", "questao_multipla_escolha"}
    )


def _iter_catalog_question_blocks(paginas: list[dict[str, Any]]):
    for pagina in paginas:
        for conteudo in pagina.get("conteudos", []):
            for bloco in conteudo.get("blocos", []):
                if _is_catalog_question_block(bloco):
                    yield bloco


def _count_total_questions_from_catalog(paginas: list[dict[str, Any]]) -> int:
    ids = {
        str(bloco["id"]).strip()
        for bloco in _iter_catalog_question_blocks(paginas)
    }
    return len(ids)


def _is_answered_payload(payload: Any) -> bool:
    if not isinstance(payload, dict):
        return False

    tipo = str(payload.get("tipo", "")).strip()

    if tipo == "texto":
        return bool(str(payload.get("resposta", "")).strip())

    if tipo == "multipla_escolha":
        return bool(str(payload.get("resposta_escolhida", "")).strip())

    return False


def _count_answered_questions(username: str, paginas: list[dict[str, Any]]) -> int:
    data = st.session_state.get("problema_data_cache")
    if not isinstance(data, dict):
        data = load_user_data(username)
        st.session_state.problema_data_cache = data

    problema_answers = _extract_problema_answers(data)

    valid_ids = {
        str(bloco["id"]).strip()
        for bloco in _iter_catalog_question_blocks(paginas)
    }

    respondidas = 0

    for qid in valid_ids:
        widget_key = f"widget_{qid}"

        # Prioriza o que está atualmente no widget, mesmo antes de salvar.
        if widget_key in st.session_state:
            valor_widget = st.session_state.get(widget_key)

            if isinstance(valor_widget, str):
                if valor_widget.strip():
                    respondidas += 1
                    continue
            elif valor_widget is not None:
                respondidas += 1
                continue

        payload = problema_answers.get(qid)
        if _is_answered_payload(payload):
            respondidas += 1

    return respondidas


def _refresh_question_counters(username: str, paginas: list[dict[str, Any]]) -> None:
    st.session_state.problema_total_questoes = _count_total_questions_from_catalog(paginas)
    st.session_state.problema_respondidas = _count_answered_questions(username, paginas)


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


def _save_conteudo_if_dirty(username: str, conteudo: dict[str, Any], paginas: list[dict[str, Any]] | None = None) -> None:
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

    if paginas is not None:
        _refresh_question_counters(username, paginas)


# -----------------------------
# AUTOSAVE
# -----------------------------

@st.fragment(run_every=f"{AUTOSAVE_INTERVAL_S}s")
def _autosave_fragment(username: str, conteudo: dict[str, Any], paginas: list[dict[str, Any]]) -> None:
    _save_conteudo_if_dirty(username, conteudo, paginas)


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


def _barra_resumo(username: str, paginas: list[dict[str, Any]]) -> None:
    _refresh_question_counters(username, paginas)

    total = st.session_state.get("problema_total_questoes", 0)
    respondidas = st.session_state.get("problema_respondidas", 0)
    progresso = 0.0 if total == 0 else respondidas / total

    st.progress(progresso)
    st.caption(f"Questões respondidas: {respondidas}/{total}")


# -----------------------------
# HELPERS DE NAVEGAÇÃO
# -----------------------------

def _get_conteudo_idx_da_pagina(pagina_id: str, total_conteudos: int) -> int:
    mapa = st.session_state.get("problema_conteudo_idx_por_pagina", {})
    idx = mapa.get(pagina_id, 0)
    idx = max(0, min(idx, max(total_conteudos - 1, 0)))
    return idx


def _set_conteudo_idx_da_pagina(pagina_id: str, idx: int) -> None:
    mapa = dict(st.session_state.get("problema_conteudo_idx_por_pagina", {}))
    mapa[pagina_id] = idx
    st.session_state.problema_conteudo_idx_por_pagina = mapa


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

    paginas = get_paginas()

    if not paginas:
        st.info("Nenhuma página foi configurada para a etapa Problema.")
        return

    # Conta total e respondidas assim que entra no menu do problema.
    _refresh_question_counters(username, paginas)

    pagina_idx = st.session_state.get("problema_pagina_idx", 0)
    pagina_idx = max(0, min(pagina_idx, len(paginas) - 1))
    st.session_state.problema_pagina_idx = pagina_idx

    pagina_atual = paginas[pagina_idx]
    conteudos_da_pagina = pagina_atual.get("conteudos", [])

    if not conteudos_da_pagina:
        st.info("Nenhum conteúdo foi configurado para esta página.")
        return

    conteudo_idx = _get_conteudo_idx_da_pagina(
        pagina_atual["id"],
        len(conteudos_da_pagina),
    )
    _set_conteudo_idx_da_pagina(pagina_atual["id"], conteudo_idx)

    conteudo_atual = conteudos_da_pagina[conteudo_idx]

    _hydrate_widgets_from_file(username, conteudo_atual, overwrite=False)
    _autosave_fragment(username, conteudo_atual, paginas)

    _barra_resumo(username, paginas)
    st.markdown("---")

    _barra_paginas(pagina_idx, len(paginas))

    nav1, nav2, nav3 = st.columns([1, 2, 1])

    with nav1:
        if pagina_idx > 0:
            if st.button("⬅ Página anterior", key="problema_pagina_anterior", use_container_width=True):
                _save_conteudo_if_dirty(username, conteudo_atual, paginas)
                st.session_state.problema_pagina_idx = pagina_idx - 1
                nova_pagina = paginas[pagina_idx - 1]
                novo_idx = _get_conteudo_idx_da_pagina(
                    nova_pagina["id"],
                    len(nova_pagina["conteudos"]),
                )
                _hydrate_widgets_from_file(username, nova_pagina["conteudos"][novo_idx], overwrite=True)
                st.rerun()

    with nav2:
        st.markdown(
            f"""
            <div style='text-align:center;font-weight:600;'>
                Etapa {pagina_idx + 1}/{len(paginas)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with nav3:
        if pagina_idx < len(paginas) - 1:
            if st.button("Próxima página ➜", key="problema_proxima_pagina", use_container_width=True):
                _save_conteudo_if_dirty(username, conteudo_atual, paginas)
                st.session_state.problema_pagina_idx = pagina_idx + 1
                nova_pagina = paginas[pagina_idx + 1]
                novo_idx = _get_conteudo_idx_da_pagina(
                    nova_pagina["id"],
                    len(nova_pagina["conteudos"]),
                )
                _hydrate_widgets_from_file(username, nova_pagina["conteudos"][novo_idx], overwrite=True)
                st.rerun()

    st.markdown("---")

    col_menu, col_main = st.columns([0.9, 2.55], gap="small")

    with col_menu:
        _menu_conteudos_style()
        st.markdown(f"**{pagina_atual.get('titulo_menu', 'Conteúdos')}**")
        st.caption(
            f"Respondidas: {st.session_state.get('problema_respondidas', 0)}/"
            f"{st.session_state.get('problema_total_questoes', 0)}"
        )

        for i, item in enumerate(conteudos_da_pagina):
            label = item.get("titulo_menu", item.get("titulo", item["id"]))

            if st.button(
                label,
                key=f"problema_menu_{pagina_atual['id']}_{item['id']}",
                use_container_width=True,
                type="primary" if i == conteudo_idx else "secondary",
            ):
                _save_conteudo_if_dirty(username, conteudo_atual, paginas)
                _set_conteudo_idx_da_pagina(pagina_atual["id"], i)
                _hydrate_widgets_from_file(username, conteudos_da_pagina[i], overwrite=True)
                st.rerun()

    with col_main:
        _flash_style(st.session_state.get("problema_saved_ids", set()))
        _render_conteudo(conteudo_atual)
        _status_salvamento()
