def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # INTRODUÇÃO
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "📐 Aplicação matemática da Lei de Faraday"
        },

        {
            "tipo": "texto",
            "texto": (
                "\n Agora que você compreende o significado físico e o formalismo da Lei de Faraday, "
                "é hora de aplicá-la para resolver problemas concretos. Use as equações:\n\n"
                "$$\\mathcal{E} = - \\frac{d\\Phi_B}{dt} \\quad \\text{e} \\quad \\Phi_B = B A \\cos\\theta$$\n\n"
                "para calcular forças eletromotrizes induzidas em diferentes configurações."
            ),
        },

        # ==================================================
        # QUESTÃO 01 - Conceitual (fluxo magnético)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0001",
            "pergunta": (
                "1. Uma espira quadrada de lado 0,10 m está imersa em um campo magnético uniforme de B = 0,50 T, "
                "perpendicular à superfície. Qual é o fluxo magnético através da espira?"
            ),
            "alternativas": {
                "a": "0,005 Wb",
                "b": "0,010 Wb",
                "c": "0,050 Wb",
                "d": "0,100 Wb",
                "e": "0,500 Wb"
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0002",
            "pergunta": (
                "2. A mesma espira é girada de modo que o campo magnético forme um ângulo de 60° com a normal à superfície. "
                "Qual é o novo fluxo magnético?"
            ),
            "alternativas": {
                "a": "0,0025 Wb",
                "b": "0,0050 Wb",
                "c": "0,0100 Wb",
                "d": "0,0250 Wb",
                "e": "0,0500 Wb"
            },
            "alternativa_correta": "a",
        },

        # ==================================================
        # QUESTÃO 02 - Variação do fluxo
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0003",
            "pergunta": (
                "3. Uma bobina com 100 espiras tem um fluxo magnético que varia de 0,02 Wb para 0,08 Wb em 0,5 segundos. "
                "Qual é a força eletromotriz induzida média?"
            ),
            "alternativas": {
                "a": "6 V",
                "b": "8 V",
                "c": "10 V",
                "d": "12 V",
                "e": "24 V"
            },
            "alternativa_correta": "d",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0004",
            "pergunta": (
                "4. Uma bobina de 200 espiras é submetida a uma variação uniforme de fluxo de 0,05 Wb para 0,01 Wb em 0,1 s. "
                "Calcule a força eletromotriz induzida."
            ),
            "alternativas": {
                "a": "40 V",
                "b": "60 V",
                "c": "80 V",
                "d": "100 V",
                "e": "120 V"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 03 - Proporcionalidade
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0005",
            "pergunta": (
                "5. Uma bobina produz uma força eletromotriz ℰ quando o fluxo varia a uma certa taxa. "
                "Se o número de espiras for triplicado e a taxa de variação do fluxo for reduzida à metade, "
                "a nova força eletromotriz será:"
            ),
            "alternativas": {
                "a": "ℰ/6",
                "b": "ℰ/3",
                "c": "1,5 ℰ",
                "d": "3 ℰ",
                "e": "6 ℰ"
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0006",
            "pergunta": (
                "6. Uma espira gira em um campo magnético uniforme. Se a velocidade angular for duplicada, "
                "a força eletromotriz máxima:"
            ),
            "alternativas": {
                "a": "cai pela metade",
                "b": "permanece a mesma",
                "c": "dobra",
                "d": "quadruplica",
                "e": "cai para um quarto"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 04 - Barra deslizante
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0007",
            "pergunta": (
                "7. Uma barra condutora de 0,20 m desliza com velocidade de 5 m/s sobre trilhos em um campo magnético "
                "uniforme de 0,30 T perpendicular ao plano. Qual é a força eletromotriz induzida?"
            ),
            "alternativas": {
                "a": "0,10 V",
                "b": "0,20 V",
                "c": "0,30 V",
                "d": "0,40 V",
                "e": "0,50 V"
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0008",
            "pergunta": (
                "8. Na mesma configuração, se a velocidade for reduzida a 2 m/s, a nova força eletromotriz será:"
            ),
            "alternativas": {
                "a": "0,06 V",
                "b": "0,12 V",
                "c": "0,18 V",
                "d": "0,24 V",
                "e": "0,30 V"
            },
            "alternativa_correta": "b",
        },

        # ==================================================
        # QUESTÃO 05 - Espira giratória
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0009",
            "pergunta": (
                "9. Uma bobina com 50 espiras de área 0,02 m² gira a 60 Hz em um campo magnético de 0,10 T. "
                "Qual é a força eletromotriz máxima? (Use ω = 2πf)"
            ),
            "alternativas": {
                "a": "3,77 V",
                "b": "7,54 V",
                "c": "15,08 V",
                "d": "30,16 V",
                "e": "37,70 V"
            },
            "alternativa_correta": "a",
        },

        # ==================================================
        # QUESTÃO 06 - Conceitual sem cálculo
        # ==================================================
        {
            "tipo": "questao_texto",
            "id": "solucao.04.004.0010",
            "pergunta": (
                "10. Sem fazer contas, responda:\n\n"
                "- Se você dobrar a velocidade de rotação de uma bobina em um gerador, o que acontece com a tensão gerada?\n"
                "- Se você dobrar o número de espiras, mantendo a mesma velocidade, o que acontece com a tensão?\n\n"
                "Explique usando a Lei de Faraday."
            ),
            "altura": 150,
        },

        # ==================================================
        # EXERCÍCIO 1: CÁLCULO DE FORÇA ELETROMOTRIZ
        # ==================================================
        # {"tipo": "titulo", "texto": "Exercício 1: Calculando a força eletromotriz"},

        {
            "tipo": "texto",
            "texto": (
                "Uma bobina com 200 espiras tem um fluxo magnético que varia conforme o gráfico abaixo:\n\n"
                "No intervalo de 0 a 0,5 s, o fluxo varia de 0 a 0,04 Wb.\n"
                "No intervalo de 0,5 a 1,0 s, o fluxo permanece constante em 0,04 Wb.\n"
                "No intervalo de 1,0 a 1,5 s, o fluxo varia de 0,04 Wb a 0,01 Wb.\n\n"
                "Calcule a força eletromotriz induzida em cada intervalo."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0011",
            "pergunta": (
                "11. Qual é a força eletromotriz induzida no intervalo de 0 a 0,5 s?"
            ),
            "alternativas": {
                "a": "8 V",
                "b": "12 V",
                "c": "16 V",
                "d": "20 V",
                "e": "24 V"
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0012",
            "pergunta": (
                "12. Qual é a força eletromotriz induzida no intervalo de 0,5 a 1,0 s?"
            ),
            "alternativas": {
                "a": "0 V",
                "b": "4 V",
                "c": "8 V",
                "d": "12 V",
                "e": "16 V"
            },
            "alternativa_correta": "a",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0013",
            "pergunta": (
                "13. Qual é a força eletromotriz induzida no intervalo de 1,0 a 1,5 s?"
            ),
            "alternativas": {
                "a": "2 V",
                "b": "4 V",
                "c": "6 V",
                "d": "8 V",
                "e": "10 V"
            },
            "alternativa_correta": "b",
        },

        # ==================================================
        # EXERCÍCIO 2: PROBLEMA INTEGRADOR (PBL + QUANTITATIVO)
        # ==================================================
        # {"tipo": "titulo", "texto": "Exercício 2: Retornando ao carregador sem fio"},

        {
            "tipo": "texto",
            "texto": (
                "Lembra do carregador sem fio que você está projetando? A bobina do carregador tem 50 espiras "
                "e área de 0,005 m². O campo magnético gerado pela bobina varia senoidalmente com amplitude de 0,02 T "
                "e frequência de 100 kHz (1 kHz = 1000 Hz).\n\n"
                "a) Qual é a força eletromotriz máxima induzida na bobina do celular?\n"
                "b) Se a distância entre as bobinas aumentar, reduzindo o campo magnético na bobina do celular para 0,01 T, "
                "qual será a nova força eletromotriz máxima?\n"
                "c) Para compensar essa perda, quantas espiras a bobina do celular precisaria ter para manter a mesma força eletromotriz?"
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0014",
            "pergunta": (
                "14. Calcule a força eletromotriz máxima induzida na bobina do celular "
                "(fórmula: ℰ_máx = N B A ω, com ω = 2πf)."
            ),
            "alternativas": {
                "a": "3,14 V",
                "b": "6,28 V",
                "c": "12,56 V",
                "d": "25,12 V",
                "e": "31,40 V"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0015",
            "pergunta": (
                "15. Se o campo magnético cair para 0,01 T (metade), qual será a nova força eletromotriz máxima?"
            ),
            "alternativas": {
                "a": "1,57 V",
                "b": "3,14 V",
                "c": "6,28 V",
                "d": "12,56 V",
                "e": "25,12 V"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.04.004.0016",
            "pergunta": (
                "16. Quantas espiras a bobina do celular precisaria ter para manter a força eletromotriz de 6,28 V "
                "com o campo reduzido a 0,01 T?"
            ),
            "alternativas": {
                "a": "50 espiras",
                "b": "75 espiras",
                "c": "100 espiras",
                "d": "150 espiras",
                "e": "200 espiras"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # GABARITO
        # ==================================================
        # {"tipo": "titulo", "texto": "✅ Verificando suas respostas"},

        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "**Questão 1:** Φ = B·A = 0,50 × (0,10)² = 0,50 × 0,01 = 0,005 Wb\n\n"
        #         "**Questão 2:** Φ = B·A·cos60° = 0,005 × 0,5 = 0,0025 Wb\n\n"
        #         "**Questão 3:** ΔΦ = 0,08 - 0,02 = 0,06 Wb; ℰ = 100 × 0,06 / 0,5 = 12 V\n\n"
        #         "**Questão 4:** ΔΦ = 0,01 - 0,05 = -0,04 Wb; |ℰ| = 200 × 0,04 / 0,1 = 80 V\n\n"
        #         "**Questão 5:** ℰ ∝ N × (dΦ/dt); 3 × 0,5 = 1,5 ℰ\n\n"
        #         "**Questão 6:** ℰ_máx ∝ ω; dobrar ω → dobra ℰ_máx\n\n"
        #         "**Questão 7:** ℰ = B·L·v = 0,30 × 0,20 × 5 = 0,30 V\n\n"
        #         "**Questão 8:** ℰ = 0,30 × 0,20 × 2 = 0,12 V\n\n"
        #         "**Questão 9:** ω = 2π × 60 = 377 rad/s; ℰ_máx = 50 × 0,02 × 0,10 × 377 = 3,77 V\n\n"
        #         "**Exercício 1a:** ℰ = 200 × (0,04 - 0)/0,5 = 200 × 0,08 = 16 V\n\n"
        #         "**Exercício 1b:** ℰ = 0 V (fluxo constante)\n\n"
        #         "**Exercício 1c:** ℰ = 200 × (0,01 - 0,04)/0,5 = 200 × (-0,06) = 12 V (módulo)\n\n"
        #         "**Exercício 2a:** ω = 2π × 100000 = 628.000 rad/s; ℰ_máx = 50 × 0,005 × 0,02 × 628000 = 3,14 × 50 = 6,28 V\n\n"
        #         "**Exercício 2b:** ℰ_máx = 6,28 × 0,01/0,02 = 3,14 V\n\n"
        #         "**Exercício 2c:** N = 50 × (0,02/0,01) = 100 espiras"
        #     ),
        # },

    ]