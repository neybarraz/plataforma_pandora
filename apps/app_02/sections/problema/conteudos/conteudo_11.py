from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Modelo sistêmico – Processamento",
        },
        {
            "tipo": "texto",
            "texto": (
                "No modelo sistêmico utilizado para representar o problema "
                "de engenharia, o processamento corresponde às etapas de "
                "análise e cálculo realizadas a partir das variáveis de entrada.\n\n"
                "No sistema de bombeamento estudado, o processamento envolve "
                "a aplicação de relações e fórmulas da eletricidade para "
                "interpretar os dados do motor e da instalação elétrica. "
                "Essas operações permitem transformar os dados iniciais em "
                "informações técnicas que orientam o dimensionamento do circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_029",
            "pergunta": (
                "No modelo sistêmico do problema elétrico, qual atividade "
                "representa corretamente uma etapa de processamento?"
            ),
            "alternativas": {
                "a": "Observar a placa do motor",
                "b": "Registrar a tensão da rede",
                "c": "Calcular a corrente nominal do motor",
                "d": "Identificar o tipo de reservatório"
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "texto",
            "texto": (
                "Entre as principais etapas de processamento deste estudo estão "
                "o cálculo da corrente nominal do motor, a análise da corrente "
                "de partida, o dimensionamento da seção adequada dos condutores "
                "e a estimativa da queda de tensão ao longo do circuito.\n\n"
                "Essas operações utilizam os dados levantados anteriormente "
                "como entradas do sistema e permitem compreender como a "
                "energia elétrica circula no circuito que alimenta o motor "
                "da motobomba."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_030",
            "pergunta": (
                "Explique, com suas palavras, por que os cálculos elétricos "
                "realizados durante a análise podem ser considerados a etapa "
                "de processamento no modelo sistêmico do problema."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]