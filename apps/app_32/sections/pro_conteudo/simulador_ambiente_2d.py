from __future__ import annotations

import streamlit as st
import matplotlib.pyplot as plt


def _to_float(valor, default):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return default


def render_simulador_ambiente_2d() -> None:
    # =========================
    # CAPTURA E CONVERSÃO SEGURA
    # =========================
    Lx_raw = st.session_state.get("problema_problema.01.001.0101", 10.0)
    Ly_raw = st.session_state.get("problema_problema.01.001.0102", 7.0)

    Lx = _to_float(Lx_raw, 10.0)
    Ly = _to_float(Ly_raw, 7.0)

    # validação mínima
    if Lx <= 0 or Ly <= 0:
        st.warning("Dimensões inválidas. Verifique os valores inseridos.")
        return

    fig, ax = plt.subplots(figsize=(6, 6))

    # =========================
    # CONTORNO DA SALA
    # =========================
    ax.plot([0, Lx], [0, 0], linewidth=2, color="black")      # sul
    ax.plot([0, Lx], [Ly, Ly], linewidth=2, color="black")    # norte
    ax.plot([0, 0], [0, Ly], linewidth=2, color="black")      # oeste
    ax.plot([Lx, Lx], [0, Ly], linewidth=2, color="black")    # leste

    # =========================
    # LINHAS INTERNAS (GRADE)
    # =========================
    ax.plot([Lx/2, Lx/2], [0, Ly], linestyle="--", color="gray")
    ax.plot([0, Lx], [Ly/2, Ly/2], linestyle="--", color="gray")

    # =========================
    # PONTOS INTERNOS (PRETOS)
    # =========================
    margem = 0.10  # 10%

    pontos_internos = {
        "NO": (Lx*margem,        Ly*(1 - margem)),
        "NE": (Lx*(1 - margem),  Ly*(1 - margem)),
        "SO": (Lx*margem,        Ly*margem),
        "SE": (Lx*(1 - margem),  Ly*margem),
        "C":  (Lx*0.5,           Ly*0.5),
    }

    for label, (x, y) in pontos_internos.items():
        ax.scatter(x, y, color="black", s=60)
        ax.text(x, y + 0.2, label, ha="center")

    # =========================
    # PONTOS DE PAREDE (VERMELHOS)
    # =========================
    pontos_parede = {
        "N1": (Lx*0.25, Ly),
        "N2": (Lx*0.75, Ly),

        "S1": (Lx*0.25, 0),
        "S2": (Lx*0.75, 0),

        "O1": (0, Ly*0.75),
        "O2": (0, Ly*0.25),

        "L1": (Lx, Ly*0.75),
        "L2": (Lx, Ly*0.25),
    }

    for label, (x, y) in pontos_parede.items():
        ax.scatter(x, y, color="red", s=60)
        ax.text(x, y + 0.2, label, color="red", ha="center")

    # =========================
    # ORIENTAÇÃO
    # =========================
    ax.text(Lx/2, Ly + 0.8, "Norte", ha="center", fontsize=14)
    ax.text(Lx/2, -1.0, "Sul", ha="center", fontsize=14)

    ax.text(-1.5, Ly/2, "Oeste", va="center", rotation=90, fontsize=14)
    ax.text(Lx + 1.0, Ly/2, "Leste", va="center", rotation=90, fontsize=14)

    # =========================
    # AJUSTES
    # =========================
    ax.set_xlim(-2, Lx + 2)
    ax.set_ylim(-2, Ly + 2)

    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_title("Planta térmica simplificada")

    st.pyplot(fig)
    plt.close(fig)