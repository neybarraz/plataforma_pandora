import streamlit as st


def get_blocos() -> list[dict]:
    return [
# ==========================================================
# 1. Inconsistência experimental: o estado térmico do ar não basta
# ==========================================================
        {"tipo": "titulo", "texto": "1. Inconsistência experimental: o estado térmico do ar não basta"},
        {"tipo": "texto", "texto": (
            "Considere a sala de aula em uso contínuo, onde diferentes ocupantes relatam sensações térmicas distintas. "
            "Alguns descrevem desconforto por frio, especialmente próximos às paredes externas, enquanto outros, em regiões centrais, "
            "não percebem o mesmo efeito ou relatam condições aceitáveis.\n\n<br>"

            "Uma análise experimental simples é realizada a partir de medições de temperatura do ar em diferentes pontos da sala. "
            "Os resultados indicam valores aproximadamente uniformes, em torno de 24 °C, com variações pequenas entre posições. "
            "No entanto, ao medir a temperatura de superfícies (como paredes, janelas e teto) observam-se diferenças relevantes. "
            "Algumas superfícies apresentam temperaturas significativamente menores que a do ar, especialmente em regiões próximas ao exterior.\n\n"

            "Do ponto de vista físico, surge uma inconsistência: se a temperatura do ar é frequentemente utilizada como indicador "
            "do estado térmico do ambiente, seria esperado que a sensação térmica fosse aproximadamente uniforme. "
            "Contudo, isso não é observado! \n\n"

            "Se a temperatura do ar é praticamente uniforme em toda a sala, por que diferentes regiões produzem sensações térmicas distintas?\n\n"

            "Responder a essa questão exige analisar com rigor o significado físico da temperatura e identificar os limites de sua utilização "
            "como variável descritiva do ambiente térmico."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0001",
            "pergunta": ( "Qual hipótese inicial é mais consistente com as observações experimentais?" ),
            "alternativas": {
                "a": "A temperatura do ar está sendo medida incorretamente.",
                "b": "A temperatura do ar é suficiente para descrever completamente o ambiente térmico.",
                "c": "A temperatura do ar pode não ser a única variável relevante para descrever o ambiente.",
                "d": "A sensação térmica não possui relação com grandezas físicas."
            },
            "alternativa_correta": "c",
        },

        {"tipo": "texto", "texto": (
            "A análise desse cenário indica que a descrição do ambiente térmico não pode se basear exclusivamente na temperatura do ar. "
            "Outros fatores físicos devem influenciar a interação energética entre o corpo humano e o ambiente. "
            "Essa limitação motiva a necessidade de aprofundar o conceito de temperatura e compreender seu significado físico de forma rigorosa."
        )},
# ==========================================================
# 2. Temperatura: variável de estado e equilíbrio térmico
# ==========================================================
        {"tipo": "titulo", "texto": "2. Temperatura: variável de estado e equilíbrio térmico"},
        {"tipo": "texto", "texto": (
            "Para analisar o comportamento térmico do ambiente de forma rigorosa, é necessário compreender o significado físico da temperatura. "
            "Na termodinâmica, a temperatura é definida como uma variável de estado. Isso significa que ela descreve a condição macroscópica "
            "de um sistema e depende apenas do estado atual, independentemente do processo pelo qual esse estado foi alcançado."
        )},

        {"tipo": "subtitulo", "texto": "Equilíbrio térmico"},
        {"tipo": "texto", "texto": (
            "A definição operacional de temperatura está associada ao conceito de equilíbrio térmico. "
            "Dois sistemas estão em equilíbrio térmico quando, ao serem colocados em contato, não ocorre troca líquida de energia entre eles."
        )},

        {"tipo": "subtitulo", "texto": "Lei Zero"},
        {"tipo": "texto", "texto": (
            "A Lei Zero da Termodinâmica estabelece que, se dois sistemas estão separadamente em equilíbrio térmico com um terceiro, "
            "então eles estão em equilíbrio térmico entre si. Essa propriedade permite definir a temperatura de forma consistente e mensurável.\n\n<br>"

            "Assim, a temperatura determina o sentido do fluxo de energia térmica: a energia tende a fluir espontaneamente do sistema de maior "
            "temperatura para o de menor temperatura."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0002",
            "pergunta": ( "Se dois sistemas A e B estão separadamente em equilíbrio térmico com um sistema C, o que se pode afirmar?" ),
            "alternativas": {
                "a": "A temperatura de A é maior que a de B.",
                "b": "A temperatura de B é maior que a de A.",
                "c": "A e B estão em equilíbrio térmico entre si.",
                "d": "Não é possível estabelecer relação entre A e B."
            },
            "alternativa_correta": "c",
        },

        {"tipo": "subtitulo", "texto": "Interpretação microscópica"},

        {"tipo": "texto", "texto": (
            "A teoria cinética dos gases fornece uma interpretação microscópica da temperatura. "
            "Em nível microscópico, a temperatura está associada à energia cinética média das partículas que compõem o sistema. "
            "Quanto maior a agitação das partículas, maior a temperatura. "
            "Para um gás ideal, essa relação pode ser expressa como:"
        )},

        {"tipo": "equacao",
        "latex": r"\langle E_c \rangle \propto T"
        },

        {"tipo": "texto", "texto": (
            "Essa relação indica que a temperatura não mede a energia total do sistema, mas sim uma média estatística associada ao movimento das partículas."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0003",
            "pergunta": ( "Se a temperatura de um sistema aumenta, o que ocorre, em média, com suas partículas?" ),
            "alternativas": {
                "a": "A massa das partículas aumenta.",
                "b": "A energia cinética média aumenta.",
                "c": "O número de partículas diminui.",
                "d": "O volume necessariamente diminui."
            },
            "alternativa_correta": "b",
        },

        {"tipo": "subtitulo", "texto": "Temperatura não é calor!"},

        {"tipo": "texto", "texto": (
            "É importante distinguir temperatura de calor. "
            "Temperatura é uma propriedade do sistema. Já o calor não é armazenado: ele representa energia em trânsito, transferida entre sistemas "
            "devido a uma diferença de temperatura. "
            "Portanto, um sistema não possui 'calor', mas sim energia interna. O termo calor só é aplicável durante processos de transferência de energia."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0004",
            "pergunta": (
                "Qual afirmação descreve corretamente a diferença entre temperatura e calor?"
            ),
            "alternativas": {
                "a": "Calor é uma propriedade armazenada no sistema.",
                "b": "Temperatura é energia em trânsito.",
                "c": "Calor é energia transferida devido à diferença de temperatura.",
                "d": "Temperatura mede a energia total do sistema."
            },
            "alternativa_correta": "c",
        },

        # {"tipo": "texto", "texto": (
        #     "Em síntese, a temperatura é uma grandeza bem definida do ponto de vista físico, associada ao estado do sistema e ao comportamento "
        #     "microscópico médio de suas partículas.\n\n"

        #     "No entanto, como será visto, essa definição, embora rigorosa, não é suficiente para descrever completamente o comportamento térmico "
        #     "de ambientes reais."
        # )},


# ==========================================================
# 3. Descrição termodinâmica do ar (gás ideal)
# ==========================================================
        {"tipo": "titulo", "texto": "3. Descrição termodinâmica do ar (gás ideal)"},
        {"tipo": "texto", "texto": "A equação dos gases ideais relaciona pressão, volume e temperatura em condições onde interações entre partículas são desprezíveis."},
        {"tipo": "equacao", "latex": r"PV = nRT"},
        {"tipo": "texto", "texto": (
            "Significado físico dos termos:\n\n"
            "- P (pressão): força por unidade de área resultante das colisões das partículas com as paredes.\n"
            "- V (volume): espaço disponível para o movimento das partículas.\n"
            "- n (número de mols): quantidade de matéria.\n"
            "- R = 8,314 J/(mol·K): constante que conecta escalas macroscópica e microscópica.\n"
            "- T (temperatura absoluta): proporcional à energia cinética média das partículas. "
            "A temperatura mede a agitação média das partículas, não a energia total do sistema."
        )},

        {"tipo": "subtitulo", "texto": "Exemplo aplicado à sala"},
        {"tipo": "texto", "texto": (
            "Vamos estimar a quantidade de ar presente na sala usando a equação dos gases ideais. "
            "Para isso, são necessários três dados: o volume do ambiente, a temperatura do ar e a pressão. "
            "A pressão será assumida como constante e igual à pressão atmosférica padrão (1,0 × 10⁵ Pa)."
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0101", "rotulo": "Comprimento (x)", "unidade": "m"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0102", "rotulo": "Largura (y)", "unidade": "m"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0103", "rotulo": "Altura (z)", "unidade": "m"},
        {"tipo": "simulador_ambiente_3d"},

        {"tipo": "texto", "texto": "Calcule o volume da sala a partir das dimensões acima."},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0104", "rotulo": "Volume da sala", "unidade": "m³"},

        {"tipo": "texto", "texto": "Meça a temperatura do ar em três posições distintas, calcule a média aritmética e registre."},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0105", "rotulo": "Temperatura do ar", "unidade": "°C"},

        {"tipo": "texto", "texto": "Converta o valor para Kelvin usando a relação:"},
        {"tipo": "equacao", "latex": r"T(K) = T(°C) + 273,15" },
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0106", "rotulo": "Temperatura do ar", "unidade": "K"},

        {"tipo": "texto", "texto": "Agora, aplique a equação dos gases ideais para encontrar o número de mols:"},
        {"tipo": "equacao", "latex": r"n = \frac{PV}{RT}"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0107", "rotulo": "Quantidade de partículas", "unidade": "mol"},

        {"tipo": "texto", "texto": (
            "O cálculo mostra que o ar pode ser tratado como um sistema macroscópico bem definido, "
            "com propriedades médias associadas à temperatura medida. O modelo assume, implicitamente, "
            "que o ambiente é termicamente uniforme."
        )},

        {"tipo": "subtitulo", "texto": "Limitação do modelo"},
        {"tipo": "texto", "texto": (
            "Essa hipótese falha ao confrontar o problema original da sala: "
            "temperatura do ar uniforme, mas sensação térmica variável e superfícies com temperaturas distintas. "
            "A equação dos gases ideais é suficiente para descrever o ar, mas insuficiente para descrever o ambiente. "
            "Para avançar, precisamos de uma ferramenta que capture variações espaciais de temperatura."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0005",
            "pergunta": (
                "Qual conclusão é mais adequada a partir da aplicação do modelo de gás ideal?"
            ),
            "alternativas": {
                "a": "O modelo está incorreto.",
                "b": "O ar não pode ser descrito por equações físicas.",
                "c": "O modelo descreve o ar, mas não explica completamente o ambiente térmico.",
                "d": "A temperatura não tem significado físico."
            },
            "alternativa_correta": "c",
        },

# ==========================================================
# 4. Temperatura como campo: T(x,y,z)
# ==========================================================
        {"tipo": "titulo", "texto": "4. Temperatura como campo: T(x,y,z)"},
        {"tipo": "texto", "texto": (
            "A inconsistência observada na sala mostra que a temperatura não pode ser tratada como uma única grandeza global. "
            "Em um ambiente real, a temperatura varia de ponto para ponto no espaço."
        )},
        {"tipo": "equacao", "latex": r"T = T(x,y,z)"},
        {"tipo": "texto", "texto": (
            "Cada ponto do ambiente pode ter um valor diferente de temperatura. "
            "A descrição por campo térmico é necessária sempre que o sistema não está em equilíbrio térmico interno, "
            "o que é regra, e não exceção, em ambientes reais."
        )},

        {"tipo": "subtitulo", "texto": "Medindo o campo: amostragem e malha"},
        {"tipo": "texto", "texto": (
            "Medições pontuais com sensores fornecem amostras discretas do campo contínuo. "
            "Para reconstruir a distribuição térmica, define-se uma malha de pontos em posições relevantes:"
            "próximo a paredes, janelas e regiões centrais."
        )},

        {"tipo": "simulador_ambiente_2d"},
        {"tipo": "texto", "texto": "Cada ponto da malha fornecerá uma medida. O conjunto desses dados permitirá analisar como a temperatura varia no espaço."},
        
        {"tipo": "subtitulo", "texto": "Definição do plano de medição"},
        {"tipo": "texto", "texto": "A temperatura do ar varia também com a altura. Defina a altura (z) onde todas as medições de temperatura do ar serão realizadas."},
 
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1001", "rotulo": "Altura da medição", "unidade": "m"},

        {"tipo": "subtitulo", "texto": "Temperatura do ar (Ta)"},
        {"tipo": "texto", "texto": (
            "Meça a temperatura do ar em cinco posições distribuídas no plano horizontal: "
            "quatro próximas aos cantos da sala (NO, NE, SO, SE) e uma no centro (C). "
            "Registre os valores em °C."
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1002", "rotulo": "NO (Noroeste)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1003", "rotulo": "NE (Nordeste)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1004", "rotulo": "SO (Sudoeste)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1005", "rotulo": "SE (Sudeste)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1006", "rotulo": "Centro (C)", "unidade": "°C"},

        {"tipo": "subtitulo", "texto": "Temperatura das superfícies (Ts)"},
        {"tipo": "texto", "texto": (
            "Superfícies como paredes trocam radiação térmica com o corpo humano, afetando a sensação térmica. "
            "Meça a temperatura em dois pontos de cada parede (Norte, Leste, Sul, Oeste) e registre os valores."
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1007", "rotulo": "N1 (Norte - esquerda)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1008", "rotulo": "N2 (Norte - direita)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1009", "rotulo": "L1 (Leste - superior)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1010", "rotulo": "L2 (Leste - inferior)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1011", "rotulo": "S1 (Sul - esquerda)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1012", "rotulo": "S2 (Sul - direita)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1013", "rotulo": "O1 (Oeste - superior)", "unidade": "°C"},
        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1014", "rotulo": "O2 (Oeste - inferior)", "unidade": "°C"},

        {"tipo": "subtitulo", "texto": "Condições do ambiente"},
        {"tipo": "texto", "texto": (
            "A temperatura externa influencia as trocas térmicas através das paredes. "
            "O número de ocupantes e equipamentos ativos adiciona calor ao ambiente."
        )},

        # {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1015", "rotulo": "Temperatura externa", "unidade": "°C"},
        # {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1016", "rotulo": "Número de ocupantes", "unidade": "pessoas"},
        # {"tipo": "entrada_numerica_inline", "id": "problema.01.001.1017", "rotulo": "Equipamentos ativos", "unidade": "unid."},


# ==========================================================
# 5. Gradiente de temperatura e análise espacial
# ==========================================================
        {"tipo": "titulo", "texto": "5. Gradiente de temperatura e análise espacial"},
        {"tipo": "texto", "texto": (
            "As medições discretas (pontuais) podem ser convertidas em uma representação contínua aproximada do campo de temperatura. "
            "O resultado é um mapa térmico, que visualiza como a temperatura varia no espaço, evidenciando regiões mais quentes e mais frias."
        )},
        {"tipo": "subtitulo", "texto": "Mapa térmico do ambiente"},
        {"tipo": "simulador_campo_termico_2d"},

        {"tipo": "subtitulo", "texto": "Gradiente de temperatura"},
        {"tipo": "texto", "texto": (
            "O mapa mostra onde a temperatura é maior ou menor, mas não indica com que rapidez ela muda ao se deslocar no espaço. "
            "Essa informação é dada pelo gradiente de temperatura. Em duas dimensões (plano horizontal da sala):"
        )},
        {"tipo": "equacao", "latex": r"\nabla T = \frac{\partial T}{\partial x} \hat{i} + \frac{\partial T}{\partial y} \hat{j}"},
        {"tipo": "texto", "texto": (
            "Onde:\n\n"
            "- ∂T/∂x: taxa de variação da temperatura na direção x (leste-oeste);\n"
            "- ∂T/∂y: taxa de variação da temperatura na direção y (norte-sul);\n"
            "- î e ĵ: vetores unitários nas direções x e y."
        )},

        {"tipo": "texto", "texto": (
            "O gradiente tem direção (aponta para onde a temperatura mais aumenta) e intensidade (mede o quão rápida é essa variação). "
            "Gradientes pequenos indicam regiões aproximadamente uniformes; gradientes grandes indicam variações bruscas em pequenas distâncias."
        )},

        {"tipo": "subtitulo", "texto": "Interpretação física"},

        {"tipo": "texto", "texto": (
            "Gradientes de temperatura indicam que o sistema não está em equilíbrio térmico local. "
            "Quanto maior o gradiente, maior a tendência de redistribuição de energia entre regiões, "
            "o que antecipa a necessidade de uma teoria de transferência de calor."
        )},

# ==========================================================
# 6. Limite do estado térmico: a temperatura não explica fluxos
# ==========================================================
        {"tipo": "titulo", "texto": "6. Limite do estado térmico: a temperatura não explica fluxos"},

        {"tipo": "texto", "texto": (
            "Com a temperatura como campo e o gradiente, conseguimos descrever onde está mais quente ou frio e com que rapidez a temperatura varia no espaço. "
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0006",
            "pergunta": "Com base na análise do campo de temperatura, qual conclusão é mais adequada?",
            "alternativas": {
                "a": "A temperatura descreve completamente o sistema térmico.",
                "b": "O modelo está incorreto e deve ser descartado.",
                "c": "A temperatura descreve o estado, mas não explica os processos de transferência de energia.",
                "d": "Não é possível modelar o ambiente com conceitos físicos."
            },
            "alternativa_correta": "c"
        },

        {"tipo": "texto", "texto": (
            "A alternativa correta aponta o limite central: temperatura descreve o estado térmico, mas não os mecanismos de transferência de energia. "
            "Sabemos que há gradientes, logo há redistribuição de energia, mas o modelo atual não diz como nem com que intensidade."
        )},

    {"tipo": "subtitulo", "texto": "Mini-entrega — Diagnóstico térmico inicial"},

    {"tipo": "texto", "texto": (
        "Com base nos dados coletados, elabore um diagnóstico térmico do ambiente contendo:\n\n"
        "- Tabela com as medições de temperatura (ar e superfícies)\n"
        "- Mapa térmico (representação do campo)\n"
        "- Regiões com maior variação térmica\n"
        "- Análise qualitativa do gradiente\n"
        "- Conclusão: por que a temperatura isoladamente é insuficiente?"
    )},

    {"tipo": "subtitulo", "texto": "Fechamento"},
    {"tipo": "texto", "texto": (
        "A temperatura é fundamental para descrever o estado térmico, mas não explica como a energia se move no ambiente. "
        "Esse é o papel da transferência de calor, o tema da próxima etapa."
    )},

    ]