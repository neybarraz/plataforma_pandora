from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Validação do problema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a construção do modelo do problema, é necessário realizar uma etapa de "
                "validação conceitual. O objetivo dessa etapa é verificar se os elementos "
                "considerados na análise são suficientes para explicar o fenômeno térmico "
                "observado no ambiente.\n\n"
                "Essa validação não corresponde ainda à solução do problema, mas sim à "
                "verificação da consistência do modelo construído. Para isso, é necessário "
                "avaliar se os mecanismos de transferência de calor considerados são "
                "adequados, se as variáveis escolhidas permitem interpretar a distribuição "
                "térmica observada e se a pergunta norteadora está alinhada com o fenômeno "
                "que se pretende investigar."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Mecanismos de transferência de calor",
        },
        {
            "tipo": "texto",
            "texto": (
                "O primeiro aspecto da validação consiste em verificar se o modelo contempla "
                "os principais mecanismos de transferência de calor presentes no ambiente. "
                "No caso de uma sala de aula, os processos de condução nas paredes, convecção "
                "entre o ar e as superfícies e trocas de calor por radiação entre superfícies "
                "desempenham papel fundamental no comportamento térmico do sistema."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_041",
            "pergunta": (
                "Por que é importante considerar diferentes mecanismos de transferência "
                "de calor na análise térmica da sala?"
            ),
            "alternativas": {
                "a": "Porque apenas um mecanismo é suficiente para explicar todo o comportamento térmico",
                "b": "Porque o calor pode ser transferido por diferentes processos físicos no ambiente",
                "c": "Porque a transferência de calor ocorre apenas pela radiação solar",
                "d": "Porque as superfícies da sala não participam das trocas de calor",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Variáveis consideradas no modelo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Outro aspecto importante da validação é verificar se as variáveis escolhidas "
                "para a análise são capazes de explicar o comportamento térmico observado. "
                "Neste estudo, foram consideradas principalmente as temperaturas do ar e "
                "das superfícies do ambiente, bem como fatores externos como radiação solar "
                "e ventilação.\n\n"
                "Essas variáveis permitem interpretar como o calor entra no sistema, como "
                "ele se movimenta no interior da sala e como se distribui no espaço."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_042",
            "pergunta": (
                "Qual conjunto de variáveis é mais adequado para explicar o comportamento "
                "térmico da sala neste estudo?"
            ),
            "alternativas": {
                "a": "Temperatura do ar e temperatura das superfícies",
                "b": "Cor das paredes e posição das carteiras",
                "c": "Quantidade de alunos e iluminação da sala",
                "d": "Altura do teto e tamanho do quadro",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "titulo",
            "texto": "Alinhamento da pergunta norteadora",
        },
        {
            "tipo": "texto",
            "texto": (
                "A última etapa da validação consiste em verificar se a pergunta norteadora "
                "formulada para o problema está coerente com o modelo construído. A pergunta "
                "deve estar diretamente relacionada ao fenômeno que está sendo analisado e "
                "às variáveis que podem ser observadas ou medidas no ambiente.\n\n"
                "No contexto deste estudo, a pergunta busca compreender se a distribuição "
                "de temperatura na sala e a relação entre temperaturas do ar e das "
                "superfícies são compatíveis com condições adequadas de conforto térmico "
                "para os ocupantes."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_043",
            "pergunta": (
                "Qual é a função da pergunta norteadora dentro da análise do problema?"
            ),
            "alternativas": {
                "a": "Definir a direção da investigação e orientar a análise do fenômeno",
                "b": "Substituir completamente a análise física do sistema",
                "c": "Eliminar a necessidade de medições experimentais",
                "d": "Determinar diretamente a solução do problema",
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "texto",
            "texto": (
                "Se o modelo inclui os principais mecanismos físicos, considera variáveis "
                "relevantes e possui uma pergunta norteadora coerente com o fenômeno "
                "observado, então o problema pode ser considerado bem estruturado. "
                "A partir desse ponto, torna-se possível avançar para a próxima etapa "
                "do processo, que corresponde à investigação e análise mais detalhada "
                "do comportamento térmico do ambiente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_044",
            "pergunta": (
                "O que caracteriza um modelo de problema bem estruturado?"
            ),
            "alternativas": {
                "a": "A presença de muitas variáveis sem relação com o fenômeno",
                "b": "A inclusão de mecanismos físicos, variáveis relevantes e uma pergunta coerente",
                "c": "A ausência de medições experimentais",
                "d": "A definição imediata da solução final",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "q_045",
            "pergunta": (
                "Explique, com suas palavras, por que a etapa de validação do problema "
                "é importante antes de iniciar a investigação detalhada do comportamento "
                "térmico da sala."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]