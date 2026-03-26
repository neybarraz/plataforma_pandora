from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Construção da análise elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a identificação das entradas do sistema, é necessário compreender "
                "como essas grandezas são analisadas e transformadas ao longo do estudo. "
                "Essa etapa corresponde ao núcleo do modelo sistêmico, no qual os dados "
                "iniciais deixam de ser apenas informações observadas e passam a ser "
                "interpretados à luz das relações da eletricidade.\n\n"
                "No contexto do sistema de bombeamento, essa análise envolve a aplicação "
                "de conceitos e relações matemáticas para interpretar as características "
                "do motor e da instalação elétrica. O objetivo é transformar os dados "
                "levantados em informações técnicas que permitam compreender o comportamento "
                "do circuito e orientar decisões de dimensionamento."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Interpretação da corrente elétrica",
        },
        {
            "tipo": "texto",
            "texto": (
                "Uma das principais etapas dessa análise é a determinação da corrente elétrica "
                "associada ao funcionamento do motor. A corrente está diretamente relacionada "
                "à potência do equipamento e à tensão de alimentação, sendo uma grandeza central "
                "para a compreensão do comportamento do circuito.\n\n"
                "A partir da análise da corrente nominal, torna-se possível avaliar as condições "
                "de operação do motor e estabelecer parâmetros iniciais para o dimensionamento "
                "da alimentação elétrica."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_029",
            "pergunta": (
                "No modelo sistêmico do problema elétrico, qual atividade "
                "representa corretamente uma etapa de análise das grandezas do sistema?"
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
            "tipo": "titulo",
            "texto": "Cálculos e relações elétricas aplicadas",
        },
        {
            "tipo": "texto",
            "texto": (
                "Além da corrente nominal, a análise do sistema envolve outras relações "
                "elétricas importantes, como a avaliação da corrente de partida, o "
                "dimensionamento da seção dos condutores e a estimativa da queda de tensão "
                "ao longo do circuito.\n\n"
                "Essas etapas utilizam as variáveis de entrada previamente identificadas "
                "e permitem compreender como a energia elétrica é distribuída no sistema. "
                "Ao aplicar essas relações, o problema deixa de ser apenas descritivo e passa "
                "a ser tratado de forma quantitativa, possibilitando uma interpretação técnica "
                "mais precisa do funcionamento do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O conjunto dessas análises mostra que o funcionamento do sistema não depende "
                "apenas da identificação de suas partes, mas da compreensão das relações entre "
                "as grandezas elétricas envolvidas. É por meio dessas relações que se torna "
                "possível explicar o comportamento do circuito e avaliar as condições adequadas "
                "de alimentação do motor."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_030",
            "pergunta": (
                "Explique, com suas palavras, por que os cálculos elétricos "
                "realizados durante a análise podem ser considerados a etapa "
                "central de interpretação no modelo sistêmico do problema."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]