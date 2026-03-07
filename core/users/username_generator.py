# core/users/username_generator.py

import re
import unicodedata


def _strip_accents(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def normalize_display_name(raw: str) -> str:
    # mantém acentos e “bonito”, apenas normaliza espaços
    name = (raw or "").strip()
    name = re.sub(r"\s+", " ", name)
    return name


def generate_base_username(display_name: str) -> str:
    # regra: primeiro_nome + ultimo_nome, sem acento e sem caracteres especiais
    s = (display_name or "").strip().lower()
    s = _strip_accents(s)
    s = re.sub(r"[^a-z\s]", " ", s)      # remove pontuação / números
    s = re.sub(r"\s+", " ", s).strip()
    parts = s.split()
    if len(parts) == 0:
        return ""
    if len(parts) == 1:
        return parts[0]
    return parts[0] + parts[-1]