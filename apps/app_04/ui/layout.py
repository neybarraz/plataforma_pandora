from __future__ import annotations

import streamlit as st


# ============================================================
# TOKENS VISUAIS
# ============================================================

RADIUS = "8px"

MENU_1_HEIGHT = "34px"   # principal
MENU_2_HEIGHT = "32px"   # secundário
MENU_3_HEIGHT = "28px"   # lateral

GRID_LATERAL = [1.05, 2.6]
GRID_GAP = "medium"


# ============================================================
# PALETA
# Uma única cor-base (azul), em três intensidades.
# Menu 1 = mais forte
# Menu 2 = médio
# Menu 3 = mais suave
# ============================================================

LIGHT_TOKENS = {
    "menu_1_bg": "#1E3A8A",
    "menu_1_bg_hover": "#1D4ED8",
    "menu_1_text": "#FFFFFF",
    "menu_1_border": "#1E3A8A",

    "menu_2_bg": "#2563EB",
    "menu_2_bg_hover": "#1D4ED8",
    "menu_2_text": "#FFFFFF",
    "menu_2_border": "#2563EB",

    "menu_3_bg": "#DBEAFE",
    "menu_3_bg_hover": "#BFDBFE",
    "menu_3_text": "#172554",
    "menu_3_border": "#60A5FA",

    "menu_inactive_text_on_dark": "rgba(255,255,255,0.92)",
    "menu_inactive_text_on_light": "#1E3A8A",
    "menu_inactive_border_strong": "#60A5FA",
    "menu_inactive_border_soft": "#93C5FD",
    "menu_inactive_hover_soft": "rgba(37,99,235,0.10)",

    "menu_shadow_soft": "0 0 0 1px rgba(37,99,235,0.10)",
    "menu_shadow_active": "0 1px 2px rgba(30,58,138,0.18)",

    "topo_text": "#111827",
    "titulo_destaque": "#3B82F6",
    "content_header": "0.95rem",
    "subtitulo_bloco": "0.78rem",
    "progress_fill": "#3B82F6",
}

DARK_TOKENS = {
    "menu_1_bg": "#1D4ED8",
    "menu_1_bg_hover": "#2563EB",
    "menu_1_text": "#FFFFFF",
    "menu_1_border": "#3B82F6",

    "menu_2_bg": "#2563EB",
    "menu_2_bg_hover": "#3B82F6",
    "menu_2_text": "#FFFFFF",
    "menu_2_border": "#60A5FA",

    "menu_3_bg": "#0F2E6E",
    "menu_3_bg_hover": "#1E3A8A",
    "menu_3_text": "#EFF6FF",
    "menu_3_border": "#3B82F6",

    "menu_inactive_text_on_dark": "rgba(255,255,255,0.94)",
    "menu_inactive_text_on_light": "#1E3A8A",
    "menu_inactive_border_strong": "rgba(96,165,250,0.88)",
    "menu_inactive_border_soft": "rgba(96,165,250,0.72)",
    "menu_inactive_hover_soft": "rgba(59,130,246,0.16)",

    "menu_shadow_soft": "0 0 0 1px rgba(96,165,250,0.14)",
    "menu_shadow_active": "0 1px 3px rgba(0,0,0,0.35)",

    "topo_text": "#FFFFFF",
    "titulo_destaque": "#60A5FA",
    "content_header": "0.95rem",
    "subtitulo_bloco": "0.78rem",
    "progress_fill": "#3B82F6",
}


# ============================================================
# HELPERS DE CSS
# ============================================================

def _css_vars() -> str:
    light = "\n".join(
        f"        --{k.replace('_', '-')}: {v};" for k, v in LIGHT_TOKENS.items()
    )
    dark = "\n".join(
        f"            --{k.replace('_', '-')}: {v};" for k, v in DARK_TOKENS.items()
    )

    return f"""
    :root {{
{light}
        --radius-default: {RADIUS};
        --menu-1-height: {MENU_1_HEIGHT};
        --menu-2-height: {MENU_2_HEIGHT};
        --menu-3-height: {MENU_3_HEIGHT};
    }}

    @media (prefers-color-scheme: dark) {{
        :root {{
{dark}
        }}
    }}
    """


def _css_topo(class_name: str) -> str:
    return f"""
    .{class_name} {{
        padding: 0.2rem 0 0.8rem 0;
        margin-bottom: 0.8rem;
        background: transparent;
        border: none;
        color: var(--topo-text);
    }}

    .{class_name} strong,
    .{class_name} p,
    .{class_name} div,
    .{class_name} span {{
        color: var(--topo-text) !important;
    }}
    """


def _css_progress() -> str:
    return """
    div[data-testid="stProgressBar"] > div > div > div {
        background-color: var(--progress-fill) !important;
    }
    """


def _css_button_group(
    container_key: str,
    *,
    level: int,
    align: str = "center",
    compact_margin: bool = False,
) -> str:
    if level == 1:
        active_bg = "var(--menu-1-bg)"
        active_bg_hover = "var(--menu-1-bg-hover)"
        active_text = "var(--menu-1-text)"
        active_border = "var(--menu-1-border)"
        inactive_border = "var(--menu-inactive-border-strong)"
        inactive_text_light = "var(--menu-inactive-text-on-light)"
        inactive_text_dark = "var(--menu-inactive-text-on-dark)"
        height_var = "var(--menu-1-height)"
        font_size = "0.90rem"
        font_weight = "700"
    elif level == 2:
        active_bg = "var(--menu-2-bg)"
        active_bg_hover = "var(--menu-2-bg-hover)"
        active_text = "var(--menu-2-text)"
        active_border = "var(--menu-2-border)"
        inactive_border = "var(--menu-inactive-border-strong)"
        inactive_text_light = "var(--menu-inactive-text-on-light)"
        inactive_text_dark = "var(--menu-inactive-text-on-dark)"
        height_var = "var(--menu-2-height)"
        font_size = "0.84rem"
        font_weight = "600"
    else:
        active_bg = "var(--menu-3-bg)"
        active_bg_hover = "var(--menu-3-bg-hover)"
        active_text = "var(--menu-3-text)"
        active_border = "var(--menu-3-border)"
        inactive_border = "var(--menu-inactive-border-soft)"
        inactive_text_light = "var(--menu-inactive-text-on-light)"
        inactive_text_dark = "var(--menu-inactive-text-on-dark)"
        height_var = "var(--menu-3-height)"
        font_size = "0.80rem"
        font_weight = "600"

    justify = "flex-start" if align == "left" else "center"
    text_align = "left" if align == "left" else "center"
    inner_padding = "0 0.70rem" if align == "left" else "0 0.55rem"
    block_margin = "0 0 0.20rem 0" if compact_margin else "0 0 0.30rem 0"

    return f"""
    .st-key-{container_key} div[data-testid="stButton"] {{
        margin: {block_margin} !important;
        padding: 0 !important;
    }}

    .st-key-{container_key} button {{
        border-radius: var(--radius-default) !important;
        padding: {inner_padding} !important;
        height: {height_var} !important;
        min-height: {height_var} !important;
        width: 100% !important;
        text-align: {text_align} !important;
        justify-content: {justify} !important;
        box-shadow: var(--menu-shadow-soft) !important;
        transition:
            background-color 0.15s ease,
            border-color 0.15s ease,
            box-shadow 0.15s ease !important;
    }}

    .st-key-{container_key} button > div {{
        padding: 0 !important;
        margin: 0 !important;
        height: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: {justify} !important;
    }}

    .st-key-{container_key} button p {{
        margin: 0 !important;
        font-size: {font_size} !important;
        font-weight: {font_weight} !important;
        line-height: 1.05 !important;
        letter-spacing: 0.01em !important;
        text-align: {text_align} !important;
    }}

    .st-key-{container_key} button[kind="primary"] {{
        background: {active_bg} !important;
        color: {active_text} !important;
        border: 1px solid {active_border} !important;
        box-shadow: var(--menu-shadow-active) !important;
    }}

    .st-key-{container_key} button[kind="primary"] p {{
        color: {active_text} !important;
    }}

    .st-key-{container_key} button[kind="primary"]:hover {{
        background: {active_bg_hover} !important;
        border: 1px solid {active_bg_hover} !important;
    }}

    .st-key-{container_key} button[kind="secondary"] {{
        background: transparent !important;
        color: {inactive_text_light} !important;
        border: 1px solid {inactive_border} !important;
    }}

    .st-key-{container_key} button[kind="secondary"] p {{
        color: {inactive_text_light} !important;
    }}

    .st-key-{container_key} button[kind="secondary"]:hover {{
        background: var(--menu-inactive-hover-soft) !important;
        border-color: {active_border} !important;
        box-shadow: var(--menu-shadow-active) !important;
    }}

    @media (prefers-color-scheme: dark) {{
        .st-key-{container_key} button[kind="secondary"] {{
            color: {inactive_text_dark} !important;
        }}

        .st-key-{container_key} button[kind="secondary"] p {{
            color: {inactive_text_dark} !important;
        }}
    }}
    """


def _css_auxiliary_classes(prefix: str) -> str:
    return f"""
    .{prefix}-nav-titulo {{
        font-weight: 700;
        font-size: 0.95rem;
        margin: 0.05rem 0 0.35rem 0;
    }}

    .{prefix}-subtitulo-bloco {{
        font-size: var(--subtitulo-bloco);
        font-weight: 600;
        margin: 0.35rem 0 0.2rem 0;
        opacity: 0.9;
    }}

    .{prefix}-content-header {{
        font-weight: 700;
        font-size: var(--content-header);
        margin: 0.05rem 0 0.5rem 0;
    }}
    """


# ============================================================
# API PÚBLICA
# ============================================================

def inject_global_layout_css() -> None:
    """
    Injeta tokens visuais globais e barra de progresso.
    Seguro para chamar em qualquer tela.
    """
    st.markdown(
        f"""
        <style>
        {_css_vars()}
        {_css_progress()}
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_topo_css(class_name: str) -> None:
    st.markdown(
        f"""
        <style>
        {_css_vars()}
        {_css_topo(class_name)}
        {_css_progress()}
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_menu_css(
    *,
    main_menu_key: str | None = None,
    submenu_key: str | None = None,
    sidebar_key: str | None = None,
) -> None:
    """
    Injeta estilos dos 3 níveis de menu, conforme os containers existentes.
    Não altera estado nem widgets.
    """
    chunks: list[str] = [_css_vars(), _css_progress()]

    if main_menu_key:
        chunks.append(
            _css_button_group(
                main_menu_key,
                level=1,
                align="center",
                compact_margin=False,
            )
        )

    if submenu_key:
        chunks.append(
            _css_button_group(
                submenu_key,
                level=2,
                align="center",
                compact_margin=False,
            )
        )

    if sidebar_key:
        chunks.append(
            _css_button_group(
                sidebar_key,
                level=3,
                align="left",
                compact_margin=True,
            )
        )

    st.markdown(
        f"""
        <style>
        {''.join(chunks)}
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_section_layout_css(
    *,
    prefix: str,
    topo_class: str | None = None,
    macro_tabs_key: str | None = None,
    sidebar_key: str | None = None,
) -> None:
    """
    Ponto de entrada para etapas como problema, investigação, solução e memorial.
    """
    chunks: list[str] = [_css_vars(), _css_progress(), _css_auxiliary_classes(prefix)]

    if topo_class:
        chunks.append(_css_topo(topo_class))

    if macro_tabs_key:
        chunks.append(
            _css_button_group(
                macro_tabs_key,
                level=2,
                align="center",
                compact_margin=False,
            )
        )

    if sidebar_key:
        chunks.append(
            _css_button_group(
                sidebar_key,
                level=3,
                align="left",
                compact_margin=True,
            )
        )

    st.markdown(
        f"""
        <style>
        {''.join(chunks)}
        </style>
        """,
        unsafe_allow_html=True,
    )


def layout_duas_colunas():
    """
    Grid visual padrão já usado nas etapas.
    Não cria conteúdo; só retorna as colunas.
    """
    return st.columns(GRID_LATERAL, gap=GRID_GAP)


def render_topo_html(class_name: str, html: str) -> None:
    st.markdown(
        f'<div class="{class_name}">{html}</div>',
        unsafe_allow_html=True,
    )


def render_titulo_destaque(texto: str, nivel: int = 2) -> None:
    tamanhos = {1: "1.55rem", 2: "1.35rem", 3: "1.18rem", 4: "1.0rem"}
    tamanho = tamanhos.get(nivel, "1.0rem")

    st.markdown(
        f"""
        <div style="
        font-size:{tamanho};
        font-weight:700;
        color:var(--titulo-destaque);
        margin-top:0.35rem;
        margin-bottom:0.45rem;
        line-height:1.15;">
        {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_texto_bloco(texto: str) -> None:
    st.markdown(
        f"""
        <div style="text-align:justify; line-height:1.5; margin-bottom:0.35rem;">
        {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_percentual_conclusao(percentual: int) -> None:
    st.markdown(
        f"""
        <div style="
        text-align:center;
        font-size:0.7rem;
        margin-top:-0.15rem;
        line-height:1;">
        {percentual}% concluído
        </div>
        """,
        unsafe_allow_html=True,
    )
