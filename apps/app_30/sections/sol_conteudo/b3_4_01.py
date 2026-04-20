from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        # ==================================================
        # ABERTURA
        # ==================================================
        {"tipo": "titulo", "texto": "Lei de Faraday: a descoberta que eletrificou o mundo"},

        { "tipo": "texto", "texto": (
                "A indução eletromagnética revolucionou a ciência e a tecnologia ao permitir converter "
                "movimento mecânico em energia elétrica. Esse princípio está na base de geradores, "
                "transformadores e de toda a indústria moderna de energia."
        ),},

        {"tipo": "subtitulo", "texto": "Michael Faraday (1791–1867)"},
        {
            "tipo": "texto",
            "texto": (
                "Faraday demonstrou que um campo magnético variável pode gerar força eletromotriz em um condutor, "
                "estabelecendo o princípio da indução eletromagnética. Suas descobertas transformaram a física e a engenharia."
            ),
        },

        { "tipo": "video", "url": "https://www.youtube.com/watch?v=iYPMZamqSH4"},

        # ==================================================
        # O CAMINHO ATÉ A INDUÇÃO
        # ==================================================
        {"tipo": "titulo", "texto": "O caminho até a descoberta"},

        {"tipo": "subtitulo", "texto": "1820 — Hans Christian Ørsted"},

        {
            "tipo": "texto",
            "texto": (
                "Ørsted descobriu que uma corrente elétrica gera um campo magnético. "
                "Eletricidade e magnetismo, antes vistos como fenômenos separados, estavam conectados."
            ),
        },

        {"tipo": "subtitulo", "texto": "1821 — Faraday: o primeiro motor"},

        {
            "tipo": "texto",
            "texto": (
                "Inspirado por Ørsted, Faraday construiu dispositivos que convertiam eletricidade em movimento. "
                "Nasceu o motor elétrico."
            ),
        },

        # ==================================================
        # O EXPERIMENTO FUNDAMENTAL
        # ==================================================
        {"tipo": "titulo", "texto": "1831 — O anel de indução"},

        {
            "tipo": "texto",
            "texto": (
                "Faraday enrolou duas bobinas em um núcleo de ferro. Ao ligar ou desligar a corrente em uma bobina, "
                "um galvanômetro conectado à outra registrava uma corrente momentânea.\n\n<br>"
                "A grande descoberta: a corrente induzida aparecia **apenas enquanto a corrente da primeira bobina variava**. "
                "Não era o campo magnético em si, mas sua **variação** que gerava corrente. \n\n"

                "Faraday confirmou o fenômeno de outra forma: ao mover um ímã através de uma bobina, "
                "uma corrente surgia durante o movimento. Se o ímã parasse, a corrente desaparecia. "
                "Invertendo o movimento, a corrente mudava de sentido. O mesmo ocorria ao mover a bobina em relação ao ímã.\n\n"
                "Conclusão: o que importa é o **movimento relativo** entre ímã e bobina."
            ),
        },
        { "tipo": "video", "url": "https://www.youtube.com/watch?v=pbT6HUDB0e8"},
        # ==================================================
        # O QUE É INDUÇÃO?
        # ==================================================
        {"tipo": "titulo", "texto": "O que é indução eletromagnética?"},

        {
            "tipo": "texto",
            "texto": (
                "\nÉ o fenômeno pelo qual a **variação do fluxo magnético** através de uma espira ou bobina "
                "gera uma força eletromotriz induzida. Se o circuito estiver fechado, surge corrente elétrica.\n\n"
                "Relação inversa com Ørsted:\n\n"
                "- Ørsted: corrente elétrica → campo magnético.\n"
                "- Faraday: campo magnético variável → corrente elétrica."
            ),
        },

        # ==================================================
        # FORMULAÇÃO MATEMÁTICA
        # ==================================================
        # {"tipo": "titulo", "texto": "A Lei de Faraday em equações"},

        # {
        #     "tipo": "equacao",
        #     "latex": r"\mathcal{E} = - \frac{d\Phi_B}{dt}"
        # },

        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "A força eletromotriz induzida é igual à taxa de variação do fluxo magnético. "
        #         "Quanto mais rápida a variação, maior a corrente induzida."
        #     ),
        # },

        # {
        #     "tipo": "equacao",
        #     "latex": r"\Phi_B = \int \vec{B}\cdot d\vec{A}"
        # },

        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "O fluxo magnético mede quanto do campo atravessa uma superfície. "
        #         "Para campo uniforme e superfície plana:"
        #     ),
        # },

        # {
        #     "tipo": "equacao",
        #     "latex": r"\Phi_B = B A \cos\theta"
        # },

        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "onde:\n"
        #         "• \\(B\\): módulo do campo magnético;\n"
        #         "• \\(A\\): área da espira;\n"
        #         "• \\(\\theta\\): ângulo entre \\(\\vec{B}\\) e a normal à superfície.\n\n"
        #         "Para uma bobina com \\(N\\) espiras:"
        #     ),
        # },

        # {
        #     "tipo": "equacao",
        #     "latex": r"\mathcal{E} = - N \frac{d\Phi_B}{dt}"
        # },

        # ==================================================
        # TRÊS FORMAS DE VARIAR O FLUXO
        # ==================================================
        {"tipo": "titulo", "texto": "Como gerar indução?"},

        {
            "tipo": "texto",
            "texto": (
                "\n A indução ocorre sempre que o fluxo magnético varia. Isso pode acontecer de três maneiras:\n\n"
                "1. **Variar $\\vec{B}$:** intensidade do campo (ex: ligar/desligar um eletroímã);\n"
                "2. **Variar $A$:** área da espira exposta ao campo;\n"
                "3. **Variar $\\theta$:** ângulo entre campo e superfície (ex: girar uma espira)."
            ),
        },

        {"tipo": "imagem", "arquivo": "faraday_02.png"},
        # ==================================================
        # LEI DE LENZ: O SENTIDO DA CORRENTE
        # ==================================================
        {"tipo": "titulo", "texto": "Lei de Lenz: oposição à mudança"},

        {
            "tipo": "texto",
            "texto": (
                "\n Em 1834, Emil Lenz respondeu uma pergunta fundamental: para onde vai a corrente induzida? "
                "**A corrente induzida sempre se opõe à variação que a produziu.**\n\n"

                "Imagine um ímã se aproximando de uma bobina. O fluxo magnético aumenta. O que a corrente induzida faz? "
                "Ela cria um campo magnético que tenta empurrar o ímã para longe, ou seja, **opõe-se à aproximação**.\n\n"
                
                "Agora imagine o ímã se afastando. O fluxo diminui. A corrente induzida, então, cria um campo que tenta puxar "
                "o ímã de volta, **opondo-se ao afastamento**.\n\n"
                "Esse comportamento revela algo profundo: a natureza não permite que você ganhe energia \"de graça\". "
                "Ao mover um ímã perto de uma bobina, parte da energia mecânica que você aplica é transformada em energia elétrica. "
                "Se a corrente induzida ajudasse o movimento, você teria um movimento acelerado sem gastar energia, o que é impossível.\n\n"
                "A Lei de Lenz é, portanto, uma consequência direta da **conservação da energia**. Ela diz que a corrente induzida "
                "sempre age contra a mudança que a causou, resistindo ao movimento relativo entre ímã e bobina."
            ),
        },

        { "tipo": "video", "url": "https://www.youtube.com/watch?v=Oz15bjsSVxY"},
        # ==================================================
        # REGRA DA MÃO DIREITA
        # ==================================================
        {"tipo": "titulo", "texto": "Regra prática: a mão direita de Fleming"},

        {
            "tipo": "texto",
            "texto": (
                "Nos anos 1880, Fleming criou uma regra para determinar o sentido da corrente induzida. "
                "Com os dedos da mão direita perpendiculares entre si:\n\n"
                "- **Polegar** → movimento do condutor;\n"
                "- **Indicador** → direção do campo magnético;\n"
                "- **Médio** → sentido da corrente induzida."
            ),
        },
        {"tipo": "imagem", "arquivo": "faraday_05.png"},
        # ==================================================
        # O PRIMEIRO GERADOR
        # ==================================================
        {"tipo": "titulo", "texto": "O disco de Faraday: nasce o gerador"},

        {
            "tipo": "texto",
            "texto": (
                "No mesmo ano da descoberta, Faraday construiu o primeiro gerador: um disco metálico girando entre os polos de um ímã.\n\n"
                "Ao girar, uma corrente contínua era gerada. Estava demonstrado: **movimento mecânico produz eletricidade**.\n\n"
                "A relação se completa:\n"
                "- motor: eletricidade → movimento;\n"
                "- gerador: movimento → eletricidade."
            ),
        },
       { "tipo": "video", "url": "https://www.youtube.com/watch?v=0KMgE3RoQVU"},
        # ==================================================
        # DO LABORATÓRIO ÀS CIDADES
        # ==================================================
        {"tipo": "titulo", "texto": "Dos laboratórios às cidades"},

        {
            "tipo": "texto",
            "texto": (
                "Os primeiros geradores eram manuais e pouco eficientes. A evolução foi rápida:\n\n"
                "- Hippolyte Pixii construiu o primeiro gerador manual baseado nos experimentos de Faraday;\n"
                "- a invenção do comutador permitiu converter corrente alternada em contínua;\n"
                "- nos anos 1880, grandes geradores acionados por turbinas começaram a operar em Londres e Nova York.\n\n"
                "A eletricidade deixou os laboratórios e iluminou as cidades."
            ),
        },

 
        # ==================================================
        # GERADORES MODERNOS
        # ==================================================
        {"tipo": "titulo", "texto": "O princípio nas usinas de energia"},

        {
            "tipo": "texto",
            "texto": (
                "Hoje, o mesmo princípio está nas usinas hidrelétricas, eólicas e termelétricas. "
                "Turbinas movidas por água, vento ou vapor giram bobinas ou ímãs, gerando corrente elétrica em larga escala.\n\n"
                "A corrente gerada é transformada (elevação de tensão) para transmissão por longas distâncias, "
                "e depois reduzida para uso seguro em residências e indústrias."
            ),
        },
        { "tipo": "video", "url": "https://www.youtube.com/watch?v=JKiwVxoMBi0"},


        # ==================================================
        # MAXWELL E A UNIFICAÇÃO
        # ==================================================
        {"tipo": "titulo", "texto": "Maxwell: a teoria que unificou tudo"},

        {
            "tipo": "texto",
            "texto": (
                "As descobertas experimentais de Faraday foram a base para o trabalho de James Clerk Maxwell. "
                "Em 1865, Maxwell unificou eletricidade e magnetismo em quatro equações. "
                "Mostrou que campos elétricos e magnéticos variáveis se propagam como ondas, e que a luz é uma delas.\n\n <br>"
                "Faraday forneceu os experimentos; Maxwell, a teoria."
            ),
        },

        # ==================================================
        # APLICAÇÃO MODERNA
        # ==================================================
        {"tipo": "titulo", "texto": "Aplicação atual: carregamento sem fio"},

        {
            "tipo": "texto",
            "texto": (
                "A indução eletromagnética está presente em tecnologias do dia a dia. "
                "Carregadores sem fio funcionam como transformadores: uma bobina gera um campo magnético variável; "
                "outra bobina, próxima, converte esse campo novamente em corrente elétrica. "
                "É o mesmo princípio usado em celulares, escovas elétricas, dispositivos médicos e até no carregamento de veículos elétricos."
            ),
        },
        { "tipo": "video", "url": "https://www.youtube.com/watch?v=GKFAbkSWbno"},
        # ==================================================
        # SÍNTESE FINAL
        # ==================================================
        {"tipo": "titulo", "texto": "Resumo"},

        {
            "tipo": "texto",
            "texto": (
                "\n A Lei de Faraday estabelece que a **variação do fluxo magnético** produz força eletromotriz induzida. "
                "Faraday completou o quadro: se correntes geram campos magnéticos (Ørsted), então campos magnéticos variáveis "
                "também geram eletricidade. "
                "Esse princípio está na base de geradores, transformadores, usinas e da distribuição de energia elétrica que "
                "alimenta o mundo moderno."
            ),
        },




# ==================================================
# QUESTÕES
# ==================================================
                {"tipo": "titulo", "texto": "🔍 Como Faraday pensaria?"},
        { "tipo": "questao_multipla_escolha", "id": "solucao.04.001.0001",
            "pergunta": (
                "Qual afirmação expressa corretamente a ideia central da Lei de Faraday?"
            ),
            "alternativas": {
                "a": "Um campo magnético constante sempre gera corrente elétrica.",
                "b": "Uma corrente elétrica constante gera automaticamente uma diferença de potencial.",
                "c": "Uma variação do fluxo magnético produz força eletromotriz induzida.",
                "d": "Toda força eletromotriz depende exclusivamente da resistência do fio.",
                "e": "A indução ocorre apenas quando há um ímã permanente."
            },
            "alternativa_correta": "c",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.04.001.0002",
            "pergunta": (
                "De acordo com o texto, o que é necessário para que ocorra indução eletromagnética?"
            ),
            "alternativas": {
                "a": "A presença de um campo magnético constante.",
                "b": "Um campo magnético de alta intensidade.",
                "c": "A variação do fluxo magnético no tempo.",
                "d": "Um ímã de grande massa.",
                "e": "Um fio condutor muito longo."
            },
            "alternativa_correta": "c",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.04.001.0003",
            "pergunta": (
                "O texto menciona três formas de variar o fluxo magnético. Quais são elas?"
            ),
            "alternativas": {
                "a": "Variar a temperatura, variar a pressão, variar a umidade.",
                "b": "Variar a intensidade do campo, variar a área da espira, variar o ângulo entre campo e superfície.",
                "c": "Variar a resistência do fio, variar a corrente, variar a tensão.",
                "d": "Variar o comprimento do fio, variar o material do ímã, variar a velocidade do movimento.",
                "e": "Variar a cor do ímã, variar o formato da bobina, variar o tipo de metal."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.04.001.0004",
            "pergunta": (
                "O que acontece quando um ímã se aproxima de uma bobina, segundo a Lei de Lenz?"
            ),
            "alternativas": {
                "a": "A corrente induzida atrai o ímã, acelerando sua aproximação.",
                "b": "A corrente induzida cria um campo que repele o ímã, opondo-se à aproximação.",
                "c": "Nenhuma corrente é gerada durante a aproximação.",
                "d": "A corrente induzida depende apenas da velocidade do ímã, não da direção.",
                "e": "A corrente induzida aquece o ímã, mas não gera campo magnético."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.04.001.0005",
            "pergunta": (
                "No experimento do anel de indução de Faraday, quando a corrente na primeira bobina era ligada ou desligada, "
                "o que acontecia na segunda bobina?"
            ),
            "alternativas": {
                "a": "Uma corrente contínua e constante era gerada.",
                "b": "Uma corrente momentânea aparecia apenas durante a variação da corrente.",
                "c": "Nenhuma corrente era gerada, pois o núcleo de ferro impedia a indução.",
                "d": "Uma corrente alternada de alta frequência era gerada continuamente.",
                "e": "A corrente na segunda bobina era sempre igual à corrente na primeira."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.04.001.0006",
            "pergunta": (
                "O que a Lei de Lenz garante do ponto de vista da conservação da energia?"
            ),
            "alternativas": {
                "a": "Que a corrente induzida sempre ajuda o movimento do ímã.",
                "b": "Que a energia elétrica gerada é maior que a energia mecânica gasta.",
                "c": "Que a corrente induzida se opõe à variação que a produziu, garantindo que parte da energia mecânica seja convertida em elétrica.",
                "d": "Que não há perda de energia durante a indução.",
                "e": "Que a energia magnética é infinita."
            },
            "alternativa_correta": "c",
        },

        { "tipo": "questao_texto", "id": "solucao.04.001.0007",
            "pergunta": (
                "Explique por que a Lei de Faraday é considerada o inverso físico da descoberta de Ørsted. "
                "Em sua resposta, relacione corrente elétrica, campo magnético e movimento."
            ),
            "altura": 140,
        },

        { "tipo": "questao_texto", "id": "solucao.04.001.0008",
            "pergunta": (
                "Descreva o experimento do anel de indução de Faraday e explique qual foi a grande descoberta "
                "que ele revelou sobre a relação entre campo magnético e corrente elétrica."
            ),
            "altura": 140,
        },

        { "tipo": "questao_texto", "id": "solucao.04.001.0009",
            "pergunta": (
                "O texto descreve três formas de variar o fluxo magnético. Escolha UMA delas e dê um exemplo prático "
                "de como ela pode ser usada para gerar corrente elétrica em um gerador."
            ),
            "altura": 140,
        },

        { "tipo": "questao_texto", "id": "solucao.04.001.0010",
            "pergunta": (
                "O que a Lei de Lenz nos ensina sobre o sentido da corrente induzida? "
                "Use o exemplo de um ímã se aproximando e se afastando de uma bobina para explicar."
            ),
            "altura": 140,
        },

 
    ]