from pathlib import Path
import json
import streamlit as st


BASE_PATH = Path(__file__).resolve().parents[1] / "conteudos"
st.write("📍 Caminho base:", BASE_PATH.resolve())


def load_tree():
    tree = {}

    if not BASE_PATH.exists():
        return tree

    for m in sorted(BASE_PATH.glob("m*")):
        m_key = m.name
        tree[m_key] = {}

        for s in sorted(m.glob("s*")):
            s_key = s.name
            tree[m_key][s_key] = {}

            for c in sorted(s.glob("c*")):
                c_key = c.name
                tree[m_key][s_key][c_key] = {}

                for b in sorted(c.glob("b*")):
                    b_key = b.name

                    content_file = b / "content.json"

                    if content_file.exists():
                        with open(content_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                    else:
                        data = {}

                    tree[m_key][s_key][c_key][b_key] = data

    return tree