from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Características da alimentação elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para analisar corretamente o funcionamento elétrico da motobomba, "
                "é necessário compreender como a energia elétrica chega até o motor. "
                "Essa energia é fornecida pela rede elétrica e distribuída através "
                "do quadro de distribuição da instalação.\n\n"
                "Entre as informações mais importantes nesse processo estão a tensão "
                "da rede, o tipo de sistema elétrico utilizado e a distância entre "
                "o ponto de alimentação e o motor. Esses dados permitem relacionar "
                "as características da rede com as informações presentes na placa "
                "do motor."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_012",
            "pergunta": (
                "Qual conjunto de informações é fundamental para caracterizar "
                "a alimentação elétrica do motor da motobomba?"
            ),
            "alternativas": {
                "a": "Somente a marca do cabo utilizado",
                "b": "Tensão da rede, tipo de sistema e distância até o motor",
                "c": "Apenas a altura do reservatório superior",
                "d": "Somente a potência hidráulica da bomba",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A alimentação elétrica do motor não ocorre diretamente a partir "
                "da rede pública. Antes de chegar ao equipamento, a energia passa "
                "por dispositivos de proteção e controle instalados no quadro "
                "de distribuição.\n\n"
                "Nesse quadro encontram-se componentes como disjuntores, "
                "contatores e barramentos de distribuição, responsáveis por "
                "proteger, controlar e distribuir a energia elétrica para os "
                "diferentes circuitos da instalação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Observe a imagem a seguir. Ela mostra um quadro de distribuição "
                "elétrico responsável por alimentar diferentes circuitos da "
                "instalação, incluindo o circuito que pode alimentar o motor "
                "da motobomba."
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "circuito_03.png",
            "caption": "Figura: quadro de distribuição utilizado para alimentar os circuitos da instalação",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=mzEPYQVviZo",
            "caption": "Exemplo visual de alimentação elétrica trifásica em um sistema real",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_013",
            "pergunta": (
                "Ao observar os cabos de alimentação no quadro apresentado, "
                "qual tipo de sistema elétrico parece estar sendo utilizado?"
            ),
            "alternativas": {
                "a": "Sistema monofásico",
                "b": "Sistema bifásico",
                "c": "Sistema trifásico",
                "d": "Sistema de corrente contínua",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_014",
            "pergunta": (
                "Qual é a principal função dos disjuntores presentes no quadro "
                "de distribuição?"
            ),
            "alternativas": {
                "a": "Aumentar a tensão da rede elétrica",
                "b": "Proteger os circuitos contra sobrecorrente e curto-circuito",
                "c": "Controlar o fluxo de água no reservatório",
                "d": "Alterar a frequência da rede elétrica",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_texto",
            "id": "q_015",
            "pergunta": (
                "Observe o quadro de distribuição apresentado na imagem e "
                "explique, com suas palavras, por que o conhecimento da "
                "tensão da rede, do tipo de sistema elétrico e da distância "
                "até o motor são informações importantes para analisar a "
                "alimentação elétrica da motobomba."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]