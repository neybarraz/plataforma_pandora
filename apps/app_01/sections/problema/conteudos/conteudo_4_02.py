from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Processos físicos do sistema térmico",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após identificar as entradas térmicas do sistema, é necessário compreender "
                "quais processos físicos explicam como o calor se movimenta no interior da sala. "
                "Esses processos descrevem os mecanismos de transferência de calor que conectam "
                "o ambiente externo, as superfícies da sala e o ar interno.\n\n"
                "No contexto deste estudo, quatro processos físicos principais são considerados: "
                "a condução térmica nas paredes, a convecção entre o ar e as superfícies, as "
                "trocas de calor por radiação entre superfícies e a mistura térmica do ar "
                "no interior da sala."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Condução térmica nas paredes",
        },
        {
            "tipo": "texto",
            "texto": (
                "A condução térmica ocorre quando o calor se transfere através de um material "
                "devido à diferença de temperatura entre duas regiões. Nas paredes de uma "
                "edificação, esse processo pode transportar calor do ambiente externo para "
                "o interior da sala ou no sentido contrário.\n\n"
                "Quando uma face da parede está mais quente que a outra, o calor tende a "
                "se deslocar através do material até que as temperaturas se aproximem. "
                "Esse processo contribui para alterar a temperatura das superfícies internas "
                "e, consequentemente, influencia o comportamento térmico do ar dentro da sala."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_030",
            "pergunta": (
                "O que caracteriza o processo de condução térmica em uma parede?"
            ),
            "alternativas": {
                "a": "Transferência de calor através do material devido a uma diferença de temperatura",
                "b": "Movimento do ar no interior da sala",
                "c": "Transferência de calor apenas pela radiação solar",
                "d": "Mistura do ar causada por ventilação",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "titulo",
            "texto": "Convecção entre o ar interno e as superfícies",
        },
        {
            "tipo": "texto",
            "texto": (
                "A convecção ocorre quando o calor é transferido entre uma superfície "
                "e um fluido em movimento, como o ar. No interior de uma sala, o ar pode "
                "trocar calor continuamente com paredes, piso, teto e objetos presentes "
                "no ambiente.\n\n"
                "Quando uma superfície está mais quente que o ar ao seu redor, ela tende "
                "a aquecer o ar próximo. Por outro lado, se estiver mais fria, pode retirar "
                "calor do ar. Esse processo contribui para modificar a temperatura do ar "
                "em diferentes regiões da sala."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_031",
            "pergunta": (
                "Em qual situação ocorre convecção térmica entre uma parede e o ar da sala?"
            ),
            "alternativas": {
                "a": "Quando existe troca de calor entre a superfície e o ar ao seu redor",
                "b": "Quando não há diferença de temperatura entre ar e parede",
                "c": "Quando apenas a radiação solar está presente",
                "d": "Quando o ar permanece completamente parado e isolado",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "titulo",
            "texto": "Trocas de calor por radiação entre superfícies",
        },
        {
            "tipo": "texto",
            "texto": (
                "A radiação térmica é o processo pelo qual o calor é transferido por meio "
                "de ondas eletromagnéticas. Diferentemente da condução e da convecção, esse "
                "processo não necessita de contato direto entre os corpos.\n\n"
                "Dentro de uma sala, as superfícies trocam energia térmica entre si por "
                "radiação. Uma parede aquecida pela radiação solar, por exemplo, pode "
                "emitir energia para outras superfícies do ambiente, contribuindo para "
                "o aquecimento do espaço."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_032",
            "pergunta": (
                "Qual característica distingue a transferência de calor por radiação?"
            ),
            "alternativas": {
                "a": "O calor se transfere apenas através de materiais sólidos",
                "b": "A transferência ocorre por contato direto entre superfícies",
                "c": "O calor pode ser transferido por ondas eletromagnéticas sem contato direto",
                "d": "O processo depende exclusivamente da circulação do ar",
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "titulo",
            "texto": "Mistura e redistribuição térmica do ar interno",
        },
        {
            "tipo": "texto",
            "texto": (
                "Além das trocas de calor entre superfícies e ar, o próprio movimento do ar "
                "no interior da sala contribui para redistribuir o calor no ambiente. "
                "Esse processo ocorre devido à circulação natural do ar ou à ventilação "
                "presente no espaço.\n\n"
                "Quando o ar se movimenta, ele transporta energia térmica de uma região "
                "para outra, podendo reduzir ou intensificar diferenças de temperatura "
                "entre diferentes partes da sala."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_033",
            "pergunta": (
                "Qual é o principal efeito da movimentação do ar no interior da sala?"
            ),
            "alternativas": {
                "a": "Eliminar completamente as trocas de calor",
                "b": "Transportar e redistribuir energia térmica no ambiente",
                "c": "Impedir a radiação térmica entre superfícies",
                "d": "Alterar apenas a iluminação da sala",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "Os processos físicos descritos — condução, convecção, radiação e mistura "
                "do ar — atuam simultaneamente no interior da sala. O comportamento térmico "
                "observado no ambiente resulta da interação entre esses mecanismos de "
                "transferência de calor e das condições térmicas presentes no sistema."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_034",
            "pergunta": (
                "Quais processos físicos explicam a transferência de calor no ambiente analisado?"
            ),
            "alternativas": {
                "a": "Condução, convecção, radiação e mistura do ar",
                "b": "Apenas condução térmica",
                "c": "Somente radiação solar",
                "d": "Somente circulação de ar",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_texto",
            "id": "q_035",
            "pergunta": (
                "Explique, com suas palavras, como os processos de condução, convecção, "
                "radiação e movimentação do ar atuam juntos para determinar o comportamento "
                "térmico da sala."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]