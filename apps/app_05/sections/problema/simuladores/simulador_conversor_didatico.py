# simulador_conversor_didatico.py
from __future__ import annotations

import math
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


@st.cache_data(show_spinner=False)
def _calc_waveforms(
    vin: float,
    duty: float,
    freq_khz: float,
    L_uh: float,
    C_uf: float,
    load_ohm: float,
    n_cycles: int = 6,
    points_per_cycle: int = 250,
) -> dict:

    freq = freq_khz * 1e3
    period = 1.0 / freq
    total_time = n_cycles * period
    n_points = n_cycles * points_per_cycle

    t = np.linspace(0.0, total_time, n_points)

    L = L_uh * 1e-6
    C = C_uf * 1e-6

    # Modelo didático da saída
    vout_ideal = vin / max(1e-6, (1.0 - duty))
    vout_target = 1.5 + duty * (35.0 - 1.5)

    i_load = vout_target / max(load_ohm, 1e-6)

    delta_i = (vin * max(duty, 1e-6)) / max(L * freq, 1e-9)
    delta_i *= 0.18

    iL = np.zeros_like(t)
    B = np.zeros_like(t)
    qC = np.zeros_like(t)
    vout = np.zeros_like(t)

    kB = 1.0

    delta_v = i_load / max(C * freq, 1e-9)
    delta_v *= 0.08

    for idx, tt in enumerate(t):

        tau = (tt % period) / period

        if tau < duty:
            frac = tau / max(duty, 1e-9)
            iL[idx] = (i_load - delta_i / 2.0) + frac * delta_i
        else:
            frac = (tau - duty) / max((1.0 - duty), 1e-9)
            iL[idx] = (i_load + delta_i / 2.0) - frac * delta_i

        B[idx] = kB * iL[idx]

        vc = vout_target + 0.5 * delta_v * math.sin(2 * math.pi * freq * tt)

        qC[idx] = C * vc
        vout[idx] = vc

    return {
        "t_ms": t * 1e3,
        "iL": iL,
        "B": B,
        "qC_uc": qC * 1e6,
        "vout": vout,
        "vout_target": vout_target,
        "vout_ideal": vout_ideal,
        "i_load": i_load,
        "delta_i": delta_i,
        "delta_v": delta_v,
    }


def _plot_signal(
    x,
    y,
    xlabel: str,
    ylabel: str,
    title: str,
    xlim: tuple | None = None,
    ylim: tuple | None = None,
):

    fig, ax = plt.subplots(figsize=(8, 3.2))

    ax.plot(x, y)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if xlim:
        ax.set_xlim(xlim)

    if ylim:
        ax.set_ylim(ylim)

    ax.grid(True, alpha=0.3)

    st.pyplot(fig, clear_figure=True)
    plt.close(fig)


def _draw_converter_diagram(vin: float, vout: float, duty: float):

    st.markdown("### Esquema didático do conversor")

    col1, col2, col3, col4, col5 = st.columns([1.4, 0.8, 1.1, 0.8, 1.2])

    with col1:
        st.metric("Entrada (bateria)", f"{vin:.2f} V")

    with col2:
        st.markdown(
            """
            <div style="text-align:center;font-size:1.8rem;padding-top:1.2rem;">
            ➜
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div style="border:1px solid #888;border-radius:10px;padding:12px;text-align:center;">
            <strong>Conversor</strong><br>
            Duty cycle: {duty:.2f} ({duty*100:.0f}%)
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div style="text-align:center;font-size:1.8rem;padding-top:1.2rem;">
            ➜
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col5:
        st.metric("Saída (carga)", f"{vout:.2f} V")


def render_simulador_conversor_didatico() -> None:

    st.subheader("Simulador didático do conversor")

    st.markdown(
        """
Este simulador mostra, de forma qualitativa, como um conversor chaveado reorganiza a energia elétrica.

Observe a relação entre:

- corrente no indutor  
- campo magnético  
- carga no capacitor  
- tensão de saída
"""
    )

    st.markdown("### Parâmetros do simulador")

    col_a, col_b = st.columns(2)

    with col_a:
        vin = st.slider("Tensão da bateria (V)", 3.0, 4.2, 3.7, 0.1)
        duty = st.slider("Duty cycle", 0.00, 1.00, 0.35, 0.01)
        freq_khz = st.slider("Frequência de chaveamento (kHz)", 20, 180, 52, 1)

    with col_b:
        L_uh = st.slider("Indutância (µH)", 10, 220, 47, 1)
        C_uf = st.slider("Capacitância (µF)", 10, 470, 220, 5)
        load_ohm = st.slider("Carga equivalente (Ω)", 5, 100, 22, 1)

    st.info(
        """
**O que é duty cycle?**
É a fração do tempo em que a chave eletrônica permanece ligada durante cada ciclo de operação.
"""
    )

    data = _calc_waveforms(
        vin,
        duty,
        freq_khz,
        L_uh,
        C_uf,
        load_ohm,
    )

    _draw_converter_diagram(
        vin,
        data["vout_target"],
        duty,
    )

    st.markdown("### Leituras principais")

    metricas = [
        ("Tensão de saída", f"{data['vout_target']:.2f} V"),
        ("Corrente média na carga", f"{data['i_load']:.2f} A"),
        ("Ripple de corrente no indutor", f"{data['delta_i']:.3f} A"),
        ("Ripple da tensão", f"{data['delta_v']:.3f} V"),
    ]

    for i in range(0, len(metricas), 2):
        col1, col2 = st.columns(2)
        col1.metric(*metricas[i])

        if i + 1 < len(metricas):
            col2.metric(*metricas[i + 1])

    st.markdown("### Visualização dos processos físicos")

    x_limits = (data["t_ms"][0], data["t_ms"][-1])

    y_limits_iL = (-1, 10)
    y_limits_B = (-1, 10)
    y_limits_qC = (-1000, 18000)
    y_limits_vout = (0, 37)

    col1, col2 = st.columns(2)

    with col1:
        _plot_signal(
            data["t_ms"],
            data["iL"],
            "Tempo (ms)",
            "Corrente (A)",
            "Corrente no indutor",
            x_limits,
            y_limits_iL,
        )
        st.caption(
            "Interpretação: quando a corrente aumenta no indutor, energia é armazenada no campo magnético."
        )

    with col2:
        _plot_signal(
            data["t_ms"],
            data["B"],
            "Tempo (ms)",
            "Campo magnético",
            "Campo magnético no indutor",
            x_limits,
            y_limits_B,
        )
        st.caption(
            "Interpretação: o campo magnético acompanha a corrente elétrica no enrolamento do indutor."
        )

    col3, col4 = st.columns(2)

    with col3:
        _plot_signal(
            data["t_ms"],
            data["qC_uc"],
            "Tempo (ms)",
            "Carga (µC)",
            "Carga no capacitor",
            x_limits,
            y_limits_qC,
        )
        st.caption(
            "Interpretação: o capacitor armazena carga elétrica e ajuda a estabilizar a tensão do circuito."
        )

    with col4:
        _plot_signal(
            data["t_ms"],
            data["vout"],
            "Tempo (ms)",
            "Tensão (V)",
            "Tensão de saída",
            x_limits,
            y_limits_vout,
        )
        st.caption(
            "Interpretação: a tensão de saída apresenta pequena ondulação devido ao chaveamento do conversor."
        )


if __name__ == "__main__":

    st.set_page_config(
        page_title="Simulador didático do conversor",
        layout="wide",
    )

    render_simulador_conversor_didatico()