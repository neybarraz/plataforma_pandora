from __future__ import annotations


def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Procedimento estruturado de verificação",
        },

        # -------------------------------------------------
        # VISÃO GERAL
        # -------------------------------------------------

        {
            "tipo": "texto",
            "texto": (
                "Ao longo das etapas anteriores, você percorreu um fluxo técnico completo:\n\n"
                "1. Observou o sistema real.\n"
                "2. Mediu grandezas físicas relevantes.\n"
                "3. Entendeu o funcionamento do carregador.\n"
                "4. Modelou o comportamento esperado.\n"
                "5. Comparou medições com o modelo.\n"
                "6. Identificou os limites dessa representação.\n\n"
                "Agora organizaremos isso como um procedimento técnico reutilizável."
            ),
        },

        # -------------------------------------------------
        # PROCEDIMENTO ESTRUTURADO
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "1. Procedimento técnico para verificar carga com TP4056",
        },

        {
            "tipo": "texto",
            "texto": (
                "Passo 1 — Medir a tensão da bateria.\n\n"
                "- Se V_bat < 4,2 V → carga ainda não finalizada.\n\n"
                "Passo 2 — Medir a corrente que entra na bateria.\n"
                "- Se I ≠ 0 → há transferência de carga.\n"
                "- Se I = 0 e V_bat < 4,2 V → possível anomalia.\n\n"
                "Passo 3 — Identificar o regime de operação.\n"
                "- V_bat < 4,2 V e I ≈ I_prog → Fase CC.\n"
                "- V_bat ≈ 4,2 V e I diminuindo → Fase CV.\n\n"
                "Passo 4 — Comparar com o comportamento esperado.\n"
                "- Curva coerente → funcionamento normal.\n"
                "- Curva incoerente → investigar causas externas ou limites do modelo."
            ),
        },

        # -------------------------------------------------
        # ESTRUTURA MENTAL
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "2. Estrutura mental construída",
        },

        {
            "tipo": "texto",
            "texto": (
                "Você deixou de agir por tentativa e erro. Agora sua análise segue uma lógica estruturada:\n\n"
                "- Medir\n"
                "- Interpretar\n"
                "- Modelar\n"
                "- Comparar\n"
                "- Decidir\n\n"
                "Essa sequência transforma observação em raciocínio técnico."
            ),
        },

        # -------------------------------------------------
        # DIFERENCIAÇÃO IMPORTANTE
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "3. Verificação funcional vs diagnóstico de falha",
        },

        {
            "tipo": "texto",
            "texto": (
                "Verificação funcional significa confirmar se o comportamento está de acordo com o regime esperado (CC/CV). "
                "Diagnóstico de falha exige investigação adicional quando o comportamento diverge do modelo. "
                "Nem toda divergência indica defeito estrutural; pode indicar limite do modelo ou influência externa."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.005.0001",
            "pergunta": (
                "Explique com suas palavras a diferença entre verificar "
                "o funcionamento e diagnosticar uma falha."
            ),
        },

        # -------------------------------------------------
        # MATURIDADE TÉCNICA
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "4. Nível de maturidade técnica",
        },

        {
            "tipo": "texto",
            "texto": (
                "O engenheiro competente não apenas mede valores.\n"
                "Ele entende o regime físico em que o sistema opera.\n\n"
                "A maturidade técnica aparece quando:\n"
                "- Você reconhece o comportamento esperado.\n"
                "- Identifica desvios.\n"
                "- Avalia se o modelo ainda é válido.\n\n"
                "Essa é a transição de operador para analista."
            ),
        },

        # -------------------------------------------------
        # FECHAMENTO FINAL
        # -------------------------------------------------

        {
            "tipo": "subtitulo",
            "texto": "5. Síntese final",
        },

        {
            "tipo": "texto",
            "texto": (
                "Para validar o TP4056 de forma estruturada:\n\n"
                "- Meça tensão.\n"
                "- Meça corrente.\n"
                "- Identifique o regime (CC ou CV).\n"
                "- Compare com o modelo.\n"
                "- Avalie os limites.\n\n"
                "Sem modelo, você observa números.\n"
                "Com modelo, você interpreta comportamento. Esse é o fechamento completo do ciclo técnico."
            ),
        },
    ]