from __future__ import annotations
import streamlit as st


def get_blocos() -> list[dict]:
    return [

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Primeira Lei da Termodinâmica e balanço de energia"},

        {"tipo": "texto", "texto": (
            "Na etapa anterior, foram identificados os mecanismos de transferência de calor presentes no ambiente. "
            "Agora, o objetivo é avançar da descrição qualitativa para a quantificação do sistema.\n\n"
            "O problema deixa de ser apenas 'como o calor se transfere' e passa a ser:\n"
            "→ quanto de energia entra, quanto sai e qual é o efeito disso no sistema.\n\n"
            "Isso é feito por meio da Primeira Lei da Termodinâmica."
        )},

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Sistema, fronteira e volume de controle"},

        {"tipo": "texto", "texto": (
            "Antes de aplicar a Primeira Lei, é necessário definir claramente o sistema de análise.\n\n"
            "Sistema: região do espaço escolhida para análise.\n"
            "Fronteira: limite que separa o sistema do meio externo.\n\n"
            "No caso da sala, podemos tratá-la como um volume de controle, onde energia pode atravessar a fronteira.\n\n"
            "Essa escolha é fundamental, pois define quais fluxos devem ser considerados no balanço energético."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0001",
            "pergunta": (
                "Ao modelar uma sala como sistema térmico, o que representa a fronteira?"
            ),
            "alternativas": {
                "a": "A temperatura média do ar.",
                "b": "As paredes, janelas e superfícies que delimitam o ambiente.",
                "c": "A quantidade de pessoas na sala.",
                "d": "A energia interna do sistema."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Primeira Lei da Termodinâmica"},

        {"tipo": "texto", "texto": (
            "A Primeira Lei expressa a conservação de energia.\n\n"
            "Para um sistema geral:"
        )},

        {"tipo": "equacao",
         "latex": r"\Delta U = Q - W,"
        },

        {"tipo": "texto", "texto": (
            "onde:\n"
            "ΔU → variação da energia interna\n"
            "Q → calor transferido para o sistema\n"
            "W → trabalho realizado pelo sistema\n\n"
            "Essa equação afirma que a energia não é criada nem destruída, apenas transformada."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0002",
            "pergunta": (
                "Se um sistema recebe calor e não realiza trabalho, o que ocorre com sua energia interna?"
            ),
            "alternativas": {
                "a": "Permanece constante.",
                "b": "Diminui.",
                "c": "Aumenta.",
                "d": "Depende apenas da massa."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Balanço de energia em regime permanente"},

        {"tipo": "texto", "texto": (
            "Para sistemas como uma sala em funcionamento contínuo, é comum assumir regime permanente.\n\n"
            "Isso significa que a energia interna do sistema não varia significativamente ao longo do tempo.\n\n"
            "Nesse caso:"
        )},

        {"tipo": "equacao",
         "latex": r"\sum \dot{Q}_{entrada} = \sum \dot{Q}_{saida}",
        },

        {"tipo": "texto", "texto": (
            "Ou seja, toda a energia que entra no sistema deve sair.\n\n"
            "Essa simplificação é poderosa, pois permite modelar o sistema sem acompanhar sua evolução temporal."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0003",
            "pergunta": (
                "Em regime permanente, qual condição é válida para o sistema?"
            ),
            "alternativas": {
                "a": "A energia interna aumenta continuamente.",
                "b": "A energia interna diminui continuamente.",
                "c": "A energia interna permanece aproximadamente constante.",
                "d": "Não há troca de energia com o meio."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Modelagem energética da sala"},

        {"tipo": "texto", "texto": (
            "A sala pode agora ser tratada como um sistema térmico completo.\n\n"
            "Entradas de energia:\n"
            "- Radiação solar\n"
            "- Equipamentos elétricos\n"
            "- Presença de pessoas\n"
            "- Entrada de ar quente\n\n"
            "Saídas de energia:\n"
            "- Perdas pelas paredes (condução)\n"
            "- Ventilação\n"
            "- Troca com superfícies mais frias\n\n"
            "O problema passa a ser identificar quais desses termos são relevantes."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0004",
            "pergunta": (
                "Qual das opções representa corretamente uma entrada de energia no sistema?"
            ),
            "alternativas": {
                "a": "Perda de calor pelas paredes.",
                "b": "Ventilação do ambiente.",
                "c": "Radiação solar incidente.",
                "d": "Troca com superfícies frias."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Hipóteses e simplificações"},

        {"tipo": "texto", "texto": (
            "Nenhum modelo real inclui todos os fenômenos possíveis.\n\n"
            "Por isso, é necessário estabelecer hipóteses, como:\n"
            "- Regime permanente\n"
            "- Propriedades constantes\n"
            "- Desprezo de termos pouco relevantes\n\n"
            "A validade do modelo depende diretamente dessas escolhas."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0005",
            "pergunta": (
                "Por que é necessário fazer simplificações em um modelo térmico?"
            ),
            "alternativas": {
                "a": "Para eliminar completamente a física do problema.",
                "b": "Para tornar o problema resolvível mantendo sua essência física.",
                "c": "Porque os fenômenos não existem na prática.",
                "d": "Para evitar cálculos matemáticos."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Mini-entrega — Balanço de energia da sala"},

        {"tipo": "texto", "texto": (
            "O aluno deve construir um modelo energético simplificado do ambiente.\n\n"
            "O relatório deve conter:\n\n"
            "- Definição do sistema (delimitação da sala)\n"
            "- Identificação das entradas e saídas de energia\n"
            "- Equação de balanço energético\n"
            "- Hipóteses adotadas\n"
            "- Justificativa para os termos desprezados\n\n"
            "O objetivo não é obter um valor exato, mas estruturar corretamente o problema físico."
        )},

        {"tipo": "texto", "texto": (
            "Ao final desta etapa, o aluno deve ser capaz de:\n\n"
            "- Aplicar a Primeira Lei da Termodinâmica\n"
            "- Construir um balanço de energia\n"
            "- Identificar termos dominantes\n"
            "- Justificar simplificações com base física\n"
            "- Interpretar o ambiente como um sistema de engenharia"
        )},

# ========================================================
# ========================================================
    ]