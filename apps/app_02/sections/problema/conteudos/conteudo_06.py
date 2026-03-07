from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Foco do problema: alimentação elétrica do motor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após identificar as características do motor, da alimentação elétrica "
                "e das condições físicas da instalação, é necessário definir com clareza "
                "qual é o foco técnico do problema a ser analisado.\n\n"
                "Neste estudo, o sistema hidráulico de bombeamento já está definido. "
                "O aspecto que será investigado é o comportamento elétrico do motor "
                "que aciona a motobomba. Isso significa que a análise será concentrada "
                "na forma como a energia elétrica é fornecida ao motor e como essa "
                "alimentação deve ser dimensionada para garantir seu funcionamento adequado."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_019",
            "pergunta": (
                "Ao definir o foco elétrico do problema, qual aspecto do sistema "
                "passa a ser o principal objeto de análise?"
            ),
            "alternativas": {
                "a": "A quantidade de água armazenada no reservatório",
                "b": "O dimensionamento da alimentação elétrica do motor",
                "c": "A altura estrutural do prédio",
                "d": "A posição física da bomba no reservatório",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Definir o foco do problema é uma etapa importante da modelagem "
                "de sistemas em engenharia. Ao estabelecer que a análise será "
                "centrada na alimentação elétrica do motor, torna-se possível "
                "identificar quais variáveis precisam ser consideradas e quais "
                "aspectos do sistema não fazem parte do escopo desta investigação.\n\n"
                "Nesse contexto, a análise elétrica do sistema envolve grandezas "
                "como potência do motor, tensão de alimentação, corrente elétrica, "
                "tipo de ligação do motor, seção dos condutores e queda de tensão "
                "no circuito."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_020",
            "pergunta": (
                "Explique, com suas palavras, por que é importante definir "
                "claramente o foco elétrico do problema antes de iniciar os "
                "cálculos do dimensionamento da alimentação do motor."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]