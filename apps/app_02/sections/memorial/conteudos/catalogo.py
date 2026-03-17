from __future__ import annotations

from apps.app_02.sections.memorial.conteudos.conclusao import get_pagina as get_conclusao
from apps.app_02.sections.memorial.conteudos.fundamentacao_modelo import (
    get_pagina as get_fundamentacao_modelo,
)
from apps.app_02.sections.memorial.conteudos.introducao import get_pagina as get_introducao
from apps.app_02.sections.memorial.conteudos.metodologia import get_pagina as get_metodologia
from apps.app_02.sections.memorial.conteudos.referencias_anexos import (
    get_pagina as get_referencias_anexos,
)
from apps.app_02.sections.memorial.conteudos.resultados_analise import (
    get_pagina as get_resultados_analise,
)


def get_paginas() -> list[dict]:
    return [
        get_introducao(),
        get_fundamentacao_modelo(),
        get_metodologia(),
        get_resultados_analise(),
        get_conclusao(),
        get_referencias_anexos(),
    ]