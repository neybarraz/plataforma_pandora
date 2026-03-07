# admin/download_utils.py

from __future__ import annotations

import io
import json
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = REPO_ROOT / "apps"


@dataclass
class ResponseFileInfo:
    app_id: str
    username: str
    filename: str
    relative_path: str
    size_bytes: int
    modified_at: str
    absolute_path: Path


def _safe_datetime(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def get_responses_dir(app_id: str | None) -> Path:
    if not app_id:
        return APPS_DIR
    return APPS_DIR / app_id / "data" / "responses"


def infer_username_from_filename(filename: str, app_id: str) -> str:
    stem = Path(filename).stem

    suffix = f"_{app_id}"
    if stem.endswith(suffix):
        username = stem[: -len(suffix)]
        return username or "-"

    prefix = f"{app_id}_"
    if stem.startswith(prefix):
        username = stem[len(prefix) :]
        return username or "-"

    return "-"


def read_json_metadata(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            payload = json.load(f)

        if isinstance(payload, dict):
            return payload
    except Exception:
        pass

    return {}


def list_response_files(app_id: str) -> tuple[Path, list[ResponseFileInfo]]:
    responses_dir = get_responses_dir(app_id)

    if not responses_dir.exists() or not responses_dir.is_dir():
        return responses_dir, []

    files: list[ResponseFileInfo] = []

    for path in sorted(responses_dir.glob("*.json")):
        stat = path.stat()

        username = infer_username_from_filename(path.name, app_id)

        if username == "-":
            metadata = read_json_metadata(path)
            username = str(metadata.get("username", "-")).strip() or "-"

        files.append(
            ResponseFileInfo(
                app_id=app_id,
                username=username,
                filename=path.name,
                relative_path=str(path.relative_to(REPO_ROOT)),
                size_bytes=stat.st_size,
                modified_at=_safe_datetime(stat.st_mtime),
                absolute_path=path,
            )
        )

    return responses_dir, files


def build_zip_bytes(app_id: str, selected_relative_paths: list[str]) -> bytes:
    buffer = io.BytesIO()

    with zipfile.ZipFile(
        buffer,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=1,
    ) as zf:
        for relative_path in selected_relative_paths:
            abs_path = REPO_ROOT / relative_path
            if not abs_path.exists() or not abs_path.is_file():
                continue

            arcname = f"{app_id}/{abs_path.name}"
            zf.write(abs_path, arcname=arcname)

    buffer.seek(0)
    return buffer.getvalue()


def format_size(num_bytes: int) -> str:
    if num_bytes < 1024:
        return f"{num_bytes} B"
    if num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    return f"{num_bytes / (1024 * 1024):.2f} MB"