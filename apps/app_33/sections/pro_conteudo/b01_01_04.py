
import streamlit as st

def get_blocos() -> list[dict]:
    return [
# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Segunda Lei da Termodinâmica e irreversibilidades"},

        {"tipo": "texto", "texto": (
            "Até o momento, foi possível descrever e quantificar o fluxo de energia no ambiente. "
            "No entanto, a Primeira Lei não responde a uma questão fundamental:\n\n"
            "→ Por que os processos térmicos ocorrem em uma direção específica?\n\n"
            "A resposta está na Segunda Lei da Termodinâmica, que introduz o conceito de direção "
            "natural dos processos e limitações físicas fundamentais."
        )},

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Sentido natural dos processos térmicos"},

        {"tipo": "texto", "texto": (
            "Observa-se experimentalmente que o calor flui espontaneamente de regiões de maior "
            "temperatura para regiões de menor temperatura.\n\n"
            "O inverso não ocorre sem a realização de trabalho externo.\n\n"
            "Esse comportamento não é explicado pela conservação de energia, mas sim pela Segunda Lei."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0001",
            "pergunta": (
                "Qual afirmação descreve corretamente o sentido natural da transferência de calor?"
            ),
            "alternativas": {
                "a": "Do corpo mais frio para o mais quente.",
                "b": "Do corpo mais quente para o mais frio.",
                "c": "Sempre do maior para o menor volume.",
                "d": "Depende apenas da massa dos corpos."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Entropia e irreversibilidade"},

        {"tipo": "texto", "texto": (
            "A Segunda Lei introduz a grandeza entropia (S), associada ao grau de irreversibilidade "
            "de um processo.\n\n"
            "Para um processo reversível:"
        )},

        {"tipo": "equacao",
         "latex": r"dS = \frac{\delta Q_{rev}}{T}",
        },

        {"tipo": "texto", "texto": (
            "Em processos reais, ocorre geração de entropia:\n\n"
        )},

        {"tipo": "equacao",
         "latex": r"\Delta S_{total} \geq 0",
        },

        {"tipo": "texto", "texto": (
            "Isso significa que todo processo real envolve irreversibilidades.\n\n"
            "A entropia não mede energia, mas sim a qualidade da energia e a dispersão dos estados possíveis."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0002",
            "pergunta": (
                "O aumento de entropia em um sistema está associado a:"
            ),
            "alternativas": {
                "a": "Aumento da energia total.",
                "b": "Aumento da organização do sistema.",
                "c": "Maior dispersão e irreversibilidade.",
                "d": "Redução da temperatura."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Desigualdade de Clausius"},

        {"tipo": "texto", "texto": (
            "A forma geral da Segunda Lei pode ser expressa pela desigualdade de Clausius:"
        )},

        {"tipo": "equacao",
         "latex": r"\oint \frac{\delta Q}{T} \leq 0",
        },

        {"tipo": "texto", "texto": (
            "Essa relação estabelece que não é possível converter integralmente calor em trabalho "
            "em um ciclo termodinâmico.\n\n"
            "Isso impõe limites fundamentais ao desempenho de sistemas térmicos."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0003",
            "pergunta": (
                "A desigualdade de Clausius implica que:"
            ),
            "alternativas": {
                "a": "Toda energia térmica pode ser convertida em trabalho.",
                "b": "Não há perdas em sistemas reais.",
                "c": "Existe limitação na conversão de calor em trabalho.",
                "d": "A energia não é conservada."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Aplicação ao ambiente da sala"},

        {"tipo": "texto", "texto": (
            "No ambiente da sala, diversos processos irreversíveis ocorrem simultaneamente:\n\n"
            "- Troca de calor entre parede fria e ar quente\n"
            "- Interação térmica entre corpo humano e superfícies\n"
            "- Mistura de massas de ar com diferentes temperaturas\n\n"
            "Esses processos não são perfeitamente controláveis e sempre resultam em geração de entropia."
        )},

        {"tipo": "texto", "texto": (
            "O desconforto térmico não é apenas consequência de diferenças de temperatura, "
            "mas também da forma como a energia se redistribui de maneira irreversível.\n\n"
            "O sistema evolui espontaneamente para estados mais prováveis, com maior entropia."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0004",
            "pergunta": (
                "Por que o desconforto térmico pode estar associado a irreversibilidades?"
            ),
            "alternativas": {
                "a": "Porque a energia não é conservada.",
                "b": "Porque os processos térmicos reais envolvem geração de entropia.",
                "c": "Porque a temperatura não varia no ambiente.",
                "d": "Porque não há troca de calor."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Qualidade da energia"},

        {"tipo": "texto", "texto": (
            "Nem toda energia possui a mesma capacidade de realizar trabalho.\n\n"
            "Energia térmica em temperaturas próximas ao ambiente possui baixa qualidade, "
            "pois apresenta menor potencial de conversão em trabalho útil.\n\n"
            "A Segunda Lei introduz essa limitação fundamental."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0005",
            "pergunta": (
                "O conceito de 'qualidade da energia' está relacionado a:"
            ),
            "alternativas": {
                "a": "Quantidade total de energia.",
                "b": "Capacidade de conversão em trabalho útil.",
                "c": "Volume do sistema.",
                "d": "Pressão do sistema."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# ========================================================
        {"tipo": "subtitulo", "texto": "Mini-entrega — Interpretação termodinâmica do ambiente"},

        {"tipo": "texto", "texto": (
            "O aluno deve elaborar um texto técnico curto respondendo à seguinte questão:\n\n"
            "→ Por que o sistema térmico da sala evolui espontaneamente em determinada direção?\n\n"
            "O texto deve incluir:\n\n"
            "- Identificação dos processos irreversíveis\n"
            "- Relação com geração de entropia\n"
            "- Interpretação física da direção do fluxo de calor\n"
            "- Conexão com o desconforto térmico observado\n\n"
            "O foco não é cálculo extenso, mas argumentação técnica baseada em conceitos físicos."
        )},

        {"tipo": "texto", "texto": (
            "Ao final desta etapa, o aluno deve ser capaz de:\n\n"
            "- Interpretar a Segunda Lei da Termodinâmica\n"
            "- Compreender o conceito de entropia\n"
            "- Identificar irreversibilidades em sistemas reais\n"
            "- Relacionar processos térmicos com direção natural\n"
            "- Diferenciar quantidade e qualidade da energia\n\n"
            "Essa etapa consolida o núcleo conceitual da termodinâmica, evitando uma abordagem puramente operacional."
        )},

# ========================================================
# ========================================================
    ]