# core/users/import_csv.py

import csv
import io
from typing import List, Dict, Tuple

from core.users.repo import create_user
from core.users.username_generator import normalize_display_name


def import_users_from_csv_bytes(csv_bytes: bytes) -> Dict:
    """
    CSV: 1 coluna (NOME_COMPLETO). Pode ter header ou não.
    Retorna resumo: created, skipped, errors, details[]
    """
    text = csv_bytes.decode("utf-8", errors="replace")
    f = io.StringIO(text)

    reader = csv.reader(f)
    rows = list(reader)

    created = 0
    skipped = 0
    errors = 0
    details: List[Dict] = []

    # detecta header (se primeira célula contém "NOME")
    start_idx = 0
    if rows and rows[0]:
        head = (rows[0][0] or "").strip().lower()
        if "nome" in head:
            start_idx = 1

    for idx in range(start_idx, len(rows)):
        row = rows[idx]
        if not row:
            continue
        raw_name = (row[0] or "").strip()
        if not raw_name:
            continue

        display = normalize_display_name(raw_name)
        ok, username, msg = create_user(display)
        if ok:
            created += 1
            details.append({"nome": display, "username": username, "status": "criado"})
        else:
            # se falhou por nome inválido ou algo do tipo, conta como erro; senão “skipped”
            if "inválido" in msg.lower():
                errors += 1
                details.append({"nome": display, "username": username, "status": f"erro: {msg}"})
            else:
                skipped += 1
                details.append({"nome": display, "username": username, "status": f"ignorado: {msg}"})

    return {
        "created": created,
        "skipped": skipped,
        "errors": errors,
        "details": details,
    }