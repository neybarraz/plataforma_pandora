from __future__ import annotations

from pathlib import Path

import streamlit as st

from ....ui.layout import (
    inject_menu_css,
    layout_duas_colunas,
    render_texto_bloco,
    render_titulo_destaque,
)

APP_DIR = Path(__file__).resolve().parents[3]
ASSETS_DIR = APP_DIR / "assets"


# ============================================================
# UTILIDADES
# ============================================================

def _inject_css() -> None:
    inject_menu_css(sidebar_key="pc_secondary_nav")


def _show_image(filename: str, caption: str = "") -> None:
    image_path = ASSETS_DIR / filename
    if image_path.exists():
        st.image(image_path, caption=caption, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: {image_path}")


def _titulo_destaque(texto: str, nivel: int = 2) -> None:
    render_titulo_destaque(texto, nivel=nivel)


def _texto_justificado(texto: str) -> None:
    render_texto_bloco(texto)


def _lista_justificada(itens: list[str]) -> None:
    html_itens = "".join(f"<li>{i}</li>" for i in itens)

    st.markdown(
        f"""
        <div style="text-align:justify; line-height:1.5; margin-bottom:0.35rem;">
            <ul>{html_itens}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CONTEÚDO DAS SEÇÕES
# ============================================================

def pagina_1() -> None:
    _titulo_destaque("Problema Central", nivel=1)

    _texto_justificado(
        """
        Neste semestre será investigado um <strong>sistema real de bombeamento entre reservatórios</strong>,
        localizado no Bloco dos Professores do Campus Cerro Largo. Esse sistema será adotado
        como problema central da disciplina, servindo como referência concreta para o desenvolvimento
        das análises técnicas ao longo do semestre.

        A proposta é utilizar o sistema como objeto de estudo para integrar observação em campo,
        levantamento de dados, modelagem simplificada e avaliação de decisões de engenharia
        associadas ao seu funcionamento. Em vez de trabalhar apenas com exercícios isolados,
        o percurso formativo estará organizado em torno da investigação progressiva de um sistema
        físico existente, com características operacionais reais.

        Ao longo do estudo, os estudantes deverão formular hipóteses, estimar parâmetros relevantes,
        interpretar informações obtidas em campo e justificar escolhas técnicas com base em princípios
        de engenharia e em evidências produzidas durante as atividades. O ambiente digital funcionará
        como espaço de registro, análise e consolidação das observações, dos modelos construídos
        e das decisões elaboradas ao longo do processo.
        """
    )


def pagina_2() -> None:
    _titulo_destaque(
        "Metodologia: visitas técnicas + validação em laboratório",
        nivel=3,
    )

    _texto_justificado(
        """
        A investigação será conduzida a partir de visitas técnicas ao sistema de bombeamento,
        com o objetivo de observar sua configuração física, identificar seus principais
        componentes e levantar informações relevantes para a análise do seu desempenho
        e das condições de operação.

        Como se trata de uma instalação em funcionamento, as possibilidades de intervenção
        direta sobre o equipamento real são limitadas. Por esse motivo, parte das medições,
        testes e verificações de hipóteses será reproduzida em bancada didática no laboratório,
        permitindo a análise controlada de fenômenos elétricos e de operação relacionados
        ao sistema estudado.

        Essa articulação entre observação em campo e validação experimental busca aproximar
        o estudo conceitual das condições reais de engenharia, permitindo que os estudantes
        comparem o comportamento observado no sistema com interpretações fundamentadas
        em modelos simplificados e em princípios técnicos.
        """
    )

    _titulo_destaque("Vídeo introdutório do sistema real", nivel=3)
    st.video("https://www.youtube.com/watch?v=aayBM_fap0c")


def pagina_3() -> None:
    _titulo_destaque("Visitas Técnicas — Dimensionamento Elétrico", nivel=2)

    _titulo_destaque("Objetivo", nivel=4)

    _texto_justificado(
        """
        Analisar o motor do sistema de bombeamento como uma carga elétrica,
        avaliando se as condições de alimentação e de instalação observadas
        são compatíveis com suas características nominais e com os critérios
        básicos de dimensionamento elétrico.
        """
    )

    st.info(
        "A alimentação elétrica do motor está coerente com sua potência, sua corrente e suas características construtivas?"
    )

    _titulo_destaque("O que observar na visita", nivel=4)

    _lista_justificada(
        [
            "Placa de identificação do motor, com atenção para potência, tensão nominal, corrente nominal e fator de potência",
            "Tipo de alimentação do motor, verificando se o sistema opera em configuração monofásica ou trifásica",
            "Distância aproximada entre o motor e o ponto de alimentação elétrica",
            "Condutores visíveis e método de instalação do circuito de alimentação",
        ]
    )

    _titulo_destaque("Conceitos aplicados", nivel=4)

    _lista_justificada(
        [
            "Potência ativa, potência aparente e fator de potência",
            "Corrente nominal e corrente de partida em motores elétricos",
            "Diferenças entre sistemas de alimentação monofásicos e trifásicos",
            "Queda de tensão em condutores elétricos",
            "Relação entre potência, corrente elétrica e rendimento do motor",
        ]
    )

    _titulo_destaque("Validação em laboratório", nivel=4)

    _lista_justificada(
        [
            "Medição experimental de tensão e corrente elétrica",
            "Estimativa da potência elétrica consumida pelo motor",
            "Comparação entre os valores calculados e os valores obtidos experimentalmente",
        ]
    )

    _titulo_destaque("Apoio visual — o que registrar", nivel=4)

    col1, col2 = st.columns(2)
    with col1:
        _show_image("motor_01.png", "Placa de identificação do motor.")
    with col2:
        _show_image("motor_02.png", "Tipo de alimentação do motor.")

    col3, col4 = st.columns(2)
    with col3:
        _show_image("circuito_01.png", "Forma de acionamento do motor.")
    with col4:
        _show_image("circuito_02.png", "Condutores e trajeto do circuito.")


# ============================================================
# ESTRUTURA DE NAVEGAÇÃO
# ============================================================

def _get_paginas() -> list[dict]:
    return [
        {
            "id": "problema_central",
            "titulo_menu": "Problema Central",
            "render": pagina_1,
        },
        {
            "id": "metodologia",
            "titulo_menu": "Metodologia",
            "render": pagina_2,
        },
        {
            "id": "dimensionamento_eletrico",
            "titulo_menu": "Dimensionamento Elétrico",
            "render": pagina_3,
        },
    ]


def _render_secondary_nav(paginas: list[dict]) -> None:
    with st.container(key="pc_secondary_nav"):
        for i, pagina in enumerate(paginas):
            if st.button(
                pagina["titulo_menu"],
                key=f"pc_secondary_{pagina['id']}",
                type="primary" if i == st.session_state.pc_pagina_idx else "secondary",
                use_container_width=True,
            ):
                st.session_state.pc_pagina_idx = i
                st.rerun()


# ============================================================
# RENDER PRINCIPAL
# ============================================================

def render_problema_central() -> None:
    _inject_css()

    paginas = _get_paginas()

    if "pc_pagina_idx" not in st.session_state:
        st.session_state.pc_pagina_idx = 0

    pagina_idx = max(0, min(st.session_state.pc_pagina_idx, len(paginas) - 1))
    st.session_state.pc_pagina_idx = pagina_idx

    pagina_atual = paginas[pagina_idx]

    col_nav, col_conteudo = layout_duas_colunas()

    with col_nav:
        _render_secondary_nav(paginas)

    with col_conteudo:
        render_fn = pagina_atual.get("render")
        if callable(render_fn):
            render_fn()


def render(ctx=None) -> None:
    del ctx
    render_problema_central()