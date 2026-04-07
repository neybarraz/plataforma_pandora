import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render_simulador_conveccao ()-> None:

    st.subheader("Simulador: Influência da Ventilação")

    st.write(
        "Este simulador mostra como a ventilação altera o coeficiente convectivo (h) "
        "e, consequentemente, a taxa de transferência de calor entre uma superfície e o ar."
    )

    # ---------------------------
    # CONTROLES
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:
        ventilacao = st.slider( "Ventilação (0–100)", 0, 100, 20)

    with col2:
        delta_T = st.slider("ΔT (°C)", -30, 30, 10)
    # ---------------------------
    # MODELO
    # ---------------------------

    # h varia de forma não linear com ventilação (mais realista)
    h = 2 + 0.03 * (ventilacao ** 1.5)

    # fluxo de calor por m²
    q = h * delta_T

    # ---------------------------
    # RESULTADOS
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div style="
                background-color:#111;
                padding:20px;
                border-radius:10px;
                text-align:center;
            ">
                <div style="font-size:14px; color:#aaa;">
                    Coeficiente convectivo
                </div>
                <div style="font-size:28px; font-weight:bold; color:white;">
                    {h:.2f} W/(m²·K)
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style="
                background-color:#111;
                padding:20px;
                border-radius:10px;
                text-align:center;
            ">
                <div style="font-size:14px; color:#aaa;">
                    Fluxo de calor
                </div>
                <div style="font-size:28px; font-weight:bold; color:white;">
                    {q:.2f} W/m²
                </div>
            </div>
        """, unsafe_allow_html=True)

    fig, ax = plt.subplots()

    ventilacoes = np.linspace(0, 100, 100)
    h_vals = 2 + 0.03 * (ventilacoes ** 1.5)
    q_vals = h_vals * delta_T

    # ---------------------------
    # FUNDO (BASEADO NO EIXO Y)
    # ---------------------------

    y_min = -1250
    y_max = 1250

    gradient = np.linspace(y_min, y_max, 256).reshape(-1, 1)

    ax.imshow(
        gradient,
        aspect='auto',
        extent=[0, 100, y_min, y_max],
        origin='lower',
        cmap='RdYlBu_r',
        alpha=0.25
    )

    # ---------------------------
    # CURVA
    # ---------------------------

    ax.plot(ventilacoes, q_vals, linewidth=2)

    # ---------------------------
    # PONTO
    # ---------------------------

    ax.scatter(
        ventilacao,
        q,
        s=150,
        c='red',
        edgecolors='black',
        zorder=5
    )

    # ---------------------------
    # CONFIG
    # ---------------------------

    ax.set_ylim(y_min, y_max)

    ax.set_xlabel("Nível de ventilação")
    ax.set_ylabel("Fluxo de calor (W/m²)")
    ax.set_title("Influência da ventilação na transferência de calor")

    st.pyplot(fig)