def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # FUNDAMENTAÇÃO CONCEITUAL
        # ==================================================
        {"tipo": "titulo", "texto": "A Lei de Ampère: formalismo matemático"},

        {
            "tipo": "texto",
            "texto": (
                "A Lei de Ampère estabelece a relação quantitativa entre correntes elétricas e o campo magnético "
                "por elas produzido. Em sua forma integral, ela é expressa como:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\oint_{\mathcal{C}} \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}}"
        },

        {
            "tipo": "texto",
            "texto": (
                "Esta equação afirma que a circulação do campo magnético ao longo de uma curva fechada "
                "qualquer é proporcional à corrente total que atravessa a superfície delimitada por essa curva."
            ),
        },

        # ==================================================
        # SIGNIFICADO DE CADA TERMO (DETALHADO)
        # ==================================================
        {"tipo": "titulo", "texto": "Significado dos termos"},

        {
            "tipo": "texto",
            "texto": (
                "\n- $\\vec{B}$: vetor campo magnético [T], tesla.\n\n"
                "- $d\\vec{\\ell}$: vetor elemento infinitesimal de comprimento ao longo da curva $\\mathcal{C}$ [m].\n"
                "- $\\vec{B} \\cdot d\\vec{\\ell}$: produto escalar, que seleciona a componente do campo paralela à curva.\n"
                "- $\\oint_{\\mathcal{C}}$: integral de linha sobre uma curva fechada $\\mathcal{C}$.\n"
                "- $\\mu_0$: permeabilidade magnética do vácuo.\n"
                "- $I_{\\text{enc}}$: corrente total líquida que atravessa qualquer superfície com fronteira $\\mathcal{C}$."
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\mu_0 = 4\pi \times 10^{-7}~\frac{T·m}{A}"
        },

        # ==================================================
        # NATUREZA VETORIAL DO PRODUTO ESCALAR
        # ==================================================
        {"tipo": "titulo", "texto": "O papel do produto escalar"},

        {
            "tipo": "texto",
            "texto": (
                "A integral não soma simplesmente o módulo do campo magnético, mas sim sua componente tangencial à curva. "
                "O produto escalar captura essa ideia:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\vec{B} \cdot d\vec{\ell} = B\, d\ell \cos\theta"
        },

        {
            "tipo": "texto",
            "texto": (
                "\n onde $\\theta$ é o ângulo entre o campo magnético e o elemento de curva. Consequências:\n\n"
                "- $\\theta = 0^\\circ$: contribuição máxima positiva.\n"
                "- $\\theta = 90^\\circ$: contribuição nula (campo perpendicular à curva).\n"
                "- $\\theta = 180^\\circ$: contribuição máxima negativa (campo oposto ao sentido de integração)."
            ),
        },

        # ==================================================
        # CONVENÇÃO DE SINAL (REGRA DA MÃO DIREITA)
        # ==================================================
        {"tipo": "titulo", "texto": "Convenção de sinal para a corrente"},

        {
            "tipo": "texto",
            "texto": (
                "\n O sinal de $I_{\\text{enc}}$ depende da orientação da curva $\\mathcal{C}$. "
                "A regra da mão direita estabelece:\n\n"
                "- Envolva a curva com os dedos da mão direita no sentido de integração.\n"
                "- O polegar indica o sentido positivo da corrente.\n\n"
                "Correntes no sentido oposto contribuem com sinal negativo:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"I_{\text{enc}} = \sum I_{+} - \sum I_{-}"
        },

        # ==================================================
        # ESCOLHA DA CURVA AMPERIANA
        # ==================================================
        {"tipo": "titulo", "texto": "A curva amperiana"},

        {
            "tipo": "texto",
            "texto": (
                "\n O sucesso da aplicação da Lei de Ampère depende da escolha inteligente da curva fechada $\\mathcal{C}$, "
                "chamada de **curva amperiana**. A curva deve explorar a simetria do problema para que:\n\n"
                "1. $\\vec{B}$ seja constante em módulo ao longo de trechos da curva;\n"
                "2. $\\vec{B}$ seja paralelo ou perpendicular a $d\\vec{\\ell}$ nesses trechos;\n"
                "3. A integral se reduza a uma soma de produtos simples."
            ),
        },


        {
            "tipo": "titulo",
            "texto": "Forma diferencial da Lei de Ampère"
        },
        {
            "tipo": "texto",
            "texto": (
                "Usando o teorema de Stokes, a forma integral pode ser convertida na forma diferencial:\n\n"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\oint_{\mathcal{C}} \vec{B} \cdot d\vec{\ell} = \mu_0 I  "
        },
        {
            "tipo": "equacao",
            "latex": r"\int_S (\nabla \times \vec{B}) \cdot d\vec{a} = \mu_0 \int_S \vec{J} \cdot d\vec{a}"
        },
        {
            "tipo": "equacao",
            "latex": r"\int_S (\nabla \times \vec{B} - \mu_0\vec{J}) \cdot d\vec{a} = 0"
        },
        {
            "tipo": "texto",
            "texto": (
                "Como a superfície é arbitrária, obtém-se:\n\n"
            ),
        },
        {
            "tipo": "equacao",
            "latex": r"\nabla \times \vec{B} = \mu_0\vec{J}"
        },
        {
            "tipo": "texto",
            "texto": (
                "Esta equação mostra que o rotacional do campo magnético é proporcional à densidade de corrente no ponto."
            ),
        },


        # ==================================================
        # APLICAÇÃO 1: FIO RETILÍNEO INFINITO
        # ==================================================
        {"tipo": "titulo", "texto": "Aplicação 1: fio retilíneo infinito"},

        {
            "tipo": "texto",
            "texto": (
                "\n Considere um fio retilíneo muito longo percorrido por corrente $I$. Por simetria cilíndrica:\n\n"
                "- O campo magnético é tangente a circunferências concêntricas ao fio.\n"
                "- O módulo de $\\vec{B}$ depende apenas da distância radial $r$.\n\n"
                "Escolhendo uma curva amperiana circular de raio $r$ centrada no fio:\n\n"
                "- $\\vec{B}$ é constante em módulo sobre toda a curva.\n"
                "- $\\vec{B}$ é paralelo a $d\\vec{\\ell}$ ($\cos\\theta = 1$).\n\n"
                "A integral de linha se reduz a:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\oint \vec{B} \cdot d\vec{\ell} = B \oint d\ell = B (2\pi r)"
        },

        {
            "tipo": "texto",
            "texto": "\n A corrente encerrada pela curva é simplesmente $I$ (toda a corrente do fio). Aplicando a lei:"
        },

        {
            "tipo": "equacao",
            "latex": r"B (2\pi r) = \mu_0 I \quad \Rightarrow \quad B = \frac{\mu_0 I}{2\pi r}"
        },

        {
            "tipo": "texto",
            "texto": (
                "\n Este resultado mostra que $B \\propto 1/r$: o campo magnético decai com a distância ao fio."
            ),
        },

        # ==================================================
        # APLICAÇÃO 2: SOLENOIDE LONGO
        # ==================================================
        {"tipo": "titulo", "texto": "Aplicação 2: solenoide longo"},

        {
            "tipo": "texto",
            "texto": (
                "Um solenoide é formado por um enrolamento helicoidal de fio. Para um solenoide ideal (infinitamente longo):\n\n"
                "- O campo interno é uniforme e paralelo ao eixo.\n"
                "- O campo externo é desprezível.\n\n"
                "Escolhe-se uma curva amperiana retangular $ABCDA$ com o lado $AB$ de comprimento $L$ dentro do solenoide, "
                "paralelo ao eixo, e o lado $CD$ fora, onde $B \\approx 0$:\n\n"
                "A integral de linha se reduz a:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\oint \vec{B} \cdot d\vec{\ell} = \int_A^B B\, d\ell = BL"
        },

        {
            "tipo": "texto",
            "texto": (
                "\n A corrente encerrada pela curva é a corrente que passa por todas as espiras atravessadas. "
                "Se o solenoide tem $n$ espiras por unidade de comprimento, o número de espiras no trecho $L$ é $nL$:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"I_{\text{enc}} = (nL) I"
        },

        {
            "tipo": "equacao",
            "latex": r"BL = \mu_0 (nL) I \quad \Rightarrow \quad B = \mu_0 n I"
        },

        {
            "tipo": "texto",
            "texto": (
                "O campo interno do solenoide é uniforme e independe do raio, dependendo apenas da densidade de espiras e da corrente."
            ),
        },

        {"tipo": "titulo", "texto": "Aplicação 3: Toroide"},
        {
            "tipo": "texto",
            "texto": (
                "Um toroide é um solenoide enrolado em forma de anel. Por simetria, as linhas de campo "
                "são circunferências concêntricas ao eixo do toroide. Escolhendo uma curva amperiana circular "
                "de raio r dentro do toroide:\n\n"
                "$$\\oint \\vec{B} \\cdot d\\vec{\\ell} = B(2\\pi r) = \\mu_0 N I$$\n\n"
                "onde N é o número total de espiras. Portanto:\n\n"
                "$$B = \\frac{\\mu_0 N I}{2\\pi r}$$"
            ),
        },

        {"tipo": "titulo", "texto": "Aplicação 4: Fio maciço com corrente uniforme"},
        {
            "tipo": "texto",
            "texto": (
                "Para um fio cilíndrico de raio R com corrente I uniformemente distribuída:\n\n"
                "- Para r ≥ R (fora do fio): $B = \\frac{\\mu_0 I}{2\\pi r}$\n"
                "- Para r < R (dentro do fio): $B = \\frac{\\mu_0 I r}{2\\pi R^2}$\n\n"
                "Dentro do fio, apenas a fração da corrente encerrada contribui: $I_{enc} = I \\frac{r^2}{R^2}$"
            ),
        },

{"tipo": "titulo", "texto": "O paradoxo do capacitor"},
{
    "tipo": "texto",
    "texto": (
        "Considere um capacitor sendo carregado. Entre as placas, não há corrente de condução (J = 0), "
        "mas há um campo elétrico variável. Maxwell percebeu que a Lei de Ampère original falharia "
        "se aplicada a uma superfície que passa entre as placas. Para resolver, ele introduziu a "
        "corrente de deslocamento:\n\n"
        "$$I_d = \\varepsilon_0 \\frac{d\\Phi_E}{dt}$$\n\n"
        "Assim, a lei de Ampère-Maxwell unifica os dois fenômenos."
    ),
},

{"tipo": "titulo", "texto": "Quando usar cada lei?"},
{
    "tipo": "texto",
    "texto": (
        "\n| Situação | Lei mais adequada | Motivo |\n"
        "|----------|-------------------|--------|\n"
        "| Fio retilíneo infinito | Ampère | Alta simetria |\n"
        "| Espira circular | Biot-Savart | Baixa simetria |\n"
        "| Solenoide longo | Ampère | Alta simetria |\n"
        "| Distribuição arbitrária | Biot-Savart (numérico) | Sem simetria |\n<br>"
    ),
},

        # ==================================================
        # LIMITAÇÕES DA LEI DE AMPÈRE
        # ==================================================
        {"tipo": "titulo", "texto": "Limitações da forma integral"},

        {
            "tipo": "texto",
            "texto": (
                "\n A Lei de Ampère na forma integral $\\oint \\vec{B} \\cdot d\\vec{\\ell} = \\mu_0 I_{\\text{enc}}$ "
                "é rigorosamente válida apenas para correntes estacionárias (constantes no tempo). "
                "Quando as correntes variam no tempo, surge uma contribuição adicional devido ao campo elétrico variável, "
                "corrigida por Maxwell com a introdução da **corrente de deslocamento**. "

                "Além disso, a aplicação direta é eficiente apenas em problemas com simetria elevada. "
                "Para configurações arbitrárias, recorre-se à Lei de Biot-Savart ou a métodos numéricos."
            ),
        },

        # ==================================================
        # CORRENTE DE DESLOCAMENTO (EXTENSÃO DE MAXWELL)
        # ==================================================
        {"tipo": "titulo", "texto": "A generalização de Maxwell"},

        {
            "tipo": "texto",
            "texto": (
                "\n Maxwell percebeu que a Lei de Ampère era incompleta para situações com campos elétricos variáveis. "
                "Ele propôs a adição da corrente de deslocamento $I_d = \\varepsilon_0 \\frac{d\\Phi_E}{dt}$, "
                "onde $\\Phi_E$ é o fluxo do campo elétrico. A lei de Ampère-Maxwell torna-se:"
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\oint \vec{B} \cdot d\vec{\ell} = \mu_0 \left( I_{\text{enc}} + \varepsilon_0 \frac{d\Phi_E}{dt} \right)"
        },

        {
            "tipo": "texto",
            "texto": (
                "Essa correção foi fundamental para prever a existência de ondas eletromagnéticas e unificar "
                "eletricidade, magnetismo e óptica."
            ),
        },

        # ==================================================
        # QUESTÕES
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.003.0001",
            "pergunta": (
                "Ao aplicar a Lei de Ampère a um fio retilíneo muito longo, por que a curva amperiana escolhida "
                "é uma circunferência centrada no fio?"
            ),
            "alternativas": {
                "a": "Porque o campo magnético é radial e a integral se anula.",
                "b": "Porque, por simetria, o campo magnético tem módulo constante e é tangente à circunferência.",
                "c": "Porque a corrente elétrica só flui em trajetórias circulares.",
                "d": "Porque a Lei de Ampère só funciona com curvas circulares.",
                "e": "Porque o campo magnético é nulo fora do fio."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.003.0002",
            "pergunta": (
                "\n Em um solenoide longo, o campo magnético interno é dado por $B = \\mu_0 n I$. "
                "A grandeza \\(n\\) representa:"
            ),
            "alternativas": {
                "a": "O número total de espiras do solenoide.",
                "b": "O comprimento total do solenoide.",
                "c": "O número de espiras por unidade de comprimento.",
                "d": "A resistência elétrica por unidade de comprimento.",
                "e": "A permeabilidade magnética do núcleo."
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.003.0003",
            "pergunta": (
                "Qual foi a principal contribuição de Maxwell à Lei de Ampère?"
            ),
            "alternativas": {
                "a": "Maxwell demonstrou que a lei só vale para correntes contínuas.",
                "b": "Maxwell adicionou a corrente de deslocamento, permitindo descrever campos variáveis no tempo.",
                "c": "Maxwell mostrou que o campo magnético é sempre conservativo.",
                "d": "Maxwell substituiu a integral de linha por uma integral de superfície.",
                "e": "Maxwell provou que a permeabilidade magnética depende do meio."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.03.003.0004",
            "pergunta": (
                "Explique o papel da curva amperiana na aplicação da Lei de Ampère. "
                "Por que sua escolha deve respeitar as simetrias do problema? "
                "Dê um exemplo de uma situação onde a lei pode ser aplicada diretamente e outra onde não pode."
            ),
            "altura": 200,
        },

    ]