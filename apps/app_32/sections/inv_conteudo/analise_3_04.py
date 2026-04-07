from __future__ import annotations


def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Como verificar se o carregamento está correto?",
        },

        # -------------------------------------------------
        # OBJETIVO
        # -------------------------------------------------

        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você já:\n"
                "- Mediu tensão e corrente.\n"
                "- Entendeu o funcionamento CC/CV.\n"
                "- Conhece o modelo simplificado.\n\n"
                "Agora o objetivo é comparar as medições com o comportamento esperado."
            ),
        },

        # -------------------------------------------------
        # CRITÉRIOS OBJETIVOS
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "1. Critérios técnicos de verificação",
        },

        {
            "tipo": "texto",
            "texto": (
                "Use os seguintes critérios para classificar o estado do carregamento:\n\n"
                "- Se V_bat < 4,2 V e I ≈ I_prog → Fase CC (normal)\n"
                "- Se V_bat ≈ 4,2 V e I diminuindo → Fase CV (normal)\n"
                "- Se V_bat < 4,2 V e I = 0 → Anomalia\n"
                "- Se V_bat > 4,2 V → Falha grave de regulação"
            ),
        },

        # -------------------------------------------------
        # INTERPRETAÇÃO
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "2. Interpretação prática",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.004.0001",
            "pergunta": (
                "Se a bateria está em 3,6 V e a corrente medida é próxima da corrente programada, "
                "em qual regime o sistema está operando?"
            ),
            "alternativas": {
                "a": "Fase CV",
                "b": "Fase CC",
                "c": "Falha do módulo",
                "d": "Fim de carga",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.004.0002",
            "pergunta": (
                "Se a bateria está em 4,18 V e a corrente está diminuindo lentamente, "
                "qual é a interpretação correta?"
            ),
            "alternativas": {
                "a": "Curto-circuito",
                "b": "Fase CV normal",
                "c": "Bateria desconectada",
                "d": "Falha térmica",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # SIMULADOR
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "3. Visualização do comportamento esperado",
        },

        {
            "tipo": "texto",
            "texto": (
                "Use o simulador abaixo para observar a curva típica de carga CC/CV "
                "e comparar com os seus dados experimentais."
            ),
        },

        {
            "tipo": "simulador_tp4056"
        },

        # -------------------------------------------------
        # DECISÃO TÉCNICA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "4. Decisão técnica",
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.004.0003",
            "pergunta": (
                "Com base nas suas medições reais, classifique o regime de operação "
                "e justifique tecnicamente sua resposta."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Se o comportamento medido segue a curva esperada, "
                "o carregamento está funcionalmente correto.\n\n"
                "Se houver divergência significativa, "
                "é necessário investigar possíveis falhas."
            ),
        },
    ]