from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Modelo sistêmico – Entradas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para analisar tecnicamente o problema elétrico do sistema de "
                "bombeamento, é útil representar o sistema por meio de um modelo "
                "sistêmico. Nesse tipo de representação, o funcionamento do sistema "
                "é organizado em três partes principais: entradas, processamento e "
                "saídas.\n\n"
                "As entradas correspondem às informações ou variáveis iniciais "
                "necessárias para realizar a análise. No caso do motor que aciona "
                "a motobomba, essas entradas são dados elétricos e características "
                "da instalação que influenciam diretamente o comportamento do "
                "circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_027",
            "pergunta": (
                "No modelo sistêmico utilizado para analisar o sistema elétrico da "
                "motobomba, qual das alternativas representa corretamente um "
                "exemplo de variável de entrada?"
            ),
            "alternativas": {
                "a": "A quantidade de água armazenada no reservatório",
                "b": "A potência do motor elétrico",
                "c": "A posição física da bomba no reservatório",
                "d": "O número de moradores do prédio",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Entre as principais entradas consideradas neste estudo estão a "
                "potência do motor, a tensão de alimentação da rede elétrica, a "
                "distância entre a fonte de energia e o motor e o fator de potência "
                "do equipamento.\n\n"
                "Essas informações permitem iniciar os cálculos elétricos "
                "necessários para compreender o comportamento do circuito e "
                "dimensionar corretamente a alimentação do motor."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_028",
            "pergunta": (
                "Explique, com suas palavras, por que a potência do motor, a "
                "tensão de alimentação, a distância da fonte e o fator de "
                "potência podem ser considerados variáveis de entrada no "
                "modelo sistêmico do problema."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]