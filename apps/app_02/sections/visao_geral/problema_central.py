# apps/app_02/sections/visao_geral/problema_central.py
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

def progresso(etapa):

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

def pagina_1():

    _titulo_destaque("Problema Central", nivel=1)

    _texto_justificado(
        """
        Neste semestre será desenvolvido o estudo de um sistema físico real:
        um <strong>sistema de bombeamento entre reservatórios</strong>
        localizado no Bloco dos Professores do Campus Cerro Largo.

        O sistema será utilizado como problema central para a análise técnica
        ao longo da disciplina. A partir dele, serão realizadas atividades de
        observação em campo, levantamento de dados, modelagem simplificada
        do sistema e avaliação de decisões de engenharia relacionadas ao seu
        funcionamento.

        Diferentemente de uma abordagem baseada exclusivamente em exercícios
        isolados, o curso está estruturado em torno da investigação progressiva
        de um sistema real. Cada etapa do estudo exigirá que hipóteses sejam
        formuladas, parâmetros sejam estimados e escolhas técnicas sejam
        justificadas com base em princípios de engenharia e evidências obtidas
        durante as atividades do semestre.

        O desenvolvimento dessas análises será apoiado por um ambiente digital
        de estudo, no qual os dados coletados, modelos construídos e decisões
        técnicas serão registrados e discutidos ao longo do curso.
        """
    )


def pagina_2():

    _titulo_destaque("Metodologia: visitas técnicas + validação em laboratório", nivel=3)

    _texto_justificado(
        """
        Ao longo do semestre serão realizadas visitas técnicas ao sistema
        de bombeamento com o objetivo de observar sua configuração física,
        identificar seus principais componentes e realizar o levantamento
        de informações relevantes para análise do sistema.

        Como se trata de uma instalação em operação, intervenções diretas
        no equipamento real são limitadas. Por esse motivo, medições,
        testes experimentais e validações de hipóteses serão reproduzidos
        em bancada didática no laboratório, permitindo a investigação
        controlada de fenômenos elétricos e de operação associados ao
        sistema estudado.
        """
    )
    _titulo_destaque("Vídeo introdutório do sistema real", nivel=3)

    st.video("https://www.youtube.com/watch?v=aayBM_fap0c")


def pagina_3():

    _titulo_destaque("Visitas Técnicas — Dimensionamento Elétrico", nivel=2)

    _titulo_destaque("Objetivo", nivel=4)

    _texto_justificado(
        """
        Analisar o motor do sistema de bombeamento como uma carga elétrica
        e avaliar se as condições de alimentação e instalação são coerentes
        com suas características nominais e com os princípios de
        dimensionamento elétrico.
        """
    )

    st.info(
        "A alimentação elétrica do motor está coerente com sua potência, corrente e características construtivas?"
    )

    _titulo_destaque("O que observar na visita", nivel=4)

    _lista_justificada(
        [
            "Placa do motor (potência, tensão nominal, corrente nominal e fator de potência)",
            "Tipo de alimentação do motor (monofásica ou trifásica)",
            "Distância aproximada entre o motor e o ponto de alimentação elétrica",
            "Condutores visíveis e método de instalação do circuito de alimentação",
        ]
    )

    _titulo_destaque("Conceitos aplicados", nivel=4)

    _lista_justificada(
        [
            "Potência ativa, potência aparente e fator de potência",
            "Corrente nominal e corrente de partida de motores elétricos",
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
            "Comparação entre valores calculados e valores obtidos experimentalmente",
        ]
    )

    _titulo_destaque("Apoio visual — o que registrar", nivel=4)

    col1, col2 = st.columns(2)

    _show_image("motor_01.png", "Placa de identificação do motor.", col1)
    _show_image("motor_02.png", "Tipo de alimentação do motor.", col2)

    col3, col4 = st.columns(2)

    _show_image("circuito_01.png", "Forma de acionamento do motor.", col3)
    _show_image("circuito_02.png", "Condutores e trajeto do circuito.", col4)


# -----------------------------
# RENDER PRINCIPAL
# -----------------------------

def render_problema_central():

    if "etapa_pc" not in st.session_state:
        st.session_state.etapa_pc = 0

    etapa = st.session_state.etapa_pc

    progresso(etapa)

    # Linha de navegação
    col1, col2, col3 = st.columns([1,2,1])

    with col1:

        if etapa > 0:

            if st.button("⬅ Voltar"):
                st.session_state.etapa_pc -= 1
                st.rerun()

    with col2:

        st.markdown(
            f"<div style='text-align:center;font-weight:600;'>Etapa {etapa+1}/3</div>",
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