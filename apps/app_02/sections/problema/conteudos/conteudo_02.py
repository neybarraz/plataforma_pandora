from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Características da motobomba e dados de placa",
        },
        {
            "tipo": "texto",
            "texto": (
                "O motor elétrico que aciona a motobomba possui uma placa de identificação "
                "onde estão registradas as principais características elétricas do equipamento. "
                "Essas informações são definidas pelo fabricante e indicam as condições "
                "nominais de operação do motor.\n\n"
                "Entre os dados presentes na placa normalmente encontram-se potência nominal, "
                "tensão de alimentação, corrente nominal, fator de potência, rendimento e "
                "tipo de ligação elétrica. Esses parâmetros representam o ponto de partida "
                "para compreender o comportamento elétrico do motor dentro do sistema de "
                "bombeamento analisado."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=ZLV_MHFdmWk",
            "caption": "Exemplo de leitura e interpretação da placa de identificação de um motor elétrico",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_003",
            "pergunta": (
                "Ao analisar a placa de identificação do motor, qual informação permite "
                "identificar diretamente a corrente nominal de operação?"
            ),
            "alternativas": {
                "a": "A cor da carcaça do motor",
                "b": "Os valores de corrente indicados em ampères associados à tensão nominal",
                "c": "A posição física do motor na instalação",
                "d": "A marca do fabricante",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Observe a placa do motor apresentada abaixo. "
                "A partir dela, identifique os principais dados elétricos "
                "utilizados para caracterizar o funcionamento do motor."
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "motor_03.png",
            "caption": "Figura: placa de identificação do motor utilizado no sistema",
        },

        # coleta de dados da placa
        {
            "tipo": "questao_texto",
            "id": "q_004",
            "pergunta": (
                "Potência nominal (cv ou kW). Informe o valor e a unidade exatamente como aparece na placa."
            ),
            "placeholder": "Exemplo de formato: 0.75 kW ou 1.0 cv",
            "altura": 100,
        },
        {
            "tipo": "questao_texto",
            "id": "q_005",
            "pergunta": (
                "Tensão nominal (V). Informe todas as tensões indicadas na placa do motor."
            ),
            "placeholder": "Formato esperado: ___ / ___ V",
            "altura": 100,
        },
        {
            "tipo": "questao_texto",
            "id": "q_006",
            "pergunta": (
                "Corrente nominal (A). Informe os valores correspondentes a cada tensão indicada."
            ),
            "placeholder": "Formato esperado: ___ / ___ A",
            "altura": 100,
        },
        {
            "tipo": "questao_texto",
            "id": "q_007",
            "pergunta": (
                "Fator de potência (cos φ). Informe o valor indicado na placa. Caso não esteja presente, escreva: 'não informado'."
            ),
            "placeholder": "Valor do cos φ indicado na placa",
            "altura": 100,
        },
        {
            "tipo": "questao_texto",
            "id": "q_008",
            "pergunta": (
                "Rendimento (η). Informe o rendimento indicado na placa. Caso não esteja presente, escreva: 'não informado'."
            ),
            "placeholder": "Valor do rendimento (%) indicado na placa",
            "altura": 100,
        },
        {
            "tipo": "questao_texto",
            "id": "q_009",
            "pergunta": (
                "Tipo de alimentação. Indique se o motor é monofásico ou trifásico e cite a evidência observada na placa."
            ),
            "placeholder": "Exemplo: trifásico (presença de L1, L2, L3 e ligação estrela/triângulo)",
            "altura": 120,
        },
    ]