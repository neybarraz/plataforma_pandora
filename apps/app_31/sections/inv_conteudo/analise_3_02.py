from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Como o carregador TP4056 funciona? (Modelo CC/CV)",
        },
        {
            "tipo": "texto",
            "texto": (
                "O TP4056 é um carregador linear para baterias de íon-lítio de 3,7 V nominal, "
                "cuja tensão máxima de carga é 4,2 V. "
                "O controle do processo ocorre em duas fases: "
                "Corrente Constante (CC) e Tensão Constante (CV)."
            ),
        },

        # -------------------------------------------------
        # FASE 1 — CORRENTE CONSTANTE
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "Fase 1 — Corrente Constante (CC)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a bateria está descarregada, o carregador impõe "
                "uma corrente aproximadamente constante. "
                "Essa corrente é programada por um resistor no pino PROG."
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"I_{charge} = \frac{1000}{R_{prog}} \quad (R\ em\ k\Omega,\ I\ em\ mA)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Durante essa fase, a corrente permanece constante "
                "e a tensão da bateria aumenta gradualmente. "
                "Fisicamente, isso significa que o fluxo de carga elétrica "
                "é controlado diretamente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.002.0001",
            "pergunta": "Na fase CC, qual grandeza é controlada diretamente pelo carregador?",
            "alternativas": {
                "a": "Tensão",
                "b": "Corrente",
                "c": "Resistência",
                "d": "Potência",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # TRANSIÇÃO
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "Transição para Tensão Constante (CV)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a bateria atinge aproximadamente 4,2 V, "
                "o carregador deixa de controlar a corrente e passa a controlar a tensão."
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"V_{bat} = 4,2\,V",
        },
        {
            "tipo": "texto",
            "texto": (
                "A partir desse ponto, a corrente começa a diminuir "
                "porque a diferença entre a tensão imposta e a tensão interna da bateria "
                "vai se reduzindo."
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"I = \frac{V_{fonte} - V_{bat}}{R_{interna}}",
        },

        # -------------------------------------------------
        # INTERPRETAÇÃO FÍSICA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "Interpretação física",
        },
        {
            "tipo": "texto",
            "texto": (
                " \n\n "
                "- Na fase CC → controle do fluxo de carga.\n"
                "- Na fase CV → controle da energia máxima armazenada.\n\n"
                "O processo evita sobrecarga e degradação química."
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "Dissipação térmica (modelo linear)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Como o TP4056 é um carregador linear, a diferença entre "
                "a tensão de entrada e a tensão da bateria é dissipada em forma de calor."
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"P = (V_{in} - V_{bat}) \cdot I",
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.002.0002",
            "pergunta": (
                "Explique por que o aquecimento é maior quando a bateria está muito descarregada."
            ),
        },

        # -------------------------------------------------
        # FIM DE CARGA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "Critério de término de carga",
        },
        {
            "tipo": "texto",
            "texto": (
                "A carga é considerada completa quando a corrente cai para "
                "aproximadamente 10% da corrente programada."
            ),
        },

        # -------------------------------------------------
        # SÍNTESE
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "Síntese técnica",
        },
        {
            "tipo": "texto",
            "texto": (
                "O método CC/CV garante:\n\n"
                "- Controle de corrente inicial\n"
                "- Limitação de tensão máxima\n"
                "- Redução gradual da corrente\n"
                "- Proteção química da bateria"
            ),
        },
    ]