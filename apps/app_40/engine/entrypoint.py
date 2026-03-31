import streamlit as st
from .content_loader import load_tree
from .storage_adapter import save_answer
from ..storage import get_section_responses


LABELS = {
    "m01": "Motor Elétrico",
    "m02": "Proteção",
    "s01": "Corrente",
    "s02": "Tensão",
    "b01": "Introdução",
    "b02": "Exercícios",
}


def run_engine(username: str):
    st.write("🚀 Novo motor ativo")
    st.write(f"Usuário: {username}")

    from ..storage import load_user_data

    st.write("DEBUG STORAGE:")
    st.write(load_user_data(username))

    tree = load_tree()

    if not tree:
        st.warning("Nenhum conteúdo encontrado em /conteudos")
        return

    # =========================
    # MENU 1 — MÓDULOS
    # =========================

    m_keys = sorted(tree.keys())
    cols = st.columns(len(m_keys))

    for i, m in enumerate(m_keys):
        label = LABELS.get(m, m)

        if cols[i].button(label, key=f"m_{m}", use_container_width=True):
            st.session_state["m_key"] = m

    m_key = st.session_state.get("m_key", m_keys[0])

    # =========================
    # MENU 2 — SUBMÓDULO
    # =========================

    s_keys = list(tree[m_key].keys())

    if len(s_keys) > 1:
        cols = st.columns(len(s_keys))

        for i, s in enumerate(s_keys):
            label = LABELS.get(s, s)

            if cols[i].button(label, key=f"s_{m_key}_{s}", use_container_width=True):
                st.session_state["s_key"] = s

        s_key = st.session_state.get("s_key", s_keys[0])
    else:
        s_key = s_keys[0]

    # =========================
    # BASE
    # =========================

    c_key = list(tree[m_key][s_key].keys())[0]
    b_keys = list(tree[m_key][s_key][c_key].keys())

    # =========================
    # NODE ATIVO
    # =========================

    if "node_id" not in st.session_state:
        st.session_state["node_id"] = f"{m_key}.{s_key}.{c_key}.{b_keys[0]}"

    node_id = st.session_state["node_id"]

    m_key, s_key, c_key, b_key = node_id.split(".")
    conteudo = tree[m_key][s_key][c_key][b_key]

    # =========================
    # LAYOUT
    # =========================

    col_menu, col_content = st.columns([1, 3])

    # =========================
    # MENU ESQUERDA
    # =========================

    with col_menu:
        for b in b_keys:
            node = f"{m_key}.{s_key}.{c_key}.{b}"
            is_active = st.session_state.get("node_id") == node

            label = LABELS.get(b, b)
            label = f"➡️ {label}" if is_active else label

            if st.button(label, key=f"b_{node}", use_container_width=True):
                st.session_state["node_id"] = node
                st.rerun()

    # =========================
    # CONTEÚDO
    # =========================

    with col_content:
        st.write(f"📍 Caminho: {node_id}")

        responses = get_section_responses(username, "problema")

        for bloco in conteudo.get("blocos", []):

            tipo = bloco.get("tipo")

            # -------------------------
            # TEXTO
            # -------------------------
            if tipo == "texto":
                st.write(bloco.get("texto", ""))

            # -------------------------
            # QUESTÃO TEXTO
            # -------------------------
            elif tipo == "questao_texto":
                qid = bloco.get("id", "q")

                full_id = f"{node_id}.{qid}"
                widget_key = f"engine_{full_id}"

                item = responses.get(full_id, {})
                valor_salvo = item.get("resposta", "")

                # 🔥 hidratação correta (sem sobrescrever input do usuário)
                if widget_key not in st.session_state:
                    st.session_state[widget_key] = valor_salvo
                elif st.session_state[widget_key] == "":
                    st.session_state[widget_key] = valor_salvo

                st.text_area(
                    bloco.get("pergunta", ""),
                    key=widget_key
                )

                if st.button("💾 Salvar", key=f"save_{full_id}"):
                    save_answer(
                        username=username,
                        node_id=node_id,
                        question_id=qid,
                        tipo="texto",
                        pergunta=bloco.get("pergunta", ""),
                        resposta=st.session_state[widget_key],
                    )
                    st.success("Salvo!")

            # -------------------------
            # MÚLTIPLA ESCOLHA
            # -------------------------
            elif tipo == "questao_multipla_escolha":
                qid = bloco.get("id", "q")

                alternativas = bloco.get("alternativas", {})
                opcoes = list(alternativas.keys())

                full_id = f"{node_id}.{qid}"
                widget_key = f"engine_{full_id}"

                item = responses.get(full_id, {})
                valor_salvo = item.get("resposta_escolhida", "")

                valor_corrigido = valor_salvo if valor_salvo in opcoes else opcoes[0]

                # 🔥 hidratação correta
                if widget_key not in st.session_state:
                    st.session_state[widget_key] = valor_corrigido

                st.radio(
                    bloco.get("pergunta", ""),
                    opcoes,
                    format_func=lambda x: alternativas[x],
                    key=widget_key
                )

                if st.button("💾 Salvar", key=f"save_{full_id}"):
                    save_answer(
                        username=username,
                        node_id=node_id,
                        question_id=qid,
                        tipo="multipla_escolha",
                        pergunta=bloco.get("pergunta", ""),
                        resposta=st.session_state[widget_key],
                        alternativas=alternativas,
                        alternativa_correta=bloco.get("alternativa_correta", ""),
                    )
                    st.success("Salvo!")

            # -------------------------
            # OUTROS
            # -------------------------
            else:
                st.warning(f"Tipo não suportado: {tipo}")
