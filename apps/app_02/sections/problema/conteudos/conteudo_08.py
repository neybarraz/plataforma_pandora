from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Delimitação do escopo da análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao analisar um problema de engenharia, é importante estabelecer "
                "claramente quais aspectos serão considerados na investigação e "
                "quais não fazem parte do estudo naquele momento. Essa definição "
                "é chamada de delimitação do escopo.\n\n"
                "No caso do sistema de bombeamento analisado, o objetivo principal "
                "é compreender o dimensionamento da alimentação elétrica do motor "
                "com base nos fundamentos da eletricidade. Assim, a análise será "
                "concentrada nas grandezas elétricas envolvidas no funcionamento "
                "do motor e no comportamento do circuito que o alimenta."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_023",
            "pergunta": (
                "Ao delimitar o escopo deste estudo, qual abordagem representa "
                "corretamente o foco da análise?"
            ),
            "alternativas": {
                "a": "Analisar detalhadamente todas as normas técnicas aplicáveis",
                "b": "Investigar exclusivamente os fundamentos elétricos envolvidos na alimentação do motor",
                "c": "Projetar completamente o sistema hidráulico do bombeamento",
                "d": "Definir todos os dispositivos de proteção elétrica da instalação",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para manter o estudo focado e coerente, alguns aspectos não serão "
                "aprofundados nesta etapa. A análise não considerará detalhamento "
                "de normas técnicas específicas de instalação elétrica nem o "
                "dimensionamento de dispositivos de proteção.\n\n"
                "Esses elementos são importantes em projetos completos de sistemas "
                "elétricos, mas não fazem parte do objetivo principal deste estudo, "
                "que é compreender os fundamentos envolvidos no dimensionamento da "
                "alimentação elétrica do motor."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_024",
            "pergunta": (
                "Explique, com suas palavras, por que é importante delimitar o "
                "escopo de um problema de engenharia antes de iniciar a análise "
                "técnica do sistema."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]