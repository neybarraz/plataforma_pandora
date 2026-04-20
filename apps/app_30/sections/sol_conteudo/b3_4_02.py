def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # PASSO 1: APRESENTAÇÃO DO PROBLEMA
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "📱 Desafio: Projetando um carregador sem fio"
        },

        {
            "tipo": "texto",
            "texto": (
                "Você é engenheira(o) de uma empresa de tecnologia que desenvolve acessórios para celulares. "
                "A empresa deseja lançar um carregador sem fio (indução) que seja mais eficiente que os concorrentes.\n\n <br>"
                "O problema: o carregador atual tem baixa eficiência quando o celular está ligeiramente desalinhado "
                "ou a mais de 5 mm de distância. Isso gera superaquecimento e carregamento lento.\n\n"
                "A equipe precisa redesenhar o carregador para resolver essas duas limitações: **baixa eficiência com desalinhamento** e **superaquecimento**.\n\n"
                "Seu desafio é entender os princípios físicos da indução eletromagnética e propor melhorias no projeto."
            ),
        },

        {"tipo": "imagem", "arquivo": "faraday_06.png"},

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
                "Antes de propor soluções, vamos ativar seus conhecimentos sobre indução eletromagnética."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.002.0001",
            "pergunta": (
                "Qual princípio físico fundamental explica o funcionamento de um carregador sem fio por indução?"
            ),
            "alternativas": {
                "a": "Um campo magnético constante gera corrente elétrica em qualquer bobina próxima.",
                "b": "Uma corrente elétrica variável em uma bobina gera um campo magnético variável, que induz corrente em outra bobina próxima.",
                "c": "A resistência elétrica do fio aquece a bobina e gera corrente por efeito termelétrico.",
                "d": "A diferença de potencial entre duas bobinas gera um campo elétrico que transfere energia."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.002.0002",
            "pergunta": (
                "O texto menciona dois problemas principais do carregador atual. Quais são eles?"
            ),
            "alternativas": {
                "a": "Baixa potência e cabo muito curto.",
                "b": "Baixa eficiência com desalinhamento e superaquecimento.",
                "c": "Alto custo e baixa durabilidade.",
                "d": "Incompatibilidade com iPhones e carregamento lento."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.04.002.0003",
            "pergunta": (
                "Com base no que você sabe sobre indução eletromagnética, formule uma hipótese: "
                "por que o desalinhamento entre o carregador e o celular reduz a eficiência? "
                "E por que o carregador pode superaquecer durante o uso?"
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
            "id": "solucao.04.002.0004",
            "pergunta": (
                "Para aumentar a eficiência de transferência de energia entre duas bobinas, qual modificação NÃO é eficaz?"
            ),
            "alternativas": {
                "a": "Aumentar o número de espiras nas bobinas.",
                "b": "Aumentar a frequência da corrente alternada.",
                "c": "Aumentar a distância entre as bobinas.",
                "d": "Usar núcleos de ferrite nas bobinas."
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.002.0005",
            "pergunta": (
                "O superaquecimento do carregador está relacionado a qual efeito físico?"
            ),
            "alternativas": {
                "a": "Efeito Joule: a corrente elétrica aquece os fios por resistência elétrica.",
                "b": "Indução eletromagnética: campos variáveis geram calor parasita no núcleo.",
                "c": "Fricção mecânica: o atrito entre as bobinas gera calor.",
                "d": "Histerese magnética: a magnetização reversa do núcleo aquece o material."
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.002.0006",
            "pergunta": (
                "Para reduzir o superaquecimento sem perder eficiência, qual estratégia é mais adequada?"
            ),
            "alternativas": {
                "a": "Reduzir a corrente elétrica (resolve o calor, mas reduz a potência transferida).",
                "b": "Usar fios mais grossos (menor resistência elétrica) e adicionar refrigeração passiva.",
                "c": "Diminuir o número de espiras (reduz calor, mas também reduz a indução).",
                "d": "Reduzir a frequência da corrente alternada."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.002.0007",
            "pergunta": (
                "O que acontece com a corrente induzida na bobina do celular quando aumentamos o número de espiras da bobina do carregador?"
            ),
            "alternativas": {
                "a": "A corrente induzida diminui.",
                "b": "A corrente induzida permanece a mesma.",
                "c": "A corrente induzida aumenta (mais espiras = maior campo magnético variável).",
                "d": "A corrente induzida se anula."
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
                "- Qual é o padrão Qi de carregamento sem fio e como ele funciona?\n"
                "- Quais materiais são usados nos núcleos das bobinas de carregadores (ex: ferrite)?\n"
                "- O que é eficiência de transferência de energia e como ela é calculada?\n"
                "- Qual a diferença entre indução eletromagnética e ressonância magnética?\n"
                "- Como a Apple, Samsung ou Xiaomi resolve o problema de desalinhamento em seus carregadores?\n"
                "- O que é a Lei de Lenz e como ela explica a oposição ao movimento?"
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.04.002.0008",
            "pergunta": (
                "Com base na sua pesquisa, descreva pelo menos duas soluções reais usadas pela indústria "
                "para aumentar a eficiência ou reduzir o superaquecimento em carregadores sem fio."
            ),
            "altura": 180,
        },

        # ==================================================
        # PASSO 5: FECHAMENTO (QUESTÃO DE SÍNTESE)
        # ==================================================
        {"tipo": "titulo", "texto": "📝 Etapa 4: Fechamento da análise"},

        {
            "tipo": "questao_texto",
            "id": "solucao.04.002.0009",
            "pergunta": (
                "Com base em tudo o que você aprendeu (conhecimentos prévios, múltipla escolha e pesquisa autônoma), "
                "responda de forma completa:\n\n"
                "1. Quais são os principais fatores que controlam a eficiência de um carregador por indução?\n"
                "2. Por que o desalinhamento reduz a eficiência?\n"
                "3. Por que o carregador superaquece durante o uso?\n"
                "4. Que modificações você proporia no projeto para resolver os dois problemas (baixa eficiência + superaquecimento)? "
                "Justifique cada proposta com os princípios físicos da Lei de Faraday e da Lei de Lenz."
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
                "propondo o redesenho do carregador sem fio para a nova linha de acessórios."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "solucao.04.002.0010",
            "pergunta": (
                "Escreva uma proposta de solução contendo:\n\n"
                "- Duas modificações no projeto para AUMENTAR A EFICIÊNCIA quando houver desalinhamento.\n"
                "- Duas modificações para REDUZIR O SUPERAQUECIMENTO.\n"
                "- Uma justificativa física para cada modificação (ex: 'aumentar o número de espiras porque, pela Lei de Faraday, a força eletromotriz induzida é proporcional ao número de espiras...').\n\n"
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