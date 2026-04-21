def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # PASSO 1: APRESENTAÇÃO DO PROBLEMA
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "🚗 Desafio: Redesenhando o sistema de freio ABS"
        },

        {
            "tipo": "texto",
            "texto": (
                "Você é engenheira(o) de uma montadora de veículos. A empresa recebeu reclamações de clientes "
                "sobre o sistema de freio ABS (Anti-lock Braking System) em um modelo popular.\n\n<br>"

                "O problema: o sistema atual demora a reagir em pisos molhados e, em frenagens bruscas, "
                "o pedal vibra excessivamente, causando desconforto e insegurança. Além disso, o sistema "
                "tem custo elevado de manutenção devido a falhas nas válvulas hidráulicas.\n\n"
                "A equipe precisa redesenhar o sistema para resolver três limitações: **tempo de resposta lento em piso molhado**, "
                "**vibração excessiva no pedal** e **falhas nas válvulas hidráulicas**.\n\n"
                "Seu desafio é entender os princípios físicos envolvidos (estática dos fluidos e eletromagnetismo) "
                "e propor melhorias no projeto."
            ),
        },

        {"tipo": "imagem", "arquivo": "fluido_07.png"},

        # ==================================================
        # PASSO 2: DISCUSSÃO INICIAL - CONHECIMENTOS PRÉVIOS
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "🔍 Etapa 1: O que você já sabe?"
        },

        {
            "tipo": "texto",
            "texto": (
                "Antes de propor soluções, vamos ativar seus conhecimentos sobre freios hidráulicos e ABS."
            ),
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.01.002.0001",
            "pergunta": (
                "Qual princípio físico explica a transmissão da força do pedal do freio até as rodas?"
            ),
            "alternativas": {
                "a": "Princípio de Arquimedes (empuxo).",
                "b": "Princípio de Pascal (transmissão integral de pressão em um fluido confinado).",
                "c": "Lei de Faraday (indução eletromagnética).",
                "d": "Princípio de Stevin (pressão hidrostática)."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_multipla_escolha",  "id": "solucao.01.002.0002",
            "pergunta": (
                "O texto menciona três problemas principais do sistema ABS atual. Quais são eles?"
            ),
            "alternativas": {
                "a": "Freio fraco, pedal duro e barulho excessivo.",
                "b": "Tempo de resposta lento em piso molhado, vibração excessiva no pedal e falhas nas válvulas hidráulicas.",
                "c": "Superaquecimento das pastilhas, desgaste precoce dos discos e vazamento de fluido.",
                "d": "Custo alto da bomba, ineficiência em baixa velocidade e consumo excessivo de fluido."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_texto", "id": "solucao.01.002.0003",
            "pergunta": (
                "Com base no que você sabe sobre freios hidráulicos e ABS, formule hipóteses: "
                "por que o sistema pode demorar a reagir em piso molhado? Por que o pedal vibra excessivamente? "
                "E por que as válvulas hidráulicas podem falhar?"
            ),
            "altura": 150,
        },

        # ==================================================
        # PASSO 3: O QUE PRECISAMOS SABER? (GUIA DE PESQUISA)
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "📚 Etapa 2: O que precisamos descobrir?"
        },

        {  "tipo": "texto", "texto": (
                "Para resolver o problema, você precisa investigar os seguintes tópicos. "
                "Responda às questões para construir seu roteiro de pesquisa."
            ),
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.01.002.0004",
            "pergunta": (
                "Para reduzir o tempo de resposta do ABS em piso molhado, qual modificação NÃO é eficaz?"
            ),
            "alternativas": {
                "a": "Aumentar a frequência de modulação das válvulas (mais ciclos por segundo).",
                "b": "Usar sensores de roda mais precisos e rápidos.",
                "c": "Aumentar o comprimento das mangueiras de freio (maior volume de fluido).",
                "d": "Reduzir a viscosidade do fluido de freio para escoamento mais rápido."
            },
            "alternativa_correta": "c",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.01.002.0005",
            "pergunta": (
                "A vibração excessiva no pedal durante o ABS está relacionada a qual fenômeno físico?"
            ),
            "alternativas": {
                "a": "Ressonância mecânica entre o pedal e o assoalho do carro.",
                "b": "Modulação rápida da pressão no fluido de freio, que é transmitida de volta ao pedal.",
                "c": "Desgaste irregular das pastilhas de freio.",
                "d": "Vazamento de fluido no cilindro mestre."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.01.002.0006",
            "pergunta": (
                "Para reduzir a vibração no pedal sem comprometer a eficiência do ABS, qual estratégia é mais adequada?"
            ),
            "alternativas": {
                "a": "Desligar o ABS em pisos molhados.",
                "b": "Adicionar um amortecedor hidráulico (pulsation damper) no circuito do fluido.",
                "c": "Reduzir a pressão máxima do sistema.",
                "d": "Aumentar o diâmetro do cilindro mestre."
            },
            "alternativa_correta": "b",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.01.002.0007",
            "pergunta": (
                "As falhas nas válvulas hidráulicas do ABS estão frequentemente associadas a qual fator?"
            ),
            "alternativas": {
                "a": "Corrosão causada por fluido de freio contaminado com água.",
                "b": "Excesso de pressão no sistema.",
                "c": "Baixa temperatura do fluido em dias frios.",
                "d": "Desalinhamento das pastilhas de freio."
            },
            "alternativa_correta": "a",
        },

        { "tipo": "questao_multipla_escolha", "id": "solucao.01.002.0008",
            "pergunta": (
                "Qual dos seguintes componentes é responsável por modular a pressão do fluido em um sistema ABS?"
            ),
            "alternativas": {
                "a": "Cilindro mestre.",
                "b": "Servo freio (amplificador de vácuo).",
                "c": "Válvulas solenoides (controladas eletronicamente).",
                "d": "Reservatório de fluido."
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # PASSO 4: INDUÇÃO À PESQUISA AUTÔNOMA
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "🔎 Etapa 3: Pesquise por conta própria"
        },

        {
            "tipo": "texto",
            "texto": (
                "Agora é sua vez de investigar! Use a internet, IAs, livros ou materiais indicados pelo professor "
                "para responder às perguntas abaixo. Anote suas descobertas.\n\n"
                "- Como funciona um sistema ABS? Quais são seus componentes principais (sensores, central eletrônica, válvulas solenoides, bomba)?\n"
                "- O que é fluido de freio DOT 3, DOT 4 ou DOT 5? Qual a diferença entre eles e por que a umidade degrada o fluido?\n"
                "- O que é frequência de modulação em um ABS e como ela afeta o tempo de resposta?\n"
                "- O que causa a pulsação no pedal do freio durante a atuação do ABS? Como os fabricantes reduzem esse efeito?\n"
                "- Quais são as soluções usadas pela Bosch, Continental ou TRW em sistemas ABS de última geração?\n"
                "- O que é frenagem regenerativa em carros elétricos e como ela se integra ao ABS?"
            ),
        },

        { "tipo": "questao_texto", "id": "solucao.01.002.0009",
            "pergunta": (
                "Com base na sua pesquisa, descreva pelo menos duas soluções reais usadas pela indústria "
                "para reduzir o tempo de resposta do ABS ou eliminar falhas nas válvulas hidráulicas."
            ),
            "altura": 180,
        },

        # ==================================================
        # PASSO 5: FECHAMENTO (QUESTÃO DE SÍNTESE)
        # ==================================================
        {"tipo": "titulo", "texto": "📝 Etapa 4: Fechamento da análise"},

        { "tipo": "questao_texto", "id": "solucao.01.002.0010",
            "pergunta": (
                "Com base em tudo o que você aprendeu (conhecimentos prévios, múltipla escolha e pesquisa autônoma), "
                "responda de forma completa:\n\n"
                "1. Quais são os principais fatores que controlam o tempo de resposta de um sistema ABS?\n"
                "2. Por que o pedal vibra excessivamente durante a frenagem com ABS e como isso pode ser mitigado?\n"
                "3. Por que as válvulas hidráulicas falham com o tempo?\n"
                "4. Que modificações você proporia no projeto para resolver os três problemas (tempo de resposta lento, vibração excessiva, falhas nas válvulas)? "
                "Justifique cada proposta com os princípios físicos da estática dos fluidos e do eletromagnetismo."
            ),
            "altura": 250,
        },

        # ==================================================
        # PASSO 6: PROPOSTA DE SOLUÇÃO (PRODUTO FINAL)
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "✅ Etapa 5: Sua solução de engenharia"
        },

        {
            "tipo": "texto",
            "texto": (
                "Parabéns! Agora você vai atuar como engenheira(o). Elabore um relatório técnico resumido "
                "propondo o redesenho do sistema ABS para o novo modelo do veículo."
            ),
        },

        { "tipo": "questao_texto", "id": "solucao.01.002.0011",
            "pergunta": (
                "Escreva uma proposta de solução contendo:\n\n"
                "- Uma modificação para REDUZIR O TEMPO DE RESPOSTA em piso molhado.\n"
                "- Uma modificação para REDUZIR A VIBRAÇÃO NO PEDAL.\n"
                "- Uma modificação para AUMENTAR A CONFIABILIDADE DAS VÁLVULAS HIDRÁULICAS.\n"
                "- Uma justificativa física para cada modificação (ex: 'reduzir a viscosidade do fluido porque, pelo Princípio de Pascal, pressão se transmite mais rapidamente em fluidos de menor viscosidade...').\n\n"
                "Seja criativo, mas mantenha a base científica correta!"
            ),
            "altura": 300,
        },

        {
            "tipo": "texto",
            "texto": (
                "🎯 Ao final, compartilhe sua solução com colegas e compare abordagens. "
                "A engenharia tem múltiplas respostas corretas, o importante é a fundamentação!"
            ),
        },

    ]