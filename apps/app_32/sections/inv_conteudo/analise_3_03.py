from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Como modelar a carga de uma bateria com TP4056",
        },

        # -------------------------------------------------
        # POR QUE MODELAR
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "1. Por que precisamos de um modelo?",
        },
        {
            "tipo": "texto",
            "texto": (
                "Antes de medir qualquer coisa, precisamos responder:\n\n"
                "O que está acontecendo fisicamente durante o carregamento?\n\n"
                "Sem modelo, você apenas observa números.\n"
                "Com modelo, você interpreta comportamento.\n\n"
                "Um modelo elétrico serve para:\n"
                "- prever o comportamento esperado\n"
                "- comparar com medições reais\n"
                "- identificar desvios"
            ),
        },

        # -------------------------------------------------
        # FUNCIONAMENTO CC/CV
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "2. O que o TP4056 faz fisicamente?",
        },
        {
            "tipo": "texto",
            "texto": (
                "O TP4056 implementa um método chamado:\n\n"
                "CC/CV — Corrente Constante / Tensão Constante\n\n"
                "Isso significa que o carregamento ocorre em duas fases distintas:\n"
                "1. Fase de Corrente Constante (CC)\n"
                "2. Fase de Tensão Constante (CV)"
            ),
        },

        # -------------------------------------------------
        # MODELO EQUIVALENTE
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "3. Modelo elétrico simplificado",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para modelar o sistema, usamos três elementos:\n"
                "1. Fonte controlada (o carregador)\n"
                "2. Bateria\n"
                "3. Resistência interna da bateria\n\n"
                "Modelo equivalente:\n\n"
                "- O TP4056 é representado como:\n"
                "  - uma fonte de corrente (fase CC)\n"
                "  - depois como uma fonte de tensão fixa de 4,2 V (fase CV)\n\n"
                "- A bateria pode ser modelada como:\n"
                "  - uma fonte de tensão variável (estado de carga)\n"
                "  - uma resistência interna em série"
            ),
        },

        {
            "tipo": "imagem_descricao",
            "texto": (
                "Diagrama sugerido: TP4056 à esquerda como fonte controlada; "
                "bateria à direita representada por uma fonte de tensão (V_bat) "
                "em série com resistência interna (R_int); "
                "seta indicando corrente I_charge."
            ),
        },

        # -------------------------------------------------
        # FASE CC
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "4. Fase 1 — Corrente Constante (CC)",
        },
        {
            "tipo": "equacao",
            "latex": r"I = I_{prog}",
        },
        {
            "tipo": "texto",
            "texto": (
                "Durante essa fase:\n"
                "- O carregador impõe uma corrente fixa.\n"
                "- A tensão da bateria aumenta gradualmente.\n\n"
                "Se a corrente é constante e a tensão sobe, então a potência entregue aumenta."
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"P = V \cdot I",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.003.0001",
            "pergunta": "Durante a fase CC, o que permanece constante?",
            "alternativas": {
                "a": "Tensão da bateria",
                "b": "Corrente de carga",
                "c": "Potência dissipada",
                "d": "Resistência interna",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.003.0002",
            "pergunta": "Por que a tensão da bateria aumenta durante o carregamento?",
        },

        # -------------------------------------------------
        # TRANSIÇÃO CV
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "5. Transição para Fase CV",
        },
        {
            "tipo": "equacao",
            "latex": r"V_{bat} = 4,2\,V",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.003.0003",
            "pergunta": "Por que o carregador não continua aumentando a tensão?",
            "alternativas": {
                "a": "Porque a corrente caiu",
                "b": "Porque 4,2 V é limite seguro para Li-ion",
                "c": "Porque a resistência interna aumentou",
                "d": "Porque o chip desliga",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # FASE CV
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "6. Fase 2 — Tensão Constante (CV)",
        },
        {
            "tipo": "equacao",
            "latex": r"I \to 0",
        },
        {
            "tipo": "texto",
            "texto": (
                "Agora a tensão permanece fixa em 4,2 V.\n"
                "A corrente diminui gradualmente à medida que a diferença "
                "entre a tensão do carregador e a tensão interna da bateria diminui."
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"I = \frac{V_{charger} - V_{bat}}{R_{int}}",
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.003.0004",
            "pergunta": (
                "O que acontece com a corrente quando V_bat se aproxima de 4,2 V?"
            ),
        },

        # -------------------------------------------------
        # GRÁFICOS
        # -------------------------------------------------

        {
            "tipo": "imagem_descricao",
            "texto": (
                "Gráfico 1: Corrente vs tempo — região plana (CC) seguida de curva decrescente (CV).\n"
                "Gráfico 2: Tensão vs tempo — subida gradual até 4,2 V e depois estabilização."
            ),
        },

        # -------------------------------------------------
        # INTERPRETAÇÃO PROFUNDA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "7. Interpretação física profunda",
        },
        {
            "tipo": "texto",
            "texto": (
                "Corrente é controlada pelo carregador na fase inicial.\n"
                "Depois passa a ser limitada pelo diferencial de tensão e resistência interna.\n"
                "O comportamento da corrente contém informação sobre o estado da bateria."
            ),
        },

        # -------------------------------------------------
        # LIMITES
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "8. Limitações do modelo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Este modelo ignora:\n"
                "- efeitos térmicos\n"
                "- variações químicas complexas\n"
                "- degradação da bateria\n"
                "- controle interno detalhado do chip"
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "investigacao.03.003.0005",
            "pergunta": "Em que situação esse modelo poderia falhar?",
        },

        # -------------------------------------------------
        # SÍNTESE
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "9. Síntese da modelagem",
        },
        {
            "tipo": "texto",
            "texto": (
                "Modelar a carga significa:\n\n"
                "1. Representar o carregador como fonte controlada.\n"
                "2. Representar a bateria como fonte + resistência interna.\n"
                "3. Entender os dois regimes: CC e CV.\n"
                "4. Prever o comportamento esperado de tensão e corrente.\n\n"
                "Sem modelo: você mede números.\n"
                "Com modelo: você interpreta comportamento."
            ),
        },
    ]