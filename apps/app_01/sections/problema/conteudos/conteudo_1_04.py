# apps/app_01/sections/problema/conteudos/conteudo_1_04.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Características físicas do ambiente",
        },
        {
            "tipo": "texto",
            "texto": (
                "A análise do conforto térmico de uma sala exige, inicialmente, a observação "
                "de suas características físicas. Dimensões, orientação das paredes, presença "
                "de portas e janelas e materiais que compõem as superfícies internas influenciam "
                "diretamente a forma como o calor é transferido no ambiente. Esses elementos "
                "definem como a radiação solar incide na sala, como o calor atravessa paredes "
                "e aberturas e como o ar interno interage com as superfícies.\n\n"
                "Em uma sala de aula, duas regiões podem apresentar comportamentos térmicos diferentes "
                "mesmo quando pertencem ao mesmo ambiente. Isso acontece porque cada parede, janela "
                "ou abertura pode receber condições térmicas distintas ao longo do dia. Como resultado, "
                "a temperatura das superfícies pode variar de uma região para outra e influenciar a "
                "temperatura do ar próximo a elas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, será importante identificar o tamanho da sala, a posição das "
                "paredes em relação aos pontos cardeais, a existência de portas e janelas e "
                "os materiais predominantes das superfícies. Essas informações permitirão "
                "relacionar a temperatura do ar e a temperatura das superfícies com os mecanismos "
                "de condução, convecção e radiação que atuam no ambiente.\n\n"
                "Assim, a caracterização física da sala não será apenas uma descrição do espaço, "
                "mas uma etapa essencial para compreender por que certas superfícies podem aquecer "
                "ou resfriar mais intensamente e como isso afeta o conforto térmico dos ocupantes."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=owf6D3QhW0M",
        #     "caption": "Elementos físicos do ambiente que influenciam o comportamento térmico de uma edificação",
        # },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_007",
            "pergunta": (
                "Qual característica física do ambiente está mais diretamente relacionada "
                "à diferença de incidência solar entre as paredes da sala?"
            ),
            "alternativas": {
                "a": "A cor das carteiras",
                "b": "A orientação das paredes em relação aos pontos cardeais",
                "c": "A quantidade de alunos presentes na sala",
                "d": "O formato do quadro da sala",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A orientação das paredes em relação aos pontos cardeais é um fator decisivo "
                "porque define como cada superfície recebe radiação solar ao longo do dia. "
                "Além disso, os materiais das paredes, piso, teto, portas e janelas possuem "
                "propriedades térmicas diferentes, o que altera a forma como absorvem, armazenam "
                "e transferem calor. Por essa razão, a caracterização física da sala não é apenas "
                "uma descrição arquitetônica, mas parte essencial da interpretação física do sistema térmico."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_008",
            "pergunta": (
                "Explique, com suas palavras, por que as dimensões da sala, a orientação das paredes "
                "e os materiais das superfícies são importantes para compreender a relação entre "
                "a temperatura do ar e a temperatura das superfícies no ambiente."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]