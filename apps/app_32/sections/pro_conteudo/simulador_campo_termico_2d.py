from __future__ import annotations

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# =========================
# UTIL
# =========================
def _to_float(valor, default):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return default


# =========================
# FUNÇÃO PRINCIPAL
# =========================
def render_gradiente_termico() -> None:

    # =========================
    # DIMENSÕES
    # =========================
    Lx = _to_float(st.session_state.get("problema_problema.01.001.0101"), 10.0)
    Ly = _to_float(st.session_state.get("problema_problema.01.001.0102"), 7.0)

    # =========================
    # TEMPERATURA DO AR (Ta)
    # =========================
    Ta = {
        "NO": _to_float(st.session_state.get("problema_problema.01.001.1002"), 25),
        "NE": _to_float(st.session_state.get("problema_problema.01.001.1003"), 25),
        "SO": _to_float(st.session_state.get("problema_problema.01.001.1004"), 25),
        "SE": _to_float(st.session_state.get("problema_problema.01.001.1005"), 25),
        "C":  _to_float(st.session_state.get("problema_problema.01.001.1006"), 25),
    }

    # =========================
    # TEMPERATURA DAS PAREDES (Ts)
    # =========================
    Ts = {
        "N1": _to_float(st.session_state.get("problema_problema.01.001.1007"), 25),
        "N2": _to_float(st.session_state.get("problema_problema.01.001.1008"), 25),
        "L1": _to_float(st.session_state.get("problema_problema.01.001.1009"), 25),
        "L2": _to_float(st.session_state.get("problema_problema.01.001.1010"), 25),
        "S1": _to_float(st.session_state.get("problema_problema.01.001.1011"), 25),
        "S2": _to_float(st.session_state.get("problema_problema.01.001.1012"), 25),
        "O1": _to_float(st.session_state.get("problema_problema.01.001.1013"), 25),
        "O2": _to_float(st.session_state.get("problema_problema.01.001.1014"), 25),
    }

    # =========================
    # MALHA
    # =========================
    nx, ny = 120, 120
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    X, Y = np.meshgrid(x, y)

    eps = 1e-6

    # =========================
    # PONTOS DE CONTROLE (ESSENCIAL)
    # =========================
    pontos = [
        # centro
        (0.5*Lx, 0.5*Ly, Ta["C"]),
        (0.15*Lx, 0.15*Ly, Ta["SO"]),
        (0.15*Lx, 0.85*Ly, Ta["NO"]),
        (0.85*Lx, 0.85*Ly, Ta["NE"]),
        (0.85*Lx, 0.15*Ly, Ta["SE"]),


        # norte
        (0.25*Lx, Ly, Ts["N1"]),
        (0.75*Lx, Ly, Ts["N2"]),

        # sul
        (0.25*Lx, 0, Ts["S1"]),
        (0.75*Lx, 0, Ts["S2"]),

        # oeste
        (0, 0.75*Ly, Ts["O1"]),
        (0, 0.25*Ly, Ts["O2"]),

        # leste
        (Lx, 0.75*Ly, Ts["L1"]),
        (Lx, 0.25*Ly, Ts["L2"]),
    ]

    # =========================
    # INTERPOLAÇÃO IDW
    # =========================
    T_total = np.zeros_like(X)
    peso_total = np.zeros_like(X)

    for px, py, temp in pontos:
        dist = np.sqrt((X - px)**2 + (Y - py)**2) + eps
        w = 1 / dist**2

        T_total += temp * w
        peso_total += w

    T_total = T_total / peso_total

    # =========================
    # PLOT
    # =========================
    fig, ax = plt.subplots(figsize=(6, 5))

    c = ax.contourf(X, Y, T_total, levels=120, cmap="coolwarm")

    ax.set_aspect("equal")
    ax.set_xlim(0, Lx)
    ax.set_ylim(0, Ly)

    fig.colorbar(c, ax=ax, label="T (°C)")

    st.pyplot(fig)
    plt.close(fig)