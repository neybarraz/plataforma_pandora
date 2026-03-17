from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st

from apps.app_05.sections.investigacao.conteudos.catalago import get_paginas
from apps.app_05.storage import load_user_data, update_question_payload


APP_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = APP_DIR / "assets"


# ============================================================
# LAYOUT / ESTILO
# ============================================================

def _inject_visual_css() -> None:
    st.markdown(
        """
        <style>
            .stButton > button {
                border-radius: 0;
                font-weight: 600;
            }

            .analise-topo {
                padding: 0.2rem 0 0.8rem 0;
                margin-bottom: 0.8rem;
                background: transparent;
                border: none;
                color: white;
            }

            .analise-topo strong,
            .analise-topo p,
            .analise-topo div {
                color: white !important;
            }

            .analise-progresso-label {
                margin: 0.25rem 0 0.35rem 0;
                font-weight: 600;
                color: white;
            }

            .st-key-analise_macro_tabs button[kind="primary"] {
                background-color: #f97316;
                color: white;
                border: 1px solid #f97316;
            }

            .st-key-analise_macro_tabs button[kind="secondary"] {
                background-color: transparent;
                color: #f97316;
                border: 1px solid #f97316;
            }

            .st-key-analise_macro_tabs button:hover {
                background-color: #ea580c;
                color: white;
                border: 1px solid #ea580c;
            }

            .st-key-analise_sidebar_header div[data-testid="stMarkdownContainer"] p,
            .st-key-analise_content_header div[data-testid="stMarkdownContainer"] p,
            .st-key-analise_status_box div[data-testid="stMarkdownContainer"] p {
                font-weight: 600;
                margin-bottom: 0.2rem;
            }

            .st-key-analise_sidebar_buttons button[kind="secondary"] {
                text-align: left;
                justify-content: flex-start;
                border: 1px solid #16a34a;
                border-radius: 0;
                background-color: transparent;
                color: white;
            }

            .st-key-analise_sidebar_buttons button[kind="primary"] {
                text-align: left;
                justify-content: flex-start;
                border: 1px solid #16a34a;
                border-radius: 0;
                background-color: #16a34a;
                color: white;
            }

            .st-key-analise_sidebar_buttons button:hover {
                background-color: #15803d;
                color: white;
                border: 1px solid #15803d;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _macro_tab_label(pagina: dict[str, Any]) -> str:
    return pagina.get("titulo_menu") or pagina.get("titulo") or pagina.get("id", "Etapa")


def _conteudo_label(item: dict[str, Any]) -> str:
    return item.get("titulo_menu") or item.get("titulo") or item.get("id", "Conteúdo")


def _normalize_label_for_button(label: str) -> str:
    return str(label).strip().upper()


def _espacamento_linha() -> None:
    st.write("")


def _render_topo() -> None:
    st.markdown(
        """
        <div class="analise-topo">
            Estrutura inicial para a investigação técnica do conforto térmico
            em sala de aula, organizada em três eixos: base de conhecimento,
            plano de análise e execução da análise.
        </div>
        """,
        unsafe_allow_html=True,
    )


def _status_salvamento() -> None:
    ultimo = st.session_state.get("analise_last_save_label", "Ainda não salvo")
    dirty_ids = set(st.session_state.get("analise_dirty_ids", set()))
    save_error = st.session_state.get("analise_save_error", "")

    with st.container(key="analise_status_box"):
        st.markdown("Status")

        if save_error:
            st.error(f"Erro ao salvar: {save_error}")
        elif dirty_ids:
            st.warning(f"Alterações pendentes em {len(dirty_ids)} item(ns).")
        else:
            st.success(ultimo)


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


def _extract_analise_answers(data: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(data, dict):
        return {}

    responses = data.get("responses", {})
    if not isinstance(responses, dict):
        return {}

    analise = responses.get("analise", {})
    if not isinstance(analise, dict):
        return {}

    return analise


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
    defaults = {
        "analise_username": username,
        "analise_pagina_idx": 0,
        "analise_conteudo_idx_por_pagina": {},
        "analise_dirty_ids": set(),
        "analise_saved_ids": set(),
        "analise_last_save_label": "Ainda não salvo",
        "analise_save_error": "",
        "analise_total_questoes": 0,
        "analise_respondidas": 0,
        "analise_data_cache": (
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
    data = st.session_state.get("analise_data_cache")
    if isinstance(data, dict):
        return

    if isinstance(saved_data, dict):
        st.session_state.analise_data_cache = saved_data
    else:
        st.session_state.analise_data_cache = load_user_data(username)


def _update_cache_question_payload(question_id: str, payload: dict[str, Any]) -> None:
    data = st.session_state.get("analise_data_cache")
    if not isinstance(data, dict):
        data = {}

    responses = data.setdefault("responses", {})
    if not isinstance(responses, dict):
        data["responses"] = {}
        responses = data["responses"]

    analise = responses.setdefault("analise", {})
    if not isinstance(analise, dict):
        responses["analise"] = {}
        analise = responses["analise"]

    analise[question_id] = payload
    st.session_state.analise_data_cache = data


def _hydrate_widgets_from_cache(
    username: str,
    conteudo: dict[str, Any],
    *,
    overwrite: bool = False,
) -> None:
    _ensure_cache_loaded(username)
    data = st.session_state.get("analise_data_cache", {})
    analise_answers = _extract_analise_answers(data)

    for bloco in conteudo.get("blocos", []):
        if bloco.get("tipo") not in {"questao_texto", "questao_multipla_escolha"}:
            continue

        qid = str(bloco["id"]).strip()
        widget_key = f"analise_widget_{qid}"

        if qid not in analise_answers:
            continue

        if (not overwrite) and (widget_key in st.session_state):
            continue

        valor = _get_saved_widget_value(analise_answers[qid])

        if bloco.get("tipo") == "questao_multipla_escolha":
            opcoes = list(bloco.get("alternativas", {}).keys())
            if valor not in opcoes:
                valor = None

        st.session_state[widget_key] = valor


def _mark_dirty_question(questao_id: str) -> None:
    dirty_ids = set(st.session_state.get("analise_dirty_ids", set()))
    dirty_ids.add(questao_id)
    st.session_state.analise_dirty_ids = dirty_ids
    st.session_state.analise_save_error = ""


def _clear_dirty_question(questao_id: str) -> None:
    dirty_ids = set(st.session_state.get("analise_dirty_ids", set()))
    dirty_ids.discard(questao_id)
    st.session_state.analise_dirty_ids = dirty_ids


def _get_widget_value(questao_id: str, default: Any = "") -> Any:
    return st.session_state.get(f"analise_widget_{questao_id}", default)


# ============================================================
# NAVEGAÇÃO
# ============================================================

def _get_conteudo_idx_da_pagina(pagina_id: str, total_conteudos: int) -> int:
    mapa = st.session_state.get("analise_conteudo_idx_por_pagina", {})
    idx = mapa.get(pagina_id, 0)

    if total_conteudos <= 0:
        return 0

    return max(0, min(idx, total_conteudos - 1))


def _set_conteudo_idx_da_pagina(pagina_id: str, idx: int) -> None:
    mapa = dict(st.session_state.get("analise_conteudo_idx_por_pagina", {}))
    mapa[pagina_id] = idx
    st.session_state.analise_conteudo_idx_por_pagina = mapa


def _render_macro_tabs(paginas: list[dict[str, Any]]) -> None:
    if not paginas:
        return

    cols = st.columns(len(paginas), gap="small")

    for i, (col, pagina) in enumerate(zip(cols, paginas)):
        with col:
            if st.button(
                _normalize_label_for_button(_macro_tab_label(pagina)),
                key=f"analise_macro_tab_{pagina['id']}",
                type="primary" if i == st.session_state.analise_pagina_idx else "secondary",
                use_container_width=True,
            ):
                st.session_state.analise_pagina_idx = i
                st.rerun()


def _render_conteudo_tabs(pagina: dict[str, Any]) -> dict[str, Any]:
    conteudos = pagina.get("conteudos", [])

    if not conteudos:
        st.warning("Nenhum conteúdo cadastrado para esta etapa.")
        return {}

    pagina_id = pagina["id"]
    idx = _get_conteudo_idx_da_pagina(pagina_id, len(conteudos))

    with st.container(key="analise_sidebar_header"):
        st.markdown("Navegação da etapa")

    with st.container(key="analise_sidebar_buttons"):
        for i, conteudo in enumerate(conteudos):
            if st.button(
                _conteudo_label(conteudo),
                key=f"analise_conteudo_tab_{pagina_id}_{conteudo['id']}",
                type="primary" if i == idx else "secondary",
                use_container_width=True,
            ):
                _set_conteudo_idx_da_pagina(pagina_id, i)
                st.rerun()

    return conteudos[idx]


# ============================================================
# QUESTÕES / PROGRESSO
# ============================================================

def _is_question_block(bloco: dict[str, Any]) -> bool:
    return bloco.get("tipo") in {"questao_texto", "questao_multipla_escolha"}


def _iter_question_blocks(paginas: list[dict[str, Any]]):
    for pagina in paginas:
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
    widget_key = f"analise_widget_{qid}"
    valor = st.session_state.get(widget_key)

    if bloco.get("tipo") == "questao_texto":
        if bool(str(valor or "").strip()):
            return True

    if bloco.get("tipo") == "questao_multipla_escolha":
        if valor is not None and str(valor).strip() != "":
            return True

    analise_answers = _extract_analise_answers(st.session_state.get("analise_data_cache", {}))
    payload = analise_answers.get(qid)
    return _is_answered_payload(payload)


def _questoes_respondidas(paginas: list[dict[str, Any]]) -> int:
    return sum(1 for bloco in _iter_question_blocks(paginas) if _questao_respondida(bloco))


def _refresh_question_counters(paginas: list[dict[str, Any]]) -> None:
    st.session_state.analise_total_questoes = _total_questoes(paginas)
    st.session_state.analise_respondidas = _questoes_respondidas(paginas)


def _render_barra_progresso(paginas: list[dict[str, Any]]) -> None:
    _refresh_question_counters(paginas)

    total = st.session_state.get("analise_total_questoes", 0)
    respondidas = st.session_state.get("analise_respondidas", 0)
    progresso = 0.0 if total == 0 else respondidas / total

    st.progress(progresso)


# ============================================================
# SALVAMENTO REAL
# ============================================================

def _build_question_payload(bloco: dict[str, Any]) -> dict[str, Any]:
    questao_id = str(bloco["id"]).strip()

    if bloco["tipo"] == "questao_texto":
        resposta = str(_get_widget_value(questao_id, "")).strip()
        return {
            "tipo": "texto",
            "pergunta": bloco.get("pergunta", ""),
            "resposta": resposta,
        }

    if bloco["tipo"] == "questao_multipla_escolha":
        resposta = _get_widget_value(questao_id, None)
        resposta = "" if resposta is None else str(resposta).strip()

        return {
            "tipo": "multipla_escolha",
            "pergunta": bloco.get("pergunta", ""),
            "alternativas": deepcopy(bloco.get("alternativas", {})),
            "resposta_escolhida": resposta,
            "alternativa_correta": bloco.get("alternativa_correta"),
        }

    raise ValueError(f"Tipo de bloco não suportado para salvamento: {bloco['tipo']}")


def _save_question(username: str, bloco: dict[str, Any]) -> bool:
    questao_id = str(bloco["id"]).strip()

    try:
        payload = _build_question_payload(bloco)

        update_question_payload(
            username=username,
            section="analise",
            question_id=questao_id,
            payload=payload,
        )

        _update_cache_question_payload(questao_id, payload)
        _clear_dirty_question(questao_id)
        st.session_state.analise_saved_ids = {questao_id}
        st.session_state.analise_last_save_label = f"Salvo às {datetime.now().strftime('%H:%M:%S')}"
        st.session_state.analise_save_error = ""
        return True

    except Exception as e:
        _mark_dirty_question(questao_id)
        st.session_state.analise_save_error = str(e)
        return False


def _question_blocks_from_conteudo(conteudo: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        bloco
        for bloco in conteudo.get("blocos", [])
        if bloco.get("tipo") in {"questao_texto", "questao_multipla_escolha"}
    ]


def _save_pending_questions(
    username: str,
    conteudo: dict[str, Any],
    paginas: list[dict[str, Any]] | None = None,
) -> None:
    dirty_ids = set(st.session_state.get("analise_dirty_ids", set()))
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
        st.session_state.analise_saved_ids = saved_ids

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
    widget_key = f"analise_widget_{questao_id}"

    st.markdown(f"**{bloco.get('pergunta', '')}**")

    st.text_area(
        label="Resposta",
        key=widget_key,
        height=bloco.get("altura", 140),
        placeholder=bloco.get("placeholder", "Digite sua resposta aqui..."),
        label_visibility="collapsed",
    )

    col_save, col_info = st.columns([1.2, 3.8], gap="small")

    with col_save:
        if st.button(
            "Salvar resposta",
            key=f"analise_save_text_{questao_id}",
            use_container_width=True,
        ):
            _save_text_question_from_button(username, bloco, paginas)

    with col_info:
        saved_data = _extract_analise_answers(st.session_state.get("analise_data_cache", {}))
        saved_payload = saved_data.get(questao_id, {})
        saved_text = ""

        if isinstance(saved_payload, dict):
            saved_text = str(saved_payload.get("resposta", ""))

        current_text = str(st.session_state.get(widget_key, "")).strip()

        if current_text != saved_text.strip():
            _mark_dirty_question(questao_id)
            if current_text:
                st.caption("Texto alterado. Clique em “Salvar resposta” para gravar.")
            else:
                st.caption("Resposta em branco.")
        else:
            _clear_dirty_question(questao_id)
            if current_text:
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
    widget_key = f"analise_widget_{questao_id}"

    valor_atual = st.session_state.get(widget_key, None)
    if valor_atual not in opcoes:
        st.session_state[widget_key] = None

    st.markdown(f"**{bloco.get('pergunta', '')}**")

    def _fmt(x: str) -> str:
        return f"{x}) {alternativas[x]}"

    st.radio(
        label="Escolha uma alternativa",
        options=opcoes,
        key=widget_key,
        format_func=_fmt,
        horizontal=False,
        label_visibility="collapsed",
        index=None,
    )

    col_save, col_info = st.columns([1.2, 3.8], gap="small")

    with col_save:
        if st.button(
            "Salvar resposta",
            key=f"analise_save_mcq_{questao_id}",
            use_container_width=True,
        ):
            _save_mcq_from_button(username, bloco, paginas)

    with col_info:
        saved_data = _extract_analise_answers(st.session_state.get("analise_data_cache", {}))
        saved_payload = saved_data.get(questao_id, {})
        saved_value = ""

        if isinstance(saved_payload, dict):
            saved_value = str(saved_payload.get("resposta_escolhida", "")).strip()

        current_value = st.session_state.get(widget_key, None)
        current_value = "" if current_value is None else str(current_value).strip()

        if current_value != saved_value:
            _mark_dirty_question(questao_id)
            if current_value:
                st.caption("Alternativa alterada. Clique em “Salvar resposta” para gravar.")
            else:
                st.caption("Nenhuma alternativa selecionada.")
        else:
            _clear_dirty_question(questao_id)
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
        st.subheader(bloco.get("texto", ""))
        return

    if tipo == "subtitulo":
        st.markdown(f"### {bloco.get('texto', '')}")
        return

    if tipo == "texto":
        st.markdown(bloco.get("texto", ""))
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
        if not url:
            st.warning("Vídeo sem URL.")
            return
        st.video(url)
        return

    if tipo == "questao_texto":
        _render_questao_texto(username, bloco, paginas)
        return

    if tipo == "questao_multipla_escolha":
        _render_questao_multipla_escolha(username, bloco, paginas)
        return

    st.markdown(f"Bloco não suportado: `{tipo}`")


def _render_conteudo(
    username: str,
    conteudo_atual: dict[str, Any],
    paginas: list[dict[str, Any]],
) -> None:
    with st.container(key="analise_section_header"):
        st.markdown(f"### {_conteudo_label(conteudo_atual)}")

    blocos = conteudo_atual.get("blocos", [])

    for i, bloco in enumerate(blocos):
        _render_bloco(username, bloco, paginas)
        if i < len(blocos) - 1:
            _espacamento_linha()

    modulo = conteudo_atual.get("modulo")
    if modulo is not None:
        render_extra = getattr(modulo, "render_controles_especiais", None)
        if callable(render_extra):
            _espacamento_linha()
            render_extra()


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
        st.warning("Nenhuma página de análise cadastrada.")
        return

    pagina_idx = st.session_state.get("analise_pagina_idx", 0)
    pagina_idx = max(0, min(pagina_idx, len(paginas) - 1))
    st.session_state.analise_pagina_idx = pagina_idx

    pagina_atual = paginas[pagina_idx]
    conteudos = pagina_atual.get("conteudos", [])

    _render_topo()
    _render_barra_progresso(paginas)
    _espacamento_linha()

    with st.container(key="analise_macro_tabs"):
        _render_macro_tabs(paginas)

    _espacamento_linha()

    if not conteudos:
        st.warning("Nenhum conteúdo cadastrado para esta etapa.")
        return

    col_sidebar, col_conteudo = st.columns([1.05, 2.6], gap="medium")

    with col_sidebar:
        conteudo_atual = _render_conteudo_tabs(pagina_atual)

    if not conteudo_atual:
        return

    _hydrate_widgets_from_cache(username, conteudo_atual, overwrite=False)

    with col_conteudo:
        with st.container(key="analise_content_header"):
            st.markdown("Conteúdo")

        _render_conteudo(username, conteudo_atual, paginas)
        _espacamento_linha()
        _status_salvamento()