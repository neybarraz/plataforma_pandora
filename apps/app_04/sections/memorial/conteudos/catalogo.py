from __future__ import annotations

from typing import Any

from .conclusao import get_pagina as get_conclusao
from .fundamentacao_modelo import get_pagina as get_fundamentacao_modelo
from .introducao import get_pagina as get_introducao
from .metodologia import get_pagina as get_metodologia
from .referencias_anexos import get_pagina as get_referencias_anexos
from .resultados_analise import get_pagina as get_resultados_analise


SECTION_KEY = "memorial"


def _normalize_pagina(
    pagina: dict[str, Any],
    numero: str,
) -> dict[str, Any]:
    page_id = str(pagina.get("id", "")).strip() or f"{SECTION_KEY}_{numero}"

    pagina["id"] = page_id
    pagina["section"] = SECTION_KEY
    pagina["numero"] = numero

    conteudos = pagina.get("conteudos", [])
    if isinstance(conteudos, list):
        for i, conteudo in enumerate(conteudos, start=1):
            if not isinstance(conteudo, dict):
                continue

            conteudo.setdefault("section", SECTION_KEY)
            conteudo.setdefault("pagina_numero", numero)
            conteudo.setdefault("numero", f"{i:03d}")

    return pagina


def get_paginas() -> list[dict[str, Any]]:
    return [
        _normalize_pagina(get_introducao(), "01"),
        _normalize_pagina(get_fundamentacao_modelo(), "02"),
        _normalize_pagina(get_metodologia(), "03"),
        _normalize_pagina(get_resultados_analise(), "04"),
        _normalize_pagina(get_conclusao(), "05"),
        _normalize_pagina(get_referencias_anexos(), "06"),
    ]