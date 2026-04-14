import streamlit as st

def get_blocos() -> list[dict]:
    return [

# ========================================================
# 1. Limitação da Primeira Lei: a direção dos processos
# ========================================================
        {"tipo": "titulo", "texto": "1. Insuficiência da Primeira Lei: a Irreversibilidade e a Direcionalidade dos Processos"},

        {"tipo": "texto", "texto": (
            "Embora a Primeira Lei da Termodinâmica fundamente o princípio da conservação da energia, permitindo o balanço rigoroso das "
            "interações sob forma de calor e trabalho, ela se mostra insuficiente para descrever a natureza fenomenológica da realidade. "
            "Sob a visão do primeiro princípio, qualquer processo que satisfaça o balanço energético"
        )}, 

        {"tipo": "equacao", "latex": r"\Delta E = Q - W ",},
          
        {"tipo": "texto", "texto": (
            "é considerado admissível.  Contudo, a Primeira Lei não impõe restrições quanto à evolução temporal ou ao sentido de ocorrência dos fenômenos.\n\n <br>"
            
            "Considere o gradiente térmico entre o ar ambiente (24 °C) e uma superfície resfriada (18 °C). Para a conservação da energia, "
            "a transferência de calor no sentido oposto, do corpo mais frio para o mais quente, seria perfeitamente válida, desde que "
            "não houvesse criação ou destruição de energia. Todavia, a evidência empírica demonstra que processos naturais possuem uma "
            "direcionalidade preferencial e são intrinsecamente irreversíveis.\n\n"
            
            "Essa assimetria fundamental entre os estados inicial e final revela que a conservação, isoladamente, não define a viabilidade "
            "de um processo. Torna-se necessária, portanto, a introdução da Segunda Lei da Termodinâmica, que estabelece o critério de "
            "espontaneidade e introduz a degradação da qualidade da energia através do conceito de entropia."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0001",
            "pergunta": (
                "Considere o gradiente térmico na sala: ar a 24 °C e parede Sul a 18 °C. A Primeira Lei da Termodinâmica "
                "permite o balanço energético ΔE = Q - W. Por que essa lei é insuficiente para descrever a "
                "evolução do sistema e a sensação de desconforto térmico?"
            ),
            "alternativas": {
                "a": "Porque a Primeira Lei não considera a temperatura dos corpos, apenas a quantidade de calor trocada, sendo válida apenas para gases ideais.",
                "b": "Porque a Primeira Lei não impõe restrições sobre o sentido do fluxo de calor, admitindo como possível a transferência da parede fria para o ar quente, desde que a energia se conserve.",
                "c": "Porque a Primeira Lei é uma consequência da Segunda Lei e, portanto, não pode ser usada de forma independente em sistemas isolados.",
                "d": "Porque a Primeira Lei só é aplicável a processos reversíveis, enquanto o fluxo de calor na sala é claramente irreversível."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# 2. Enunciados de Clausius e Kelvin-Planck
# ========================================================
        {"tipo": "titulo", "texto": "2. Segunda Lei: Enunciados de Clausius e Kelvin-Planck"},

        {"tipo": "subtitulo", "texto": "Enunciado de Clausius: Direcionalidade do Fluxo Térmico"},

        {"tipo": "texto", "texto": (
            "O postulado de Clausius estabelece a impossibilidade de um processo cujo único efeito seja a transferência "
            "de calor de um reservatório térmico de menor temperatura para um de maior temperatura, sem que haja a "
            "interação de trabalho externo sobre o sistema. "
            
            "Análise termodinâmica aplicada ao ambiente:\n\n"
            "- Processo Espontâneo: Ocorre o fluxo de calor da superfície aquecida (35 °C) para o ar ambiente (24 °C), "
            "impulsionado pelo gradiente de temperatura natural.\n"
            "- Processo Não-Espontâneo: A transferência térmica inversa (do ar a 24 °C para a parede a 35 °C) é fisicamente "
            "irrealizável de forma isolada, pois violaria a restrição de Clausius.\n\n"
            
            "Para extrair energia térmica de uma região resfriada e rejeitá-la em um ambiente de temperatura superior, "
            "é mandatória a execução de um ciclo de refrigeração, o qual consome trabalho exergético (fornecido, por exemplo, "
            "pelo compressor de um sistema de climatização)."
        )},

        {"tipo": "subtitulo", "texto": "Enunciado de Kelvin-Planck: Limitações na Conversão de Calor em Trabalho"},

        {"tipo": "texto", "texto": (
            "O enunciado de Kelvin-Planck impõe que é impossível operar um dispositivo que atue em um ciclo termodinâmico "
            "e produza trabalho líquido enquanto troca calor com apenas um reservatório térmico. Em termos de engenharia, "
            "isso implica que nenhuma máquina térmica pode atingir uma eficiência térmica de 100%. "
            
            "Sempre haverá a necessidade de rejeição de calor (Q_f) para um reservatório de menor temperatura, "
            "caracterizando a degradação da energia. O limite superior de eficiência para qualquer máquina operando "
            "entre dois reservatórios térmicos é definido pelo Ciclo de Carnot:"
        )},

        {"tipo": "equacao",
         "latex": r"\eta_{ter, max} = 1 - \frac{T_{frio}}{T_{quente}}",
        },

        {"tipo": "texto", "texto": (
            "onde as temperaturas devem ser expressas em escalas absolutas (Kelvin). "
            "Ao analisarmos o potencial de conversão do calor que flui do ar (24 °C) para uma parede fria (23,5 °C), "
            "observamos que o reduzido gradiente térmico impõe uma severa restrição à eficiência máxima teórica:"
        )},

        {"tipo": "equacao", "latex": r"\eta_{Carnot} = 1 - \frac{23,5}{24} \approx 0,02 \ (2\%)",},

        {"tipo": "texto", "texto": (
            "Este resultado demonstra que, mesmo sob condições de reversibilidade ideal (sem perdas por atrito ou "
            "outras irreversibilidades internas), apenas 2% da energia térmica transferida poderia ser convertida em "
            "trabalho útil. A fração remanescente (98%) representa anergia, sendo obrigatoriamente rejeitada para o "
            "meio exterior conforme exigido pela Segunda Lei."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0002",
            "pergunta": (
                "Conforme o enunciado de Kelvin-Planck e o texto, uma máquina térmica operando entre o ar da sala (24 °C) "
                "e a parede Sul (18 °C) teria uma eficiência máxima teórica (Carnot) de aproximadamente 2%. "
                "Se essa máquina recebesse 10.000 kJ do ar quente, qual seria o trabalho líquido máximo realizado e a "
                "quantidade de calor rejeitada para a parede fria, respectivamente?"
            ),
            "alternativas": {
                "a": "10.000 kJ e 0 kJ, pois a energia se conserva pela Primeira Lei.",
                "b": "9.800 kJ e 200 kJ, confirmando a degradação da energia.",
                "c": "200 kJ e 9.800 kJ, sendo a rejeição de calor para a fonte fria obrigatória pela Segunda Lei.",
                "d": "200 kJ e 10.000 kJ, violando a Primeira Lei."
            },
            "alternativa_correta": "c",
        },

        {"tipo": "subtitulo", "texto": "Equivalência Lógica dos Enunciados"},   

        {"tipo": "texto", "texto": (
            "Embora as abordagens de Clausius e Kelvin-Planck foquem em fenômenos distintos (transferência de calor e conversão "
            "em trabalho, respectivamente) elas constituem formulações logicamente equivalentes da Segunda Lei. A demonstração "
            "clássica dessa equivalência revela que a violação de um enunciado implica, necessariamente, na negação do outro. "
            "Ambos os postulados convergem para a mesma realidade física: a existência de uma irreversibilidade intrínseca "
            "na natureza, que impõe uma assimetria temporal aos processos térmicos e estabelece um limite fundamental à "
            "transformação de calor em trabalho útil."
        )},

# ========================================================
# 3. Entropia: a métrica da irreversibilidade e a degradação da energia
# ========================================================
        {"tipo": "titulo", "texto": "3. Entropia: a Formalização da Irreversibilidade"},

        {"tipo": "texto", "texto": (
            "A entropia ($S$) é uma propriedade termodinâmica de estado introduzida pela Segunda Lei para quantificar as "
            "irreversibilidades e a direção de evolução de um sistema. Ao contrário da energia, que é uma grandeza conservada, "
            "a entropia é uma grandeza passível de criação. Em sistemas reais, a entropia é gerada continuamente devido a "
            "fenômenos dissipativos, como atrito, expansão livre e transferência de calor através de gradientes finitos de temperatura. "
            "Para uma fronteira onde ocorre uma transferência de calor reversível (ΔQ_rev), a variação infinitesimal "
            "de entropia é definida pela relação de Clausius:"
        )},

        {"tipo": "equacao",
         "latex": r"dS = \left( \frac{\delta Q}{T} \right)_{rev}",
        },

        {"tipo": "texto", "texto": (
            "A presença da temperatura absoluta (T) no denominador carrega uma implicação teórica profunda: para uma magnitude fixada "
            "de calor ΔQ, a variação de entropia é inversamente proporcional ao nível térmico em que a troca ocorre. "
            "Consequentemente, o calor rejeitado a temperaturas mais baixas representa uma maior dispersão energética e uma "
            "maior perda de potencial de realização de trabalho. "
            "O Princípio do Aumento da Entropia estabelece que, para qualquer processo real que ocorra em um sistema isolado (ou no conjunto sistema + vizinhança), "
            "a variação da entropia total deve ser positiva:"
        )},

        {"tipo": "equacao", "latex": r"S_{ger} \geq 0", },
        {"tipo": "equacao", "latex": r"\Delta S_{total} \geq 0", },
        {"tipo": "equacao", "latex": r"\Delta S_{sistema} + \Delta S_{vizinhanca} \geq 0", },

        {"tipo": "texto", "texto": (
            "Nesta formulação, a igualdade aplica-se estritamente a processos reversíveis (ideais). Para todos os processos "
            "espontâneos e tecnicamente realizáveis, a desigualdade estrita (S_ger > 0) prevalece, servindo como a "
            "métrica quantitativa da ineficiência e da degradação da qualidade da energia no universo."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0003",
            "pergunta": (
                "O texto define a variação de entropia como dS = (δQ/T)_rev. Na situação real da sala, o calor flui "
                "do ar (24 °C = 297 K) para a parede Sul (18 °C = 291 K) através de um diferencial finito de temperatura. "
                "Com base no Princípio do Aumento da Entropia, o que se pode afirmar sobre S_ger = ΔS_total?"
            ),
            "alternativas": {
                "a": "ΔS_total = 0, pois o processo é espontâneo e, portanto, termodinamicamente reversível.",
                "b": "ΔS_total < 0, pois a energia está sendo degradada de uma forma de alta qualidade (ar quente) para uma de baixa qualidade (parede fria).",
                "c": "ΔS_total > 0, pois a transferência de calor através de uma diferença finita de temperatura é um processo intrinsecamente irreversível, gerando entropia.",
                "d": "ΔS_total não pode ser determinada, pois a equação dS = δQ/T só é válida para processos reversíveis."
            },
            "alternativa_correta": "c",
        },

# ========================================================
# 4. Geração de entropia em processos na sala
# ========================================================
 {"tipo": "titulo", "texto": "4. Mecanismos de Geração de Entropia no Ambiente"},

        {"tipo": "texto", "texto": (
            "\n\nNo ambiente real da sala de aula, a geração de entropia ($S_{ger} > 0$) é a evidência direta da "
            "presença de irreversibilidades. Diversos fenômenos dissipativos ocorrem simultaneamente, cada um "
            "contribuindo para a degradação da exergia (potencial de trabalho) do sistema:\n\n"
            
            "1. **Transferência de Calor através de Diferenciais Finitos de Temperatura**: É a principal fonte de "
            "irreversibilidade no ambiente. A taxa de geração de entropia é proporcional ao fluxo térmico e ao "
            "gradiente de temperatura ($1/T_f - 1/T_q$). Portanto, quanto maior o salto térmico entre o ar e as "
            "paredes, maior a destruição de potencial exergético.\n\n"
            
            "2. **Mistura Irreversível de Fluxos**: Ocorre durante a ventilação ou infiltrações, onde massas de ar com "
            "diferentes entalpias e temperaturas se misturam. Do ponto de vista molecular e macroscópico, este processo "
            "de equilíbrio é intrinsecamente irreversível e eleva a entropia total da mistura.\n\n"
            
            "3. **Dissipação Viscosa e Atrito**: O movimento do ar, seja por convecção natural ou forçada (ventiladores/climatizadores), "
            "envolve tensões cisalhantes e atrito fluido. A energia cinética e o trabalho mecânico fornecido às pás dos ventiladores "
            "acabam sendo dissipados como calor de baixa qualidade, elevando a entropia do fluido.\n\n"
            
            "4. **Interações Radiativas entre Superfícies**: A troca líquida de radiação entre o corpo humano, mobiliário "
            "e superfícies (como paredes e janelas) a diferentes temperaturas configura um processo de transferência "
            "térmica irreversível, contribuindo para o balanço global de entropia do sistema."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0004",
            "pergunta": (
                "O texto lista diversos mecanismos de geração de entropia no ambiente da sala. Qual dos seguintes processos, "
                "se ocorresse na sala, NÃO contribuiria para a geração de entropia (S_ger = 0) e, portanto, seria um processo ideal?"
            ),
            "alternativas": {
                "a": "Transferência de calor do ar (24 °C) para a parede fria (18 °C) por convecção natural.",
                "b": "Mistura de ar quente e frio proveniente de um sistema de ventilação.",
                "c": "Troca de calor por radiação entre a parede Sul (18 °C) e o corpo do ocupante (≈ 37 °C).",
                "d": "Transferência de calor por condução através de uma parede com gradiente de temperatura nulo (equilíbrio térmico perfeito) ou um processo hipotético perfeitamente reversível."
            },
            "alternativa_correta": "d",
        },

# ========================================================
# 5. Qualidade da energia e exergia
# ========================================================
        {"tipo": "titulo", "texto": "5. Qualidade da Energia e o Conceito de Exergia"},

        {"tipo": "texto", "texto": (
            "A Segunda Lei da Termodinâmica estabelece que a energia possui não apenas uma magnitude, mas também uma "
            "hierarquia de qualidade. Nem toda forma de energia possui a mesma competência para a realização de trabalho útil.\n\n"
            
            "- **Energia de Alta Qualidade**: Trabalho mecânico e energia elétrica podem, teoricamente, ser convertidos integralmente "
            "em outras formas de energia (baixa entropia).\n"
            "- **Energia de Qualidade Intermediária**: Calor proveniente de fontes a altas temperaturas (combustão, vapor superaquecido).\n"
            "- **Energia de Baixa Qualidade**: Calor rejeitado a temperaturas próximas ao estado morto (temperatura ambiente).\n\n"
            
            "A propriedade que quantifica o potencial de trabalho máximo extraível de uma substância ou fluxo de energia, até que "
            "esta atinja o equilíbrio com o meio, é denominada **Exergia** (ou Disponibilidade). Para uma quantidade de calor $Q$ "
            "disponível a uma temperatura $T$, em um ambiente de referência $T_0$, a exergia é expressa pela relação de disponibilidade de Carnot:"
        )},

        {"tipo": "equacao",
        "latex": r"X_Q = Q \left(1 - \frac{T_0}{T}\right)",
        },

        {"tipo": "texto", "texto": (
            "\n À medida que a temperatura da fonte ($T$) se aproxima da temperatura de referência do reservatório térmico ($T_0$), o conteúdo "
            "exergético decai. No limite em que $T = T_0$, a exergia é nula: a energia térmica torna-se anergia, não possuindo "
            "mais potencial para gerar trabalho.\n\n<br>"
            
            "No contexto do diagnóstico térmico da sala, o calor transferido entre o ar (24 °C) e as superfícies resfriadas (23,5 °C) "
            "opera em diferenciais térmicos muito baixos em relação ao meio externo. A exergia associada a esses fluxos é "
            "desprezível, o que fundamenta a inviabilidade técnica e econômica de sistemas de recuperação energética para "
            "esses gradientes, consolidando o entendimento de que nem toda energia recuperada é energia aproveitável."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0005",
            "pergunta": (
                "\n A exergia ($X_Q$) do calor Q transferido entre o ar e a parede é definida como $X_Q = Q (1 - T0/T)$. "
                "Considere que o ambiente externo (T0) é de 300 K. Se compararmos 1000 J de calor disponíveis a 500 K (vapor) "
                "com 1000 J de calor disponíveis a 350 K (água morna), o que se pode afirmar sobre a qualidade da energia?"
            ),
            "alternativas": {
                "a": "Ambos têm a mesma exergia, pois a quantidade de calor (1000 J) é idêntica, de acordo com a Primeira Lei.",
                "b": "O calor a 500 K tem maior exergia, pois a razão (1 - T0/T) é maior, indicando maior potencial de conversão em trabalho.",
                "c": "O calor a 350 K tem maior exergia, pois sua temperatura está mais próxima de T0, tornando a conversão mais fácil.",
                "d": "Nenhum dos dois possui exergia, pois a Segunda Lei proíbe a conversão integral de calor em trabalho."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# 6. Aplicação à sala de aula: por que o desconforto térmico é irreversível?
# ========================================================
        {"tipo": "titulo", "texto": "6. Síntese: Irreversibilidade e as Implicações no Conforto Térmico"},

        {"tipo": "texto", "texto": (
            "O desconforto térmico observado nos ocupantes adjacentes à face Sul do edifício transcende a análise puramente "
            "escalar da temperatura; ele é o resultado direto da irreversibilidade dos processos de transferência de calor "
            "e da elevada taxa de geração de entropia na interface corpo-ambiente.\n\n<br>"
            
            "Sob a visão da Segunda Lei, o corpo humano atua como um sistema termodinâmico fora do equilíbrio, operando em regime "
            "estacionário, que deve dissipar calor continuamente (metabolismo) para manter sua homeostase térmica (≈ 37 °C). "
            "Quando a temperatura de uma superfície (parede fria a 18 °C) é significativamente inferior à temperatura do ar (24 °C), "
            "estabelece-se um gradiente térmico acentuado que potencializa a transferência de calor por radiação e convecção.\n\n"
            
            "Esta exaustão térmica do corpo para a parede é um processo intrinsecamente irreversível. A magnitude do fluxo radiante "
            "é tal que a taxa de perda energética excede a capacidade de regulação metabólica do indivíduo, resultando na percepção "
            "de desconforto. Note que essa energia dissipada representa uma destruição de exergia: uma vez transferido para a parede "
            "fria, esse calor se degrada em anergia no ambiente, sendo impossível o seu retorno ao corpo sem a aplicação de um ciclo "
            "térmico externo e consumo de trabalho.\n\n"
            
            "Portanto, a Segunda Lei fornece a fundamentação física para compreender que o conforto térmico não depende apenas "
            "da 'quantidade' de energia no ar, mas das condições de contorno e da eficiência das trocas exergéticas entre o ocupante "
            "e as superfícies ao seu redor."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.004.0006",
            "pergunta": (
                "Um ocupante próximo à parede Sul (18 °C) relata desconforto por frio, enquanto outro no centro da sala (ar a 24 °C) "
                "está confortável. Com base na Segunda Lei e no conceito de irreversibilidade, qual explicação é mais adequada?"
            ),
            "alternativas": {
                "a": "A temperatura do ar no centro é maior, o que viola a Segunda Lei, pois o calor deveria fluir para a parede.",
                "b": "A perda de calor do corpo (≈ 37 °C) para a parede fria (18 °C) é um processo irreversível que ocorre a uma alta taxa, devido ao grande gradiente, e essa destruição de exergia não pode ser totalmente compensada pelo metabolismo.",
                "c": "O calor flui do corpo para a parede, mas esse processo é reversível, e o desconforto se deve apenas a um fator psicológico.",
                "d": "A entropia do corpo diminui devido à perda de calor, o que é um processo espontâneo e não causa desconforto."
            },
            "alternativa_correta": "b",
        },

# ========================================================
# 7. Mini-entrega — Análise termodinâmica da sala
# ========================================================
        {"tipo": "titulo", "texto": "7. Mini-entrega: Análise termodinâmica da sala"},

        {"tipo": "texto", "texto": (
            "Com base nos conceitos apresentados, elabore um relatório técnico respondendo às seguintes questões:\n\n"
            "1. Por que a Primeira Lei é insuficiente para descrever completamente o comportamento térmico da sala?\n\n"
            "2. Aplique o enunciado de Clausius ao fluxo de calor entre o ar e a parede Sul. Qual é a direção natural e por quê?\n\n"
            "3. Calcule o rendimento máximo teórico (Carnot) de uma máquina térmica que operasse entre o ar (24 °C) e a parede Sul (18 °C). Interprete o resultado.\n\n"
            "4. Identifique três processos irreversíveis que ocorrem na sala e explique como cada um contribui para a geração de entropia.\n\n"
            "5. Discuta o conceito de qualidade da energia aplicado ao calor que sai pela parede Sul.\n\n"
            "O relatório deve conter argumentação técnica baseada nas equações e conceitos apresentados, não apenas descrição qualitativa."
        )},

    {"tipo": "subtitulo", "texto": "Competências desenvolvidas"},
        {"tipo": "texto", "texto": (
            "\n**Ao final deste bloco, o acadêmico deve ser capaz de:**\n\n"
            "- Aplicar os enunciados de Clausius e Kelvin-Planck a um problema real de engenharia térmica.\n"
            "- Calcular o rendimento de Carnot e interpretar seu significado físico.\n"
            "- Identificar e quantificar (qualitativamente) processos irreversíveis em um ambiente construído.\n"
            "- Compreender a relação entre entropia, qualidade da energia e exergia.\n"
            "- Relacionar a Segunda Lei da Termodinâmica com problemas de conforto térmico e eficiência energética.\n\n"
            "Esta etapa consolida os fundamentos termodinâmicos necessários para análises mais avançadas, "
            "como sistemas de climatização e eficiência energética de edificações."
        )},

    ]
