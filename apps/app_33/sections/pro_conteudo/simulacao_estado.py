from __future__ import annotations

from typing import Any

import streamlit as st


def _status_badge(label: str, value: str) -> str:
    value_lower = value.lower()

    if "ativa" in value_lower or "ligado" in value_lower or "carregando" in value_lower:
        bg = "#dcfce7"
        border = "#22c55e"
        fg = "#166534"
    elif "inativa" in value_lower or "desligado" in value_lower:
        bg = "#fee2e2"
        border = "#ef4444"
        fg = "#991b1b"
    else:
        bg = "#e0f2fe"
        border = "#0284c7"
        fg = "#075985"

    return f"""
    <div style="
        border:1px solid {border};
        background:{bg};
        color:{fg};
        border-radius:10px;
        padding:0.7rem 0.8rem;
        margin-bottom:0.45rem;
    ">
        <div style="font-size:0.82rem; opacity:0.9;">{label}</div>
        <div style="font-size:0.98rem; font-weight:700;">{value}</div>
    </div>
    """


def _flow_card(title: str, items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f"""
    <div style="
        border:1px solid #e5e7eb;
        border-radius:12px;
        padding:0.9rem 1rem;
        margin-bottom:0.7rem;
    ">
        <div style="font-weight:700; margin-bottom:0.5rem;">{title}</div>
        <ul style="margin:0; padding-left:1.2rem;">
            {lis}
        </ul>
    </div>
    """


def _simple_energy_diagram(state_key: str) -> None:
    if state_key == "fonte_conectada":
        st.markdown(
            """
            <div style="
                border:1px solid #e5e7eb;
                border-radius:12px;
                padding:1rem;
                margin-top:0.2rem;
                margin-bottom:0.5rem;
            ">
                <div style="font-weight:700; margin-bottom:0.7rem;">Fluxo de energia no sistema</div>
                <div style="display:flex; flex-wrap:wrap; gap:0.6rem; align-items:center;">
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">Fonte externa</div>
                    <div style="font-size:1.2rem;">→</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">TP4056</div>
                    <div style="font-size:1.2rem;">→</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">Bateria</div>
                    <div style="font-size:1.2rem;">→</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">LM2596</div>
                    <div style="font-size:1.2rem;">→</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">LED</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div style="
                border:1px solid #e5e7eb;
                border-radius:12px;
                padding:1rem;
                margin-top:0.2rem;
                margin-bottom:0.5rem;
            ">
                <div style="font-weight:700; margin-bottom:0.7rem;">Fluxo de energia no sistema</div>
                <div style="display:flex; flex-wrap:wrap; gap:0.6rem; align-items:center;">
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1; opacity:0.55;">Fonte externa</div>
                    <div style="font-size:1.2rem; opacity:0.45;">×</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">Bateria</div>
                    <div style="font-size:1.2rem;">→</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">LM2596</div>
                    <div style="font-size:1.2rem;">→</div>
                    <div style="padding:0.7rem 0.9rem; border-radius:10px; border:1px solid #cbd5e1;">LED</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_simulacao_estado(bloco: dict[str, Any]) -> None:
    titulo = bloco.get("titulo", "Simulação")
    descricao = bloco.get("descricao", "")
    estados = bloco.get("estados", {})
    estado_inicial = bloco.get("estado_inicial")
    pergunta_guiada = bloco.get("pergunta_guiada", "")

    if not estados:
        st.warning("Nenhum estado foi configurado para esta simulação.")
        return

    state_keys = list(estados.keys())
    if estado_inicial not in state_keys:
        estado_inicial = state_keys[0]

    widget_key = f"simulacao_estado_selector_{bloco.get('id', 'default')}"

    if widget_key not in st.session_state:
        st.session_state[widget_key] = estado_inicial

    st.markdown(f"#### {titulo}")
    if descricao:
        st.markdown(descricao)

    labels = {key: estados[key].get("titulo", key) for key in state_keys}
    current_index = state_keys.index(st.session_state[widget_key])

    selected_key = st.radio(
        "Selecione o estado de operação",
        options=state_keys,
        index=current_index,
        format_func=lambda x: labels[x],
        horizontal=True,
        key=widget_key,
        label_visibility="visible",
    )

    estado = estados[selected_key]

    st.info(estado.get("resumo", ""))

    col1, col2 = st.columns([1.6, 1])

    with col1:
        _simple_energy_diagram(selected_key)

        fluxos = estado.get("fluxos", [])
        observacoes = estado.get("observacoes", [])

        if fluxos:
            st.markdown(
                _flow_card("Caminho da energia", fluxos),
                unsafe_allow_html=True,
            )

        if observacoes:
            st.markdown(
                _flow_card("O que observar", observacoes),
                unsafe_allow_html=True,
            )

    with col2:
        indicadores = estado.get("indicadores", {})
        if indicadores:
            st.markdown("**Indicadores do estado**")
            html = "".join(
                _status_badge(label.capitalize(), value)
                for label, value in indicadores.items()
            )
            st.markdown(html, unsafe_allow_html=True)

    if pergunta_guiada:
        st.markdown(
            f"""
            <div style="
                border-left:4px solid #14B8A6;
                padding:0.75rem 0.9rem;
                margin-top:0.6rem;
                border-radius:6px;
            ">
                <strong>Pergunta guiada:</strong><br>
                {pergunta_guiada}
            </div>
            """,
            unsafe_allow_html=True,
        )