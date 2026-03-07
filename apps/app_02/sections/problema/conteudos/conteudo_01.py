# apps/app_02/sections/problema/conteudos/conteudo_01.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Finalidade do sistema de bombeamento",
        },
        {
            "tipo": "texto",
            "texto": (
                "O sistema analisado tem como finalidade realizar o bombeamento de água "
                "do reservatório inferior para o reservatório superior por meio de uma motobomba "
                "acionada por motor elétrico. Para que esse transporte ocorra, o motor precisa "
                "fornecer energia mecânica à bomba, permitindo vencer a carga hidráulica do sistema "
                "e elevar a água até o nível desejado.\n\n"
                "Ao observar a finalidade do sistema, procure identificar a relação entre a função "
                "hidráulica desempenhada pela bomba e a demanda elétrica exigida do motor. "
                "Essa relação será fundamental para compreender, nas próximas etapas, "
                "o dimensionamento da alimentação elétrica do motor."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, o desafio consiste em analisar o sistema de bombeamento "
                "do Bloco dos Professores e determinar como deve ser dimensionada a "
                "alimentação elétrica do motor da motobomba."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=PSuVujxAcOg",
            "caption": "Funcionamento básico de um sistema de bombeamento de água",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_001",
            "pergunta": (
                "Qual variável está diretamente ligada à origem da demanda elétrica do motor "
                "no sistema de bombeamento?"
            ),
            "alternativas": {
                "a": "A temperatura ambiente da instalação",
                "b": "A distância entre a fonte e o motor",
                "c": "O conjugado exigido pela carga hidráulica da bomba",
                "d": "O tipo de sistema elétrico, independentemente da carga",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "texto",
            "texto": (
                "A demanda elétrica do motor está diretamente associada ao esforço mecânico "
                "que a bomba precisa desenvolver para movimentar a água. Quanto maior a carga "
                "hidráulica do sistema, maior será a potência mecânica requerida e, "
                "consequentemente, maior será a potência elétrica absorvida pelo motor."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_002",
            "pergunta": (
                "Explique, com suas palavras, como a carga hidráulica do sistema de bombeamento "
                "influencia a demanda elétrica do motor da motobomba."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]