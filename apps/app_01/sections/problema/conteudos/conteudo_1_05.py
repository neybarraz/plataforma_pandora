# apps/app_01/sections/problema/conteudos/conteudo_1_05.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Condições térmicas observadas",
        },
        {
            "tipo": "texto",
            "texto": (
                "As condições térmicas observadas em uma sala de aula correspondem ao conjunto "
                "de características físicas que descrevem como a temperatura se manifesta no "
                "ambiente em um determinado instante. Nesse contexto, dois aspectos são "
                "especialmente importantes: a temperatura do ar interno e a temperatura das "
                "superfícies que delimitam a sala, como paredes, piso, teto, portas e janelas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Mesmo quando a temperatura média do ambiente parece adequada, podem existir "
                "diferenças entre a temperatura do ar e a temperatura das superfícies em "
                "diferentes regiões da sala. Essas diferenças podem ser provocadas, por exemplo, "
                "pela incidência de radiação solar em uma parede, pela proximidade de janelas, "
                "pelo aquecimento desigual das superfícies ou pela circulação não uniforme do ar. "
                "Por isso, a observação das condições térmicas não deve se limitar a um único "
                "valor de temperatura, mas considerar a relação entre o ar e as superfícies "
                "do ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, será importante identificar quais regiões da sala apresentam "
                "maiores temperaturas do ar, quais superfícies podem estar mais aquecidas ou "
                "mais resfriadas e de que maneira a radiação solar influencia esse comportamento. "
                "Quando a temperatura de uma superfície é maior que a do ar, ela tende a transferir "
                "calor para o ambiente; quando é menor, tende a receber calor do ar. Essa análise "
                "ajudará a compreender por que determinadas áreas podem produzir maior sensação "
                "de desconforto térmico para os ocupantes."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=0Hu0KmdraD0",
        #     "caption": "Calor se movimentando.",
        # },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_006",
            "pergunta": (
                "Por que a observação das condições térmicas de uma sala não deve se basear "
                "apenas em um único valor de temperatura do ar?"
            ),
            "alternativas": {
                "a": "Porque a temperatura do ar não sofre influência das superfícies do ambiente",
                "b": "Porque o conforto térmico depende apenas da ventilação natural",
                "c": "Porque diferentes regiões da sala podem apresentar diferenças entre a temperatura do ar e a temperatura das superfícies devido à radiação solar e às trocas de calor",
                "d": "Porque a temperatura do ar é sempre igual à temperatura das paredes",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "texto",
            "texto": (
                "A análise térmica de um ambiente interno exige considerar a interação entre o "
                "ar e as superfícies. Paredes aquecidas pela radiação solar, por exemplo, podem "
                "transferir calor para o ar e modificar a temperatura em regiões próximas. Da "
                "mesma forma, superfícies mais frias podem receber calor do ar e reduzir a "
                "temperatura local. Assim, as condições térmicas observadas resultam de um sistema "
                "de trocas de calor que produz diferenças entre temperaturas do ar e das superfícies "
                "e, consequentemente, diferentes condições de conforto térmico dentro da mesma sala."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_007",
            "pergunta": (
                "Explique, com suas palavras, como a comparação entre a temperatura do ar, a "
                "temperatura das superfícies e a influência da radiação solar ajuda a entender "
                "a formação de regiões mais quentes e mais frias dentro da sala."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]