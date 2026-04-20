def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # PASSO 1: APRESENTAÇÃO DO PROBLEMA
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "🚗 Desafio: Projetando um motor para carro elétrico"
        },

        {
            "tipo": "texto",
            "texto": (
                "Você é engenheira(o) de uma montadora de veículos elétricos. A empresa deseja lançar um novo modelo "
                "que seja mais eficiente e potente que os concorrentes.\n\n<br>"
                "O problema: o motor atual tem baixo torque em baixas rotações e superaquece em subidas íngremes. "
                "A equipe precisa redesenhar o motor para resolver essas duas limitações.\n\n"
                "Seu desafio é entender os princípios físicos envolvidos e propor melhorias no projeto."
            ),
        },

        {"tipo": "imagem", "arquivo": "ampere_02.png"},

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
                "Antes de propor soluções, vamos ativar seus conhecimentos sobre motores elétricos."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.002.0001",
            "pergunta": (
                "Qual princípio físico fundamental explica o funcionamento de um motor elétrico?"
            ),
            "alternativas": {
                "a": "Um campo magnético variável gera corrente elétrica (indução eletromagnética).",
                "b": "Uma corrente elétrica gera um campo magnético que interage com ímãs, produzindo força e movimento.",
                "c": "A resistência elétrica do fio aquece o motor e gera expansão térmica, produzindo movimento.",
                "d": "A diferença de potencial entre dois pontos gera um campo elétrico que empurra os elétrons."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.002.0002",
            "pergunta": (
                "O texto menciona três fatores que influenciam a força gerada por um motor elétrico. "
                "Quais são eles?"
            ),
            "alternativas": {
                "a": "Tensão da bateria, bitola do fio, temperatura ambiente.",
                "b": "Campo magnético, corrente elétrica, número de espiras.",
                "c": "Velocidade de rotação, atrito das escovas, diâmetro do eixo.",
                "d": "Resistência do cobre, isolamento térmico, lubrificação."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.03.002.0003",
            "pergunta": (
                "Com base no que você aprendeu sobre motores elétricos, formule uma hipótese: "
                "por que um motor pode perder torque em baixas rotações? E por que ele pode superaquecer em subidas?"
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

        {
            "tipo": "texto",
            "texto": (
                "Para resolver o problema, você precisa investigar os seguintes tópicos. "
                "Responda às questões para construir seu roteiro de pesquisa."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.002.0004",
            "pergunta": (
                "Para aumentar o torque do motor (força de rotação), qual modificação NÃO é eficaz?"
            ),
            "alternativas": {
                "a": "Aumentar a corrente elétrica que passa pelas bobinas.",
                "b": "Usar ímãs mais potentes (ex: ímãs de neodímio).",
                "c": "Aumentar o número de espiras nas bobinas.",
                "d": "Aumentar a distância entre o ímã e a bobina."
            },
            "alternativa_correta": "d",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.002.0005",
            "pergunta": (
                "O superaquecimento do motor em subidas está relacionado a qual efeito físico?"
            ),
            "alternativas": {
                "a": "Efeito Joule: a corrente elétrica aquece os fios por resistência elétrica.",
                "b": "Indução eletromagnética: campos variáveis geram calor parasita.",
                "c": "Fricção mecânica: o atrito das escovas com o comutador gera calor.",
                "d": "Histerese magnética: a magnetização reversa dos ímãs aquece o motor."
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.002.0006",
            "pergunta": (
                "Para resolver o superaquecimento sem perder torque, qual estratégia é mais adequada?"
            ),
            "alternativas": {
                "a": "Reduzir a corrente elétrica (resolve o calor, mas reduz o torque).",
                "b": "Usar fios mais grossos (menor resistência elétrica) e sistema de refrigeração líquida.",
                "c": "Diminuir o número de espiras (reduz calor e mantém torque).",
                "d": "Trocar ímãs permanentes por eletroímãs mais fracos."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.002.0007",
            "pergunta": (
                "O que acontece com o torque se dobrarmos o número de espiras e mantivermos a mesma corrente?"
            ),
            "alternativas": {
                "a": "O torque cai pela metade.",
                "b": "O torque permanece o mesmo.",
                "c": "O torque dobra (mais espiras = mais força magnética).",
                "d": "O torque quadruplica."
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
                "- Quais materiais são usados em ímãs de motores de carros elétricos (ex: neodímio)?\n"
                "- O que é eficiência de um motor elétrico e como ela é calculada?\n"
                "- Quais são as vantagens dos motores de corrente alternada (AC) sobre os de corrente contínua (DC) em carros?\n"
                "- O que é um inversor de frequência e qual seu papel no carro elétrico?\n"
                "- Como o Tesla Model 3 ou outro EV famoso resolve o problema de superaquecimento?"
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.03.002.0008",
            "pergunta": (
                "Com base na sua pesquisa, descreva pelo menos duas soluções reais usadas pela indústria "
                "para aumentar o torque ou reduzir o superaquecimento em motores de carros elétricos."
            ),
            "altura": 180,
        },

        # ==================================================
        # PASSO 5: FECHAMENTO (QUESTÃO DE SÍNTESE)
        # ==================================================
        {"tipo": "titulo", "texto": "📝 Etapa 4: Fechamento da análise"},

        {
            "tipo": "questao_texto",
            "id": "solucao.03.002.0009",
            "pergunta": (
                "Com base em tudo o que você aprendeu (conhecimentos prévios, múltipla escolha e pesquisa autônoma), "
                "responda de forma completa:\n\n"
                "1. Quais são os três principais fatores que controlam o torque de um motor elétrico?\n"
                "2. Por que o motor superaquece em subidas?\n"
                "3. Que modificações você proporia no projeto para resolver os dois problemas (baixo torque + superaquecimento)? "
                "Justifique cada proposta com os princípios físicos envolvidos."
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
                "propondo o redesenho do motor elétrico para o novo veículo."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.03.002.0010",
            "pergunta": (
                "Escreva uma proposta de solução contendo:\n\n"
                "- Duas modificações no projeto para AUMENTAR O TORQUE em baixas rotações.\n"
                "- Duas modificações para REDUZIR O SUPERAQUECIMENTO em subidas.\n"
                "- Uma justificativa física para cada modificação (ex: 'aumentar o número de espiras porque...').\n\n"
                # "- Um diagrama mental ou lista de prós/contras (opcional, mas valorizado).\n\n"
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