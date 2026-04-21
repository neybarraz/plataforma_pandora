def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # ABERTURA
        # ==================================================
        {"tipo": "titulo", "texto": "Estática dos Fluidos: a física do que não flui"},

        {
            "tipo": "texto",
            "texto": (
                "O que une o fundo do oceano, um freio de caminhão e um navio flutuando?\n\n<br>"
                "Todos obedecem às mesmas leis da estática dos fluidos, o ramo da física que estuda "
                "líquidos e gases em repouso. Sem ela, não haveria barragens, submarinos, "
                "elevadores hidráulicos nem a prensa que molda peças de metal. "
                "Vamos entender como esses conceitos surgiram e como eles se conectam."
            ),
        },

        # ==================================================
        # O QUE É UM FLUIDO?
        # ==================================================
        {"tipo": "titulo", "texto": "1. O que é um fluido?"},

        {"tipo": "texto", "texto": (
                "Qual a diferença entre empurrar uma mesa e empurrar um balde de água?\n\n"
                
                "- A mesa resiste. Você aplica força lateral, ela pode até se deslocar inteira, mas sua forma permanece. "
                "O sólido suporta esforços tangenciais. As ligações internas seguram o tranco.\n\n"
                
                "- A água não. Se você aplica qualquer força tangencial, por menor que seja, ela se deforma sem parar. "
                
                "O fluido simplesmente não consegue sustentar tensão de cisalhamento em equilíbrio. Ele escorre.\n\n"
                "Essa é a definição: fluido é todo material que se deforma continuamente sob ação de uma tensão de cisalhamento, "
                "não importa quão pequena seja essa tensão. Vale para líquidos e gases. "
        ),},
        {"tipo": "imagem", "arquivo": "fluido_01.png"},
        { "tipo": "texto", "texto": (               
                "Na estática dos fluidos, olhamos para um caso específico: o fluido em repouso. Não há movimento macroscópico, "
                "mas isso não significa que as forças sumiram. Pressão interna, peso da coluna de fluido e forças externas "
                "se equilibram com precisão. Aparentemente simples, mas fisicamente profundo."
        ),},


        # ==================================================
        # DENSIDADE: O QUÃO COMPACTO É?
        # ==================================================
        {"tipo": "titulo", "texto": "2. Densidade: por que o óleo flutua na água?"},

        { "tipo": "texto", "texto": (
            "A resposta está em uma grandeza fundamental chamada densidade. "
            "A densidade mede quanta massa existe em um determinado volume. "
            "Em termos físicos, ela é definida por:"
        ),},
        {"tipo": "equacao",
            "latex": r"\rho = \frac{m}{V}"
        },
        { "tipo": "texto", "texto": (
                "\n onde $\\rho$ é a densidade, $m$ a massa e $V$ o volume.\n\n"
                "Quanto maior a massa no mesmo volume, maior a densidade.\n\n"
                "O óleo tem densidade menor que a água. Por isso ele fica em cima. "
                "Não porque é \"mais leve\" no senso comum, mas porque tem menos massa por volume.\n\n"
                "A regra é simples: em sistemas com fluidos diferentes, o menos denso ocupa a parte superior."
            ),
        },

        # ==================================================
        # PRESSÃO: FORÇA ESPALHADA
        # ==================================================
        {"tipo": "titulo", "texto": "3. Pressão: força que se espalha"},
        { "tipo": "texto",  "texto": (
                "A pressão surge quando uma força é aplicada sobre uma superfície distribuindo-se por uma área. "
                "Fisicamente, ela é definida como a razão entre a força normal aplicada e a área sobre a qual essa força atua: "
            ),
        },
        { "tipo": "equacao",
            "latex": r"P = \frac{F}{A}"
        },
        { "tipo": "texto", "texto": (
                "onde:\n\n"
                "- $P$ é a pressão;\n"
                "- $F$ é a força normal à superfície;\n"
                "- $A$ é a área de aplicação.\n\n"
                "Para uma mesma força, quanto menor a área, maior a pressão exercida. "
                "Esse princípio explica o funcionamento de ferramentas como lâminas e pontas concentradoras de esforço.\n\n"

                "Nos fluidos em repouso, a pressão possui uma característica fundamental: ela atua igualmente em todas as direções "
                "e sempre de forma perpendicular às superfícies. Essa isotropia é consequência direta da incapacidade do fluido "
                "de resistir a tensões de cisalhamento em equilíbrio."
            ),
        },

        # ==================================================
        # PRESSÃO HIDROSTÁTICA: QUANTO MAIS FUNDO, MAIOR A PRESSÃO
        # ==================================================
        {"tipo": "titulo", "texto": "4. Pressão hidrostática: quanto mais fundo, maior a pressão"},
        {"tipo": "imagem", "arquivo": "fluido_02.png"},
        { "tipo": "texto", "texto": (
                "Em um fluido em repouso, a pressão varia com a profundidade devido ao peso da coluna de fluido acima do ponto analisado.\n\n<br>"
                "Considere um elemento de fluido de área \\(A\\) e altura \\(h\\). O equilíbrio vertical exige que a diferença de pressão "
                "entre sua base e seu topo equilibre o peso do fluido contido nesse volume.\n\n"
                "O peso da coluna é dado por:"
            ),
        },
        { "tipo": "equacao", "latex": r"W = m g" },
        { "tipo": "equacao", "latex": r"F - F_o = \rho V g " },
        { "tipo": "equacao", "latex": r"F - F_o = \rho (A h) g" },
        { "tipo": "equacao", "latex": r"\frac{F}{A} - \frac{F_o}{A} = \rho h g" },

        { "tipo": "texto", "texto": (
                "Como a pressão é força por unidade de área, a variação de pressão entre o topo e a base é:\n\n"
        ), },
        { "tipo": "equacao", "latex": r"P - P_o = \rho h g" },
        { "tipo": "texto", "texto": (
                "\n Portanto, a pressão em um ponto a uma profundidade $h$ é dada por:"
        ), },
        { "tipo": "equacao", "latex": r"P = P_0 + \rho g h" },
        { "tipo": "texto", "texto": (
                "\n onde $P_0$ é a pressão na superfície.\n\n"
                "Esse resultado mostra que a pressão hidrostática depende exclusivamente da profundidade, da densidade do fluido "
                "e da aceleração da gravidade, sendo independente da geometria do recipiente.\n\n"
                "Essa propriedade leva ao chamado paradoxo hidrostático: recipientes com formas distintas, mas com a mesma altura de fluido, "
                "produzem a mesma pressão na base."
        ),},
        {"tipo": "imagem", "arquivo": "fluido_03.png"},
        { "tipo": "texto", "texto": (
                "Do ponto de vista de engenharia, isso implica que estruturas como barragens devem ser dimensionadas para suportar "
                "pressões crescentes com a profundidade, independentemente do volume total armazenado."
        ),},


        # ==================================================
        # PRINCÍPIO DE PASCAL: MULTIPLICANDO FORÇAS
        # ==================================================
        {"tipo": "titulo", "texto": "5. Princípio de Pascal: multiplicando forças"},
        {"tipo": "texto", "texto": (
                "O princípio de Pascal: uma pressão aplicada a um fluido confinado se transmite "
                "igualmente para todos os pontos. "
                "Por que isso acontece? \n\n<br>"
                "Porque o fluido em repouso não sustenta tensões de cisalhamento. "
                "A única forma de equilíbrio é a pressão agindo com a mesma intensidade em todas as direções. "
                "A consequência prática é direta: se a pressão é igual em dois pontos, "
                "então forças diferentes podem surgir em áreas diferentes. "
        ),},
        { "tipo": "equacao", "latex": r"\frac{F_1}{A_1} = \frac{F_2}{A_2}"},
        {
            "tipo": "texto",
            "texto": (
                "Traduzindo: uma força pequena aplicada numa área pequena gera uma força grande numa área grande. "
                "A pressão é a mesma. O que muda é a área. "
                "É assim que um macaco hidráulico levanta um caminhão com o esforço de uma mão. "
                "Freios, prensas, elevadores hidráulicos e até cadeiras de dentista funcionam com essa mesma ideia."
            ),
        },
        {"tipo": "imagem", "arquivo": "fluido_04.png"},
        # ==================================================
        # EMPUXO E ARQUIMEDES: O MOMENTO "EUREKA!"
        # ==================================================
        {"tipo": "titulo", "texto": "6. Empuxo: por que alguns objetos flutuam?"},
        { "tipo": "texto",  "texto": (
                "O princípio de Arquimedes: todo corpo imerso em um fluido recebe uma força para cima chamada empuxo. "
                "De onde vem essa força? \n\n<br> A pressão hidrostática aumenta com a profundidade. A parte de baixo do corpo sofre pressão maior que a parte de cima. "
                "Essa diferença gera uma força resultante vertical para cima."
        ),},
        { "tipo": "equacao",  "latex": r"P = P_0 + \rho g h" },
        { "tipo": "texto", "texto": (
                "A consequência direta dessa variação de pressão é que o empuxo equivale ao peso do fluido deslocado.\n\n"
        ), },
        { "tipo": "equacao", "latex": r"E = \rho g V" },
        { "tipo": "texto",  "texto": (
            "\n onde: $E$ é o empuxo, $\\rho$ a densidade do fluido e $V$ o volume de fluido deslocado.\n\n"
            "Na prática, o que determina se um corpo flutua ou afunda é a comparação entre empuxo e peso:\n\n"
            "- se o empuxo for maior que o peso, o corpo sobe.\n"
            "- se o empuxo for menor, o corpo afunda.\n"
            "- se forem iguais, o corpo fica em equilíbrio em qualquer profundidade.\n\n"
            "É assim que um navio de aço flutua: ele desloca um volume enorme de água, gerando empuxo suficiente para equilibrar seu peso. "
            "Submarinos controlam a profundidade ajustando o volume de água nos tanques de lastro, mudando assim seu peso total."
            ),
        },
        {"tipo": "imagem", "arquivo": "fluido_05.png"},
 

        # ==================================================
        # TECNOLOGIA ATUAL
        # ==================================================
        {"tipo": "titulo", "texto": "7. Aplicação atual: o freio ABS do seu carro"},

        { "tipo": "texto", "texto": (
                "O freio do seu carro é um exemplo direto de estática dos fluidos em ação. "
                "Você pisa no pedal com uma força pequena. O que acontece dentro do sistema?"
        ), },
        {"tipo": "imagem", "arquivo": "fluido_06.png"},
        { "tipo": "equacao", "latex": r"F = P\cdot A" },
        { "tipo": "texto", "texto": (
                "Essa força gera pressão no fluido de freio. "
                "Pelo princípio de Pascal, a pressão se transmite igualmente por todo o fluido confinado. "
                "Nos pistões das rodas, a área é maior. "
                "Mesma pressão, área maior, força maior. "
                "A força pequena do seu pé vira uma força enorme nas pastilhas de freio. "
        ), },
        { "tipo": "equacao", "latex": r"\frac{F_1}{A_1} = \frac{F_2}{A_2}" },
        { "tipo": "texto", "texto": (
            "É só isso. Sem engrenagens, sem alavancas complicadas. Fluido e pressão. "
            "O sistema ABS vai além. Sensores detectam quando uma roda está prestes a travar. "
            "Válvulas abrem e fecham rapidamente, modulando a pressão do fluido dezenas de vezes por segundo. "
            "Resultado: a roda não trava, o carro continua controlável e você para com segurança. "
            "Engenharia pura: transmissão de pressão mais controle eletrônico."
        ), },

       # ==================================================
        # SÍNTESE DOS CONCEITOS
        # ==================================================
        {"tipo": "titulo", "texto": "O quadro completo"},

        { "tipo": "texto", "texto": (
                "Vamos organizar as ideias:\n\n"
                "- **Fluido**: substância que se deforma sob qualquer força tangencial.\n"
                "- **Densidade**: quanta massa cabe em um dado volume.\n"
                "- **Pressão**: força distribuída por área; nos fluidos, age em todas as direções.\n"
                "- **Pressão hidrostática (Stevin)**: aumenta com a profundidade, independe da forma do recipiente.\n"
                "- **Princípio de Pascal**: pressão aplicada a um fluido confinado se transmite integralmente.\n"
                "- **Empuxo (Arquimedes)**: força para cima igual ao peso do fluido deslocado.\n\n"
                "Esses conceitos, descobertos entre a Grécia Antiga e o século XVII, formam a base da engenharia hidráulica moderna."
        ),},
        # ==================================================
        # QUESTÕES
        # ==================================================
        {"tipo": "titulo", "texto": "🔍 O que você aprendeu?"},

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.001.0001",
            "pergunta": (
                "O que diferencia um fluido de um sólido?"
            ),
            "alternativas": {
                "a": "Fluidos são sempre líquidos; sólidos são sempre duros.",
                "b": "Fluidos se deformam continuamente sob qualquer força tangencial; sólidos resistem.",
                "c": "Fluidos não têm massa; sólidos têm.",
                "d": "Fluidos só existem na natureza; sólidos são artificiais.",
                "e": "Fluidos não podem ser comprimidos; sólidos sim."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.001.0002",
            "pergunta": (
                "O princípio descoberto por Arquimedes dentro de uma banheira afirma que:"
            ),
            "alternativas": {
                "a": "A pressão aumenta com a profundidade.",
                "b": "A pressão se transmite igualmente por todo o fluido.",
                "c": "Todo corpo imerso sofre uma força para cima igual ao peso do fluido deslocado.",
                "d": "Fluidos mais densos afundam sempre.",
                "e": "A densidade não influencia a flutuação."
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.001.0003",
            "pergunta": (
                "O sistema de freios hidráulicos de um carro é uma aplicação direta de qual princípio?"
            ),
            "alternativas": {
                "a": "Princípio de Stevin (pressão hidrostática).",
                "b": "Princípio de Arquimedes (empuxo).",
                "c": "Princípio de Pascal (transmissão de pressão).",
                "d": "Paradoxo hidrostático.",
                "e": "Lei da densidade."
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.001.0004",
            "pergunta": (
                "Por que barragens são construídas mais largas na base do que no topo?"
            ),
            "alternativas": {
                "a": "Para economizar material.",
                "b": "Por razões estéticas apenas.",
                "c": "Porque a pressão da água é maior nas camadas mais profundas.",
                "d": "Para facilitar a passagem de peixes.",
                "e": "Porque a água é mais densa no fundo."
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.01.001.0005",
            "pergunta": (
                "Explique, com suas palavras, como um navio de aço (material mais denso que a água) consegue flutuar. "
                "Use o conceito de empuxo e densidade média em sua resposta."
            ),
            "altura": 140,
        },

    ]