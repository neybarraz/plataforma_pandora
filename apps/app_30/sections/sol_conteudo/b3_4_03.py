def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # FORMULAÇÃO MATEMÁTICA
        # ==================================================
        {"tipo": "titulo", "texto": "A Lei de Faraday: formalismo matemático"},

        {
            "tipo": "texto",
            "texto": (
                "A Lei de Faraday estabelece a relação quantitativa entre a variação do fluxo magnético "
                "e a força eletromotriz induzida. Em sua forma integral, ela é expressa como:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\mathcal{E} = - \frac{d\Phi_B}{dt}"
        },

        {
            "tipo": "texto",
            "texto": (
                "Esta equação afirma que a força eletromotriz induzida em um circuito é igual à taxa de "
                "variação temporal do fluxo magnético que atravessa a superfície do circuito, com sinal negativo.\n\n <br>"

                "Significado dos termos:\n\n"
                "\n- $\\mathcal{E}$: força eletromotriz induzida [V], volt.\n\n"
                "- $\\Phi_B$: fluxo magnético através da superfície [Wb], weber.\n"
                "- $\\frac{d\\Phi_B}{dt}$: taxa de variação temporal do fluxo magnético.\n"
                "- $-$: sinal negativo, indicando oposição à variação (Lei de Lenz)."
            ),
        },

        # ==================================================
        # DEFINIÇÃO DE FLUXO MAGNÉTICO
        # ==================================================
        {"tipo": "titulo", "texto": "O fluxo magnético"},

        {
            "tipo": "equacao",
            "latex": r"\Phi_B = \int \vec{B}\cdot d\vec{A}"
        },

        {
            "tipo": "texto",
            "texto": (
                "O fluxo magnético mede quanto do campo magnético atravessa uma superfície. "
                "Para campo uniforme e superfície plana:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\Phi_B = B A \cos\theta"
        },

        {
            "tipo": "texto",
            "texto": (
                "onde:\n\n"
                "- $B$: módulo do campo magnético [T];\n"
                "- $A$: área da superfície [m²];\n"
                "- $\\theta$: ângulo entre $\\vec{B}$ e a normal à superfície.\n"
                "- $\\theta = 0^\\circ$: o fluxo é máximo (campo perpendicular à superfície)\n "
                "- $\\theta = 90^\\circ$: o fluxo é nulo (campo paralelo à superfície)."
            ),
        },

        # ==================================================
        # FORÇA ELETROMOTRIZ
        # ==================================================
        {"tipo": "titulo", "texto": "Força eletromotriz induzida"},

        {
            "tipo": "texto",
            "texto": (
                "A força eletromotriz induzida não é uma força no sentido mecânico, mas sim uma diferença de potencial "
                "que surge no circuito. Ela pode ser entendida como o trabalho realizado por unidade de carga "
                "para mover cargas elétricas ao longo do circuito. "
                "Para uma bobina com \\(N\\) espiras, a lei assume a forma:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\mathcal{E} = - N \frac{d\Phi_B}{dt}"
        },

        {
            "tipo": "texto",
            "texto": (
                "Cada espira contribui igualmente para a força eletromotriz total. "
                "Por isso, aumentar o número de espiras é uma estratégia eficiente para ampliar a indução."
            ),
        },

        # ==================================================
        # LEI DE LENZ (MATEMÁTICA)
        # ==================================================
        {"tipo": "titulo", "texto": "Lei de Lenz: o sentido da corrente"},

        {
            "tipo": "texto",
            "texto": (
                "O sinal negativo na Lei de Faraday é a expressão matemática da Lei de Lenz.\n\n"
                "- $\\left(\\frac{d\\Phi_B}{dt} < 0\\right)$: Se o fluxo magnético aumenta, a força eletromotriz induzida é negativa, "
                "gerando uma corrente cujo campo magnético se opõe a esse aumento.\n\n"
                "- $\\left(\\frac{d\\Phi_B}{dt} < 0\\right)$: Se o fluxo diminui, a força eletromotriz é positiva, gerando uma corrente "
                "que tenta compensar a perda. "
                "Essa oposição garante a conservação da energia no processo de indução."
            ),
        },

        # ==================================================
        # FORMA DIFERENCIAL
        # ==================================================
        {"tipo": "titulo", "texto": "Forma diferencial da Lei de Faraday"},

        {
            "tipo": "texto",
            "texto": (
                "Usando o teorema de Stokes, a Lei de Faraday pode ser expressa em sua forma diferencial:"
            ),
        },

        {"tipo": "equacao",
            "latex": r"\oint_{\mathcal{C}} \vec{E} \cdot d\vec{\ell} = - \frac{d}{dt} \int_S \vec{B} \cdot d\vec{A}"
        },

        {"tipo": "equacao",
            "latex": r"\int_{\mathcal{S}} \left(\vec{\nabla} \times \vec{E}\right)\cdot\hat{n}~dA  = - \frac{d}{dt} \int_S \vec{B} \cdot d\vec{A}"
        },

        {"tipo": "equacao",
            "latex": r"\int_{\mathcal{S}} \left(\vec{\nabla} \times \vec{E} + \frac{\partial \vec{B}}{\partial t} \right)\cdot\hat{n}~dA = 0"
        },

        {"tipo": "equacao",
            "latex": r"\nabla \times \vec{E} = - \frac{\partial \vec{B}}{\partial t}"
        },

        {
            "tipo": "texto",
            "texto": (
                "Esta equação mostra que um campo magnético variável no tempo produz um campo elétrico "
                "cujo rotacional é não-nulo. Diferentemente da eletrostática, onde o campo elétrico é conservativo, "
                "aqui o campo elétrico forma linhas fechadas ao redor da região onde o campo magnético varia."
            ),
        },

        # ==================================================
        # TRÊS FORMAS DE VARIAR O FLUXO
        # ==================================================
        {"tipo": "titulo", "texto": "As três formas de variar o fluxo"},

        {
            "tipo": "texto",
            "texto": (
                "A indução ocorre sempre que o fluxo magnético varia. Matematicamente, isso pode acontecer de três maneiras:\n\n"
                "1. **Variar $B$**: $\\mathcal{E} = - N A \\cos\\theta \\frac{dB}{dt}$\n"
                "2. **Variar $A$**: $\\mathcal{E} = - N B \\cos\\theta \\frac{dA}{dt}$\n"
                "3. **Variar $\\theta$**: $\\mathcal{E} = - N B A (-\\sin\\theta) \\frac{d\\theta}{dt} = N B A \\sin\\theta \\frac{d\\theta}{dt}$\n\n"
                "A terceira forma é a base dos geradores elétricos: ao girar uma bobina em um campo magnético, "
                "o ângulo varia continuamente, gerando uma força eletromotriz alternada."
            ),
        },

        # ==================================================
        # FORÇA ELETROMOTRIZ ALTERNADA
        # ==================================================
        {"tipo": "titulo", "texto": "Gerando corrente alternada"},

        {
            "tipo": "texto",
            "texto": (
                "Quando uma bobina gira com velocidade angular constante \\(\\omega\\) em um campo magnético uniforme, "
                "o ângulo varia como \\(\\theta = \\omega t\\). A força eletromotriz induzida torna-se:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\mathcal{E} = - N B A \frac{d}{dt}(\cos\omega t) = N B A \omega \sin\omega t"
        },

        {
            "tipo": "texto",
            "texto": (
                "O resultado é uma força eletromotriz alternada (AC), que varia senoidalmente no tempo. "
                "Esse é o princípio de funcionamento dos geradores elétricos em usinas de energia."
            ),
        },
        { "tipo": "video", "url": "https://www.youtube.com/watch?v=hpwIofLcams"},
        # ==================================================
        # APLICAÇÃO 1: ESPIRA RETANGULAR GIRANDO
        # ==================================================
        {"tipo": "titulo", "texto": "Aplicação 1: espira girando em campo uniforme"},

        {
            "tipo": "texto",
            "texto": (
                "Considere uma espira retangular de área A girando com frequência f em um campo magnético uniforme B. "
                "A força eletromotriz máxima é dada por:\n\n"
                "$$\\mathcal{E}_{\\text{máx}} = N B A \\omega$$\n\n"
                "onde $\\omega$ é a velocidade angular ($\\omega = 2\\pi f$).\n\n"
                "Quanto maior a área da espira, o campo magnético, o número de espiras ou a velocidade de rotação, "
                "maior será a tensão gerada."
            ),
        },

        # ==================================================
        # APLICAÇÃO 2: BARRA DESLIZANDO EM TRILHOS
        # ==================================================
        {"tipo": "titulo", "texto": "Aplicação 2: barra condutora em movimento"},

        {
            "tipo": "texto",
            "texto": (
                "Uma barra condutora de comprimento L desliza com velocidade v sobre trilhos paralelos "
                "em uma região com campo magnético uniforme B perpendicular ao plano. "
                "A força eletromotriz induzida é dada por:\n\n"
                "$$\\mathcal{E} = B L v$$\n\n"
                "Este é um exemplo de variação da área: conforme a barra se move, a área do circuito aumenta, "
                "variando o fluxo magnético."
            ),
        },

        # ==================================================
        # APLICAÇÃO 3: SOLENOIDE COM NÚCLEO
        # ==================================================
        {"tipo": "titulo", "texto": "Aplicação 3: solenoide com núcleo de ferro"},

        {
            "tipo": "texto",
            "texto": (
                "A presença de um núcleo ferromagnético (como ferro) dentro de uma bobina amplifica o campo magnético.\n\n"
                "Nesse caso, o fluxo magnético é dado por:\n\n"
                "$$\\Phi_B = \\mu_r \\mu_0 n I A$$\n\n"
                "onde $\\mu_r$ é a permeabilidade relativa do material (para o ferro, pode chegar a 5000).\n\n"
                "Isso explica por que transformadores e carregadores sem fio usam núcleos de ferrite: "
                "eles concentram o campo magnético e aumentam a eficiência da indução."
            ),
        },

        # ==================================================
        # LIMITAÇÕES
        # ==================================================
        {"tipo": "titulo", "texto": "Limitações da forma integral"},

        {
            "tipo": "texto",
            "texto": (
                "\n A Lei de Faraday na forma integral $\\mathcal{E} = - d\\Phi_B/dt$ é válida para qualquer situação, "
                "desde que o fluxo magnético seja bem definido. No entanto, para campos magnéticos que variam rapidamente "
                "ou em materiais com propriedades complexas, a forma diferencial $\\nabla \\times \\vec{E} = -\\partial \\vec{B}/\\partial t$ "
                "é mais adequada, pois descreve o fenômeno ponto a ponto."
            ),
        },

        # ==================================================
        # QUESTÕES CONCEITUAIS
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.003.0001",
            "pergunta": (
                "\n Na equação $\\mathcal{E} = - N d\\Phi_B/dt$, o que representa o sinal negativo?"
            ),
            "alternativas": {
                "a": "Que a corrente induzida é sempre negativa.",
                "b": "Que a força eletromotriz se opõe à variação do fluxo (Lei de Lenz).",
                "c": "Que o fluxo magnético é sempre decrescente.",
                "d": "Que o número de espiras reduz a força eletromotriz.",
                "e": "Que a área da espira deve ser constante."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.003.0002",
            "pergunta": (
                "Em uma espira girando em um campo magnético uniforme, a força eletromotriz máxima depende de:"
            ),
            "alternativas": {
                "a": "Apenas do campo magnético B.",
                "b": "Apenas da área A da espira.",
                "c": "Apenas da velocidade angular ω.",
                "d": "Do produto B × A × ω × N.",
                "e": "Apenas do número de espiras N."
            },
            "alternativa_correta": "d",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.003.0003",
            "pergunta": (
                "Uma barra condutora desliza sobre trilhos em um campo magnético. A força eletromotriz induzida é dada por:"
            ),
            "alternativas": {
                "a": "ℰ = B L / v",
                "b": "ℰ = B L v",
                "c": "ℰ = B / (L v)",
                "d": "ℰ = v / (B L)",
                "e": "ℰ = B v / L"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.04.003.0004",
            "pergunta": (
                "\n Explique o significado físico da forma diferencial da Lei de Faraday: \n\n$\\vec{\\nabla} \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$. "
                "\n\n Como ela se diferencia da eletrostática?"
            ),
            "altura": 160,
        },

    ]