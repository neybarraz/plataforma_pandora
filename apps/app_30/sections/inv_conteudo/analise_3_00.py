from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Situação real: verificação de carga com TP4056",
        },
        {
            "tipo": "texto",
            "texto": (
                "Você montou um circuito utilizando o módulo TP4056 para carregar uma bateria "
                "de íon-lítio de 3,7 V nominal. A alimentação de entrada é de 5 V, proveniente "
                "de uma fonte USB. Os LEDs do módulo indicam funcionamento.\n\n"
                "No entanto, em engenharia não basta que o sistema pareça ativo. "
                "É necessário verificar se a bateria está realmente sendo carregada de forma correta. "
                "O objetivo desta etapa é observar o comportamento elétrico do sistema antes "
                "de aplicar qualquer modelo teórico."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Identificação do problema técnico",
        },
        {
            "tipo": "texto",
            "texto": (
                "A pergunta central desta etapa é:\n\n"
                "O módulo está carregando corretamente a bateria?\n\n"
                "Para responder a essa pergunta, é necessário observar grandezas físicas mensuráveis. "
                "Não se deve modificar o circuito nem ajustar componentes neste momento. "
                "O foco está na medição e na coleta de evidências."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.000.0001",
            "pergunta": (
                "Ao iniciar a verificação do processo de carga com o TP4056, "
                "qual grandeza deve ser medida primeiro para avaliar o estado inicial da bateria?"
            ),
            "alternativas": {
                "a": "Corrente de carga instantânea",
                "b": "Tensão nos terminais da bateria",
                "c": "Resistência equivalente do circuito",
                "d": "Potência dissipada no módulo",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Medição da tensão da bateria",
        },
        {
            "tipo": "texto",
            "texto": (
                "A tensão medida nos terminais da bateria fornece uma indicação inicial do seu estado de carga. "
                "Uma bateria Li-ion completamente carregada atinge aproximadamente 4,2 V. "
                "Se a medição indicar valores como 3,5 V ou 3,6 V, isso significa que a bateria ainda "
                "não está totalmente carregada e deve estar na fase de carregamento.\n\n"
                "Nesta etapa, registre o valor medido e acompanhe sua variação ao longo do tempo."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.000.0002",
            "pergunta": (
                "Se a bateria apresenta 3,6 V, qual é a interpretação mais adequada?"
            ),
            "alternativas": {
                "a": "A bateria está completamente carregada",
                "b": "A bateria está parcialmente carregada",
                "c": "O módulo está em falha",
                "d": "O carregador está sobrecarregando a bateria",
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
                "Além da tensão, é fundamental medir a corrente que está fluindo para a bateria. "
                "A presença de corrente indica transferência efetiva de carga elétrica. "
                "Se houver tensão mas não houver corrente, o processo de carregamento pode não estar "
                "ocorrendo. Portanto, a análise deve considerar simultaneamente tensão e corrente."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "investigacao.03.000.0003",
            "pergunta": (
                "Por que medir apenas a tensão não é suficiente para confirmar o carregamento?"
            ),
            "alternativas": {
                "a": "Porque tensão não pode ser medida diretamente",
                "b": "Porque pode existir tensão sem fluxo significativo de corrente",
                "c": "Porque a tensão sempre permanece constante",
                "d": "Porque a bateria não depende de tensão para carregar",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Coleta de dados experimentais",
        },

        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, registre medições reais do circuito em operação.\n\n"
                "Objetivo: obter evidências experimentais sobre o comportamento do processo de carga.\n\n"
                "Procedimento:\n"
                "1. Energize o módulo TP4056.\n"
                "2. Verifique se a bateria está corretamente conectada.\n"
                "3. Meça tensão e corrente utilizando o multímetro.\n\n"
                "Observe o comportamento ao longo do tempo, mas não realize interpretações ainda."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Medições iniciais (instante da energização)",
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "investigacao.03.000.0001",
            "rotulo": "Tensão inicial da bateria",
            "unidade": "V",
            "placeholder": "Ex: 3.65"
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "investigacao.03.000.0002",
            "rotulo": "Corrente inicial de carga",
            "unidade": "A",
            "placeholder": "Ex: 0.85"
        },

        {
            "tipo": "titulo",
            "texto": "Medições após alguns minutos de operação",
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "investigacao.03.000.0003",
            "rotulo": "Tensão após alguns minutos",
            "unidade": "V",
            "placeholder": "Ex: 3.78"
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "investigacao.03.000.0004",
            "rotulo": "Corrente após alguns minutos",
            "unidade": "A",
            "placeholder": "Ex: 0.82"
        },

        {
            "tipo": "texto",
            "texto": (
                "Após registrar os valores, responda mentalmente:\n\n"
                "- A tensão variou ao longo do tempo?\n"
                "- A corrente permaneceu constante ou mudou?\n\n"
                "Essas observações serão analisadas na próxima etapa."
            ),
        },
    ]