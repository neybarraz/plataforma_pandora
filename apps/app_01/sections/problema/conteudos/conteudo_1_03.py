# apps/app_01/sections/problema/conteudos/conteudo_1_03.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Objetivo da análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo desta análise é investigar como a distribuição de temperatura "
                "no interior da sala influencia as condições de conforto térmico dos ocupantes. "
                "Para isso, a sala será tratada como um sistema térmico no qual o ar, as "
                "superfícies internas e as condições externas interagem continuamente por meio "
                "de trocas de calor.\n\n"
                "A análise não se limita a identificar um valor médio de temperatura. O foco "
                "está em compreender como diferentes regiões do ambiente podem apresentar "
                "comportamentos térmicos distintos e como a temperatura do ar se relaciona com "
                "a temperatura das superfícies do ambiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesse contexto, o estudo busca construir uma leitura física do ambiente a "
                "partir de medições distribuídas na sala, permitindo comparar a temperatura "
                "do ar e a temperatura das superfícies em diferentes pontos do espaço. "
                "Diferenças entre essas temperaturas indicam a existência de trocas de calor "
                "entre o ar e as superfícies, o que pode influenciar diretamente a sensação "
                "térmica percebida pelos ocupantes.\n\n"
                "Ao final, pretende-se avaliar se a distribuição térmica observada é compatível "
                "com uma condição adequada de conforto térmico e identificar possíveis regiões "
                "críticas de desconforto."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=DzJCgSx6V-M",
            "caption": "Introdução à análise de conforto térmico em ambientes internos.",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_005",
            "pergunta": (
                "Qual é o objetivo principal da análise de conforto térmico proposta para a sala?"
            ),
            "alternativas": {
                "a": "Determinar apenas a temperatura média do ambiente, sem considerar sua distribuição espacial",
                "b": "Investigar como a distribuição de temperatura no ambiente influencia o conforto térmico dos ocupantes",
                "c": "Medir exclusivamente a temperatura externa para estimar o desempenho térmico da sala",
                "d": "Avaliar somente os materiais das paredes, sem relacioná-los ao comportamento térmico do ambiente",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A análise do conforto térmico exige observar o ambiente de forma espacial. "
                "Isso significa que não basta conhecer um único valor de temperatura; é "
                "necessário compreender como ela se distribui no interior da sala e como se "
                "relaciona com a temperatura das superfícies do ambiente.\n\n"
                "Quando há diferenças entre a temperatura do ar e a temperatura das superfícies, "
                "ocorrem trocas de calor que podem alterar a sensação térmica dos ocupantes. "
                "Assim, a interpretação do conforto térmico depende da análise conjunta dessas "
                "variáveis e dos mecanismos de transferência de calor envolvidos."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_006",
            "pergunta": (
                "Explique, com suas palavras, por que a análise do conforto térmico não deve "
                "considerar apenas a temperatura média da sala, mas também a relação entre "
                "a temperatura do ar e a temperatura das superfícies do ambiente."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]