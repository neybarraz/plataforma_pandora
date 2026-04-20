def get_blocos() -> list[dict]:
    return [

        # ==================================================
        # INTRODUÇÃO
        # ==================================================
        {
            "tipo": "titulo",
            "texto": "📐 Aplicação matemática da Lei de Ampère"
        },

        {
            "tipo": "texto",
            "texto": (
                "\n Agora que você compreende o significado físico e o formalismo da Lei de Ampère, "
                "é hora de aplicá-la para resolver problemas concretos. Use a equação: "
                "$\\oint \\vec{B} \\cdot d\\vec{\\ell} = \\mu_0 I_{\\text{enc}}$ "
                "para calcular campos magnéticos em diferentes configurações."
            ),
        },

        # ==================================================
        # QUESTÃO 01 - Conceitual (fio retilíneo)
        # ==================================================
        # {"tipo": "titulo", "texto": "📐 Aplicação matemática da Lei de Ampère"},
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0001",
            "pergunta": (
                "1. Considere um fio retilíneo infinito com corrente I = 10 A. "
                "Um segundo fio, paralelo ao primeiro, está a uma distância r e não possui corrente própria. "
                "Qual das afirmações sobre o campo magnético no segundo fio é correta?"
            ),
            "alternativas": {
                "a": "O campo magnético é zero porque o segundo fio não tem corrente.",
                "b": "O campo magnético é constante e independe da distância r.",
                "c": "O campo magnético é proporcional a 1/r e tangente a circunferências centradas no primeiro fio.",
                "d": "O campo magnético é radial e aponta para o primeiro fio.",
                "e": "O campo magnético é paralelo ao segundo fio."
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 02 - Correspondência (curva amperiana)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0002",
            "pergunta": (
                "2. Associe cada situação (coluna da numérica) com a curva amperiana mais adequada (coluna da alfabética):\n\n"
                "- (1) Fio retilíneo infinito.\n"
                "- (2) Solenoide longo.\n"
                "- (3) Toroide (anel).\n"

                "- (A) Retângulo com um lado dentro do solenoide.\n"
                "- (B) Circunferência centrada no fio.\n"
                "- (C) Circunferência dentro do toroide."

                "\n\nA associação correta é:"
            ),
            "alternativas": {
                "a": "1-A, 2-B, 3-C",
                "b": "1-B, 2-A, 3-C",
                "c": "1-B, 2-C, 3-A",
                "d": "1-C, 2-B, 3-A",
                "e": "1-A, 2-C, 3-B"
            },
            "alternativa_correta": "b",
        },

        # ==================================================
        # QUESTÃO 03 - Análise de erro
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0003",
            "pergunta": (
                "3. Um estudante aplicou a Lei de Ampère a um fio retilíneo infinito e escreveu:\n\n"
                "$$\\oint \\vec{B} \\cdot d\\vec{\\ell} = \\mu_0 I $$\n\n"
                "$$B \\oint d\\ell = \\mu_0 I $$\n\n"
                "$$B(2\\pi r) = \\mu_0 I$$\n\n"
                "Ele concluiu que B = μ₀I/(2πr). O raciocínio está correto, mas ele cometeu um erro conceitual. Qual é?"
            ),
            "alternativas": {
                "a": "Ele esqueceu que a corrente deve estar em amperes.",
                "b": "Ele assumiu que B é constante na curva, o que é verdade por simetria. Na verdade, não há erro.",
                "c": "Ele usou a curva errada; deveria ser um retângulo.",
                "d": "Ele esqueceu de considerar a direção do campo; a equação está dimensionalmente errada.",
                "e": "Ele não verificou que a corrente encerrada depende da orientação da curva."
            },
            "alternativa_correta": "b",
        },

        # ==================================================
        # QUESTÃO 04 - Ordenação (sequência lógica)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0004",
            "pergunta": (
                "4. Ordene os passos corretos para aplicar a Lei de Ampère a um problema:\n\n"
                "- (1) Calcular a corrente encerrada I_enc.\n"
                "- (2) Escolher uma curva amperiana que respeite a simetria.\n"
                "- (3) Resolver para B.\n"
                "- (4) Analisar a simetria do problema.\n"
                "- (5) Calcular a integral ∮ B·dℓ.\n\n"
                "A sequência correta é:"
            ),
            "alternativas": {
                "a": "4 → 2 → 5 → 1 → 3",
                "b": "2 → 4 → 1 → 5 → 3",
                "c": "1 → 2 → 4 → 5 → 3",
                "d": "4 → 1 → 2 → 5 → 3",
                "e": "2 → 5 → 1 → 4 → 3"
            },
            "alternativa_correta": "a",
        },

        # ==================================================
        # QUESTÃO 05 - Verdadeiro ou Falso (múltiplas afirmações)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0005",
            "pergunta": (
                "5. Considere as afirmações sobre a Lei de Ampère:\n\n"
                "- I. A lei é válida apenas para correntes estacionárias.\n"
                "- II. A corrente $I_{enc}$ inclui apenas correntes que atravessam a superfície delimitada pela curva.\n"
                "- III. O campo $B$ na integral é gerado apenas pelas correntes dentro da curva.\n\n"
                "Quais estão corretas?"
            ),
            "alternativas": {
                "a": "Apenas I.",
                "b": "Apenas II.",
                "c": "Apenas I e II.",
                "d": "Apenas II e III.",
                "e": "I, II e III."
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 06 - Proporcionalidade (fio)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0006",
            "pergunta": (
                "6. Um fio retilíneo infinito produz um campo magnético $B$ a uma distância $r$. "
                "Se a corrente for duplicada e a distância for reduzida à metade, o novo campo magnético será:"
            ),
            "alternativas": {
                "a": "B/2",
                "b": "B",
                "c": "2B",
                "d": "4B",
                "e": "8B"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 07 - Proporcionalidade (solenoide)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0007",
            "pergunta": (
                "7. Um solenoide ideal tem campo interno $B$. Se o número de espiras por metro for triplicado "
                "e a corrente for reduzida à metade, o novo campo será:"
            ),
            "alternativas": {
                "a": "B/6",
                "b": "B/3",
                "c": "1,5 B",
                "d": "3B",
                "e": "6B"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 08 - Comparação fio × solenoide
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0008",
            "pergunta": (
                "8. Um fio retilíneo e um solenoide longo são percorridos pela mesma corrente I. "
                "Qual afirmação sobre seus campos magnéticos é verdadeira?"
            ),
            "alternativas": {
                "a": "Ambos os campos decaem com 1/r.",
                "b": "O campo do fio é uniforme; o campo do solenoide decai com 1/r.",
                "c": "O campo do fio decai com 1/r; o campo interno do solenoide é uniforme.",
                "d": "Ambos os campos são uniformes.",
                "e": "Ambos os campos independem da corrente."
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 09 - Conceitual sem cálculo
        # ==================================================
        {
            "tipo": "questao_texto",
            "id": "solucao.03.004.0009",
            "pergunta": (
                "9. Sem fazer contas, responda:\n\n"
                "- Se você dobrar a corrente em um fio retilíneo, o que acontece com o campo magnético a uma distância r?\n"
                "- Se você dobrar a distância r, mantendo a corrente constante, o que acontece com o campo?\n\n"
                "Explique usando a Lei de Ampère."
            ),
            "altura": 150,
        },

        # ==================================================
        # EXERCÍCIO 1: FIO RETILÍNEO (NUMÉRICO)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0010",
            "pergunta": (
                "10. Um fio retilíneo muito longo é percorrido por uma corrente elétrica de I = 5 A."
                " Calcule o campo magnético a uma distância r = 0,10 m do fio."
            ),
            "alternativas": {
                "a": "0,5 × 10⁻⁵ T",
                "b": "1,0 × 10⁻⁵ T",
                "c": "2,0 × 10⁻⁵ T",
                "d": "5,0 × 10⁻⁵ T",
                "e": "10,0 × 10⁻⁵ T"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0011",
            "pergunta": (
                "11. Um fio retilíneo muito longo é percorrido por uma corrente elétrica de I = 5 A. "
                "A que distância o campo magnético vale B = 1,0 × 10⁻⁵ T?"
            ),
            "alternativas": {
                "a": "0,05 m",
                "b": "0,10 m",
                "c": "0,20 m",
                "d": "0,50 m",
                "e": "1,00 m"
            },
            "alternativa_correta": "b",
        },

        # ==================================================
        # EXERCÍCIO 2: SOLENOIDE (NUMÉRICO) - MÚLTIPLA ESCOLHA
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0012",
            "pergunta": (
                "12. Você precisa projetar um solenoide que gere um campo magnético de B = 0,03 T no vácuo, "
                "utilizando uma corrente máxima de I = 2 A. "
                "Qual deve ser a densidade de espiras n (espiras por metro) necessária?"
            ),
            "alternativas": {
                "a": "aproximadamente 5.970 espiras/m",
                "b": "aproximadamente 11.940 espiras/m",
                "c": "aproximadamente 23.880 espiras/m",
                "d": "aproximadamente 47.760 espiras/m",
                "e": "aproximadamente 2.985 espiras/m"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0013",
            "pergunta": (
                "13. Você precisa projetar um solenoide que gere um campo magnético de B = 0,03 T no vácuo, "
                "utilizando uma corrente máxima de I = 2 A. "
                "Se o solenoide tiver comprimento L = 0,5 m, quantas espiras serão necessárias?"
            ),
            "alternativas": {
                "a": "aproximadamente 2.985 espiras",
                "b": "aproximadamente 5.970 espiras",
                "c": "aproximadamente 11.940 espiras",
                "d": "aproximadamente 23.880 espiras",
                "e": "aproximadamente 1.500 espiras"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0014",
            "pergunta": (
                "14. Você precisa projetar um solenoide que gere um campo magnético de $B = 0,03~T$ no vácuo, "
                "utilizando uma corrente máxima de $I = 2~A$. "
                "Se você dobrar o comprimento do solenoide, mantendo o mesmo número total de espiras e a mesma corrente, "
                "o que acontece com o campo magnético B?"
            ),
            "alternativas": {
                "a": "B dobra",
                "b": "B permanece o mesmo",
                "c": "B cai pela metade",
                "d": "B quadruplica",
                "e": "B cai para um quarto"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # EXERCÍCIO 3: PROBLEMA INTEGRADOR (PBL + QUANTITATIVO)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0015",
            "pergunta": (
                "15. Lembra do motor do carro elétrico? O motor tem um solenoide com 500 espiras "
                "distribuídas em um comprimento de 0,25 m. A corrente máxima suportada pelo fio é 10 A. "
                "Calcule o campo magnético gerado pelo solenoide."
            ),
            "alternativas": {
                "a": "1,26 × 10⁻² T",
                "b": "2,51 × 10⁻² T",
                "c": "5,02 × 10⁻² T",
                "d": "1,00 × 10⁻² T",
                "e": "3,14 × 10⁻² T"
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0016",
            "pergunta": (
                "16. Lembra do motor do carro elétrico? O motor tem um solenoide com 500 espiras "
                "distribuídas em um comprimento de 0,25 m. A corrente máxima suportada pelo fio é 10 A. "
                "Se o torque é proporcional a B × I, qual modificação é mais eficiente para aumentar o torque: "
                "dobrar a corrente ou dobrar o número de espiras? (Considere que dobrar espiras dobra n e, portanto, dobra B)"
            ),
            "alternativas": {
                "a": "Dobrar a corrente é mais eficiente porque aumenta o torque mais rapidamente.",
                "b": "Dobrar o número de espiras é mais eficiente porque produz o mesmo ganho de torque com menos aquecimento.",
                "c": "Ambas as modificações são igualmente eficientes.",
                "d": "Dobrar a corrente não afeta o torque.",
                "e": "Dobrar o número de espiras não afeta o torque."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.03.004.0017",
            "pergunta": (
                "17. Lembra do motor do carro elétrico? O motor tem um solenoide com 500 espiras "
                "distribuídas em um comprimento de 0,25 m. A corrente máxima suportada pelo fio é 10 A. "
                "Qual das duas modificações (dobrar corrente ou dobrar espiras) causa mais superaquecimento? Por quê?"
            ),
            "alternativas": {
                "a": "Dobrar espiras causa mais aquecimento porque aumenta a resistência do fio.",
                "b": "Dobrar corrente causa mais aquecimento porque a potência dissipada é proporcional a I² (Efeito Joule).",
                "c": "Ambas causam o mesmo aquecimento.",
                "d": "Nenhuma das duas causa aquecimento significativo.",
                "e": "Dobrar espiras causa mais aquecimento porque o campo magnético maior gera mais calor."
            },
            "alternativa_correta": "b",
        },

    ]