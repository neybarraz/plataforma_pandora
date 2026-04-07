import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render_simulador_radiacao():

    st.subheader("Simulador: Influência das Superfícies")

    st.write(
        "Este simulador mostra como a temperatura das superfícies afeta a troca de calor "
        "por radiação com o corpo humano, mesmo quando a temperatura do ar permanece constante."
    )

    # ---------------------------
    # PARÂMETROS FIXOS
    # ---------------------------
    
    sigma = 5.67e-8  # W/(m²·K⁴)
    epsilon = 0.95   # emissividade efetiva (corpo + parede)
    T_corpo = 34     # °C (temperatura típica da pele)
    A = 1.8          # m² (área superficial corporal aproximada)

    # ---------------------------
    # CONTROLE
    # ---------------------------

    T_parede = st.slider( "Temperatura da parede (°C)", 0, 100, 24 )

    # ---------------------------
    # MODELO CORRETO
    # ---------------------------

    T_parede_K = T_parede + 273.15
    T_corpo_K = T_corpo + 273.15

    # Fluxo radiativo líquido (W)
    q_rad = epsilon * sigma * A * (T_parede_K**4 - T_corpo_K**4)

    # Fluxo por área (W/m²) para exibição
    q_rad_area = q_rad / A

    # ---------------------------
    # RESULTADOS
    # ---------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Temperatura do corpo", f"{T_corpo} °C")

    with col2:
        st.metric("Temperatura da parede", f"{T_parede} °C")

    # with col3:
    #     st.metric("Emissividade", f"{epsilon}")
    with col3:
        st.metric("Fluxo radioativo", f"{q_rad_area:.0f} W/m²")

    # st.markdown("---")

    # st.markdown(f"### Fluxo radiativo líquido: **{q_rad:.1f} W** (≈ {q_rad_area:.0f} W/m²)")

    # ---------------------------
    # INTERPRETAÇÃO
    # ---------------------------

    if T_parede > T_corpo:
        st.error(f"⚠️ Parede mais quente que o corpo: calor flui da parede para o corpo. \n\n Ganho de {q_rad:.0f} W.")
    elif T_parede < T_corpo:
        st.info(f"❄️ Parede mais fria que o corpo: calor flui do corpo para a parede. \n\n Perda de {abs(q_rad):.0f} W.")
    else:
        st.success("✅ Equilíbrio radiativo: parede e corpo na mesma temperatura")

    # ---------------------------
    # GRÁFICO
    # ---------------------------

    T_range = np.linspace(0, 100, 100)
    T_range_K = T_range + 273.15
    q_range = epsilon * sigma * A * (T_range_K**4 - T_corpo_K**4)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(T_range, q_range, linewidth=2, color='darkred')
    ax.axhline(0, color='gray', linestyle='--', linewidth=1)
    ax.axvline(T_corpo, color='gray', linestyle='--', linewidth=1, label=f'T_corpo = {T_corpo}°C')
    ax.scatter(T_parede, q_rad, c='red', s=150, zorder=5, edgecolors='black')

    ax.set_xlabel("Temperatura da parede (°C)")
    ax.set_ylabel("Fluxo radiativo líquido (W)")
    ax.set_title("Troca de calor por radiação entre corpo e parede")
    ax.legend()
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)
