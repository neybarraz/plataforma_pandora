from __future__ import annotations


def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Quando o modelo simplificado deixa de funcionar?",
        },

        # -------------------------------------------------
        # OBJETIVO
        # -------------------------------------------------

        {
            "tipo": "texto",
            "texto": (
                "Até aqui utilizamos um modelo simplificado do processo de carga:\n\n"
                "- Fonte controlada (TP4056)\n"
                "- Bateria modelada como tensão variável + resistência interna\n"
                "- Dois regimes: CC e CV\n\n"
                "Esse modelo é suficiente para prever o comportamento ideal.\n"
                "Mas todo modelo possui limites de validade."
            ),
        },

        # -------------------------------------------------
        # LIMITE 1 — EFEITOS TÉRMICOS
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "1. Efeitos térmicos",
        },

        {
            "tipo": "texto",
            "texto": (
                "O TP4056 é um carregador linear. "
                "Quando a bateria está muito descarregada, a diferença entre V_in e V_bat é grande."
                "Isso gera dissipação de potência:"
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"P = (V_in - V_bat) · I",
        },
        {
            "tipo": "texto",
            "texto": (
                "Se a temperatura subir excessivamente, o chip reduz automaticamente a corrente. "
                "Nesse caso, o comportamento real deixa de seguir o modelo ideal."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.005.0001",
            "pergunta": (
                "Por que o aquecimento pode fazer a corrente medida ser menor "
                "que a corrente programada?"
            ),
        },

        # -------------------------------------------------
        # LIMITE 2 — BATERIA DEGRADADA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "2. Resistência interna variável",
        },

        {
            "tipo": "texto",
            "texto": (
                "O modelo considera uma resistência interna aproximadamente constante.\n\n"
                "Na prática, baterias degradadas podem apresentar resistência interna elevada.\n"
                "Isso altera o comportamento da corrente durante a fase CV.\n\n"
                "A curva real pode não seguir o decaimento esperado."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.005.0002",
            "pergunta": (
                "Se a resistência interna da bateria for muito alta, "
                "o que pode acontecer durante o carregamento?"
            ),
            "alternativas": {
                "a": "Corrente maior que a programada",
                "b": "A tensão não atinge 4,2 V corretamente",
                "c": "A bateria carrega mais rápido",
                "d": "Nenhuma alteração ocorre",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # LIMITE 3 — MODELO QUÍMICO IGNORADO
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "3. Simplificação química",
        },

        {
            "tipo": "texto",
            "texto": (
                "O modelo elétrico ignora os processos eletroquímicos internos.\n\n"
                "A dinâmica real da bateria envolve:\n"
                "- Difusão de íons\n"
                "- Reações químicas\n"
                "- Dependência com temperatura\n\n"
                "Esses efeitos não aparecem no modelo elétrico simplificado."
            ),
        },

        # -------------------------------------------------
        # LIMITE 4 — COMPONENTES NÃO IDEAIS
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "4. Componentes não ideais",
        },

        {
            "tipo": "texto",
            "texto": (
                "Conexões ruins, cabos longos ou fontes instáveis "
                "podem alterar o comportamento observado.\n\n"
                "O modelo assume alimentação estável e conexões ideais."
            ),
        },

        # -------------------------------------------------
        # INTERPRETAÇÃO AVANÇADA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "5. Interpretação técnica",
        },

        {
            "tipo": "texto",
            "texto": (
                "Quando o comportamento medido não coincide com o modelo, "
                "isso não significa automaticamente que o módulo está defeituoso.\n\n"
                "Pode significar que:\n"
                "- O modelo não contempla todos os efeitos físicos presentes.\n"
                "- Há variáveis externas influenciando o sistema."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.005.0003",
            "pergunta": (
                "Explique a diferença entre erro de medição, falha do sistema "
                "e limitação do modelo."
            ),
        },

        # -------------------------------------------------
        # SÍNTESE CONCEITUAL
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "6. Síntese conceitual",
        },

        {
            "tipo": "texto",
            "texto": (
                "Modelos são ferramentas de interpretação. Eles são válidos dentro de um conjunto de hipóteses."
                "Quando as hipóteses deixam de ser satisfeitas, o modelo deixa de descrever corretamente o sistema."
                "Reconhecer o limite do modelo é um passo de maturidade técnica."
            ),
        },
    ]