# apps/app_01/sections/problema/conteudos/conteudo_1_01.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Situação do ambiente",
        },
        {
            "tipo": "texto",
            "texto": (
                "O problema analisado nesta etapa está relacionado ao conforto térmico em uma sala "
                "utilizada para permanência de pessoas ao longo das atividades acadêmicas. Em situações "
                "desse tipo, os ocupantes podem perceber que determinadas regiões do ambiente parecem "
                "mais quentes ou mais frias do que outras, mesmo quando todos estão inseridos na mesma sala. "
                "Essa percepção indica que o ambiente pode não apresentar um comportamento térmico uniforme."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Do ponto de vista físico, a sala deve ser compreendida como um sistema térmico no qual "
                "ocorrem trocas de calor entre o ar interno, as superfícies que delimitam o ambiente "
                "(paredes, piso, teto, portas e janelas) e as fontes externas de energia, como a radiação solar. "
                "Por isso, a análise do problema não depende apenas da temperatura do ar, mas também da "
                "temperatura das superfícies. Quando a temperatura de uma parede é diferente da temperatura "
                "do ar próximo a ela, podem ocorrer trocas de calor que influenciam a sensação térmica "
                "dos ocupantes."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, a sala será investigada como um ambiente em que a temperatura do ar e a "
                "temperatura das superfícies precisam ser observadas, comparadas e interpretadas em conjunto. "
                "O objetivo inicial não é ainda propor uma solução, mas compreender a situação do ambiente, "
                "reconhecer a existência de desuniformidade térmica e entender por que esse fenômeno constitui "
                "um problema físico relevante para a análise do conforto térmico."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=CKbc7PtbTzU",
        #     "caption": "Exemplo introdutório sobre trocas de calor e comportamento térmico em ambientes internos.",
        # },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_001",
            "pergunta": (
                "Ao observar que diferentes regiões da sala apresentam sensações térmicas distintas, "
                "qual é a interpretação física mais adequada para essa situação?"
            ),
            "alternativas": {
                "a": "A sala apresenta temperatura perfeitamente uniforme em todos os pontos.",
                "b": "O ambiente pode apresentar diferenças entre a temperatura do ar e das superfícies, gerando trocas de calor locais.",
                "c": "A sensação térmica depende apenas da quantidade de pessoas presentes na sala.",
                "d": "As superfícies do ambiente não influenciam o comportamento térmico interno.",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando uma sala apresenta regiões com diferentes sensações térmicas, isso sugere que o "
                "ambiente não está em equilíbrio térmico uniforme. Em termos físicos, podem existir "
                "diferenças entre a temperatura do ar e a temperatura das superfícies, o que favorece "
                "trocas de calor por condução, convecção e radiação. Reconhecer essas diferenças é o "
                "primeiro passo para transformar a percepção de desconforto em um problema de análise científica."
            ),
        },
    ]
