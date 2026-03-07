# core/permissions/stage_unlock.py

from core.db.conn import get_conn

STAGES = [
    "visao_geral",
    "problema",
    "investigacao",
    "solucao",
    "memorial",
    "avaliacao",
]


def get_stage_unlocks_for_app(app_id: str) -> dict[str, set[str]]:
    """
    Retorna um dict no formato:
        {
            "username": {"visao_geral", "problema", "investigacao"},
            ...
        }

    Traz somente etapas com unlocked = 1.
    """
    conn = get_conn()
    try:
        rows = conn.execute(
            """
            SELECT username, stage
            FROM stage_unlock
            WHERE app_id = ? AND unlocked = 1
            """,
            (app_id,),
        ).fetchall()

        out: dict[str, set[str]] = {}
        for row in rows:
            username = row["username"]
            stage = row["stage"]
            out.setdefault(username, set()).add(stage)

        return out

    finally:
        conn.close()


def bulk_set_stage_unlocks_for_app(app_id: str, unlock_map: dict[str, set[str]]) -> None:
    """
    Salva o desbloqueio de etapas para um app.

    Parâmetro:
        unlock_map = {
            "username_a": {"visao_geral", "problema"},
            "username_b": {"visao_geral", "problema", "investigacao"},
            ...
        }

    Observação:
    O chamador deve garantir a consistência da cascata.
    """
    if not unlock_map:
        return

    conn = get_conn()
    try:
        for username, unlocked_stages in unlock_map.items():
            if not isinstance(unlocked_stages, (set, list, tuple)):
                unlocked_stages = set()

            unlocked_stages = set(unlocked_stages)

            for stage in STAGES:
                allowed = 1 if stage in unlocked_stages else 0

                exists = conn.execute(
                    """
                    SELECT 1
                    FROM stage_unlock
                    WHERE username = ? AND app_id = ? AND stage = ?
                    """,
                    (username, app_id, stage),
                ).fetchone()

                if exists:
                    conn.execute(
                        """
                        UPDATE stage_unlock
                        SET unlocked = ?
                        WHERE username = ? AND app_id = ? AND stage = ?
                        """,
                        (allowed, username, app_id, stage),
                    )
                else:
                    conn.execute(
                        """
                        INSERT INTO stage_unlock (username, app_id, stage, unlocked)
                        VALUES (?, ?, ?, ?)
                        """,
                        (username, app_id, stage, allowed),
                    )

        conn.commit()

    finally:
        conn.close()