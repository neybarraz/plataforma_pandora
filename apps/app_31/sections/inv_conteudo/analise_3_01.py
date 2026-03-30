from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Verificação do processo de carga",
        },
        {
            "tipo": "texto",
            "texto": (
                "O módulo TP4056 está energizado e conectado a uma bateria de íon-lítio. "
                "Os LEDs indicam funcionamento, mas em engenharia não se deve confiar apenas em indicadores visuais. "
                "Nesta etapa, o objetivo é observar o comportamento elétrico real do sistema. "
                "Antes de discutir modelos teóricos ou fases de carregamento, precisamos responder: \n\n"
                "Há carregamento efetivo da bateria neste instante?"
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Grandezas fundamentais a serem observadas",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para determinar o estado do sistema, apenas duas grandezas precisam ser medidas: \n\n"
                "- Tensão nos terminais da bateria (V)\n"
                "- Corrente que entra na bateria (I)\n\n"
                "A tensão indica o nível de energia armazenada.\n"
                "A corrente indica se há transferência real de carga elétrica."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.001.0001",
            "pergunta": (
                "Qual grandeza é indispensável para confirmar que a bateria está sendo carregada?"
            ),
            "alternativas": {
                "a": "Temperatura do módulo",
                "b": "Tensão da bateria",
                "c": "Corrente que entra na bateria",
                "d": "Potência dissipada no circuito",
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "titulo",
            "texto": "Medição da tensão da bateria",
        },
        {
            "tipo": "texto",
            "texto": (
                "Meça a tensão diretamente nos terminais da bateria. "
                "Uma bateria Li-ion totalmente carregada atinge aproximadamente 4,2 V.\n"
                "Valores abaixo disso indicam que a carga ainda não está completa.\n\n"
                "Registre o valor medido e observe se ele varia ao longo do tempo."
            ),
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "obs.02.000.0001",
            "rotulo": "Tensão medida na bateria",
            "unidade": "V",
            "placeholder": "Ex: 3.72"
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.001.0002",
            "pergunta": (
                "Se a tensão medida for 3,7 V, qual é a interpretação mais adequada?"
            ),
            "alternativas": {
                "a": "Bateria totalmente carregada",
                "b": "Bateria parcialmente carregada",
                "c": "Falha no módulo",
                "d": "Sobretensão",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Medição da corrente de carga",
        },
        {
            "tipo": "texto",
            "texto": (
                "Agora meça a corrente que está entrando na bateria. "
                "A corrente deve ser medida em série com a bateria. "
                "Se houver corrente significativa fluindo para dentro da bateria, "
                "o carregamento está ocorrendo. "
                "Se houver tensão mas corrente igual a zero, "
                "não há carregamento efetivo."
            ),
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "obs.02.000.0002",
            "rotulo": "Corrente medida na bateria",
            "unidade": "A",
            "placeholder": "Ex: 0.80"
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.001.0003",
            "pergunta": (
                "Por que medir apenas a tensão não é suficiente para confirmar o carregamento?"
            ),
            "alternativas": {
                "a": "Porque tensão não pode ser medida diretamente",
                "b": "Porque pode existir tensão sem fluxo de corrente",
                "c": "Porque tensão não influencia a carga",
                "d": "Porque a bateria não depende de tensão",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Análise conjunta das medições",
        },
        {
            "tipo": "texto",
            "texto": (
                "A interpretação correta depende da análise simultânea de tensão e corrente.\n\n "
                "- Tensão abaixo de 4,2 V e corrente significativa → carregamento ativo.\n "
                "- Tensão próxima de 4,2 V e corrente diminuindo → fase final de carga.\n "
                "- Tensão abaixo de 4,2 V e corrente zero → carregamento não está ocorrendo.\n\n "
                "Evite conclusões baseadas em apenas uma grandeza."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "investigacao.03.001.0004",
            "pergunta": (
                "Explique com suas palavras por que a corrente é a evidência direta "
                "de que há carregamento da bateria."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Conclusão da etapa",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa você não modelou o funcionamento interno do TP4056. "
                "Você apenas observou o estado elétrico do sistema. "
                "Se houver corrente entrando na bateria e a tensão estiver abaixo de 4,2 V, "
                "o processo de carga está ocorrendo. "
                "Na próxima etapa será analisado por que esse comportamento ocorre "
                "e como o carregador regula corrente e tensão."
            ),
        },
    ]