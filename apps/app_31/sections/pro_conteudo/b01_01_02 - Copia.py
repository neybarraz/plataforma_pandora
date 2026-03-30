from __future__ import annotations

import streamlit as st


def _get_valor(qid: str, fallback: str = "—") -> str:
    key = f"problema_{qid}"
    valor = st.session_state.get(key)

    if valor is None or str(valor).strip() == "":
        return fallback

    return str(valor).strip()


def _texto_tensao() -> str:
    tensao_medida = _get_valor("problema.01.001.0011", "um valor de tensão")
    tensao_nominal = _get_valor("problema.01.001.0002", "o valor da placa")

    return (
        f"No motor, você mediu {tensao_medida} V. "
        f"Agora compare esse valor com o valor indicado na placa do motor, que é {tensao_nominal} V.\n\n"
        "- Se os valores forem próximos, a energia está chegando como esperado.\n"
        "- Se o valor medido for menor, isso mostra que parte da energia está sendo perdida no caminho "
        "entre o quadro e o motor."
    )

def _texto_corrente() -> str:
    corrente = _get_valor("problema.01.001.0012", "um valor de corrente")

    return (
        f"Agora observe a corrente medida no motor, que é {corrente} A. "
        "Ter tensão disponível não garante funcionamento. "
        "O motor só opera quando a energia realmente circula pelo circuito. "
        "Se há tensão, mas não há corrente, isso significa que a energia não está fluindo. "
        "Ou seja, existe potencial elétrico, mas não existe movimento de cargas."
    )

def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Perguntas de diagnóstico do sistema elétrico",
        },

        {
            "tipo": "texto",
            "texto": (
                "Depois da visita técnica, você já possui medições e informações do sistema. "
                "Agora o objetivo é transformar esses dados em diagnóstico. "
                "Nesta etapa, a análise é guiada por perguntas-chave:\n\n"
                "- a energia está chegando ao motor?\n"
                "- essa energia está circulando?\n"
                "- o caminho está adequado?\n"
                "- as condições do sistema permitem funcionamento correto?\n\n"
                "O ponto de partida é o contraste entre a medição real e o comportamento esperado do sistema. "
                "A partir dessa análise, as variações observadas são traduzidas e descritas em linguagem matemática."
            ),
        },

        # -------------------------------------------------
        # VERIFICAÇÃO 1 — TENSÃO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Verificação 1: a energia chega ao motor?",
        },
        {
            "tipo": "texto",
            "texto": _texto_tensao(),
        },

        {
            "tipo": "equacao",
            "latex": r"\Delta V = V_{fonte} - V_{motor}",
        },

        {
            "tipo": "texto",
            "texto": (
                "Essa expressão mostra a diferença entre a tensão de saída do quadro e a tensão que realmente "
                "chega ao motor. "
                "Quando essa diferença aparece, ela recebe o nome de queda de tensão."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0001",
            "pergunta": (
                "Se a tensão medida no motor for menor que a indicada na placa, o que isso significa?"
            ),
            "alternativas": {
                "a": "O motor está recebendo energia extra",
                "b": "Parte da energia está sendo perdida no caminho",
                "c": "O motor está desligado",
                "d": "O cabo está superdimensionado",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0002",
            "pergunta": (
                "Se você mede zero de tensão no motor, qual é a interpretação mais provável?"
            ),
            "alternativas": {
                "a": "O sistema está funcionando normalmente",
                "b": "A energia não está chegando ao motor",
                "c": "O motor está consumindo demais",
                "d": "O cabo está com pouca resistência",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # VERIFICAÇÃO 2 — CORRENTE
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Verificação 2: a energia está circulando?",
        },
        {
            "tipo": "texto",
            "texto": _texto_corrente(),
        },
        {
            "tipo": "equacao",
            "latex": r"V = R \cdot I",
        },

        {
            "tipo": "texto",
            "texto": (
                "A Lei de Ohm mostra que tensão, corrente e resistência estão conectadas. "
                "No diagnóstico, ela permite interpretar o comportamento real do circuito. "
                "Se a corrente for zero, isso indica que existe uma interrupção no circuito. "
                "Ou seja:\n\n"
                "- a energia não está circulando\n"
                "- existe uma barreira no caminho da corrente\n"
                "- o motor não recebe potência, mesmo com tensão presente"
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0003",
            "pergunta": (
                "Se existe tensão no motor, mas a corrente medida é zero, o que isso indica?"
            ),
            "alternativas": {
                "a": "O motor está funcionando normalmente",
                "b": "A energia não está circulando",
                "c": "A tensão está alta",
                "d": "O cabo está correto",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "Agora considere outro cenário. "
                "Se a corrente medida for maior que o esperado, isso indica que o sistema está sob esforço. "
                "Quando a tensão no motor é menor do que deveria, o sistema tenta compensar. "
                "Para manter a potência, a corrente aumenta. "
                "Isso pode indicar:\n\n"
                "- queda de tensão no cabo\n"
                "- esforço maior do motor\n"
                "- aquecimento do sistema"
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0004",
            "pergunta": (
                "Se a corrente medida for maior que o esperado, o que pode estar acontecendo?"
            ),
            "alternativas": {
                "a": "O sistema está sem carga",
                "b": "O motor pode estar recebendo menos tensão do que deveria",
                "c": "O cabo está muito grosso",
                "d": "A distância é pequena",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # VERIFICAÇÃO 3 — CAMINHO FECHADO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Verificação 3: o caminho está completo?",
        },

        {
            "tipo": "texto",
            "texto": (
                "Para a energia circular, o caminho elétrico precisa estar completo. "
                "Se houver uma interrupção em qualquer ponto, o motor deixa de funcionar, "
                "mesmo que ainda exista tensão em parte do circuito."
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"I = \frac{V}{R}",
        },

        {
            "tipo": "texto",
            "texto": (
                "Essa forma da relação anterior ajuda a enxergar o diagnóstico de outro jeito. "
                "Se a tensão existe, mas a corrente tende a zero, isso indica que a resistência equivalente "
                "do caminho ficou muito alta, como acontece em uma interrupção, mau contato ou componente aberto."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0005",
            "pergunta": (
                "Qual situação indica que o caminho da energia está interrompido?"
            ),
            "alternativas": {
                "a": "Corrente alta",
                "b": "Tensão nominal",
                "c": "Corrente zero",
                "d": "Motor girando normalmente",
            },
            "alternativa_correta": "c",
        },

        # -------------------------------------------------
        # VERIFICAÇÃO 4 — CABO / DISTÂNCIA
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Verificação 4: o cabo está influenciando demais o sistema?",
        },

        {
            "tipo": "texto",
            "texto": (
                "A energia sai do quadro e percorre todo o cabo até o motor. "
                "Esse percurso não é neutro. "
                "Quanto maior a distância, maior tende a ser o efeito do próprio cabo sobre o sistema. "
                "Por isso, o comprimento do circuito entra diretamente no diagnóstico."
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"R = \rho \frac{L}{A}",
        },

        {
            "tipo": "texto",
            "texto": (
                "Essa relação mostra que a resistência do cabo aumenta com o comprimento e diminui "
                "quando a seção (área) do condutor aumenta. "
                "Ou seja: cabos longos e finos dificultam mais a passagem da energia."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0006",
            "pergunta": (
                "Se a distância entre o quadro e o motor aumenta, o que tende a acontecer?"
            ),
            "alternativas": {
                "a": "A energia chega mais forte",
                "b": "Nada muda no circuito",
                "c": "A influência do cabo tende a aumentar",
                "d": "O motor consome menos energia",
            },
            "alternativa_correta": "c",
        },

        # -------------------------------------------------
        # VERIFICAÇÃO 5 — CONDIÇÕES DE OPERAÇÃO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Verificação 5: o cabo está operando em condições favoráveis?",
        },

        {
            "tipo": "texto",
            "texto": (
                "O desempenho do cabo não depende apenas do material e da bitola. "
                "A forma de instalação e a temperatura do ambiente também alteram o comportamento do sistema. "
                "Se o ambiente estiver muito quente, ou se a instalação dificultar a dissipação de calor, "
                "o cabo pode aquecer mais do que o esperado."
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"P = R \cdot I^2",
        },

        {
            "tipo": "texto",
            "texto": (
                "Essa expressão mostra que a energia dissipada em forma de calor cresce com a resistência "
                "e com o quadrado da corrente. "
                "Por isso, correntes elevadas e condições térmicas ruins tornam o circuito mais crítico."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.002.0007",
            "pergunta": (
                "Qual situação pode aumentar o aquecimento do cabo?"
            ),
            "alternativas": {
                "a": "Ambiente mais frio",
                "b": "Distância menor",
                "c": "Temperatura ambiente elevada",
                "d": "Queda de corrente",
            },
            "alternativa_correta": "c",
        },

        # -------------------------------------------------
        # FECHAMENTO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Síntese do diagnóstico",
        },

        {
            "tipo": "texto",
            "texto": (
                "O diagnóstico do sistema segue uma sequência lógica:\n\n"
                "1. Verificar se a tensão chega ao motor\n"
                "2. Verificar se a energia circula\n"
                "3. Confirmar se o caminho está completo\n"
                "4. Avaliar o efeito do comprimento do cabo\n"
                "5. Considerar as condições de operação\n\n"
                "Agora o problema já pode ser lido em duas camadas:\n"
                "- pela observação do sistema real\n"
                "- e pelas relações matemáticas que descrevem esse comportamento\n\n"
                "Na próxima etapa, essas relações serão usadas para dimensionar o cabo corretamente."
            ),
        },

    ]