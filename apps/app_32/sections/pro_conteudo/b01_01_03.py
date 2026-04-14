from __future__ import annotations
import streamlit as st


def get_blocos() -> list[dict]:
    return [

# ========================================================
# 1. Introdução: do fluxo ao balanço
# ========================================================
        {"tipo": "titulo", "texto": "1. Da transferência de calor ao balanço de energia"},

        {"tipo": "texto", "texto": (
            "Na etapa do estado térmico, mapeamos o campo de temperaturas da sala, identificando que o ar tem distribuição "
            "relativamente uniforme, mas as superfícies (paredes, janelas) apresentam temperaturas significativamente diferentes. "
            "Na etapa de fluxo de calor, identificamos os três mecanismos de transferência de calor (condução, convecção, radiação) "
            "e construímos um mapa qualitativo dos fluxos, indicando direção e intensidade relativa das trocas térmicas em cada parede.\n\n"
            
            "Nesta etapa, vamos avançar da descrição qualitativa para a quantificação do sistema. O problema deixa de ser apenas "
            "'como o calor se transfere' e passa a ser: quanto de energia entra, quanto sai e qual é o efeito líquido no sistema.\n\n"
            
            "Isso é feito por meio da Primeira Lei da Termodinâmica, o princípio da conservação da energia: a energia não é criada "
            "nem destruída, apenas transformada. Para um sistema, a variação de sua energia interna é igual à diferença entre a "
            "energia que entra e a que sai.\n\n"
            
            "Aplicando esse princípio à sala, obtém-se um balanço de energia: toda energia que entra (por radiação solar, "
            "equipamentos, pessoas, etc.) deve ser igual à energia que sai (por perdas nas paredes, ventilação, etc.) mais a "
            "variação da energia armazenada no sistema. A Primeira Lei conecta os fluxos identificados no seu mapa com a "
            "variação da energia interna da sala."
        )},
# ========================================================
# 2. Sistema, fronteira e volume de controle
# ========================================================
        {"tipo": "titulo", "texto": "2. Definição do sistema de análise"},

        {"tipo": "texto", "texto": (
            "Antes de aplicar a Primeira Lei da Termodinâmica, é necessário definir o sistema de análise. "
            "Essa escolha determina quais fluxos de energia e massa devem ser contabilizados no balanço.\n\n"
            
            "**Sistema:** porção do espaço ou da matéria isolada para estudo. Pode ser fechado (sem troca de massa) "
            "ou aberto (com troca de massa).\n\n"
            
            "**Fronteira:** superfície real ou imaginária que separa o sistema do meio externo. Através dela ocorrem "
            "as interações de calor, trabalho e massa. A fronteira pode ser fixa, móvel, rígida, elástica, real (parede) "
            "ou virtual (um plano imaginário cortando o ar).\n\n"
            
            "**Volume de controle:** abordagem prática para sistemas abertos, onde fixamos uma região no espaço (a sala) "
            "e analisamos o que atravessa suas fronteiras. Essa é a escolha mais adequada para a sala, pois: "
            "(1) as dimensões são fixas, (2) há troca de ar (ventilação/infiltração), (3) a fronteira coincide com as "
            "paredes, janelas, piso e teto.\n\n"
            
            "A definição correta da fronteira é fundamental: ela separa o que está dentro (sistema) do que está fora "
            "(vizinhança) e estabelece quais termos entram no balanço energético."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0001",
            "pergunta": (
                "Uma sala de aula está sendo modelada termicamente para análise do balanço energético em regime permanente. "
                "As paredes externas são de alvenaria, há janelas de vidro, uma porta de madeira que permanece fechada "
                "durante o período de análise, e o sistema de ar condicionado renova parcialmente o ar interno. "
                "Considerando a modelagem como volume de controle, qual alternativa descreve corretamente a fronteira "
                "do sistema e os fluxos que a atravessam?"
            ),
            "alternativas": {
                "a": "A fronteira é definida apenas pelas superfícies externas das paredes externas; calor e massa atravessam essa fronteira.",
                "b": "A fronteira é definida pelas superfícies internas das paredes, piso e teto; apenas calor atravessa a fronteira, pois a porta está fechada.",
                "c": "A fronteira é definida pelas superfícies internas das paredes, piso e teto, incluindo as janelas e a porta; calor e massa (ar de renovação) atravessam a fronteira.",
                "d": "A fronteira é definida por um plano imaginário a 10 cm das paredes; apenas radiação solar atravessa a fronteira."
            },
            "alternativa_correta": "c",
        },


# ========================================================
# 3. Primeira Lei da Termodinâmica
# ========================================================
        {"tipo": "titulo", "texto": "3. Primeira Lei da Termodinâmica"},

        {"tipo": "texto", "texto": (
            "A Primeira Lei da Termodinâmica é o princípio fundamental da conservação da energia: "
            "a energia não pode ser criada nem destruída, apenas transformada de uma forma para outra. "
            "Para um sistema termodinâmico, essa lei estabelece uma relação quantitativa entre as "
            "interações de energia que atravessam sua fronteira e a variação de sua energia interna.\n\n"
            
            "Para um sistema fechado (sem troca de massa), a Primeira Lei é expressa por:"
        )},

        {"tipo": "equacao",
        "latex": r"\Delta U = Q - W"
        },

        {"tipo": "texto", "texto": (
            "onde cada termo representa:\n\n"
            "• **ΔU (variação da energia interna):** energia armazenada no sistema associada à agitação molecular, "
            "ligaçães químicas e interações entre partículas. Unidade: joule [J].\n\n"
            
            "• **Q (calor):** energia transferida através da fronteira devido exclusivamente a uma diferença de temperatura.\n"
            "   - Q > 0: calor é transferido do ambiente para o sistema (o sistema **recebe** calor).\n"
            "   - Q < 0: calor é transferido do sistema para o ambiente (o sistema **perde** calor).\n"
            "   - Q = 0: processo adiabático (sem troca de calor).\n\n"
            
            "• **W (trabalho):** energia transferida através da fronteira por meios mecânicos, elétricos, de expansão, etc.\n"
            "   - W > 0: o sistema realiza trabalho sobre o ambiente (expansão, eixo, etc.).\n"
            "   - W < 0: o ambiente realiza trabalho sobre o sistema (compressão, ventilador, etc.).\n"
            "   - W = 0: sem transferência de trabalho (volume constante, sem partes móveis).\n\n"
            
            "**Interpretação física combinada:**\n\n"
            "A variação da energia interna é dada por ΔU = Q - W.\n\n"
            "- **Q > 0 e W = 0:** calor entra → energia interna aumenta (ex: aquecedor na sala).\n"
            "- **Q < 0 e W = 0:** calor sai → energia interna diminui (ex: resfriamento passivo).\n"
            "- **Q = 0 e W > 0:** sistema realiza trabalho → energia interna diminui (ex: gás expandindo).\n"
            "- **Q = 0 e W < 0:** trabalho é realizado sobre o sistema → energia interna aumenta (ex: compressor).\n"
            "- **Q > 0 e W > 0:** calor entra e trabalho sai → efeito líquido depende da magnitude relativa.\n"
            "- **Q > 0 e W < 0:** calor entra e trabalho entra → energia interna aumenta com certeza.\n\n"
            
            "A energia não é criada nem destruída: ela apenas se transforma entre calor, trabalho e energia interna."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0002",
            "pergunta": (
                "Uma sala de aula está sendo aquecida exclusivamente por um aquecedor elétrico (resistência) instalado em sua parede. "
                "O aquecedor transfere 1500 J de energia para o ar da sala a cada segundo (potência de 1500 W). "
                "Durante esse processo, não há realização de trabalho mecânico (W = 0), pois não há partes móveis, ventiladores ou expansão significativa do ar. "
                "Considerando a convenção termodinâmica usual (Q positivo para calor que entra no sistema, W positivo para trabalho realizado pelo sistema), "
                "qual afirmação descreve corretamente o efeito no balanço energético da sala?"
            ),
            "alternativas": {
                "a": "ΔU = +1500 J (a energia interna da sala aumenta, pois o calor está entrando e não há trabalho saindo).",
                "b": "ΔU = -1500 J (a energia interna da sala diminui, pois o calor está saindo do sistema).",
                "c": "ΔU = 0 J (a energia interna permanece constante, pois a sala está em regime permanente).",
                "d": "ΔU = +3000 J (a energia interna dobra, pois o calor entra e o trabalho também é positivo)."
            },
            "alternativa_correta": "a",
        },
# ========================================================
# 4. Balanço de energia em regime permanente
# ========================================================
        {"tipo": "titulo", "texto": "4. Balanço de energia em regime permanente"},


        {"tipo": "texto", "texto": (
            "Em muitas aplicações de engenharia, incluindo a análise térmica de edificações, as condições operacionais "
            "se mantêm estáveis ao longo do tempo. Nesses casos, adota-se a hipótese de **regime permanente** (ou estado estacionário).\n\n<br>"
            
            "**O que significa regime permanente?**\n\n"
            "A energia interna do sistema (U) não varia com o tempo, ou seja, ΔU = 0. Isso ocorre quando as temperaturas, "
            "pressões e demais propriedades termodinâmicas se mantêm constantes ao longo do tempo, mesmo que haja fluxos "
            "de energia através das fronteiras.\n\n"
            
            "**Consequência para a Primeira Lei:**\n\n"
            "Partindo da equação geral ΔU = Q - W e impondo ΔU = 0, obtém-se Q = W. No entanto, para a maioria dos sistemas "
            "térmicos de edificações (salas, câmaras, fornos), não há realização de trabalho mecânico (W = 0). "
            "Nesse caso, a Primeira Lei se reduz a:"
        )},

        {"tipo": "equacao",
        "latex": r"\sum \dot{Q}_{entrada} = \sum \dot{Q}_{saida}",
        },

        {"tipo": "texto", "texto": (
            "onde o símbolo \dot{Q} (Q ponto) representa **taxa de transferência de calor** (potência térmica), "
            "geralmente medida em watts (W) ou joules por segundo (J/s).\n\n<br>"
            
            "**Interpretação física:**\n\n"
            "Toda a energia que entra no sistema (por radiação solar, aquecedores, pessoas, equipamentos) deve ser "
            "integralmente igual à energia que sai (por perdas pelas paredes, janelas, ventilação, etc.). "
            "Não há acúmulo ou redução de energia no interior do sistema.\n\n"
            
            "**Por que essa simplificação é útil?**\n"
            "1. Elimina a variável tempo da análise, reduzindo a complexidade matemática.\n"
            "2. Permite dimensionar sistemas de climatização com base em condições médias.\n"
            "3. Facilita a identificação de termos dominantes no balanço energético.\n"
            "4. É uma aproximação válida para a maioria das situações reais de operação contínua (escritórios, salas de aula, residências).\n\n"
            
            "**Limitação:** O regime permanente não descreve transitórios, como o aquecimento inicial da sala pela manhã "
            "ou o resfriamento noturno. Para essas situações, é necessário resolver a equação diferencial completa com ΔU ≠ 0."
        )},
        {"tipo": "simulador_balanco"},

        { "tipo": "questao_texto", "id": "problema.01.003.0003",
            "pergunta": (
                "Com base no simulador, identifique quais são as principais entradas e saídas de energia "
                "da sala e indique qual delas parece ter maior influência no balanço térmico."
            ),
            "placeholder": "Descreva em 2-3 linhas..."
        },

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0202",
            "pergunta": "Qual termo você identificou como dominante?",
            "alternativas": {
                "a": "Ganho solar",
                "b": "Carga interna",
                "c": "Perdas por condução",
                "d": "Ventilação"
            },
            "alternativa_correta": "a",
        },

# ========================================================
# 5. Hipóteses e simplificações
# ========================================================
        {"tipo": "titulo", "texto": "5. Construção do modelo simplificado"},

        {"tipo": "texto", "texto": (
            "\n\nNenhum modelo físico inclui todos os fenômenos possíveis. A realidade é complexa demais para ser descrita "
            "em sua totalidade. Por isso, o engenheiro deve estabelecer **hipóteses simplificadoras** que tornam o problema "
            "tratável matematicamente sem perder a essência física do fenômeno.\n\n"
            
            "No caso da sala, algumas simplificações comuns são:\n\n"
            "- **Regime permanente:** assume-se que as temperaturas não variam no tempo, eliminando a variável temporal.\n"
            "- **Propriedades constantes:** k (condutividade), h (convecção) e cp (calor específico) não variam com a temperatura.\n"
            "- **Desprezo de termos pouco relevantes:** por exemplo, ignorar a condução pelo piso se ele for isolado.\n"
            "- **Geometria simplificada:** tratar paredes como planas e uniformes, ignorando cantos e descontinuidades.\n"
            "- **Distribuição uniforme de temperatura:** mesmo sabendo que há gradientes, assume-se T constante no ar.\n\n"
            
            "**Critério para uma boa simplificação:**\n"
            "A simplificação é válida se o erro introduzido for pequeno comparado aos termos dominantes. "
            "Por exemplo, desprezar a condução pelo piso é aceitável se a perda for <5% do total.\n\n"
            
            "A validade do modelo depende diretamente dessas escolhas. Um modelo super simplificado pode ser "
            "matematicamente simples, mas fisicamente irrelevante. Um modelo complexo demais pode ser inviável de resolver."
        )},


        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0005",
            "pergunta": (
                "Em uma análise térmica de uma sala, um engenheiro decide desprezar a transferência de calor por radiação "
                "entre as paredes internas e os ocupantes, assumindo que apenas a convecção é relevante. "
                "Medições posteriores mostram que a radiação responde por 30% da troca térmica total. "
                "Qual afirmação sobre essa simplificação é correta?"
            ),
            "alternativas": {
                "a": "A simplificação é válida porque qualquer simplificação é aceitável na engenharia.",
                "b": "A simplificação é inválida porque o erro introduzido (30%) é significativo e altera o resultado.",
                "c": "A simplificação é válida porque 30% é um erro pequeno e pode ser desprezado.",
                "d": "A simplificação não afeta o modelo, pois radiação e convecção são fenômenos idênticos."
            },
            "alternativa_correta": "b",
        },

        {"tipo": "questao_multipla_escolha", "id": "problema.01.003.0006",
            "pergunta": (
                "Com base nos ΔT que você calculou para as paredes da sala, se você decidisse desprezar a convecção "
                "em todas as paredes com |ΔT| < 2°C, isso seria uma simplificação adequada? Por quê?"
            ),
            "alternativas": {
                "a": "Sim, porque paredes com ΔT pequeno têm pouca influência no balanço total.",
                "b": "Não, porque todas as paredes devem ser consideradas, independentemente do ΔT.",
                "c": "Sim, porque a convecção nunca é relevante em salas pequenas.",
                "d": "Não, porque o regime permanente exige que todos os termos sejam incluídos."
            },
            "alternativa_correta": "a",
        },








# ========================================================
# 7. Mini-entrega: balanço de energia da sala
# ========================================================
        {"tipo": "titulo", "texto": "6. Mini-entrega: balanço de energia da sala"},

        {"tipo": "texto", "texto": (
            "Nesta etapa, você deve construir um **modelo energético simplificado** do ambiente, aplicando a Primeira Lei "
            "da Termodinâmica ao sistema estudado.\n\n"
            
            "**Instruções para a mini-entrega:**\n\n"
            
            "1. **Definição do sistema:** delimite claramente o volume de controle da sala, indicando suas fronteiras "
            "(paredes, piso, teto, janelas, portas).\n\n"
            
            "2. **Identificação dos fluxos:** liste todas as entradas e saídas de energia que atravessam a fronteira:\n"
            "   - **Entradas:** radiação solar (janelas), ganhos internos (ocupantes, equipamentos, iluminação), "
            "calor de aquecedores (se houver), calor por condução através de paredes externas (se T_ext > T_int).\n"
            "   - **Saídas:** perdas por condução através de paredes (se T_int > T_ext), perdas por ventilação/infiltração "
            "(ar quente saindo), radiação para o céu (janelas).\n\n"
            
            "3. **Equação de balanço energético:** escreva a equação completa da Primeira Lei para o volume de controle, "
            "identificando cada termo com sua unidade.\n\n"
            
            "4. **Hipóteses adotadas:** explicite todas as simplificações utilizadas (ex.: regime permanente, propriedades "
            "constantes, desprezo de termos).\n\n"
            
            "5. **Justificativa dos termos desprezados:** para cada termo ignorado, explique por que ele é pouco relevante "
            "(ex.: \"a condução pelo piso foi desprezada porque o piso está sobre laje isolada termicamente\").\n\n"
            
            "**Critérios de avaliação:**\n\n"
            "| Critério | Peso | Descrição |\n"
            "|----------|------|-----------|\n"
            "| Definição correta do sistema e fronteira | 25% | Volume de controle bem delimitado |\n"
            "| Identificação completa das entradas e saídas | 25% | Todos os fluxos relevantes listados |\n"
            "| Equação de balanço correta | 25% | Primeira Lei aplicada corretamente |\n"
            "| Hipóteses e justificativas adequadas | 25% | Simplificações coerentes e bem fundamentadas |\n\n"
            
            "O objetivo não é obter um valor exato, mas **estruturar corretamente o problema físico**. "
            "Um bom balanço energético identifica os termos dominantes e permite dimensionar sistemas de climatização "
            "ou orientar intervenções de eficiência energética."
        )},

# ========================================================
# 7. Fechamento: da temperatura ao balanço de energia
# ========================================================
        {"tipo": "titulo", "texto": "7. Fechamento: da temperatura ao balanço de energia"},

        {"tipo": "texto", "texto": (
            "Neste bloco, consolidamos os conceitos dos dois blocos anteriores, integrando a descrição do estado térmico "
            "(temperatura como campo) e dos mecanismos de transferência de calor em uma estrutura quantitativa: o balanço de energia.\n\n"
            
            "**Principais conclusões:**\n\n"
            "- A **Primeira Lei da Termodinâmica** (conservação da energia) é o fundamento de qualquer análise energética.\n"
            "- A escolha adequada do **sistema e da fronteira** determina quais fluxos devem ser contabilizados.\n"
            "- Em **regime permanente**, a energia que entra é igual à energia que sai: ∑Q_entrada = ∑Q_saída.\n"
            "- **Hipóteses simplificadoras** são necessárias, mas devem ser justificadas com base física.\n"
            "- O balanço energético conecta os fluxos do mapa de calor (bloco anterior) à dinâmica do sistema.\n\n"
            
            "Com esse arcabouço, a sala deixa de ser apenas um conjunto de temperaturas medidas e passa a ser um sistema "
            "termodinâmico modelado matematicamente. A próxima etapa aplicará esse modelo para dimensionamento de sistemas "
            "de climatização e análise de eficiência energética."
        )},

# ========================================================
# 9. Competências desenvolvidas
# ========================================================
        {"tipo": "subtitulo", "texto": "Competências desenvolvidas"},

        {"tipo": "texto", "texto": (
            "Ao final deste bloco, o aluno deve ser capaz de:\n\n"
            "- Aplicar a Primeira Lei da Termodinâmica a um ambiente construído;\n"
            "- Definir adequadamente sistema, fronteira e volume de controle;\n"
            "- Construir um balanço de energia completo, identificando entradas e saídas;\n"
            "- Justificar simplificações com base física e critério de erro;\n"
            "- Interpretar o ambiente como um sistema de engenharia sujeito à conservação da energia;\n"
            "- Preparar a base para modelagem energética e dimensionamento de sistemas de climatização."
        )},

    ]
