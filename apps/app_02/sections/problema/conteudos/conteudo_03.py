from __future__ import annotations



def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Incertezas do levantamento técnico",
        },
        {
            "tipo": "texto",
            "texto": (
                "No levantamento inicial de um sistema real, nem todas as informações "
                "estão disponíveis ou confirmadas com precisão. Alguns dados podem ser "
                "estimados, incompletos ou ainda não medidos diretamente.\n\n"
                "No sistema de bombeamento analisado, certas informações elétricas ou "
                "condições da instalação podem apresentar incertezas. Reconhecer essas "
                "limitações é importante porque os cálculos realizados nas etapas "
                "seguintes dependem diretamente da qualidade dos dados coletados."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_010",
            "pergunta": (
                "Qual situação representa um exemplo de incerteza em um levantamento técnico?"
            ),
            "alternativas": {
                "a": "Tensão da rede apenas assumida, sem medição",
                "b": "Potência registrada diretamente da placa do motor",
                "c": "Identificação do fabricante do equipamento",
                "d": "Leitura da frequência indicada na placa do motor",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando um dado é apenas estimado ou assumido, ele introduz incerteza "
                "no modelo do sistema. Isso pode afetar resultados importantes, como "
                "o cálculo da corrente do motor, a escolha da seção dos condutores "
                "ou a estimativa da queda de tensão.\n\n"
                "Por essa razão, em projetos de engenharia é fundamental identificar "
                "quais informações são confiáveis e quais ainda precisam ser "
                "confirmadas por medição ou verificação técnica."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_011",
            "pergunta": (
                "Descreva um exemplo de dado que pode apresentar incerteza em um "
                "levantamento técnico do sistema de bombeamento e explique como "
                "essa incerteza pode influenciar os cálculos elétricos."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]