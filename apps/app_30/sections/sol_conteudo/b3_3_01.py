def get_blocos() -> list[dict]:
    return [

        {"tipo": "titulo", "texto": "Linha do tempo do eletromagnetismo"},

        {
            "tipo": "texto",
            "texto": (
                "O desenvolvimento do eletromagnetismo não aconteceu de forma isolada. "
                "Foi uma sequência de descobertas conectadas, onde cada avanço abriu caminho "
                "para aplicações práticas que transformaram a engenharia."
            ),
        },

        # -------------------------------------------------
        # GILBERT
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1600 — William Gilbert"},

        {
            "tipo": "texto",
            "texto": (
                "William Gilbert realizou os primeiros estudos científicos sistemáticos sobre "
                "eletricidade e magnetismo. Ele identificou que a Terra se comporta como um ímã, "
                "mas ainda não havia relação entre eletricidade e magnetismo."
            ),
        },

        # -------------------------------------------------
        # OERSTED
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1820 — Hans Christian Ørsted"},

        {
            "tipo": "texto",
            "texto": (
                "Ørsted descobriu que uma corrente elétrica gera um campo magnético. "
                "Ao passar corrente por um fio, ele observou o desvio de uma bússola próxima. "
                "Essa descoberta unificou eletricidade e magnetismo, mostrando que ambos fazem "
                "parte do mesmo fenômeno físico."
            ),
        },

        # -------------------------------------------------
        # AMPERE
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1820–1825 — André-Marie Ampère"},

        {
            "tipo": "texto",
            "texto": (
                "A descoberta de Ørsted (1820) mostrou que correntes elétricas geram campos magnéticos. "
                "Ampère aprofundou essa ideia ao investigar como correntes diferentes interagem entre si.\n\n"
                "Ele observou algo fundamental:\n"
                "- Dois fios paralelos com corrente no mesmo sentido se atraem.\n"
                "- Com correntes em sentidos opostos, eles se repelem.\n\n"
                "Essa foi a primeira evidência clara de que o campo magnético não é apenas um efeito local "
                "ao redor de um fio, mas sim um agente físico capaz de produzir forças entre condutores distantes.\n\n"
                "Com base nesses experimentos, Ampère formulou uma lei matemática que relaciona:\n"
                "- a intensidade da força entre os fios,\n"
                "- o valor das correntes,\n"
                "- e a distância entre eles.\n\n"
                "Assim, o fenômeno descoberto por Ørsted deixou de ser apenas uma observação qualitativa "
                "e passou a ser descrito de forma precisa e previsível.\n\n"
                "Esse avanço deu origem a um novo campo da física: a eletrodinâmica, que estuda as interações "
                "entre correntes elétricas e campos magnéticos."
            ),
        },

        {
            "tipo": "equacao",
            "latex": r"\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{enc}"
        },

        # -------------------------------------------------
        # FARADAY MOTOR
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1821 — Michael Faraday (motor elétrico)"},

        {
            "tipo": "texto",
            "texto": (
                "Faraday construiu o primeiro motor elétrico, convertendo energia elétrica em movimento mecânico. "
                "Foi a primeira aplicação prática do eletromagnetismo."
            ),
        },

        # -------------------------------------------------
        # FARADAY INDUÇÃO
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1831 — Faraday e Joseph Henry (indução)"},

        {
            "tipo": "texto",
            "texto": (
                "Faraday e Joseph Henry descobriram a indução eletromagnética: um campo magnético variável "
                "gera corrente elétrica. Esse fenômeno é o inverso do observado por Ørsted. "
                "Com isso, foi possível criar os primeiros geradores elétricos, convertendo movimento em eletricidade."
            ),
        },

        # -------------------------------------------------
        # JACOBI
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1839 — Moritz von Jacobi"},

        {
            "tipo": "texto",
            "texto": (
                "Jacobi desenvolveu o primeiro motor elétrico giratório prático, capaz de realizar trabalho contínuo. "
                "Esse avanço marcou a transição da teoria para aplicações reais."
            ),
        },

        # -------------------------------------------------
        # DAVIDSON
        # -------------------------------------------------
        {"tipo": "subtitulo", "texto": "1842 — Robert Davidson"},

        {
            "tipo": "texto",
            "texto": (
                "Davidson construiu uma locomotiva movida a motor elétrico, demonstrando o uso do eletromagnetismo "
                "no transporte e na engenharia aplicada."
            ),
        },

        # -------------------------------------------------
        # SÍNTESE
        # -------------------------------------------------
        {"tipo": "titulo", "texto": "Consolidação do conceito"},

        {
            "tipo": "texto",
            "texto": (
                "O eletromagnetismo se baseia em duas relações fundamentais: correntes elétricas geram campos magnéticos "
                "e campos magnéticos variáveis geram correntes elétricas. "
 
                "Essas duas ideias formam a base de dispositivos como motores, geradores e transformadores, "
                "sendo essenciais para toda a engenharia elétrica moderna."
            ),
        },

        # -------------------------------------------------
        # QUESTÃO
        # -------------------------------------------------
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.001.0001",
            "pergunta": (
                "A descoberta de Ørsted (1820) e a descoberta da indução eletromagnética por Faraday e Henry (1831) "
                "são consideradas fenômenos inversos entre si. Isso significa que:"
            ),
            "alternativas": {
                "a": "Ørsted usou ímãs para gerar corrente, enquanto Faraday usou corrente para gerar campos magnéticos.",
                "b": "Ørsted mostrou que corrente elétrica gera campo magnético; Faraday mostrou que campo magnético variável gera corrente elétrica.",
                "c": "Ambos os fenômenos geram corrente elétrica, mas em direções opostas.",
                "d": "Ørsted trabalhou com corrente contínua e Faraday com corrente alternada, por isso são inversos.",
                "e": "A descoberta de Ørsted foi teórica, enquanto a de Faraday foi prática, representando o inverso do método científico."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": "⚡ Ørsted: corrente elétrica → campo magnético.\n\n"
            "🔁 Faraday/Henry: campo magnético variável → corrente elétrica. \n\n"
            "Essa relação simétrica é o 'inverso'."
        },

        {"tipo": "imagem", "arquivo": "ampere_01.png"},


        # -------------------------------------------------
        # CONSTRUCAO DE MOTORES ELETRICOS
        # -------------------------------------------------
        {"tipo": "titulo", "texto": "Construção de motores elétricos"},

        {
            "tipo": "texto",
            "texto": (
                "Quando um fio conduzindo corrente elétrica é colocado em um campo magnético, "
                "surge uma força sobre o condutor. Essa força é máxima quando a corrente está "
                "perpendicular às linhas do campo magnético."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Uma espira (volta de fio) entre os polos de um ímã sofre forças em sentidos opostos "
                "em seus lados paralelos: um lado é empurrado para cima, o outro para baixo. "
                "Esse par de forças cria um torque, fazendo a espira girar e convertendo energia "
                "elétrica em energia mecânica."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "Após meia volta (180 graus), a direção da força se inverte naturalmente, fazendo a espira parar. "
                "Em 1832, Hippolyte Pixii resolveu essa limitação ao criar o comutador: um dispositivo que inverte "
                "o sentido da corrente a cada meia volta, mantendo a força magnética sempre no mesmo sentido de rotação."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "No mesmo ano, William Sturgeon desenvolveu o primeiro motor com comutador capaz de mover máquinas. "
                "Em 1837, Thomas Davenport construiu um motor mais potente, atingindo cerca de 600 rotações por minuto, "
                "suficiente para acionar uma prensa de impressão e outras máquinas-ferramenta."
            ),
        },

        {"tipo": "titulo", "texto": "Interpretação física do motor elétrico"},

        {
            "tipo": "texto",
            "texto": (
                "O motor elétrico converte energia elétrica em trabalho mecânico por meio da interação "
                "entre corrente e campo magnético. O comutador garante rotação contínua, tornando o processo eficiente."
            ),
        },

        # -------------------------------------------------
        # QUESTÃO
        # -------------------------------------------------
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.001.0002",
            "pergunta": (
                "Em um motor elétrico simples, a espira para após meia volta (180 graus). "
                "Qual a causa física desse problema e qual invenção o resolveu?"
            ),
            "alternativas": {
                "a": "A causa é o superaquecimento do fio; a solução foi o resfriamento a água criado por Jacobi.",
                "b": "A causa é a inversão natural da direção da força magnética; a solução foi o comutador criado por Hippolyte Pixii.",
                "c": "A causa é a falta de ímãs permanentes; a solução foi o uso de eletroímãs por Sturgeon.",
                "d": "A causa é o desgaste mecânico da espira; a solução foi o uso de rolamentos por Davenport.",
                "e": "A causa é a resistência elétrica do fio; a solução foi o aumento da corrente elétrica."
            },
            "alternativa_correta": "b",
        },
        {"tipo": "titulo", "texto": "Um mundo eletrodinâmico"},

        {
            "tipo": "texto",
            "texto": (
                "Com o avanço da eletrodinâmica, os motores elétricos tornaram-se mais eficientes e potentes. "
                "Três estratégias principais permitiram esse progresso: uso de ímãs mais intensos, aumento da corrente elétrica "
                "e construção de bobinas com maior número de espiras (usando fios mais finos). A redução da distância entre o ímã "
                "e a bobina também intensifica a interação magnética, ampliando a força gerada.\n\n <br>"
                "Atualmente, motores de corrente contínua são comuns em pequenos dispositivos alimentados por pilhas. "
                "Já os motores universais, que utilizam eletroímãs no lugar de ímãs permanentes, são amplamente empregados em eletrodomésticos."
            ),
        },
    

        # -------------------------------------------------
        # QUESTÃO
        # -------------------------------------------------
        {
            "tipo": "questao_texto",
            "id": "solucao.03.001.0003",
            "pergunta": (
                "Com base no texto, explique quais estratégias tornaram os motores elétricos mais eficientes e potentes. "
                "Em seguida, diferencie os motores de corrente contínua dos motores universais quanto às suas aplicações atuais."
            ),
            "altura": 140,
        },

    ]