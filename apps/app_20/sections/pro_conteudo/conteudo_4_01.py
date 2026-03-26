from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Entradas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para analisar tecnicamente o problema elétrico associado ao sistema de "
                "bombeamento, é útil representá-lo por meio de um modelo sistêmico. "
                "Nesse tipo de representação, o funcionamento do sistema é organizado "
                "a partir de três elementos principais: entradas, processamento e saídas.\n\n"
                "As entradas correspondem às informações iniciais que caracterizam o "
                "problema e condicionam a análise do sistema. No caso do motor que "
                "aciona a motobomba, essas entradas são grandezas elétricas e dados "
                "da instalação que influenciam diretamente o comportamento do circuito "
                "e a definição das condições de alimentação."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Potência do motor",
        },
        {
            "tipo": "texto",
            "texto": (
                "A potência do motor é uma das entradas fundamentais do sistema. "
                "Ela expressa a demanda energética associada ao funcionamento do "
                "equipamento e constitui uma referência importante para a análise "
                "da corrente elétrica exigida e das condições de alimentação necessárias.\n\n"
                "No estudo do sistema de bombeamento, essa grandeza permite iniciar "
                "a interpretação técnica do problema, pois está diretamente relacionada "
                "ao comportamento elétrico do motor e ao dimensionamento básico do circuito."
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
            "tipo": "titulo",
            "texto": "Tensão de alimentação e demais variáveis de entrada",
        },
        {
            "tipo": "texto",
            "texto": (
                "Além da potência do motor, outras entradas importantes do sistema são "
                "a tensão de alimentação da rede elétrica, a distância entre a fonte "
                "de energia e o motor e o fator de potência do equipamento. Essas "
                "grandezas ajudam a definir em que condições o motor opera e quais "
                "parâmetros devem ser considerados na análise elétrica.\n\n"
                "Em conjunto, essas informações permitem organizar o problema de forma "
                "estruturada e iniciar os cálculos necessários para compreender o "
                "comportamento do circuito e avaliar o dimensionamento da alimentação "
                "do motor."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Dentro e fora do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao construir o modelo sistêmico, também é necessário definir as fronteiras "
                "da análise. Dentro do sistema estão as grandezas elétricas e os elementos "
                "diretamente relacionados ao problema de alimentação do motor, como sua "
                "potência, a tensão de alimentação, o fator de potência e a distância "
                "associada ao circuito de alimentação.\n\n"
                "Fora do sistema permanecem outros aspectos que não fazem parte do recorte "
                "adotado nesta etapa, como detalhes estruturais do prédio, modificações "
                "hidráulicas da instalação ou fatores de uso que não interferem diretamente "
                "na modelagem elétrica inicial. Essa delimitação permite concentrar a análise "
                "nas entradas mais relevantes para o problema estudado."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "As entradas do sistema correspondem, portanto, às variáveis que definem "
                "as condições iniciais da análise elétrica. Ao identificá-las e organizá-las "
                "de forma coerente, torna-se possível construir uma representação técnica "
                "mais clara do problema e preparar as etapas seguintes da investigação."
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