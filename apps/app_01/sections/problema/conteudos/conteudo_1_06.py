from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Sistema de medição",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para analisar o conforto térmico da sala, é necessário definir um sistema de medição "
                "capaz de registrar tanto a temperatura do ar quanto a temperatura das superfícies do "
                "ambiente. Nesse estudo, a sala é observada como um sistema térmico no qual o ar interno "
                "e as paredes trocam calor continuamente. Por isso, a medição não deve se limitar ao ar, "
                "mas incluir também as superfícies, permitindo comparar essas temperaturas em diferentes "
                "regiões da sala.\n\n"
                "Essa comparação é importante porque, quando a temperatura de uma parede é diferente da "
                "temperatura do ar próximo a ela, podem ocorrer trocas de calor que influenciam o "
                "comportamento térmico local. Assim, o sistema de medição deve permitir observar não "
                "apenas onde o ambiente está mais quente ou mais frio, mas também como o ar e as "
                "superfícies interagem termicamente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste problema, os pontos de medição são identificados como N1, N2, O1, O2, L1, L2, "
                "S1, S2 e C, correspondendo a posições associadas às direções norte, oeste, leste, sul "
                "e ao centro da sala. Em cada região, o objetivo é medir a temperatura do ar e a "
                "temperatura da superfície próxima, de modo a comparar essas grandezas em diferentes "
                "partes do ambiente.\n\n"
                "Além da posição dos sensores, o momento da coleta também é relevante. As medições devem "
                "ser realizadas em um mesmo intervalo de tempo, para que os valores obtidos representem "
                "uma mesma condição térmica do ambiente e possam ser comparados de forma coerente."
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "sala04.png",
            "caption": (
                "Esquema da sala com os pontos de medição de temperatura do ar e das superfícies. "
                "A distribuição dos sensores permite comparar o comportamento térmico em diferentes regiões do ambiente."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=8CwFn2wNQ8Q",
        #     "caption": "Exemplo de medição e comparação entre temperaturas do ar e das superfícies em ambientes internos",
        # },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_011",
            "pergunta": (
                "Qual é a principal finalidade do sistema de medição adotado na análise térmica da sala?"
            ),
            "alternativas": {
                "a": "Determinar apenas a temperatura média do ar no ambiente",
                "b": "Comparar a temperatura do ar e das superfícies em diferentes pontos da sala",
                "c": "Medir exclusivamente a temperatura externa do edifício",
                "d": "Eliminar a influência das superfícies sobre o conforto térmico",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A principal função do sistema de medição é permitir a comparação entre a temperatura "
                "do ar e a temperatura das superfícies em diferentes regiões da sala. Quando essas "
                "temperaturas são diferentes, existe tendência de troca de calor entre o ar e a "
                "superfície. Se a parede estiver mais quente que o ar, ela tende a aquecer o ambiente "
                "próximo; se estiver mais fria, tende a receber calor do ar. Dessa forma, a medição "
                "em vários pontos permite interpretar o comportamento térmico da sala com base nas "
                "interações entre ar e superfícies."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_012",
            "pergunta": (
                "Explique, com suas palavras, por que é importante medir a temperatura do ar e a "
                "temperatura das superfícies em diferentes pontos da sala para analisar o conforto térmico."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]