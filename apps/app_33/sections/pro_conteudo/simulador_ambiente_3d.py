from __future__ import annotations

import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def _get_valor_limpo(qid: str) -> float | None:
    chave = f"problema_{qid}"
    valor_bruto = st.session_state.get(chave)

    if valor_bruto is None or str(valor_bruto).strip() in ["", "—", "None"]:
        return None

    try:
        return float(str(valor_bruto).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None

def _draw_room(Lx: float, Ly: float, Lz: float) -> None:
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection="3d")

    # Vértices do paralelepípedo
    x = [0, Lx]
    y = [0, Ly]
    z = [0, Lz]

    # Linhas da caixa (12 arestas)
    edges = [
        # base
        [(0,0,0),(Lx,0,0)], [(Lx,0,0),(Lx,Ly,0)],
        [(Lx,Ly,0),(0,Ly,0)], [(0,Ly,0),(0,0,0)],

        # topo
        [(0,0,Lz),(Lx,0,Lz)], [(Lx,0,Lz),(Lx,Ly,Lz)],
        [(Lx,Ly,Lz),(0,Ly,Lz)], [(0,Ly,Lz),(0,0,Lz)],

        # verticais
        [(0,0,0),(0,0,Lz)], [(Lx,0,0),(Lx,0,Lz)],
        [(Lx,Ly,0),(Lx,Ly,Lz)], [(0,Ly,0),(0,Ly,Lz)],
    ]

    for edge in edges:
        xs = [edge[0][0], edge[1][0]]
        ys = [edge[0][1], edge[1][1]]
        zs = [edge[0][2], edge[1][2]]
        ax.plot(xs, ys, zs)

    # Eixos principais
    ax.quiver(0, 0, 0, Lx*0.8, 0, 0, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, Ly*0.8, 0, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, Lz*0.8, arrow_length_ratio=0.1)

    ax.text(Lx*0.85, 0, 0, "x")
    ax.text(0, Ly*0.85, 0, "y")
    ax.text(0, 0, Lz*0.85, "z")

    # Ajustes visuais
    ax.set_xlim(0, Lx)
    ax.set_ylim(0, Ly)
    ax.set_zlim(0, Lz)

    ax.set_xticks([0, Lx/2, Lx])
    ax.set_yticks([0, Ly/2, Ly])
    ax.set_zticks([0, Lz/2, Lz])

    ax.set_box_aspect([Lx, Ly, Lz])
    ax.view_init(elev=20, azim=35)

    ax.set_xlabel("compr.")
    ax.set_ylabel("largura")
    ax.set_zlabel("altura")

    ax.set_title("Representação do ambiente 3D")

    st.pyplot(fig)
    plt.close(fig)

def render_simulador_ambiente_3d() -> None:
    # 🔹 ler valores vindos das questões
    Lx = _get_valor_limpo("problema.01.001.0101")
    Ly = _get_valor_limpo("problema.01.001.0102")
    Lz = _get_valor_limpo("problema.01.001.0103")

    # 🔹 fallback (caso ainda não preenchido)
    if Lx is None or Ly is None or Lz is None:
        st.warning("Preencha as dimensões da sala para visualizar o modelo.")

        c1, c2, c3 = st.columns(3)

        with c1:
            Lx = st.slider("Comprimento (x) [m]", 1.0, 20.0, 6.0, 0.5)

        with c2:
            Ly = st.slider("Largura (y) [m]", 1.0, 20.0, 5.0, 0.5)

        with c3:
            Lz = st.slider("Altura (z) [m]", 1.0, 6.0, 3.0, 0.1)

    # else:
    #     st.success(
    #         f"Dimensões carregadas: x={Lx:.2f} m | y={Ly:.2f} m | z={Lz:.2f} m"
    #     )

    _draw_room(Lx, Ly, Lz)



if __name__ == "__main__":
    st.set_page_config(layout="wide")
    render_simulador_ambiente_3d()