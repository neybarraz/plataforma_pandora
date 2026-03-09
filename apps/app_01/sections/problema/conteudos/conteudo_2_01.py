from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Tensão central",
        },
        {
            "tipo": "texto",
            "texto": (
                "A tensão central do problema está na desuniformidade térmica observada no interior "
                "da sala. Em um ambiente destinado à permanência de pessoas, espera-se que as condições "
                "térmicas sejam relativamente estáveis e homogêneas. No entanto, quando diferentes "
                "regiões da sala apresentam comportamentos térmicos distintos, surgem zonas de maior "
                "e menor aquecimento, o que pode comprometer o conforto dos ocupantes."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa desuniformidade não se manifesta apenas pela diferença entre regiões mais quentes "
                "e mais frias do ar. Ela também aparece quando a temperatura das superfícies difere da "
                "temperatura do ar próximo a elas. Nessas condições, passam a ocorrer trocas de calor "
                "entre paredes e ar interno, alterando localmente o comportamento térmico do ambiente. "
                "Assim, a tensão central do problema não está apenas na existência de calor, mas na "
                "maneira desigual como ele se distribui e se transfere dentro da sala."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Do ponto de vista da análise física, reconhecer essa desuniformidade é essencial para "
                "delimitar o problema. O desconforto térmico percebido pelos ocupantes deixa de ser "
                "interpretado como uma sensação subjetiva isolada e passa a ser tratado como resultado "
                "de um sistema térmico em que ar, superfícies e radiação interagem de forma não uniforme. "
                "É exatamente essa diferença espacial de comportamento térmico que constitui a tensão "
                "central a ser investigada."
            ),
        },
        # {
        #     "tipo": "video",
        #     "url": "https://www.youtube.com/watch?v=CKbc7PtbTzU",
        #     "caption": "Exemplo introdutório sobre desuniformidade térmica em ambientes internos.",
        # },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_013",
            "pergunta": (
                "Qual situação representa melhor a tensão central do problema de conforto térmico na sala?"
            ),
            "alternativas": {
                "a": "A sala possui uma única temperatura média e comportamento térmico uniforme em todos os pontos",
                "b": "A desuniformidade térmica do ambiente gera diferenças entre regiões e influencia o conforto dos ocupantes",
                "c": "O problema depende apenas da temperatura externa, sem relação com as superfícies internas",
                "d": "O desconforto térmico ocorre somente quando não existe ventilação natural",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A tensão central do problema está associada à existência de diferenças térmicas no "
                "interior da sala. Quando o ar e as superfícies não apresentam comportamento homogêneo, "
                "o ambiente passa a produzir regiões com condições térmicas distintas. Isso afeta a "
                "forma como o calor é transferido e explica por que o conforto térmico pode variar "
                "de um ponto para outro dentro do mesmo espaço."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_014",
            "pergunta": (
                "Explique, com suas palavras, por que a desuniformidade térmica no interior da sala "
                "pode ser considerada a tensão central do problema de conforto térmico."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]