# admin/permissions_panel.py

import streamlit as st
from config import ADMIN_USERNAME, APP_CATALOG
from core.users.repo import list_users
from core.permissions.app_access import get_users_with_access, bulk_set_access_for_app
from core.permissions.stage_unlock import (
    STAGES,
    get_stage_unlocks_for_app,
    bulk_set_stage_unlocks_for_app,
)

# labels curtas (layout compacto e alinhado)
STAGE_LABELS = {
    "visao_geral": "Visão Geral",
    "problema": "Probl.",
    "investigacao": "Invest.",
    "solucao": "Soluc.",
    "memorial": "Mem. Tec.",
    "avaliacao": "Avalia.",
}

# Etapas que obedecem cascata pedagógica
CASCADE_STAGES = ["problema", "investigacao", "solucao", "memorial"]


def _get_auth_username() -> str | None:
    """
    Normaliza o usuário autenticado da plataforma.
    Aceita:
    - st.session_state["auth_user"] como string
    - st.session_state["auth_user"] como dict com chave 'username'
    """
    auth_user = st.session_state.get("auth_user")

    if isinstance(auth_user, str) and auth_user.strip():
        return auth_user.strip()

    if isinstance(auth_user, dict):
        username = auth_user.get("username")
        if isinstance(username, str) and username.strip():
            return username.strip()

    return None


def _init_perm_state():
    st.session_state.setdefault("perm_selected_app", None)
    st.session_state.setdefault("perm_search", "")
    st.session_state.setdefault("perm_force_sync", None)
    st.session_state.setdefault("stage_force_sync", None)


def _get_access_key(app_id: str, username: str) -> str:
    return f"perm_{app_id}_{username}"


def _get_stage_key(app_id: str, username: str, stage: str) -> str:
    return f"stage_{app_id}_{username}_{stage}"


def _ensure_admin_in_users(users: list[dict]) -> list[dict]:
    """
    Garante que o admin também exista na lista trabalhada pelo painel,
    mesmo que não venha do list_users().
    """
    usernames = {str(u.get("username", "")).strip() for u in users}

    if ADMIN_USERNAME not in usernames:
        users.append(
            {
                "username": ADMIN_USERNAME,
                "nome": "Administrador",
            }
        )

    return users


def _sync_access_from_db(app_id: str, users: list[dict]):
    allowed = get_users_with_access(app_id)
    for u in users:
        uname = u["username"]
        # admin sempre aparece como tendo acesso no painel
        st.session_state[_get_access_key(app_id, uname)] = (
            True if uname == ADMIN_USERNAME else (uname in allowed)
        )


def _sync_stages_from_db(app_id: str, users: list[dict]):
    """
    Preenche o estado das etapas no session_state para este app.
    Só é seguro chamar antes de instanciar os checkboxes.
    """
    unlocked_map = get_stage_unlocks_for_app(app_id)

    for u in users:
        uname = u["username"]
        unlocked = unlocked_map.get(uname, set())

        if not isinstance(unlocked, (set, list, tuple)):
            unlocked = set()

        unlocked = set(unlocked)

        for stage in STAGES:
            st.session_state[_get_stage_key(app_id, uname, stage)] = (stage in unlocked)


def _select_app(app_id: str):
    st.session_state["perm_selected_app"] = app_id
    st.session_state["perm_force_sync"] = app_id
    st.session_state["stage_force_sync"] = app_id


def _enforce_cascade(app_id: str, username: str, changed_stage: str):
    """
    Regras:
    - visao_geral: independente
    - avaliacao: independente
    - problema -> investigacao -> solucao -> memorial: em cascata

    Cascata:
    - Se marcar uma etapa da cascata, marca todas as anteriores da cascata.
    - Se desmarcar uma etapa da cascata, desmarca todas as posteriores da cascata.
    """
    if changed_stage not in STAGES:
        return

    if changed_stage not in CASCADE_STAGES:
        return

    idx = CASCADE_STAGES.index(changed_stage)
    current = bool(
        st.session_state.get(_get_stage_key(app_id, username, changed_stage), False)
    )

    if current:
        for j in range(0, idx + 1):
            stage = CASCADE_STAGES[j]
            st.session_state[_get_stage_key(app_id, username, stage)] = True
    else:
        for j in range(idx, len(CASCADE_STAGES)):
            stage = CASCADE_STAGES[j]
            st.session_state[_get_stage_key(app_id, username, stage)] = False


def _get_stage_label(stage: str) -> str:
    return STAGE_LABELS.get(stage, stage.replace("_", " ").title())


def permissions_panel():
    current_username = _get_auth_username()

    if current_username != ADMIN_USERNAME:
        st.error("Acesso negado.")
        return

    _init_perm_state()

    st.subheader("Permissões")
    st.caption("1) Clique em um App. 2) Marque alunos. 3) Salve.")

    if not APP_CATALOG:
        st.warning("APP_CATALOG está vazio no config.py.")
        return

    users = list_users()
    if users is None:
        users = []

    users = _ensure_admin_in_users(users)

    users = sorted(users, key=lambda u: (u.get("nome") or "").lower())

    # ---------- GRID DE APPS ----------
    st.markdown("### Apps")
    col_left, col_right = st.columns(2, gap="large")

    for i, app in enumerate(APP_CATALOG):
        app_id = app["app_id"]
        title = app.get("title", app_id)
        subtitle = app.get("subtitle", "")

        target_col = col_left if (i % 2 == 0) else col_right
        with target_col:
            is_selected = (st.session_state["perm_selected_app"] == app_id)
            label = f"✅ {title}" if is_selected else title

            st.button(
                label,
                key=f"pick_{app_id}",
                use_container_width=True,
                help=subtitle or app_id,
                on_click=_select_app,
                args=(app_id,),
            )
            st.caption(app_id)

    st.divider()

    # ---------- APP SELECIONADO ----------
    app_id = st.session_state.get("perm_selected_app")
    if not app_id:
        st.info("Clique em um app acima para editar permissões.")
        return

    # ---------- SINCRONIZAÇÃO SEGURA ----------
    if st.session_state.get("perm_force_sync") == app_id:
        _sync_access_from_db(app_id, users)
        st.session_state["perm_force_sync"] = None

    if st.session_state.get("stage_force_sync") == app_id:
        _sync_stages_from_db(app_id, users)
        st.session_state["stage_force_sync"] = None

    st.markdown(f"### App selecionado: `{app_id}`")

    # Busca
    st.session_state["perm_search"] = st.text_input(
        "Buscar aluno (nome ou username)",
        value=st.session_state["perm_search"],
        placeholder="ex.: maicon, anacosta, silva...",
    ).strip().lower()

    q = st.session_state["perm_search"]
    if q:
        users_filtered = [
            u for u in users
            if q in (u.get("nome") or "").lower()
            or q in (u.get("username") or "").lower()
        ]
    else:
        users_filtered = users

    total = len(users)
    liberados = sum(
        bool(st.session_state.get(_get_access_key(app_id, u["username"]), False))
        for u in users
    )
    st.caption(f"{liberados} liberados / {total} usuários")

    # Ações rápidas (acesso)
    c1, c2, c3 = st.columns([1, 1, 2])

    with c1:
        if st.button("Marcar todos", use_container_width=True, key=f"all_{app_id}"):
            for u in users:
                st.session_state[_get_access_key(app_id, u["username"])] = True
            st.rerun()

    with c2:
        if st.button("Desmarcar todos", use_container_width=True, key=f"none_{app_id}"):
            for u in users:
                # admin permanece com acesso no painel
                if u["username"] == ADMIN_USERNAME:
                    st.session_state[_get_access_key(app_id, u["username"])] = True
                else:
                    st.session_state[_get_access_key(app_id, u["username"])] = False
            st.rerun()

    with c3:
        if st.button("Recarregar do banco", use_container_width=True, key=f"reload_{app_id}"):
            st.session_state["perm_force_sync"] = app_id
            st.session_state["stage_force_sync"] = app_id
            st.rerun()

    # ---------- BLOCO 1: ACESSO AO APP ----------
    st.markdown("#### Acesso ao App")

    h1, h2, h3 = st.columns([0.6, 1.4, 3.0])
    with h1:
        st.markdown("**Acesso**")
    with h2:
        st.markdown("**Username**")
    with h3:
        st.markdown("**Nome**")

    for u in users_filtered:
        uname = u["username"]
        nome = u["nome"]
        k = _get_access_key(app_id, uname)

        r1, r2, r3 = st.columns([0.6, 1.4, 3.0])
        with r1:
            disabled = uname == ADMIN_USERNAME
            st.checkbox("", key=k, label_visibility="collapsed", disabled=disabled)
        with r2:
            st.write(uname)
        with r3:
            st.write(nome)

    if st.button("Salvar permissões do app", use_container_width=True, key=f"save_access_{app_id}"):
        full_map = {
            u["username"]: bool(st.session_state.get(_get_access_key(app_id, u["username"]), False))
            for u in users
            if u["username"] != ADMIN_USERNAME
        }

        bulk_set_access_for_app(app_id, full_map)

        st.session_state["perm_force_sync"] = app_id
        st.success("Permissões do app salvas.")
        st.rerun()

    st.divider()

    # ---------- BLOCO 2: PROGRESSÃO POR ETAPAS ----------
    st.markdown("#### Progressão por etapas (somente usuários com acesso)")

    allowed_usernames = [
        u["username"] for u in users
        if bool(st.session_state.get(_get_access_key(app_id, u["username"]), False))
    ]

    if not allowed_usernames:
        st.info("Nenhum usuário com acesso a este app. Libere usuários acima para aparecerem aqui.")
        return

    stage_col_widths = []
    for stage in STAGES:
        if stage == "memorial":
            stage_col_widths.append(1.2)
        elif stage == "visao_geral":
            stage_col_widths.append(1.3)
        elif stage == "avaliacao":
            stage_col_widths.append(1.0)
        else:
            stage_col_widths.append(0.9)

    header_cols = st.columns([1.6] + stage_col_widths)
    header_cols[0].markdown("**Username**")

    for idx, stage in enumerate(STAGES, start=1):
        header_cols[idx].markdown(f"**{_get_stage_label(stage)}**")

    for uname in allowed_usernames:
        row = st.columns([1.6] + stage_col_widths)
        row[0].write(uname)

        for i_stage, stage in enumerate(STAGES):
            k = _get_stage_key(app_id, uname, stage)
            row[i_stage + 1].checkbox(
                "",
                key=k,
                label_visibility="collapsed",
                on_change=_enforce_cascade,
                args=(app_id, uname, stage),
            )

    if st.button("Salvar progressão", use_container_width=True, key=f"save_stage_{app_id}"):
        unlock_map: dict[str, set[str]] = {}

        for uname in allowed_usernames:
            unlocked = set()
            for stage in STAGES:
                if bool(st.session_state.get(_get_stage_key(app_id, uname, stage), False)):
                    unlocked.add(stage)
            unlock_map[uname] = unlocked

        bulk_set_stage_unlocks_for_app(app_id, unlock_map)

        st.session_state["stage_force_sync"] = app_id
        st.success("Progressão salva.")
        st.rerun()