from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Entradas térmicas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para compreender o comportamento térmico da sala, é necessário identificar "
                "quais fatores externos e internos influenciam a temperatura do ambiente. "
                "Esses fatores são chamados de entradas térmicas do sistema, pois representam "
                "as condições que alimentam o comportamento térmico da sala.\n\n"
                "No contexto deste estudo, quatro entradas térmicas principais serão "
                "consideradas: a temperatura externa, a radiação solar incidente, a "
                "temperatura das superfícies do ambiente e as condições de ventilação."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Temperatura externa",
        },
        {
            "tipo": "texto",
            "texto": (
                "A temperatura externa influencia diretamente o comportamento térmico de "
                "um ambiente interno. Quando a temperatura do exterior é elevada, parte "
                "desse calor pode ser transferida para o interior por meio das paredes, "
                "janelas e demais superfícies da edificação.\n\n"
                "Assim, a temperatura externa funciona como uma condição de contorno "
                "do sistema térmico da sala, afetando a quantidade de calor que pode "
                "entrar ou sair do ambiente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_024",
            "pergunta": (
                "De que forma a temperatura externa pode influenciar o comportamento térmico da sala?"
            ),
            "alternativas": {
                "a": "Não exerce nenhuma influência sobre o ambiente interno",
                "b": "Pode influenciar as trocas de calor através das superfícies da sala",
                "c": "Afeta apenas a iluminação do ambiente",
                "d": "Altera apenas a circulação de pessoas no espaço",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Radiação solar incidente",
        },
        {
            "tipo": "texto",
            "texto": (
                "A radiação solar é uma das principais fontes de energia térmica em "
                "ambientes internos. Quando a luz solar incide sobre paredes, janelas "
                "ou outras superfícies da sala, parte dessa energia é absorvida e "
                "convertida em calor.\n\n"
                "Esse aquecimento pode elevar a temperatura das superfícies e, "
                "posteriormente, influenciar a temperatura do ar interno por meio "
                "das trocas de calor entre as superfícies e o ambiente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_025",
            "pergunta": (
                "Qual é o principal efeito da radiação solar sobre as superfícies da sala?"
            ),
            "alternativas": {
                "a": "Reduz a temperatura das paredes",
                "b": "Aumenta a temperatura das superfícies ao fornecer energia térmica",
                "c": "Elimina as trocas de calor no ambiente",
                "d": "Afeta apenas a iluminação do espaço",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Temperatura das superfícies",
        },
        {
            "tipo": "texto",
            "texto": (
                "As superfícies do ambiente, como paredes, piso e teto, possuem "
                "temperaturas próprias que podem ser diferentes da temperatura do "
                "ar interno. Essas superfícies podem absorver calor da radiação solar, "
                "trocar calor com o ambiente externo e interagir termicamente com o ar "
                "presente na sala.\n\n"
                "Quando a temperatura de uma superfície é diferente da temperatura "
                "do ar ao seu redor, ocorre transferência de calor entre esses dois "
                "elementos, influenciando o comportamento térmico local."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_026",
            "pergunta": (
                "Por que a temperatura das superfícies é importante para a análise térmica da sala?"
            ),
            "alternativas": {
                "a": "Porque as superfícies não participam das trocas de calor",
                "b": "Porque elas podem trocar calor com o ar e influenciar o ambiente",
                "c": "Porque apenas determinam a cor do ambiente",
                "d": "Porque afetam apenas a ventilação da sala",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Condições de ventilação",
        },
        {
            "tipo": "texto",
            "texto": (
                "A ventilação influencia a forma como o ar se movimenta no interior "
                "da sala. Quando existe circulação de ar, o calor pode ser redistribuído "
                "entre diferentes regiões do ambiente.\n\n"
                "Esse movimento pode reduzir diferenças de temperatura ou transportar "
                "ar aquecido ou resfriado de uma região para outra, afetando o campo "
                "térmico da sala e a sensação térmica dos ocupantes."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_027",
            "pergunta": (
                "Qual é o papel da ventilação no comportamento térmico do ambiente?"
            ),
            "alternativas": {
                "a": "Eliminar completamente as trocas de calor",
                "b": "Redistribuir o calor por meio da movimentação do ar",
                "c": "Alterar apenas a iluminação da sala",
                "d": "Impedir que o ar se movimente no ambiente",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "As entradas térmicas identificadas — temperatura externa, radiação solar, "
                "temperatura das superfícies e ventilação — constituem os fatores que "
                "influenciam o comportamento térmico da sala. Ao analisar essas variáveis "
                "em conjunto, torna-se possível compreender como o calor entra, se "
                "distribui e se transforma dentro do ambiente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_028",
            "pergunta": (
                "Qual conjunto representa corretamente as entradas térmicas consideradas na análise?"
            ),
            "alternativas": {
                "a": "Temperatura externa, radiação solar, temperatura das superfícies e ventilação",
                "b": "Número de alunos, cor das paredes e iluminação artificial",
                "c": "Altura da sala e posição das carteiras",
                "d": "Quantidade de equipamentos eletrônicos apenas",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_texto",
            "id": "q_029",
            "pergunta": (
                "Explique, com suas palavras, como as entradas térmicas do sistema "
                "(temperatura externa, radiação solar, superfícies e ventilação) "
                "podem influenciar o comportamento térmico da sala."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]