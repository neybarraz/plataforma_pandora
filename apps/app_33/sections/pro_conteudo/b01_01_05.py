import streamlit as st

def get_blocos() -> list[dict]:
    return [


# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Máquinas térmicas e soluções de engenharia"},

        {"tipo": "texto", "texto": (
            "Após analisar os fluxos de calor, construir o balanço energético e compreender os limites "
            "impostos pela Segunda Lei, o problema passa a ser de engenharia:\n\n"
            "→ Como intervir no sistema para melhorar o conforto térmico?\n\n"
            "Essa etapa conecta os conceitos fundamentais com soluções reais utilizadas em climatização."
        )},

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Máquinas térmicas e refrigeradores"},

        {"tipo": "texto", "texto": (
            "Máquinas térmicas operam convertendo calor em trabalho.\n\n"
            "Já os sistemas de refrigeração realizam o processo inverso: utilizam trabalho para remover calor "
            "de uma região de menor temperatura para outra de maior temperatura.\n\n"
            "Isso não ocorre espontaneamente e exige energia externa."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.005.0001",
            "pergunta": (
                "Qual é a função principal de um sistema de refrigeração?"
            ),
            "alternativas": {
                "a": "Gerar frio como forma de energia.",
                "b": "Reduzir a energia total do sistema.",
                "c": "Remover calor de uma região e rejeitá-lo em outra.",
                "d": "Eliminar completamente a transferência de calor."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Rendimento e coeficiente de desempenho (COP)"},

        {"tipo": "texto", "texto": (
            "O desempenho de sistemas térmicos é avaliado por métricas específicas.\n\n"
            "Para máquinas térmicas:"
        )},

        {"tipo": "equacao",
         "latex": r"\eta = \frac{W}{Q_{entrada}}",
        },

        {"tipo": "texto", "texto": (
            "Para refrigeradores:"
        )},

        {"tipo": "equacao",
         "latex": r"COP = \frac{Q_{removido}}{W}",
        },

        {"tipo": "texto", "texto": (
            "O COP pode ser maior que 1, pois não representa eficiência energética, mas sim "
            "a relação entre calor removido e trabalho fornecido."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.005.0002",
            "pergunta": (
                "Por que o coeficiente de desempenho (COP) pode ser maior que 1?"
            ),
            "alternativas": {
                "a": "Porque viola a conservação de energia.",
                "b": "Porque considera calor transferido, não apenas energia convertida.",
                "c": "Porque o sistema não realiza trabalho.",
                "d": "Porque elimina perdas térmicas."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Limites impostos pela Segunda Lei"},

        {"tipo": "texto", "texto": (
            "A Segunda Lei impõe limites ao desempenho desses sistemas.\n\n"
            "O desempenho máximo é dado pelo ciclo de Carnot:"
        )},

        {"tipo": "equacao",
         "latex": r"COP_{Carnot} = \frac{T_f}{T_q - T_f}",
        },

        {"tipo": "texto", "texto": (
            "onde T_f é a temperatura da região fria e T_q da região quente.\n\n"
            "Nenhum sistema real pode ultrapassar esse limite."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.005.0003",
            "pergunta": (
                "O ciclo de Carnot representa:"
            ),
            "alternativas": {
                "a": "Um sistema real de alto desempenho.",
                "b": "Um limite teórico ideal.",
                "c": "Um sistema sem transferência de calor.",
                "d": "Um processo irreversível."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Aplicação ao conforto térmico"},

        {"tipo": "texto", "texto": (
            "Diante do desconforto térmico observado na sala, diversas soluções podem ser propostas.\n\n"
            "Cada solução atua de forma diferente no balanço energético:\n\n"
            "- Ventilação → aumenta convecção e redistribui energia\n"
            "- Isolamento → reduz fluxo de calor por condução\n"
            "- Sombreamento → reduz ganho por radiação\n"
            "- Refrigeração → remove calor do ambiente\n\n"
            "A escolha da solução depende da análise física do sistema."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.005.0004",
            "pergunta": (
                "Qual intervenção atua diretamente reduzindo o ganho de calor por radiação solar?"
            ),
            "alternativas": {
                "a": "Ventilação",
                "b": "Isolamento interno",
                "c": "Sombreamento",
                "d": "Refrigeração"
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Análise técnica das soluções"},

        {"tipo": "texto", "texto": (
            "Uma solução adequada não é aquela que simplesmente reduz a temperatura, "
            "mas aquela que atua de forma coerente com o balanço de energia e os limites físicos do sistema.\n\n"
            "Por exemplo:\n"
            "- Refrigeração consome energia e possui limite de eficiência\n"
            "- Isolamento pode reduzir perdas sem consumo energético contínuo\n"
            "- Ventilação pode ser eficaz ou não dependendo das condições externas\n\n"
            "A decisão deve ser fundamentada fisicamente."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.005.0005",
            "pergunta": (
                "Qual critério deve orientar a escolha de uma solução térmica?"
            ),
            "alternativas": {
                "a": "Apenas reduzir a temperatura rapidamente.",
                "b": "Minimizar custos independentemente do efeito físico.",
                "c": "Analisar o balanço energético e os limites termodinâmicos.",
                "d": "Aplicar sempre o mesmo tipo de solução."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Mini-entrega — Proposta de intervenção térmica"},

        {"tipo": "texto", "texto": (
            "O aluno deve propor uma solução para melhorar o conforto térmico da sala.\n\n"
            "O relatório deve conter:\n\n"
            "- Diagnóstico do problema (com base nas etapas anteriores)\n"
            "- Identificação dos mecanismos dominantes\n"
            "- Proposta de intervenção (ventilação, isolamento, sombreamento ou refrigeração)\n"
            "- Justificativa baseada no balanço de energia\n"
            "- Discussão dos limites impostos pela Segunda Lei\n\n"
            "A proposta deve ser tecnicamente fundamentada, não apenas descritiva."
        )},

        {"tipo": "texto", "texto": (
            "Ao final desta etapa, o aluno deve ser capaz de:\n\n"
            "- Relacionar teoria termodinâmica com soluções reais\n"
            "- Avaliar desempenho de sistemas térmicos\n"
            "- Interpretar limites físicos de eficiência\n"
            "- Propor intervenções com base em modelos\n"
            "- Atuar como engenheiro na tomada de decisão\n\n"
            "Essa etapa encerra o ciclo completo: análise, modelagem e decisão técnica."
        )},

# ========================================================
# ========================================================
    ]