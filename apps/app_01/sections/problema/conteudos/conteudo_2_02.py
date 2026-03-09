from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Foco de análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após identificar a tensão central do problema, é necessário definir com mais "
                "clareza qual será o foco da análise térmica. Nesta etapa, o estudo concentra-se "
                "na forma como a temperatura se distribui dentro da sala e como essa distribuição "
                "influencia as trocas de calor entre o ar, as superfícies e os ocupantes.\n\n"
                "A análise será organizada a partir de quatro aspectos principais: a distribuição "
                "espacial da temperatura do ar, o gradiente térmico no ambiente, a diferença entre "
                "a temperatura do ar e a temperatura das superfícies e, por fim, a relação entre "
                "o campo térmico do ambiente e o conforto térmico percebido pelas pessoas."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Distribuição espacial da temperatura do ar",
        },
        {
            "tipo": "texto",
            "texto": (
                "A temperatura do ar em uma sala não é necessariamente a mesma em todos os pontos "
                "do ambiente. Fatores como incidência de radiação solar, proximidade de paredes "
                "aquecidas, circulação do ar e presença de aberturas podem gerar diferenças "
                "térmicas entre regiões da sala.\n\n"
                "Por essa razão, a análise do conforto térmico exige observar a distribuição "
                "espacial da temperatura do ar. Ao medir a temperatura em diferentes posições, "
                "torna-se possível identificar regiões mais quentes e regiões mais frias dentro "
                "do mesmo ambiente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_015",
            "pergunta": (
                "Por que é importante medir a temperatura do ar em diferentes pontos da sala?"
            ),
            "alternativas": {
                "a": "Porque a temperatura do ar é sempre uniforme em todos os pontos",
                "b": "Porque diferentes regiões da sala podem apresentar temperaturas distintas",
                "c": "Porque a temperatura depende apenas da quantidade de pessoas presentes",
                "d": "Porque apenas a temperatura externa influencia o ambiente interno",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Gradiente térmico no ambiente",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a temperatura varia entre diferentes regiões do ambiente, forma-se um "
                "gradiente térmico. Esse gradiente representa a variação espacial da temperatura "
                "no interior da sala.\n\n"
                "Gradientes térmicos indicam que o calor não está distribuído de maneira uniforme. "
                "Em alguns pontos o ambiente pode estar mais aquecido, enquanto em outros pode "
                "estar mais frio. Essa variação influencia a forma como o calor se movimenta e "
                "como as pessoas percebem o conforto térmico no espaço."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_016",
            "pergunta": (
                "O que indica a existência de um gradiente térmico em uma sala?"
            ),
            "alternativas": {
                "a": "Que todas as regiões apresentam exatamente a mesma temperatura",
                "b": "Que existem diferenças de temperatura entre pontos do ambiente",
                "c": "Que a temperatura externa é maior que a interna",
                "d": "Que não existem trocas de calor no ambiente",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Diferença entre temperatura do ar e temperatura das superfícies",
        },
        {
            "tipo": "texto",
            "texto": (
                "Outro aspecto importante da análise é a comparação entre a temperatura do ar "
                "e a temperatura das superfícies do ambiente. Paredes, piso, teto e janelas "
                "podem apresentar temperaturas diferentes do ar ao seu redor.\n\n"
                "Quando essa diferença existe, surgem trocas de calor entre o ar e as superfícies. "
                "Se a superfície estiver mais quente que o ar, ela tende a transferir calor para "
                "o ambiente. Se estiver mais fria, tende a receber calor do ar. Essas interações "
                "contribuem para modificar a temperatura local e influenciam o comportamento "
                "térmico da sala."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_017",
            "pergunta": (
                "O que pode ocorrer quando a temperatura de uma parede é maior que a temperatura do ar próximo a ela?"
            ),
            "alternativas": {
                "a": "A parede tende a transferir calor para o ar",
                "b": "O ar transfere calor para a parede",
                "c": "Não ocorre nenhuma troca de calor",
                "d": "A temperatura do ar passa a ser igual à externa",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "titulo",
            "texto": "Campo térmico e conforto térmico",
        },
        {
            "tipo": "texto",
            "texto": (
                "O conjunto das temperaturas observadas no ambiente forma o chamado campo térmico "
                "da sala. Esse campo representa como o calor se distribui no espaço e permite "
                "identificar regiões com diferentes comportamentos térmicos.\n\n"
                "A relação entre esse campo térmico e o conforto térmico é direta. Ambientes em "
                "que a temperatura se distribui de maneira mais uniforme tendem a proporcionar "
                "maior conforto para os ocupantes. Por outro lado, quando existem gradientes "
                "térmicos acentuados ou superfícies muito aquecidas ou muito frias, podem surgir "
                "regiões de desconforto dentro da sala."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_018",
            "pergunta": (
                "Como o campo térmico de um ambiente pode influenciar o conforto térmico?"
            ),
            "alternativas": {
                "a": "Ambientes com distribuição térmica mais uniforme tendem a proporcionar maior conforto",
                "b": "O conforto térmico depende apenas da temperatura externa",
                "c": "O campo térmico não tem relação com a sensação térmica das pessoas",
                "d": "O conforto depende apenas da ventilação",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_texto",
            "id": "q_019",
            "pergunta": (
                "Explique, com suas palavras, como a distribuição da temperatura do ar e "
                "a diferença entre temperaturas do ar e das superfícies podem influenciar "
                "o conforto térmico em uma sala."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]