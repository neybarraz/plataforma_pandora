# core/permissions/stage_unlock.py

import os

from core.db.conn import get_conn

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()

STAGES = [
    "visao_geral",
    "problema",
    "investigacao",
    "solucao",
    "memorial",
    "avaliacao",
]


def _ph() -> str:
    """
    SQLite  -> ?
    Postgres -> %s
    """
    return "%s" if DATABASE_URL else "?"


def _row_value(row, key: str, index: int = 0):
    if row is None:
        return None

    if isinstance(row, dict):
        return row.get(key)

    try:
        return row[key]
    except Exception:
        pass

    try:
        return row[index]
    except Exception:
        return None


def get_stage_unlocks_for_app(app_id: str) -> dict[str, set[str]]:
    """
    Retorna:
        {
            "username": {"visao_geral", "problema", ...},
            ...
        }

    Traz somente etapas com unlocked = 1.
    """
    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT username, stage
            FROM stage_unlock
            WHERE app_id = {ph} AND unlocked = 1
            """,
            (app_id,),
        )
        rows = cur.fetchall()

        out: dict[str, set[str]] = {}
        for row in rows:
            username = _row_value(row, "username", 0)
            stage = _row_value(row, "stage", 1)

            if username and stage:
                out.setdefault(username, set()).add(stage)

        return out

    finally:
        conn.close()


def bulk_set_stage_unlocks_for_app(app_id: str, unlock_map: dict[str, set[str]]) -> None:
    """
    Salva o desbloqueio de etapas para um app.

    unlock_map = {
        "username_a": {"visao_geral", "problema"},
        "username_b": {"visao_geral", "problema", "investigacao"},
    }
    """
    if not unlock_map:
        return

    ph = _ph()
    conn = get_conn()

    try:
        cur = conn.cursor()

        for username, unlocked_stages in unlock_map.items():
            if not isinstance(unlocked_stages, (set, list, tuple)):
                unlocked_stages = set()

            unlocked_stages = set(unlocked_stages)

            for stage in STAGES:
                allowed = 1 if stage in unlocked_stages else 0

                cur.execute(
                    f"""
                    SELECT 1
                    FROM stage_unlock
                    WHERE username = {ph} AND app_id = {ph} AND stage = {ph}
                    """,
                    (username, app_id, stage),
                )
                exists = cur.fetchone()

                if exists:
                    cur.execute(
                        f"""
                        UPDATE stage_unlock
                        SET unlocked = {ph}
                        WHERE username = {ph} AND app_id = {ph} AND stage = {ph}
                        """,
                        (allowed, username, app_id, stage),
                    )
                else:
                    cur.execute(
                        f"""
                        INSERT INTO stage_unlock (username, app_id, stage, unlocked)
                        VALUES ({ph}, {ph}, {ph}, {ph})
                        """,
                        (username, app_id, stage, allowed),
                    )

        conn.commit()

    finally:
        conn.close()
