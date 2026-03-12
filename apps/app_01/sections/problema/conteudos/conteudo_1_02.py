# apps/app_01/sections/problema/conteudos/conteudo_1_02.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "O que é conforto térmico?",
        },
        {
            "tipo": "texto",
            "texto": (
                "O conforto térmico pode ser entendido como a condição em que o corpo humano "
                "não percebe frio nem calor excessivo durante sua permanência em determinado "
                "ambiente. Em termos físicos, isso significa que as trocas de calor entre o corpo "
                "e o meio ocorrem de modo suficientemente equilibrado para que não haja sensação "
                "acentuada de aquecimento ou resfriamento.\n\n"
                "Em uma sala de aula, essa condição é especialmente importante porque influencia "
                "o bem-estar, a permanência e a capacidade de concentração dos ocupantes. "
                "Quando o ambiente apresenta regiões muito quentes ou muito frias, o desconforto "
                "térmico passa a fazer parte da experiência do usuário, mesmo que a temperatura "
                "média da sala pareça aceitável."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=CKbc7PtbTzU",
            "caption": "Introdução ao conceito de conforto térmico em ambientes internos",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_002",
            "pergunta": (
                "Do ponto de vista físico, quando se pode afirmar que existe conforto térmico "
                "em um ambiente interno?"
            ),
            "alternativas": {
                "a": "Quando a temperatura do ambiente é sempre inferior à temperatura externa",
                "b": "Quando o corpo humano troca calor com o ambiente de forma próxima do equilíbrio",
                "c": "Quando todas as superfícies do ambiente apresentam exatamente a mesma temperatura",
                "d": "Quando não existe ventilação no interior da sala",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "O conforto térmico está diretamente relacionado ao balanço de calor entre o corpo "
                "humano e o ambiente. O corpo produz calor continuamente devido ao metabolismo e "
                "precisa dissipar essa energia para o meio ao redor. Quando essa troca ocorre de forma "
                "equilibrada, a sensação térmica tende a ser confortável.\n\n"
                "Esse equilíbrio, no entanto, não depende apenas da temperatura do ar. Ele também está "
                "associado à temperatura das superfícies que cercam o ocupante, como paredes, piso, teto "
                "e janelas. Quando existe diferença entre a temperatura do ar e a temperatura dessas "
                "superfícies, surgem trocas de calor que influenciam a sensação térmica percebida.\n\n"
                "Em um ambiente interno, o calor pode ser transferido por condução, convecção e radiação, "
                "e todos esses processos participam da forma como o corpo percebe o espaço térmico ao seu redor. "
                "Por isso, ao estudar conforto térmico em uma sala, não basta observar apenas um valor médio "
                "de temperatura. É necessário analisar como a temperatura do ar e a temperatura das superfícies "
                "se relacionam e como essa distribuição interfere nas trocas de calor entre o corpo e o ambiente."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_003",
            "pergunta": (
                "Explique, com suas palavras, por que o conforto térmico não depende apenas da "
                "temperatura do ar, mas também da temperatura das superfícies do ambiente e dos "
                "processos de transferência de calor."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]