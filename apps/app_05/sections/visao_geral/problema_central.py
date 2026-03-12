# apps/app_05/sections/visao_geral/problema_central.py
from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = APP_DIR / "assets"


# -----------------------------
# UTILIDADES
# -----------------------------

def _show_image(filename: str, caption: str, column) -> None:
    image_path = ASSETS_DIR / filename
    if image_path.exists():
        column.image(image_path, caption=caption, use_container_width=True)


def _titulo_destaque(texto: str, nivel: int = 2) -> None:
    tamanhos = {1: "2.2rem", 2: "1.8rem", 3: "1.35rem", 4: "1.15rem"}
    tamanho = tamanhos.get(nivel, "1.2rem")

    st.markdown(
        f"""
        <div style="
        font-size:{tamanho};
        font-weight:700;
        color:#14B8A6;
        margin-top:0.6rem;
        margin-bottom:0.8rem;">
        {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _texto_justificado(texto: str) -> None:
    st.markdown(
        f"""
        <div style="text-align:justify;">
        {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _lista_justificada(itens: list[str]) -> None:
    html_itens = "".join(f"<li>{i}</li>" for i in itens)

    st.markdown(
        f"""
        <div style="text-align:justify;">
        <ul>{html_itens}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# BARRA DE PROGRESSO
# -----------------------------

def progresso(etapa: int) -> None:
    cores = []

    for i in range(3):
        if i < etapa:
            cores.append("#22c55e")  # verde
        elif i == etapa:
            cores.append("#f59e0b")  # laranja
        else:
            cores.append("#e5e7eb")  # cinza

    st.markdown(
        f"""
        <div style="display:flex; gap:8px; margin-bottom:10px;">
            <div style="flex:1;height:10px;background:{cores[0]};border-radius:5px"></div>
            <div style="flex:1;height:10px;background:{cores[1]};border-radius:5px"></div>
            <div style="flex:1;height:10px;background:{cores[2]};border-radius:5px"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# CONTEÚDO DAS ETAPAS
# -----------------------------

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
    _titulo_destaque("Metodologia: investigação do sistema + validação conceitual", nivel=3)

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
    col1 = st.columns(1)[0]

    _show_image(
        "im_05_01.png",
        "Sistema de energia de reserva com bateria Li-ion (3,7 V), carregador TP4056 e conversor LM2596 que regula a saída para 5 V, garantindo alimentação estável do circuito.",
        col1
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

    # _titulo_destaque("Apoio visual — o que registrar", nivel=4)

    # col1, col2 = st.columns(2)

    # _show_image("bateria_01.png", "Bateria utilizada no sistema didático.", col1)
    # _show_image("tp4056_01.png", "Módulo de carregamento TP4056.", col2)

    # col3, col4 = st.columns(2)

    # _show_image("lm2596_01.png", "Conversor de tensão LM2596.", col3)
    # _show_image("led_01.png", "Placa de LED utilizada como carga.", col4)


# -----------------------------
# RENDER PRINCIPAL
# -----------------------------

def render_problema_central() -> None:
    if "etapa_pc" not in st.session_state:
        st.session_state.etapa_pc = 0

    etapa = st.session_state.etapa_pc

    progresso(etapa)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if etapa > 0:
            if st.button("⬅ Voltar"):
                st.session_state.etapa_pc -= 1
                st.rerun()

    with col2:
        st.markdown(
            f"<div style='text-align:center;font-weight:600;'>Etapa {etapa + 1}/3</div>",
            unsafe_allow_html=True,
        )

    with col3:
        if etapa < 2:
            if st.button("Próximo ➜"):
                st.session_state.etapa_pc += 1
                st.rerun()

    if etapa == 0:
        pagina_1()
    elif etapa == 1:
        pagina_2()
    elif etapa == 2:
        pagina_3()