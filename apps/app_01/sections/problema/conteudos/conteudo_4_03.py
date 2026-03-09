from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Saídas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após identificar as entradas térmicas do sistema e compreender os processos "
                "físicos envolvidos na transferência de calor, é possível observar os resultados "
                "térmicos que aparecem no ambiente. Esses resultados correspondem às saídas do "
                "sistema térmico analisado.\n\n"
                "No contexto deste estudo, as principais saídas do sistema são as temperaturas "
                "medidas em diferentes pontos da sala, o campo de temperatura do ambiente e "
                "os gradientes térmicos que surgem a partir da distribuição espacial dessas "
                "temperaturas."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Temperatura do ar em cada ponto da sala",
        },
        {
            "tipo": "texto",
            "texto": (
                "A primeira saída do sistema corresponde à temperatura do ar medida nos "
                "diferentes pontos de observação da sala. Ao registrar essas medições em "
                "posições distribuídas no ambiente, torna-se possível identificar como "
                "a temperatura varia ao longo do espaço.\n\n"
                "Esses valores representam dados experimentais fundamentais para a análise "
                "térmica, pois permitem comparar diferentes regiões do ambiente e identificar "
                "possíveis zonas mais quentes ou mais frias dentro da sala."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_036",
            "pergunta": (
                "Qual é a função de medir a temperatura do ar em vários pontos da sala?"
            ),
            "alternativas": {
                "a": "Determinar apenas a temperatura média do ambiente",
                "b": "Observar como a temperatura se distribui em diferentes regiões da sala",
                "c": "Medir exclusivamente a temperatura externa",
                "d": "Eliminar a influência das superfícies no ambiente",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Campo de temperatura do ambiente",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando as temperaturas medidas em diferentes pontos da sala são analisadas "
                "em conjunto, é possível construir uma representação espacial conhecida como "
                "campo de temperatura do ambiente.\n\n"
                "Esse campo descreve como o calor está distribuído no interior da sala e "
                "permite visualizar regiões com diferentes níveis de aquecimento. Em muitas "
                "situações, essa representação pode ser apresentada por meio de mapas térmicos "
                "ou gráficos de distribuição de temperatura."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_037",
            "pergunta": (
                "O que representa o campo de temperatura de um ambiente?"
            ),
            "alternativas": {
                "a": "A temperatura externa do edifício",
                "b": "A distribuição espacial da temperatura no ambiente",
                "c": "A ventilação do espaço",
                "d": "A quantidade de radiação solar recebida",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Gradiente térmico interno",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando existem diferenças de temperatura entre regiões do ambiente, "
                "forma-se um gradiente térmico. Esse gradiente representa a variação "
                "da temperatura entre diferentes pontos da sala.\n\n"
                "Gradientes térmicos indicam que o calor não está distribuído de forma "
                "uniforme no espaço. Quanto maior a diferença de temperatura entre duas "
                "regiões, maior tende a ser o fluxo de calor entre elas."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_038",
            "pergunta": (
                "O que indica a existência de um gradiente térmico em um ambiente?"
            ),
            "alternativas": {
                "a": "Que todas as regiões possuem a mesma temperatura",
                "b": "Que existem diferenças de temperatura entre pontos do espaço",
                "c": "Que o ambiente está completamente isolado",
                "d": "Que não existem trocas de calor",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "A análise das saídas do sistema — temperaturas locais, campo térmico "
                "e gradientes de temperatura — permite interpretar como o calor está "
                "distribuído no ambiente. Essas informações são fundamentais para avaliar "
                "se o comportamento térmico da sala está associado a condições adequadas "
                "ou inadequadas de conforto térmico para os ocupantes."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_039",
            "pergunta": (
                "Qual conjunto representa corretamente as principais saídas do sistema térmico analisado?"
            ),
            "alternativas": {
                "a": "Temperatura externa, radiação solar e ventilação",
                "b": "Temperatura do ar em diferentes pontos, campo térmico e gradiente térmico",
                "c": "Quantidade de alunos e iluminação da sala",
                "d": "Altura da sala e posição das carteiras",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "q_040",
            "pergunta": (
                "Explique, com suas palavras, como as medições de temperatura em diferentes "
                "pontos da sala podem ser usadas para construir o campo térmico do ambiente "
                "e identificar gradientes de temperatura."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]