from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Condições físicas da instalação",
        },
        {
            "tipo": "texto",
            "texto": (
                "Além das características do motor e da alimentação elétrica, o "
                "dimensionamento de um circuito também depende das condições físicas "
                "da instalação. Elementos como o método de instalação dos condutores, "
                "a temperatura ambiente e o comprimento total do circuito podem "
                "influenciar diretamente o comportamento elétrico do sistema.\n\n"
                "Ao analisar o sistema de bombeamento, é importante observar como "
                "os cabos estão instalados, em que ambiente operam e qual é a "
                "distância total percorrida pelo circuito até o motor. Essas "
                "condições determinam como o calor gerado pela corrente elétrica "
                "é dissipado e influenciam diretamente a capacidade de condução "
                "dos cabos."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_016",
            "pergunta": (
                "Qual fator físico da instalação influencia diretamente o "
                "dimensionamento dos condutores elétricos?"
            ),
            "alternativas": {
                "a": "A cor da parede onde passa o eletroduto",
                "b": "O método de instalação e a temperatura ambiente",
                "c": "O nome do operador do sistema",
                "d": "A idade do reservatório",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "As condições físicas da instalação influenciam a capacidade de "
                "condução de corrente dos condutores e também o comportamento "
                "da queda de tensão ao longo do circuito. Ambientes com maior "
                "temperatura podem reduzir a capacidade de dissipação de calor "
                "dos cabos, enquanto circuitos mais longos tendem a apresentar "
                "maior queda de tensão.\n\n"
                "Outro fator importante é o método de instalação. Cabos instalados "
                "em eletrodutos, bandejas ou embutidos em paredes possuem condições "
                "diferentes de ventilação e dissipação térmica. Por essa razão, "
                "ao analisar um sistema elétrico real, é fundamental considerar "
                "não apenas os equipamentos conectados, mas também como os "
                "condutores estão instalados."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=yV9_Rt-ML4g",
            "caption": "Exemplo de instalação de condutores em eletrodutos",
        },
        {
            "tipo": "texto",
            "texto": (
                "Observe no vídeo como os condutores elétricos podem ser instalados "
                "em eletrodutos. Esse tipo de instalação é muito comum em sistemas "
                "prediais e industriais, pois protege os cabos e organiza o trajeto "
                "dos circuitos.\n\n"
                "Ao analisar um circuito real, é importante identificar o método "
                "de instalação utilizado, pois ele influencia diretamente a forma "
                "como o calor gerado pela corrente elétrica é dissipado."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_017",
            "pergunta": (
                "Qual é a principal função do eletroduto em uma instalação elétrica?"
            ),
            "alternativas": {
                "a": "Aumentar a potência do motor",
                "b": "Proteger e organizar o trajeto dos condutores elétricos",
                "c": "Reduzir o consumo de energia do motor",
                "d": "Substituir os dispositivos de proteção do circuito",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_texto",
            "id": "q_018",
            "pergunta": (
                "Explique, com suas palavras, como o método de instalação dos "
                "condutores (por exemplo, em eletrodutos), a temperatura ambiente "
                "e o comprimento do circuito podem influenciar o dimensionamento "
                "elétrico da alimentação do motor."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]