import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def render_simulador_tp4056():

    st.subheader("Simulador de carga CC/CV – TP4056")

    # -----------------------------------
    # PARÂMETROS INTERATIVOS
    # -----------------------------------

    I_prog = st.slider(
        "Corrente programada (A)",
        min_value=0.05,
        max_value=3.0,
        value=1.0,
        step=0.05
    )

    V0 = st.slider(
        "Tensão inicial da bateria (V)",
        min_value=1.0,
        max_value=5.0,
        value=3.0,
        step=0.1
    )

    V_max = 4.2  # tensão limite Li-ion
    C_bat = 2000  # parâmetro fictício didático
    tau = 1500    # constante de tempo para fase CV

    t = np.linspace(0, 5000, 1000)

    V = []
    I = []

    # -----------------------------------
    # COMPORTAMENTO FÍSICO
    # -----------------------------------

    if V0 >= V_max:
        st.warning("A bateria já está acima ou no limite de 4,2 V. Não ocorre carregamento.")
        V = np.full_like(t, V0)
        I = np.zeros_like(t)

    else:
        t_cc_final = (V_max - V0) * C_bat / I_prog

        for time in t:

            if time <= t_cc_final:
                # Fase CC
                V_inst = V0 + (I_prog / C_bat) * time
                I_inst = I_prog
            else:
                # Fase CV
                V_inst = V_max
                I_inst = I_prog * np.exp(-(time - t_cc_final) / tau)

            V.append(V_inst)
            I.append(I_inst)

        V = np.array(V)
        I = np.array(I)

    # -----------------------------------
    # GRÁFICO
    # -----------------------------------

    fig, ax1 = plt.subplots()

    ax1.plot(t, V)
    ax1.set_ylabel("Tensão (V)")
    ax1.set_xlabel("Tempo")

    ax2 = ax1.twinx()
    ax2.plot(t, I)
    ax2.set_ylabel("Corrente (A)")

    plt.title("Simulação de carga CC/CV")
    st.pyplot(fig)

    # -----------------------------------
    # DIAGNÓSTICO AUTOMÁTICO
    # -----------------------------------

    if V0 < V_max:
        st.info(
            f"Fase inicial: Corrente constante de aproximadamente {I_prog:.2f} A "
            f"até a bateria atingir 4,2 V."
        )
    else:
        st.info("Nenhuma fase de carga ativa.")