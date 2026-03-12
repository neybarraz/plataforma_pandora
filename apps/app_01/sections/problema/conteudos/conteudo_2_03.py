from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Delimitação do escopo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após definir o foco da análise térmica, é necessário estabelecer também os "
                "limites do estudo. A delimitação do escopo define quais aspectos do sistema "
                "serão considerados na investigação e quais elementos permanecerão fora da "
                "análise. Essa etapa é importante porque permite concentrar a investigação "
                "nos fenômenos físicos mais relevantes para compreender o comportamento "
                "térmico da sala."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste problema, a análise será realizada considerando a sala em duas dimensões, "
                "observando a distribuição de temperatura ao longo do plano horizontal do "
                "ambiente. Essa simplificação permite representar o comportamento térmico da "
                "sala de forma mais clara, sem a necessidade de analisar variações complexas "
                "ao longo da altura do espaço."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além disso, a investigação considerará apenas duas grandezas térmicas principais: "
                "a temperatura do ar e a temperatura das superfícies do ambiente. A comparação "
                "entre essas duas temperaturas permite interpretar as trocas de calor entre o "
                "ar e as paredes da sala, ajudando a compreender a formação de regiões mais "
                "quentes ou mais frias no espaço."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Por fim, o estudo não levará em conta sistemas ativos de climatização, como "
                "aparelhos de ar-condicionado, ventiladores ou sistemas mecânicos de controle "
                "térmico. Dessa forma, o comportamento térmico observado será interpretado "
                "principalmente a partir das interações naturais entre radiação solar, "
                "superfícies da sala e ar interno."
            ),
        },

        {
            "tipo": "texto",
            "texto": (
                "A delimitação do escopo permite transformar um fenômeno complexo em um problema "
                "de análise viável. Ao restringir o estudo a determinadas variáveis — neste caso, "
                "a temperatura do ar e a temperatura das superfícies — torna-se possível "
                "investigar de forma mais clara como o calor se distribui no ambiente e como "
                "essas condições influenciam o conforto térmico."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "q_013",
            "pergunta": (
                "Explique, com suas palavras, por que a análise térmica deste estudo foi "
                "delimitada considerando apenas duas dimensões da sala e apenas as "
                "temperaturas do ar e das superfícies."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]