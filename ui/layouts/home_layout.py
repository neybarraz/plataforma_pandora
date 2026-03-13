# ui/layouts/home_layout.py

import os
import base64
import streamlit as st

from config import APP_CATALOG
from ui.components.header import render_header, get_allowed_apps_for_current_user


def _asset_path(*parts: str) -> str:
    here = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(here, "assets", *parts)


def _img_to_data_uri(path: str) -> str | None:
    if not path or not os.path.exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().replace(".", "")
    if ext not in ("png", "jpg", "jpeg", "webp"):
        return None
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    return f"data:image/{mime};base64,{b64}"


def _escape_attr(s: str) -> str:
    return (s or "").replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def _card_css():
    st.markdown(
        """
        <style>
        .hero{
            border-radius: 18px;
            padding: 18px 18px;
            border: 1px solid rgba(255,255,255,0.10);
            background: rgba(255,255,255,0.03);
            margin-bottom: 14px;
        }
        .hero-title{ font-size: 22px; font-weight: 800; margin: 0 0 6px 0; }
        .hero-sub{ opacity: 0.78; margin: 0; line-height: 1.35; }

        /* =========================
           AJUSTES RÁPIDOS (MEXA AQUI)
           ========================= */
        :root{
            --CARD_H: 250px;     /* altura do card */
            --TXT_H:   84px;     /* altura do overlay do texto */
            --HOVER_Z: 1.04;     /* zoom no hover */
            --BTN_GAP: -14px;    /* espaço entre card e botão (use -6, -10, -14...) */
        }

        /* CARD */
        .app-card{
            border-radius: 18px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.10);
            background: rgba(255,255,255,0.03);
            margin: 0;                 /* não deixa margem aqui, controle no gap */
            position: relative;
            height: var(--CARD_H);

            transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
        }
        .app-card:hover{
            transform: translateY(-2px) scale(var(--HOVER_Z));
            border-color: rgba(255,255,255,0.22);
            box-shadow: 0 10px 28px rgba(0,0,0,0.35);
        }

        /* IMAGEM ocupa tudo */
        .app-img{
            position: absolute;
            inset: 0;
            overflow: hidden;
            background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
            line-height: 0;
            z-index: 1;
        }
        .app-img img{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            margin: 0;
            padding: 0;
            border: 0;
        }
        .app-img::after{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0.00), rgba(0,0,0,0.18));
            pointer-events: none;
        }

        /* lock */
        .lock{
            position:absolute;
            right:10px; top:10px;
            padding: 6px 10px;
            border-radius: 999px;
            background: rgba(0,0,0,0.55);
            border: 1px solid rgba(255,255,255,0.15);
            font-size: 12px;
            z-index: 3;
        }

        /* TEXTO overlay 80% */
        .card-body{
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: var(--TXT_H);
            padding: 10px 12px;

            background: rgba(10,15,25,0.80);
            backdrop-filter: blur(4px);

            display:flex;
            flex-direction:column;
            justify-content:center;
            gap: 3px;

            z-index: 2;
        }
        .card-title{
            font-size:15px;
            font-weight:750;
            margin:0;
            line-height:1.2;

            display:-webkit-box;
            -webkit-line-clamp:2;
            -webkit-box-orient:vertical;
            overflow:hidden;
        }
        .card-sub{
            opacity:0.82;
            margin:0;
            font-size:12px;
            line-height:1.2;

            display:-webkit-box;
            -webkit-line-clamp:1;
            -webkit-box-orient:vertical;
            overflow:hidden;
        }

        /* Tooltip */
        .app-card[data-tip]:hover::before{
            content: attr(data-tip);
            position: absolute;
            left: 10px;
            right: 10px;
            top: 10px;
            z-index: 5;

            background: rgba(0,0,0,0.86);
            border: 1px solid rgba(255,255,255,0.14);
            border-radius: 12px;
            padding: 10px 12px;

            font-size: 12px;
            line-height: 1.25;
            color: rgba(255,255,255,0.92);

            box-shadow: 0 10px 28px rgba(0,0,0,0.35);
        }

        /* GAP entre card e botão (controle fino) */
        .btn-gap{
            height: 0px;
            margin-top: var(--BTN_GAP);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_home():
    _card_css()
    render_header()

    st.markdown(
        """
        <div class="hero">
          <div class="hero-title">Laboratórios de Engenharia Aplicada</div>
          <p class="hero-sub">
            Estude sistemas reais de engenharia.
            Analise dados, investigue mecanismos e compreenda como a tecnologia funciona na prática.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    user = st.session_state.get("auth_user")
    allowed = get_allowed_apps_for_current_user() if user else set()

    cols = st.columns(3)

    for i, app in enumerate(APP_CATALOG):
        col = cols[i % 3]
        with col:
            app_id = app["app_id"]
            title = app["title"]
            subtitle = app.get("subtitle", "")
            description = app.get("description", "")

            img_name = app.get("card_image")
            img_path = _asset_path("app_cards", img_name) if img_name else None
            img_uri = _img_to_data_uri(img_path) if img_path else None

            is_allowed = (app_id in allowed)
            is_logged = bool(user)
            is_locked = (is_logged and not is_allowed)

            tip = _escape_attr(description)
            safe_title = _escape_attr(title)
            safe_sub = _escape_attr(subtitle)

            img_html = f'<img src="{img_uri}" alt="{safe_title}"/>' if img_uri else ""

            st.markdown(
                f"""
                <div class="app-card" data-tip="{tip}">
                  <div class="app-img">
                    {img_html}
                    {("<div class='lock'>🔒 bloqueado</div>" if is_locked else "")}
                  </div>
                  <div class="card-body">
                    <p class="card-title">{safe_title}</p>
                    <p class="card-sub">{safe_sub}</p>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # aproxima o botão do card (mexa em --BTN_GAP)
            st.markdown('<div class="btn-gap"></div>', unsafe_allow_html=True)

            if not is_logged:
                st.button(
                    "Entrar para acessar o laboratório",
                    key=f"btn_login_{app_id}",
                    help=description,
                    use_container_width=True,
                    disabled=True,
                )
            else:
                if is_allowed:
                    if st.button(
                        "Abrir laboratório",
                        key=f"btn_open_{app_id}",
                        help=description,
                        use_container_width=True,
                    ):
                        st.session_state["current_app"] = app_id
                        st.session_state["current_view"] = "app"
                        st.rerun()
                else:
                    st.button(
                        "Bloqueado",
                        key=f"btn_lock_{app_id}",
                        help=description,
                        use_container_width=True,
                        disabled=True,

                    )



