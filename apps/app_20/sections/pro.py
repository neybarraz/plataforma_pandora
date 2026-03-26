from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st

from .pro_conteudo.pro_catalogo import get_paginas
from .pro_conteudo.simulacao_estado import render_simulacao_estado
from .pro_conteudo.simulador_conversor_didatico import render_simulador_conversor_didatico
from ..storage import load_user_data, save_question_response, get_section_stats
from ..ui.layout import (
    inject_section_layout_css,
    layout_duas_colunas,
    render_texto_bloco,
    render_titulo_destaque,
    render_topo_html,
)


SECTION_KEY = "problema"

APP_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = APP_DIR / "assets"

def _inject_visual_css() -> None:
    inject_section_layout_css(
        prefix="problema",
        topo_class="problema-topo",
        macro_tabs_key="problema_macro_tabs",
        sidebar_key="problema_sidebar_buttons",
    )

def _refresh_question_counters(username: str) -> None:
    stats = get_section_stats(username, SECTION_KEY)
    st.session_state.problema_total_questoes = stats["total_questoes"]
    st.session_state.problema_respondidas = stats["respondidas"]

def _render_topo() -> None:
    render_topo_html(
        "problema-topo",
        """
        Nesta etapa, o desafio é organizado de forma estruturada para orientar a análise, reunindo a visão inicial do caso, os dados disponíveis, os parâmetros relevantes e as condições que limitam o problema, ao mesmo tempo em que se define o foco da investigação, a pergunta central a ser respondida e a representação do sistema, permitindo transformar uma situação ampla em um recorte técnico claro, objetivo e investigável.
        """,
    )

def _titulo_destaque(texto: str, nivel: int = 2) -> None:
    render_titulo_destaque(texto, nivel=nivel)

def _texto_bloco(texto: str) -> None:
    render_texto_bloco(texto)


def _espacamento_linha() -> None:
    st.write("")


def _show_image(filename: str, caption: str = "") -> None:
    image_path = ASSETS_DIR / filename

    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: {image_path}")


def _status_salvamento() -> None:
    ultimo = st.session_state.get("problema_last_save_label", "Ainda não salvo")
    dirty_ids = set(st.session_state.get("problema_dirty_ids", set()))
    save_error = st.session_state.get("problema_save_error", "")

    if save_error:
        st.error(f"Erro ao salvar: {save_error}")
    elif dirty_ids:
        st.warning(f"Alterações pendentes em {len(dirty_ids)} questão(ões).")
    else:
        st.success(ultimo)


def _macro_tab_label(pagina: dict[str, Any]) -> str:
    return pagina.get("titulo_menu") or pagina.get("titulo") or pagina.get("id", "Etapa")


def _conteudo_label(item: dict[str, Any]) -> str:
    return item.get("titulo_menu") or item.get("titulo") or item.get("id", "Conteúdo")


def _normalize_label_for_button(label: str) -> str:
    return str(label).strip()


def _render_macro_tabs(
    paginas: list[dict[str, Any]],
    pagina_idx: int,
    username: str,
    conteudo_atual: dict[str, Any] | None,
) -> None:
    if not paginas:
        return

    cols = st.columns(len(paginas), gap="small")

    for i, (col, pagina) in enumerate(zip(cols, paginas)):
        with col:
            if st.button(
                _normalize_label_for_button(_macro_tab_label(pagina)),
                key=f"problema_macro_tab_{pagina['id']}",
                type="primary" if i == pagina_idx else "secondary",
                use_container_width=True,
            ):
                if conteudo_atual is not None:
                    _save_pending_questions(username, conteudo_atual)
                st.session_state.problema_pagina_idx = i
                st.rerun()


# ============================================================
# ESTRUTURAL
# ============================================================

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


def _extract_section_answers(data: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(data, dict):
        return {}

    responses = data.get("responses", {})
    if not isinstance(responses, dict):
        return {}

    section_data = responses.get(SECTION_KEY, {})
    if not isinstance(section_data, dict):
        return {}

    return section_data


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
    current_username = st.session_state.get("problema_username")
    if current_username != username:
        st.session_state.problema_username = username
        st.session_state.problema_dirty_ids = set()
        st.session_state.problema_saved_ids = set()
        st.session_state.problema_last_save_label = "Ainda não salvo"
        st.session_state.problema_save_error = ""
        st.session_state.problema_pagina_idx = 0
        st.session_state.problema_conteudo_idx_por_pagina = {}
        st.session_state.problema_total_questoes = 0
        st.session_state.problema_respondidas = 0
        st.session_state.problema_data_cache = load_user_data(username)

    defaults = {
        "problema_username": username,
        "problema_dirty_ids": set(),
        "problema_saved_ids": set(),
        "problema_last_save_label": "Ainda não salvo",
        "problema_save_error": "",
        "problema_pagina_idx": 0,
        "problema_conteudo_idx_por_pagina": {},
        "problema_total_questoes": 0,
        "problema_respondidas": 0,
        "problema_data_cache": load_user_data(username),
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _ensure_cache_loaded(username: str) -> None:
    data = st.session_state.get("problema_data_cache")
    if not isinstance(data, dict):
        st.session_state.problema_data_cache = load_user_data(username)


def _replace_cache_with_data(data: dict[str, Any]) -> None:
    if isinstance(data, dict):
        st.session_state.problema_data_cache = data


def _hydrate_widgets_from_file(
    username: str,
    conteudo: dict[str, Any],
    *,
    overwrite: bool = False,
) -> None:
    _ensure_cache_loaded(username)
    data = st.session_state.get("problema_data_cache", {})
    section_answers = _extract_section_answers(data)

    for bloco in conteudo["blocos"]:
        if bloco["tipo"] not in {"questao_texto", "questao_multipla_escolha"}:
            continue

        qid = str(bloco["id"]).strip()
        widget_key = f"problema_widget_{qid}"

        if qid not in section_answers:
            continue

        if (not overwrite) and (widget_key in st.session_state):
            continue

        valor = _get_saved_widget_value(section_answers[qid])

        if bloco["tipo"] == "questao_multipla_escolha":
            opcoes = list(bloco["alternativas"].keys())
            if valor not in opcoes:
                valor = None

        st.session_state[widget_key] = valor


def _mark_dirty_question(questao_id: str) -> None:
    dirty_ids = set(st.session_state.get("problema_dirty_ids", set()))
    dirty_ids.add(questao_id)
    st.session_state.problema_dirty_ids = dirty_ids
    st.session_state.problema_save_error = ""


def _clear_dirty_question(questao_id: str) -> None:
    dirty_ids = set(st.session_state.get("problema_dirty_ids", set()))
    dirty_ids.discard(questao_id)
    st.session_state.problema_dirty_ids = dirty_ids


def _get_widget_value(questao_id: str, default: Any = "") -> Any:
    return st.session_state.get(f"problema_widget_{questao_id}", default)


def _is_catalog_question_block(bloco: dict[str, Any]) -> bool:
    if not isinstance(bloco, dict):
        return False

    bloco_id = str(bloco.get("id", "")).strip()
    bloco_tipo = str(bloco.get("tipo", "")).strip()

    return bool(bloco_id) and bloco_tipo in {"questao_texto", "questao_multipla_escolha"}

def _build_question_meta(bloco: dict[str, Any]) -> dict[str, Any]:
    return {
        "origem_bloco_tipo": str(bloco.get("tipo", "")).strip(),
        "flow_type": str(bloco.get("flow_type", "")).strip(),
        "titulo_bloco": str(
            bloco.get("titulo")
            or bloco.get("titulo_menu")
            or bloco.get("id", "")
        ).strip(),
    }


def _save_question(username: str, bloco: dict[str, Any]) -> bool:
    questao_id = str(bloco["id"]).strip()

    try:
        if bloco["tipo"] == "questao_texto":
            updated_data = save_question_response(
                username=username,
                section=SECTION_KEY,
                question_id=questao_id,
                question_type="texto",
                pergunta=bloco["pergunta"],
                resposta=str(_get_widget_value(questao_id, "")).strip(),
                meta=_build_question_meta(bloco),
            )

        elif bloco["tipo"] == "questao_multipla_escolha":
            resposta = _get_widget_value(questao_id, None)
            resposta = "" if resposta is None else str(resposta).strip()

            updated_data = save_question_response(
                username=username,
                section=SECTION_KEY,
                question_id=questao_id,
                question_type="multipla_escolha",
                pergunta=bloco["pergunta"],
                resposta=resposta,
                alternativas=bloco.get("alternativas", {}),
                alternativa_correta=bloco.get("alternativa_correta", ""),
                meta=_build_question_meta(bloco),
            )

        else:
            raise ValueError(f"Tipo de bloco não suportado para salvamento: {bloco['tipo']}")

        _replace_cache_with_data(updated_data)
        _clear_dirty_question(questao_id)
        st.session_state.problema_saved_ids = {questao_id}
        st.session_state.problema_last_save_label = (
            f"Salvo às {datetime.now().strftime('%H:%M:%S')}"
        )
        st.session_state.problema_save_error = ""
        return True

    except Exception as e:
        _mark_dirty_question(questao_id)
        st.session_state.problema_save_error = str(e)
        return False


def _question_blocks_from_conteudo(conteudo: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        bloco
        for bloco in conteudo["blocos"]
        if bloco["tipo"] in {"questao_texto", "questao_multipla_escolha"}
    ]



def _save_text_question_from_button(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    _mark_dirty_question(str(bloco["id"]).strip())
    _save_question(username, bloco)
    _refresh_question_counters(username)


def _save_mcq_on_change(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    _mark_dirty_question(str(bloco["id"]).strip())
    _save_question(username, bloco)
    _refresh_question_counters(username)


def _get_conteudo_idx_da_pagina(pagina_id: str, total_conteudos: int) -> int:
    mapa = st.session_state.get("problema_conteudo_idx_por_pagina", {})
    idx = mapa.get(pagina_id, 0)
    idx = max(0, min(idx, max(total_conteudos - 1, 0)))
    return idx


def _set_conteudo_idx_da_pagina(pagina_id: str, idx: int) -> None:
    mapa = dict(st.session_state.get("problema_conteudo_idx_por_pagina", {}))
    mapa[pagina_id] = idx
    st.session_state.problema_conteudo_idx_por_pagina = mapa


def _get_paginas_visiveis() -> list[dict[str, Any]]:
    paginas = get_paginas()

    paginas_filtradas: list[dict[str, Any]] = []
    for pagina in paginas:
        label = _macro_tab_label(pagina).strip().lower()
        if "valida" in label:
            continue
        paginas_filtradas.append(pagina)

    return paginas_filtradas[:4]


# ============================================================
# PEDAGÓGICA
# ============================================================

def _render_bloco_pedagogico(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    tipo = bloco["tipo"]

    if tipo == "titulo":
        _titulo_destaque(bloco["texto"], nivel=2)
        return

    if tipo == "subtitulo":
        _titulo_destaque(bloco["texto"], nivel=3)
        return

    if tipo == "texto":
        _texto_bloco(bloco["texto"])
        return

    if tipo == "video":
        url = bloco.get("url")

        if bloco.get("titulo"):
            _titulo_destaque(bloco["titulo"], nivel=3)

        if bloco.get("descricao"):
            _texto_bloco(bloco["descricao"])

        if url:
            st.video(url)

        if bloco.get("caption"):
            st.caption(bloco["caption"])

        return

    if tipo == "imagem":
        _show_image(
            filename=bloco["arquivo"],
            caption=bloco.get("caption", ""),
        )
        return

    if tipo == "simulacao_estado":
        render_simulacao_estado(bloco)
        return

    if tipo == "simulador_conversor":
        if bloco.get("titulo"):
            _titulo_destaque(bloco["titulo"], nivel=3)

        if bloco.get("descricao"):
            _texto_bloco(bloco["descricao"])

        render_simulador_conversor_didatico()

        if bloco.get("pergunta_guiada"):
            st.info(bloco["pergunta_guiada"])
        return

    if tipo == "questao_texto":
        _render_questao_texto(username, bloco, paginas)
        return

    if tipo == "questao_multipla_escolha":
        _render_questao_multipla_escolha(username, bloco, paginas)
        return


def _render_questao_texto(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    questao_id = str(bloco["id"]).strip()
    widget_key = f"problema_widget_{questao_id}"

    st.markdown(bloco["pergunta"])

    st.text_area(
        label="Sua resposta",
        key=widget_key,
        height=bloco.get("altura", 160),
        placeholder=bloco.get("placeholder", ""),
        label_visibility="visible",
    )

    col_save, col_info = st.columns([1.2, 3.8], gap="small")

    with col_save:
        if st.button(
            "Salvar resposta",
            key=f"save_text_{questao_id}",
            use_container_width=True,
        ):
            _save_text_question_from_button(username, bloco, paginas)

    with col_info:
        saved_data = _extract_section_answers(
            st.session_state.get("problema_data_cache", {})
        )
        saved_payload = saved_data.get(questao_id, {})
        saved_text = ""

        if isinstance(saved_payload, dict):
            saved_text = str(saved_payload.get("resposta", ""))

        current_text = str(st.session_state.get(widget_key, "")).strip()

        if current_text and current_text != saved_text.strip():
            st.caption("Texto alterado. Clique em “Salvar resposta” para gravar.")
        elif current_text:
            st.caption("Texto salvo.")
        else:
            st.caption("Resposta em branco.")


def _render_questao_multipla_escolha(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    questao_id = str(bloco["id"]).strip()
    alternativas = bloco["alternativas"]
    opcoes = list(alternativas.keys())
    widget_key = f"problema_widget_{questao_id}"

    valor_atual = st.session_state.get(widget_key, None)
    if valor_atual not in opcoes:
        st.session_state[widget_key] = None

    st.markdown(bloco["pergunta"])

    def _fmt(x: str) -> str:
        return f"{x}) {alternativas[x]}"

    st.radio(
        label="Escolha uma alternativa",
        options=opcoes,
        format_func=_fmt,
        key=widget_key,
        index=None,
        horizontal=False,
        on_change=_save_mcq_on_change,
        args=(username, bloco, paginas),
        label_visibility="visible",
    )


def _render_conteudo_pedagogico(
    username: str,
    conteudo: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    for i, bloco in enumerate(conteudo["blocos"]):
        _render_bloco_pedagogico(username, bloco, paginas)

        if i < len(conteudo["blocos"]) - 1:
            _espacamento_linha()

def _save_pending_questions(
    username: str,
    conteudo: dict[str, Any],
) -> None:
    dirty_ids = set(st.session_state.get("problema_dirty_ids", set()))
    if not dirty_ids:
        return

    saved_ids: set[str] = set()

    for bloco in _question_blocks_from_conteudo(conteudo):
        qid = str(bloco["id"]).strip()
        if qid not in dirty_ids:
            continue

        ok = _save_question(username, bloco)
        if ok:
            saved_ids.add(qid)

    if saved_ids:
        st.session_state.problema_saved_ids = saved_ids

    _refresh_question_counters(username)
# ============================================================
# ORQUESTRAÇÃO DA TELA
# ============================================================

def render(
    username: str | None = None,
    saved_data: dict[str, Any] | None = None,
    ctx: dict[str, Any] | None = None,
) -> None:
    del saved_data

    username = _resolve_username(username=username, ctx=ctx)
    _ensure_state(username)
    _ensure_cache_loaded(username)
    _inject_visual_css()

    paginas = _get_paginas_visiveis()

    if not paginas:
        st.info("Nenhuma página foi configurada para a etapa Problema.")
        return

    _refresh_question_counters(username)

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

    _render_topo()

    with st.container(key="problema_macro_tabs"):
        _render_macro_tabs(
            paginas=paginas,
            pagina_idx=pagina_idx,
            username=username,
            conteudo_atual=conteudo_atual,
        )

    _espacamento_linha()

    # col_lateral, col_conteudo = layout_duas_colunas()

    # with col_lateral:
    #     with st.container(key="problema_sidebar_buttons"):
    #         for i, item in enumerate(conteudos_da_pagina):
    #             label = _conteudo_label(item)

    #             if st.button(
    #                 label,
    #                 key=f"problema_menu_{pagina_atual['id']}_{item['id']}",
    #                 use_container_width=True,
    #                 type="primary" if i == conteudo_idx else "secondary",
    #             ):
    #                 _save_pending_questions(username, conteudo_atual)
    #                 _set_conteudo_idx_da_pagina(pagina_atual["id"], i)
    #                 # st.rerun()


    # with col_conteudo:
    _render_conteudo_pedagogico(username, conteudo_atual, paginas)
    _espacamento_linha()
    _status_salvamento()