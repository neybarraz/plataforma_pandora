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
        Neste semestre será investigado um <strong>sistema didático de energia de reserva</strong>,
        construído para representar, em pequena escala, o funcionamento de um no-break.
        O sistema é formado por uma bateria de telefone celular, um módulo de carregamento,
        um conversor de tensão e uma placa de LED que atua como carga elétrica.

        Esse sistema será utilizado como problema central da disciplina para analisar,
        de forma aplicada, como conceitos de eletricidade e magnetismo aparecem em um
        dispositivo tecnológico real. Em vez de estudar os conceitos de forma isolada,
        a proposta é compreender como eles se articulam para permitir armazenamento de
        energia, controle de tensão e continuidade de alimentação da carga quando a fonte
        principal é interrompida.

        Ao longo do estudo, os estudantes irão observar o circuito, levantar dados,
        interpretar o papel físico de cada componente e construir explicações técnicas
        fundamentadas em conceitos do eletromagnetismo. O ambiente digital servirá como
        espaço de investigação, registro, análise e consolidação das decisões tomadas
        durante o processo.
        """
    )


def pagina_2() -> None:
    _titulo_destaque(
        "Metodologia: investigação do sistema + validação conceitual",
        nivel=3,
    )

    _texto_justificado(
        """
        A análise será desenvolvida a partir da interação direta com o sistema didático.
        Os estudantes poderão observar o comportamento do circuito em funcionamento,
        realizar medições elétricas, comparar estados de operação e discutir o papel
        dos principais componentes presentes no sistema.

        Como o foco da disciplina não é a montagem eletrônica em si, a investigação estará
        centrada na <strong>física envolvida no funcionamento</strong> do dispositivo.
        Isso inclui a interpretação da corrente elétrica no circuito, a regulação da tensão,
        o armazenamento de energia na bateria, a atuação do capacitor e o papel do indutor
        no conversor de tensão.

        Além das observações experimentais, serão utilizados recursos digitais, imagens,
        vídeos e simulações para tornar visíveis processos internos do circuito que não
        podem ser observados diretamente, especialmente aqueles relacionados aos campos
        elétricos e magnéticos.
        """
    )

    _show_image(
        "im_05_01.png",
        "Sistema de energia de reserva com bateria Li-ion (3,7 V), carregador TP4056 e conversor LM2596 que regula a saída para 5 V, garantindo alimentação estável do circuito.",
    )


def pagina_3() -> None:
    _titulo_destaque("Investigação inicial — funcionamento físico do sistema", nivel=2)

    _titulo_destaque("Objetivo", nivel=4)

    _texto_justificado(
        """
        Compreender como o sistema mantém a alimentação da carga mesmo quando a fonte
        externa é interrompida, identificando quais fenômenos físicos explicam o papel
        da bateria, do carregador, do conversor de tensão e da placa de LED no conjunto.
        """
    )

    st.info(
        "Como os fenômenos do eletromagnetismo explicam o funcionamento do sistema de energia de reserva?"
    )

    _titulo_destaque("O que observar na investigação", nivel=4)

    _lista_justificada(
        [
            "Tensão nominal da bateria e sua função como elemento de armazenamento de energia",
            "Presença do módulo TP4056 e sua relação com o carregamento controlado da bateria",
            "Conversor LM2596 e sua função na regulação da tensão de saída",
            "Comportamento da placa de LED quando a fonte externa está conectada ou desconectada",
            "Possíveis pontos de medição de tensão e corrente no circuito",
        ]
    )

    _titulo_destaque("Conceitos aplicados", nivel=4)

    _lista_justificada(
        [
            "Carga elétrica, corrente elétrica e diferença de potencial",
            "Circuitos elétricos e transferência de energia",
            "Capacitância e armazenamento de energia em campo elétrico",
            "Campo magnético gerado por corrente elétrica em condutores e indutores",
            "Lei de Ampère no entendimento do indutor presente no conversor",
            "Lei de Faraday associada à variação de corrente e indução no circuito",
            "Relação entre fenômenos eletromagnéticos e funcionamento de dispositivos tecnológicos",
        ]
    )

    _titulo_destaque("Validação no sistema didático", nivel=4)

    _lista_justificada(
        [
            "Medição experimental da tensão da bateria",
            "Medição da tensão de saída do conversor",
            "Observação do comportamento da carga com e sem fonte externa",
            "Comparação entre o que é observado no circuito e a explicação física proposta",
        ]
    )


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
            "id": "investigacao_inicial",
            "titulo_menu": "Investigação inicial",
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