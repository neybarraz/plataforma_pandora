from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st

from .conteudos.catalogo import get_paginas
from ...storage import load_user_data, save_question_response
from ...ui.layout import (
    inject_section_layout_css,
    layout_duas_colunas,
    render_percentual_conclusao,
    render_texto_bloco,
    render_titulo_destaque,
    render_topo_html,
)

SECTION_KEY = "memorial"

APP_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = APP_DIR / "assets"

def _inject_visual_css() -> None:
    inject_section_layout_css(
        prefix="memorial",
        topo_class="memorial-topo",
        sidebar_key="memorial_sidebar_buttons",
    )

def _titulo_destaque(texto: str, nivel: int = 2) -> None:
    render_titulo_destaque(texto, nivel=nivel)


def _texto_bloco(texto: str) -> None:
    render_texto_bloco(texto)


def _macro_tab_label(pagina: dict[str, Any]) -> str:
    return pagina.get("titulo_menu") or pagina.get("titulo") or pagina.get("id", "Etapa")


def _conteudo_label(item: dict[str, Any]) -> str:
    return item.get("titulo_menu") or item.get("titulo") or item.get("id", "Conteúdo")


def _normalize_label_for_button(label: str) -> str:
    return str(label).strip()


def _espacamento_linha() -> None:
    st.write("")


def _render_topo() -> None:
    render_topo_html(
        "memorial-topo",
        """
        Estrutura guiada para apoiar a escrita do memorial técnico. O objetivo é ajudar o aluno
        a transformar o problema investigado em um texto técnico coerente, com contexto, modelo,
        metodologia, resultados, análise e decisão técnica.
        """,
    )


def _status_salvamento() -> None:
    ultimo = st.session_state.get("memorial_last_save_label", "Ainda não salvo")
    dirty_ids = set(st.session_state.get("memorial_dirty_ids", set()))
    save_error = st.session_state.get("memorial_save_error", "")

    if save_error:
        st.error(f"Erro ao salvar: {save_error}")
    elif dirty_ids:
        st.warning(f"Alterações pendentes em {len(dirty_ids)} item(ns).")
    else:
        st.success(ultimo)

def _barra_resumo_topo(paginas: list[dict[str, Any]]) -> None:
    _refresh_question_counters(paginas)

    total = st.session_state.get("memorial_total_questoes", 0)
    respondidas = st.session_state.get("memorial_respondidas", 0)
    progresso = 0.0 if total == 0 else respondidas / total
    percentual = int(progresso * 100)

    st.progress(progresso)
    render_percentual_conclusao(percentual)


# ============================================================
# ESTADO / CACHE
# ============================================================

def _resolve_username(
    username: str | None = None,
    ctx: dict[str, Any] | None = None,
) -> str:
    if isinstance(username, str) and username.strip():
        return username.strip()

    if isinstance(ctx, dict):
        ctx_username = ctx.get("username")
        if isinstance(ctx_username, str) and ctx_username.strip():
            return ctx_username.strip()

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


def _ensure_state(
    username: str,
    saved_data: dict[str, Any] | None = None,
) -> None:
    current_username = st.session_state.get("memorial_username")
    if current_username != username:
        st.session_state.memorial_username = username
        st.session_state.memorial_pagina_idx = 0
        st.session_state.memorial_dirty_ids = set()
        st.session_state.memorial_saved_ids = set()
        st.session_state.memorial_last_save_label = "Ainda não salvo"
        st.session_state.memorial_save_error = ""
        st.session_state.memorial_total_questoes = 0
        st.session_state.memorial_respondidas = 0
        st.session_state.memorial_data_cache = (
            saved_data if isinstance(saved_data, dict) else load_user_data(username)
        )

    defaults = {
        "memorial_username": username,
        "memorial_pagina_idx": 0,
        "memorial_dirty_ids": set(),
        "memorial_saved_ids": set(),
        "memorial_last_save_label": "Ainda não salvo",
        "memorial_save_error": "",
        "memorial_total_questoes": 0,
        "memorial_respondidas": 0,
        "memorial_data_cache": (
            saved_data if isinstance(saved_data, dict) else load_user_data(username)
        ),
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _ensure_cache_loaded(
    username: str,
    saved_data: dict[str, Any] | None = None,
) -> None:
    data = st.session_state.get("memorial_data_cache")
    if isinstance(data, dict):
        return

    if isinstance(saved_data, dict):
        st.session_state.memorial_data_cache = saved_data
    else:
        st.session_state.memorial_data_cache = load_user_data(username)


def _replace_cache_with_data(data: dict[str, Any]) -> None:
    if isinstance(data, dict):
        st.session_state.memorial_data_cache = data


def _hydrate_widgets_from_cache(
    paginas: list[dict[str, Any]],
    *,
    overwrite: bool = False,
) -> None:
    data = st.session_state.get("memorial_data_cache", {})
    section_answers = _extract_section_answers(data)

    for pagina in paginas:
        for conteudo in pagina.get("conteudos", []):
            for bloco in conteudo.get("blocos", []):
                if bloco.get("tipo") not in {"questao_texto", "questao_multipla_escolha"}:
                    continue

                qid = str(bloco["id"]).strip()
                widget_key = f"memorial_widget_{qid}"

                if qid not in section_answers:
                    continue

                if (not overwrite) and (widget_key in st.session_state):
                    continue

                valor = _get_saved_widget_value(section_answers[qid])

                if bloco.get("tipo") == "questao_multipla_escolha":
                    opcoes = list(bloco.get("alternativas", {}).keys())
                    if valor not in opcoes:
                        valor = None

                st.session_state[widget_key] = valor


def _mark_dirty_question(questao_id: str) -> None:
    dirty_ids = set(st.session_state.get("memorial_dirty_ids", set()))
    dirty_ids.add(questao_id)
    st.session_state.memorial_dirty_ids = dirty_ids
    st.session_state.memorial_save_error = ""


def _clear_dirty_question(questao_id: str) -> None:
    dirty_ids = set(st.session_state.get("memorial_dirty_ids", set()))
    dirty_ids.discard(questao_id)
    st.session_state.memorial_dirty_ids = dirty_ids


def _get_widget_value(questao_id: str, default: Any = "") -> Any:
    return st.session_state.get(f"memorial_widget_{questao_id}", default)


# ============================================================
# NAVEGAÇÃO / PROGRESSO
# ============================================================

def _render_sidebar_paginas(
    username: str,
    paginas: list[dict[str, Any]],
) -> None:
    if not paginas:
        return

    pagina_idx = st.session_state.get("memorial_pagina_idx", 0)
    pagina_idx = max(0, min(pagina_idx, len(paginas) - 1))

    for i, pagina in enumerate(paginas):
        label = _normalize_label_for_button(_macro_tab_label(pagina))

        if st.button(
            label,
            key=f"memorial_menu_{pagina['id']}",
            use_container_width=True,
            type="primary" if i == pagina_idx else "secondary",
        ):
            pagina_atual = paginas[pagina_idx]
            _save_pending_questions(username, pagina_atual, paginas)
            st.session_state.memorial_pagina_idx = i
            st.rerun()


def _is_question_block(bloco: dict[str, Any]) -> bool:
    return bloco.get("tipo") in {"questao_texto", "questao_multipla_escolha"}


def _iter_question_blocks(paginas: list[dict[str, Any]]):
    for pagina in paginas:
        for conteudo in pagina.get("conteudos", []):
            for bloco in conteudo.get("blocos", []):
                if _is_question_block(bloco):
                    yield bloco


def _iter_question_blocks_from_pagina(pagina: dict[str, Any]):
    for conteudo in pagina.get("conteudos", []):
        for bloco in conteudo.get("blocos", []):
            if _is_question_block(bloco):
                yield bloco


def _total_questoes(paginas: list[dict[str, Any]]) -> int:
    ids = {str(bloco["id"]).strip() for bloco in _iter_question_blocks(paginas)}
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


def _questao_respondida(bloco: dict[str, Any]) -> bool:
    qid = str(bloco["id"]).strip()
    widget_key = f"memorial_widget_{qid}"
    valor = st.session_state.get(widget_key)

    if bloco.get("tipo") == "questao_texto":
        if bool(str(valor or "").strip()):
            return True

    if bloco.get("tipo") == "questao_multipla_escolha":
        if valor is not None and str(valor).strip() != "":
            return True

    section_answers = _extract_section_answers(
        st.session_state.get("memorial_data_cache", {})
    )
    payload = section_answers.get(qid)
    return _is_answered_payload(payload)


def _questoes_respondidas(paginas: list[dict[str, Any]]) -> int:
    return sum(1 for bloco in _iter_question_blocks(paginas) if _questao_respondida(bloco))


def _refresh_question_counters(paginas: list[dict[str, Any]]) -> None:
    st.session_state.memorial_total_questoes = _total_questoes(paginas)
    st.session_state.memorial_respondidas = _questoes_respondidas(paginas)


# ============================================================
# SALVAMENTO REAL
# ============================================================

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
                pergunta=bloco.get("pergunta", ""),
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
                pergunta=bloco.get("pergunta", ""),
                resposta=resposta,
                alternativas=bloco.get("alternativas", {}),
                alternativa_correta=bloco.get("alternativa_correta", ""),
                meta=_build_question_meta(bloco),
            )

        else:
            raise ValueError(f"Tipo de bloco não suportado para salvamento: {bloco['tipo']}")

        _replace_cache_with_data(updated_data)
        _clear_dirty_question(questao_id)
        st.session_state.memorial_saved_ids = {questao_id}
        st.session_state.memorial_last_save_label = (
            f"Salvo às {datetime.now().strftime('%H:%M:%S')}"
        )
        st.session_state.memorial_save_error = ""
        return True

    except Exception as e:
        _mark_dirty_question(questao_id)
        st.session_state.memorial_save_error = str(e)
        return False


def _save_pending_questions(
    username: str,
    pagina: dict[str, Any],
    paginas: list[dict[str, Any]] | None = None,
) -> None:
    dirty_ids = set(st.session_state.get("memorial_dirty_ids", set()))
    if not dirty_ids:
        return

    saved_ids: set[str] = set()

    for bloco in _iter_question_blocks_from_pagina(pagina):
        qid = str(bloco["id"]).strip()
        if qid not in dirty_ids:
            continue

        ok = _save_question(username, bloco)
        if ok:
            saved_ids.add(qid)

    if saved_ids:
        st.session_state.memorial_saved_ids = saved_ids

    if paginas is not None:
        _refresh_question_counters(paginas)


def _save_text_question_from_button(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    _mark_dirty_question(str(bloco["id"]).strip())
    _save_question(username, bloco)
    _refresh_question_counters(paginas)


def _save_mcq_from_button(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    _mark_dirty_question(str(bloco["id"]).strip())
    _save_question(username, bloco)
    _refresh_question_counters(paginas)


# ============================================================
# RENDERIZAÇÃO DOS BLOCOS
# ============================================================

def _render_questao_texto(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    questao_id = str(bloco["id"]).strip()
    widget_key = f"memorial_widget_{questao_id}"

    st.markdown(bloco.get("pergunta", ""))

    st.text_area(
        label="Sua resposta",
        key=widget_key,
        height=bloco.get("altura", 160),
        placeholder=bloco.get("placeholder", "Digite sua resposta aqui..."),
        label_visibility="visible",
    )

    col_save, col_info = st.columns([1.2, 3.8], gap="small")

    with col_save:
        if st.button(
            "Salvar resposta",
            key=f"memorial_save_text_{questao_id}",
            use_container_width=True,
        ):
            _save_text_question_from_button(username, bloco, paginas)

    with col_info:
        saved_data = _extract_section_answers(
            st.session_state.get("memorial_data_cache", {})
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
    alternativas = bloco.get("alternativas", {})
    opcoes = list(alternativas.keys())
    widget_key = f"memorial_widget_{questao_id}"

    valor_atual = st.session_state.get(widget_key, None)
    if valor_atual not in opcoes:
        st.session_state[widget_key] = None

    st.markdown(bloco.get("pergunta", ""))

    def _fmt(x: str) -> str:
        return f"{x}) {alternativas[x]}"

    st.radio(
        label="Escolha uma alternativa",
        options=opcoes,
        key=widget_key,
        format_func=_fmt,
        horizontal=False,
        label_visibility="visible",
        index=None,
    )

    col_save, col_info = st.columns([1.2, 3.8], gap="small")

    with col_save:
        if st.button(
            "Salvar resposta",
            key=f"memorial_save_mcq_{questao_id}",
            use_container_width=True,
        ):
            _save_mcq_from_button(username, bloco, paginas)

    with col_info:
        saved_data = _extract_section_answers(
            st.session_state.get("memorial_data_cache", {})
        )
        saved_payload = saved_data.get(questao_id, {})
        saved_value = ""

        if isinstance(saved_payload, dict):
            saved_value = str(saved_payload.get("resposta_escolhida", "")).strip()

        current_value = st.session_state.get(widget_key, None)
        current_value = "" if current_value is None else str(current_value).strip()

        if current_value != saved_value:
            if current_value:
                st.caption("Alternativa alterada. Clique em “Salvar resposta” para gravar.")
            else:
                st.caption("Nenhuma alternativa selecionada.")
        else:
            if current_value:
                st.caption("Alternativa salva.")
            else:
                st.caption("Nenhuma alternativa selecionada.")


def _render_imagem(bloco: dict[str, Any]) -> None:
    arquivo_ou_url = (
        bloco.get("arquivo")
        or bloco.get("url")
        or bloco.get("arquivo_ou_url")
        or ""
    )

    legenda = bloco.get("legenda") or bloco.get("caption") or ""
    fonte = bloco.get("fonte") or ""

    if not arquivo_ou_url:
        st.warning("Imagem sem arquivo ou URL.")
        return

    arquivo_ou_url = str(arquivo_ou_url).strip()

    if arquivo_ou_url.startswith("http://") or arquivo_ou_url.startswith("https://"):
        st.image(
            arquivo_ou_url,
            caption=legenda if legenda else None,
            use_container_width=True,
        )
    else:
        image_path = ASSETS_DIR / arquivo_ou_url

        if not image_path.exists():
            st.warning(f"Imagem não encontrada: {image_path}")
            return

        st.image(
            str(image_path),
            caption=legenda if legenda else None,
            use_container_width=True,
        )

    if fonte:
        st.caption(f"Fonte: {fonte}")


def _render_bloco(
    username: str,
    bloco: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    tipo = bloco.get("tipo", "")

    if tipo == "titulo":
        _titulo_destaque(bloco.get("texto", ""), nivel=2)
        return

    if tipo == "subtitulo":
        _titulo_destaque(bloco.get("texto", ""), nivel=3)
        return

    if tipo == "texto":
        _texto_bloco(bloco.get("texto", ""))
        return

    if tipo == "lista":
        for item in bloco.get("itens", []):
            st.markdown(f"- {item}")
        return

    if tipo == "alerta":
        nivel = bloco.get("nivel", "info")
        texto = bloco.get("texto", "")

        if nivel == "success":
            st.success(texto)
        elif nivel == "warning":
            st.warning(texto)
        elif nivel == "error":
            st.error(texto)
        else:
            st.info(texto)
        return

    if tipo == "imagem":
        _render_imagem(bloco)
        return

    if tipo == "video":
        url = bloco.get("url", "")

        if bloco.get("titulo"):
            _titulo_destaque(bloco["titulo"], nivel=3)

        if bloco.get("descricao"):
            _texto_bloco(bloco["descricao"])

        if not url:
            st.warning("Vídeo sem URL.")
            return

        st.video(url)

        if bloco.get("caption"):
            st.caption(bloco["caption"])
        return

    if tipo == "questao_texto":
        _render_questao_texto(username, bloco, paginas)
        return

    if tipo == "questao_multipla_escolha":
        _render_questao_multipla_escolha(username, bloco, paginas)
        return

    st.markdown(f"Bloco não suportado: `{tipo}`")


def _render_pagina_em_sequencia(
    username: str,
    pagina_atual: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    conteudos = pagina_atual.get("conteudos", [])

    if not conteudos:
        st.warning("Nenhum conteúdo cadastrado para esta etapa.")
        return

    for idx, conteudo in enumerate(conteudos):
        if conteudo.get("titulo") or conteudo.get("titulo_menu"):
            _titulo_destaque(_conteudo_label(conteudo), nivel=2)

        blocos = conteudo.get("blocos", [])

        for i, bloco in enumerate(blocos):
            _render_bloco(username, bloco, paginas)
            if i < len(blocos) - 1:
                _espacamento_linha()

        if idx < len(conteudos) - 1:
            st.divider()


# ============================================================
# ORQUESTRAÇÃO
# ============================================================

def render(
    username: str | None = None,
    saved_data: dict[str, Any] | None = None,
    ctx: dict[str, Any] | None = None,
) -> None:
    username = _resolve_username(username=username, ctx=ctx)
    _ensure_state(username, saved_data=saved_data)
    _ensure_cache_loaded(username, saved_data=saved_data)
    _inject_visual_css()

    paginas = get_paginas()

    if not paginas:
        st.warning("Nenhuma página de memorial cadastrada.")
        return

    _hydrate_widgets_from_cache(paginas, overwrite=False)

    pagina_idx = st.session_state.get("memorial_pagina_idx", 0)
    pagina_idx = max(0, min(pagina_idx, len(paginas) - 1))
    st.session_state.memorial_pagina_idx = pagina_idx

    pagina_atual = paginas[pagina_idx]

    _render_topo()
    _espacamento_linha()

    col_lateral, col_conteudo = layout_duas_colunas()

    with col_lateral:
        with st.container(key="memorial_sidebar_buttons"):
            _render_sidebar_paginas(username, paginas)

        _barra_resumo_topo(paginas)

    with col_conteudo:
        _render_pagina_em_sequencia(username, pagina_atual, paginas)
        _espacamento_linha()
        _status_salvamento()