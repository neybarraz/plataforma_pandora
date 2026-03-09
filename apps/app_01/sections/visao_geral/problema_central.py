# apps/app_01/sections/visao_geral/problema_central.py
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
        O conforto térmico em uma sala de aula está diretamente relacionado ao modo como o ambiente permite que o corpo humano 
        mantenha seu **equilíbrio térmico** durante a permanência no espaço. O corpo humano produz calor continuamente devido 
        ao metabolismo e precisa dissipar essa energia para o ambiente por meio de processos físicos como **condução, convecção 
        e radiação**. Quando as condições térmicas do ambiente favorecem esse balanço de trocas de calor, a sensação térmica 
        tende a ser confortável. Caso contrário, surgem sensações de frio ou calor excessivo.

        Em ambientes internos, como salas de aula, o conforto térmico depende principalmente da **temperatura do ar**, da 
        **temperatura das superfícies que delimitam o ambiente** (paredes, piso e teto) e da **distribuição espacial dessas temperaturas**. 
        Quando essas variáveis apresentam valores próximos e relativamente uniformes, o ambiente tende a proporcionar condições mais 
        estáveis para o equilíbrio térmico do corpo. No entanto, quando existem **gradientes de temperatura dentro da sala**, algumas 
        regiões podem tornar-se mais quentes ou mais frias do que outras, criando zonas de desconforto térmico para os ocupantes.

        Esse fenômeno pode ser influenciado por diversos fatores físicos, como a **incidência de radiação solar nas paredes**, as 
        **propriedades térmicas dos materiais da construção**, a **ventilação do ambiente** e as **trocas de calor entre o ar e as 
        superfícies internas**. Como resultado, mesmo que a temperatura média do ambiente pareça adequada, a distribuição térmica 
        pode não ser uniforme, afetando a sensação térmica em diferentes pontos da sala.

        Dessa forma, o problema central consiste em **analisar como a distribuição de temperatura no interior da sala influencia as 
        condições de conforto térmico dos ocupantes**. Para isso, é necessário observar e medir as temperaturas em diferentes pontos 
        do ambiente, construir um **campo de temperatura da sala** e identificar possíveis gradientes térmicos. A partir dessa análise, 
        torna-se possível avaliar se o ambiente apresenta condições adequadas de conforto ou se existem regiões onde o equilíbrio térmico 
        do corpo humano pode ser comprometido.
        """
    )


def pagina_2():

    _titulo_destaque("Metodologia de Análise do Campo Térmico da Sala", nivel=3)

    _texto_justificado(
        """
        A metodologia para análise do conforto térmico na sala de aula baseia-se na **observação do 
        ambiente, na coleta de dados térmicos e na análise da distribuição espacial de temperatura**. 
        O procedimento busca identificar como as condições térmicas do ambiente influenciam o equilíbrio das 
        trocas de calor entre o corpo humano e o meio, permitindo avaliar se o espaço apresenta condições 
        adequadas de conforto.

        Inicialmente é realizada a **caracterização do ambiente de estudo**. Nessa etapa são registradas as 
        principais características físicas da sala, como dimensões, orientação das paredes em relação aos pontos 
        cardeais, presença de portas e janelas e materiais predominantes das superfícies internas. Essas informações 
        são importantes porque influenciam diretamente os processos de transferência de calor no ambiente, 
        especialmente a condução através das paredes e a incidência de radiação solar.

        Em seguida é definida a **rede de pontos de medição térmica** dentro da sala. Sensores de temperatura são 
        distribuídos em diferentes posições do ambiente, representando regiões próximas às paredes norte, sul, 
        leste e oeste, além de pontos intermediários e um ponto central. Essa distribuição permite captar possíveis 
        variações espaciais de temperatura e identificar gradientes térmicos dentro do ambiente.

        Após a definição dos pontos de medição, realiza-se a **coleta de dados térmicos**. Em cada ponto são registradas 
        as temperaturas do ar e, quando possível, as temperaturas das superfícies próximas. As medições são realizadas 
        em um mesmo intervalo de tempo para garantir que os valores representem uma condição térmica comparável em toda a sala.

        Com os dados obtidos, procede-se à **organização e tratamento das informações**. As temperaturas registradas em 
        cada ponto são utilizadas para construir uma representação espacial do campo térmico do ambiente. Por meio de 
        técnicas de interpolação ou representação gráfica, é possível gerar um mapa de distribuição de temperatura 
        da sala, evidenciando regiões de maior e menor temperatura.

        A etapa seguinte consiste na **análise do campo térmico**. Nessa fase são identificadas possíveis zonas quentes 
        e frias e avaliado o gradiente térmico presente no ambiente. Os valores observados são comparados com faixas de 
        temperatura normalmente associadas ao conforto térmico em ambientes internos, permitindo avaliar se determinadas 
        regiões da sala apresentam condições favoráveis ou desfavoráveis para os ocupantes.

        Por fim, realiza-se a **interpretação dos resultados e a avaliação do conforto térmico do ambiente**. A análise da 
        distribuição de temperatura permite verificar se o ambiente apresenta condições térmicas relativamente uniformes 
        ou se existem regiões com potencial de desconforto. A partir dessa interpretação, é possível discutir os fatores 
        físicos que contribuem para o comportamento térmico observado, como incidência solar, propriedades térmicas das 
        superfícies e circulação de ar no ambiente.
        """
    )
    _titulo_destaque("Vídeo introdutório do sistema real", nivel=3)

    st.video("https://www.youtube.com/watch?v=mmesl7zwpJE")

def pagina_3():
    _titulo_destaque("Visita Técnica — Conforto Térmico em Sala de Aula", nivel=2)

    _titulo_destaque("Objetivo", nivel=4)

    _texto_justificado(
        """
        Analisar o ambiente da sala de aula sob a perspectiva das trocas de calor
        entre o corpo humano e o meio, avaliando como a distribuição de temperatura
        no espaço influencia as condições de conforto térmico dos ocupantes.
        O estudo busca identificar possíveis variações espaciais de temperatura
        e compreender os fatores físicos que contribuem para a formação de
        gradientes térmicos no ambiente.
        """
    )

    st.info(
        "A distribuição de temperatura na sala proporciona condições adequadas de conforto térmico para os ocupantes?"
    )

    _titulo_destaque("O que observar na visita", nivel=4)

    _lista_justificada(
        [
            "Dimensões gerais da sala e organização do espaço interno",
            "Orientação das paredes em relação aos pontos cardeais (Norte, Sul, Leste e Oeste)",
            "Presença e posição de portas, janelas e possíveis aberturas para ventilação",
            "Incidência de radiação solar nas paredes ou janelas durante o período de observação",
            "Distribuição dos pontos de medição de temperatura no ambiente",
        ]
    )

    _titulo_destaque("Conceitos aplicados", nivel=4)

    _lista_justificada(
        [
            "Temperatura, calor e equilíbrio térmico",
            "Transferência de calor por condução, convecção e radiação",
            "Influência das superfícies do ambiente nas trocas de calor",
            "Distribuição espacial de temperatura em ambientes internos",
            "Relação entre gradiente térmico do ambiente e conforto térmico humano",
        ]
    )

    _titulo_destaque("Validação em laboratório", nivel=4)

    _lista_justificada(
        [
            "Medição experimental da temperatura do ar em diferentes pontos da sala",
            "Registro das temperaturas das superfícies próximas aos pontos de medição",
            "Construção de um mapa de distribuição térmica do ambiente",
            "Análise do gradiente térmico interno e comparação com faixas de conforto térmico",
        ]
    )

    _titulo_destaque("Apoio visual — o que registrar", nivel=4)
    col1, col2 = st.columns(2)

    _show_image(
        "sala01.png",
        "Planta da sala com a localização dos pontos de medição utilizados na análise térmica.",
        col1
    )

    _show_image(
        "sala03.png",
        "Esquema dos processos de transferência de calor no ambiente interno da sala.",
        col2
    )

    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    _show_image(
        "sala02.png",
        "Mapa do campo térmico da sala, indicando a distribuição espacial da temperatura.",
        col_centro
    )



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