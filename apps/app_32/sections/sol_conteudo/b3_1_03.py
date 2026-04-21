def get_blocos() -> list[dict]:
    return [

        {"tipo": "titulo", "texto": "Lista de exercícios: Hidrostática"},

        {
            "tipo": "texto",
            "texto": (
                "Resolva as questões abaixo aplicando os conceitos e equações da estática dos fluidos. "
                "Todas as questões são de múltipla escolha com uma única alternativa correta."
            ),
        },

        # ==================================================
        # QUESTÃO 1 - DENSIDADE E MASSA ESPECÍFICA
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.001",
            "pergunta": (
                "1. Um engenheiro precisa armazenar 500 litros de um fluido industrial cuja densidade é 0,85 g/cm³. "
                "Qual a massa total do fluido armazenado, em quilogramas?\n\n"
                "Dados: 1 L = 0,001 m³; ρ_água = 1000 kg/m³"
            ),
            "alternativas": {
                "a": "425 kg",
                "b": "500 kg",
                "c": "588 kg",
                "d": "425.000 kg",
                "e": "500.000 kg"
            },
            "alternativa_correta": "a",
        },

        # ==================================================
        # QUESTÃO 2 - PRESSÃO E ÁREA
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.002",
            "pergunta": (
                "2. Uma prensa hidráulica possui um êmbolo menor com área de 5 cm² e um êmbolo maior com área de 500 cm². "
                "Se uma força de 200 N é aplicada no êmbolo menor, qual a força resultante no êmbolo maior, em kN?"
            ),
            "alternativas": {
                "a": "2 kN",
                "b": "5 kN",
                "c": "10 kN",
                "d": "20 kN",
                "e": "50 kN"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 3 - PRESSÃO HIDROSTÁTICA
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.003",
            "pergunta": (
                "3. Um mergulhador desce a uma profundidade de 30 metros em água doce (ρ = 1000 kg/m³). "
                "Considerando a pressão atmosférica na superfície como 1,01 × 10⁵ Pa e g = 10 m/s², "
                "qual a pressão absoluta sobre o mergulhador, em atm? (1 atm = 1,01 × 10⁵ Pa)"
            ),
            "alternativas": {
                "a": "1 atm",
                "b": "2 atm",
                "c": "3 atm",
                "d": "4 atm",
                "e": "5 atm"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 4 - EMPUXO E FLUTUAÇÃO
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.004",
            "pergunta": (
                "4. Um bloco cúbico de madeira com aresta de 0,5 m e densidade 600 kg/m³ flutua na água (ρ = 1000 kg/m³). "
                "Qual a altura da parte submersa do bloco? (g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "0,10 m",
                "b": "0,20 m",
                "c": "0,30 m",
                "d": "0,40 m",
                "e": "0,50 m"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 5 - PARADOXO HIDROSTÁTICO
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.005",
            "pergunta": (
                "5. Dois recipientes têm a mesma altura de água (h = 2 m). O recipiente A tem base larga e volume de 10 m³. "
                "O recipiente B tem base estreita e volume de 2 m³. Comparando a pressão no fundo de ambos:"
            ),
            "alternativas": {
                "a": "A pressão em A é maior porque tem mais água.",
                "b": "A pressão em B é maior porque a água está mais concentrada.",
                "c": "As pressões são iguais porque dependem apenas da altura.",
                "d": "A pressão em A é o dobro da pressão em B.",
                "e": "A pressão em B é 5 vezes maior que em A."
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 6 - APLICAÇÃO DE PASCAL EM FREIOS
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.006",
            "pergunta": (
                "6. O sistema de freio hidráulico de um carro tem cilindro mestre com área de 3 cm² e pistões nas rodas "
                "com área de 12 cm² cada. Se o motorista aplica uma força de 150 N no pedal, qual a força aplicada "
                "em cada roda? (Considere o sistema ideal, sem perdas)"
            ),
            "alternativas": {
                "a": "150 N",
                "b": "300 N",
                "c": "450 N",
                "d": "600 N",
                "e": "1200 N"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 7 - DENSIDADE RELATIVA
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.007",
            "pergunta": (
                "7. Um corpo de 2 kg ocupa um volume de 0,0025 m³. Determine a densidade desse material "
                "e verifique se ele afunda ou flutua na água (ρ_água = 1000 kg/m³)."
            ),
            "alternativas": {
                "a": "ρ = 500 kg/m³, flutua",
                "b": "ρ = 800 kg/m³, flutua",
                "c": "ρ = 1000 kg/m³, indiferente",
                "d": "ρ = 1200 kg/m³, afunda",
                "e": "ρ = 800 kg/m³, afunda"
            },
            "alternativa_correta": "b",
        },

        # ==================================================
        # QUESTÃO 8 - PRESSÃO EM BARragem
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.008",
            "pergunta": (
                "8. Uma barragem retém água até uma profundidade de 15 m. Qual a pressão manométrica (excluindo a atmosférica) "
                "no ponto mais profundo? Considere ρ_água = 1000 kg/m³ e g = 9,8 m/s²."
            ),
            "alternativas": {
                "a": "1,47 × 10² Pa",
                "b": "1,47 × 10⁴ Pa",
                "c": "1,47 × 10⁵ Pa",
                "d": "1,47 × 10⁶ Pa",
                "e": "1,47 × 10⁷ Pa"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 9 - EMPUXO EM SUBMARINO
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.009",
            "pergunta": (
                "9. Um submarino tem volume total de 500 m³ e está completamente submerso na água do mar "
                "(ρ = 1030 kg/m³). Qual o empuxo exercido sobre ele? (g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "5,00 × 10⁵ N",
                "b": "5,00 × 10⁶ N",
                "c": "5,15 × 10⁵ N",
                "d": "5,15 × 10⁶ N",
                "e": "5,15 × 10⁷ N"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 10 - PRESSÃO EM DIFERENTES PROFUNDIDADES
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.010",
            "pergunta": (
                "10. Um tanque contém duas camadas de fluidos imiscíveis: 2 m de óleo (ρ = 800 kg/m³) sobre 3 m de água (ρ = 1000 kg/m³). "
                "Qual a pressão manométrica no fundo do tanque? (g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "1,6 × 10⁴ Pa",
                "b": "3,0 × 10⁴ Pa",
                "c": "4,6 × 10⁴ Pa",
                "d": "6,2 × 10⁴ Pa",
                "e": "7,8 × 10⁴ Pa"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 11 - PRINCÍPIO DE PASCAL COM MÚLTIPLOS ÊMBOLOS
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.011",
            "pergunta": (
                "11. Uma prensa hidráulica possui três êmbolos interligados pelo mesmo fluido. "
                "Os êmbolos têm áreas: A₁ = 4 cm², A₂ = 20 cm² e A₃ = 100 cm². "
                "Se uma força de 80 N é aplicada no êmbolo 1, qual a força resultante no êmbolo 3?"
            ),
            "alternativas": {
                "a": "400 N",
                "b": "800 N",
                "c": "1000 N",
                "d": "2000 N",
                "e": "4000 N"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 12 - EMPUXO COM CORPO PARCIALMENTE IMERSO
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.012",
            "pergunta": (
                "12. Um cilindro de madeira de altura 0,8 m e densidade 450 kg/m³ flutua na água (ρ = 1000 kg/m³). "
                "Qual a altura da parte emersa (acima da água)? (g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "0,24 m",
                "b": "0,36 m",
                "c": "0,44 m",
                "d": "0,56 m",
                "e": "0,68 m"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 13 - PRESSÃO EM TUBULAÇÃO (FLUIDO EM REPOUSO)
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.013",
            "pergunta": (
                "13. Um reservatório fechado contém água (ρ = 1000 kg/m³) e ar pressurizado acima da superfície. "
                "Um manômetro instalado a 4 m de profundidade mede 1,8 × 10⁵ Pa (pressão manométrica). "
                "Qual a pressão manométrica do ar no topo do reservatório? (g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "1,0 × 10⁵ Pa",
                "b": "1,2 × 10⁵ Pa",
                "c": "1,4 × 10⁵ Pa",
                "d": "1,6 × 10⁵ Pa",
                "e": "1,8 × 10⁵ Pa"
            },
            "alternativa_correta": "c",
        },

        # ==================================================
        # QUESTÃO 14 - EQUILÍBRIO ENTRE DOIS FLUIDOS
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.014",
            "pergunta": (
                "14. Um tubo em U contém mercúrio (ρ = 13.600 kg/m³). Em um dos ramos, adiciona-se água (ρ = 1000 kg/m³) "
                "até que a coluna de água tenha altura de 0,68 m. Qual a diferença de altura entre os níveis de mercúrio "
                "nos dois ramos? (g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "0,005 m",
                "b": "0,010 m",
                "c": "0,025 m",
                "d": "0,050 m",
                "e": "0,100 m"
            },
            "alternativa_correta": "d",
        },

        # ==================================================
        # QUESTÃO 15 - FORÇA EM SUPERFÍCIE SUBMERSA
        # ==================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "solucao.01.003.015",
            "pergunta": (
                "15. Uma comporta retangular vertical de 2 m de largura e 3 m de altura está completamente submersa em água, "
                "com seu topo a 1 m da superfície. Qual a força resultante da água sobre a comporta? "
                "(ρ = 1000 kg/m³, g = 10 m/s²)"
            ),
            "alternativas": {
                "a": "6,0 × 10⁴ N",
                "b": "1,2 × 10⁵ N",
                "c": "1,8 × 10⁵ N",
                "d": "2,4 × 10⁵ N",
                "e": "3,0 × 10⁵ N"
            },
            "alternativa_correta": "d",
        },
        # ==================================================
        # # QUESTÃO 11 - GABARITO COMENTADO
        # # ==================================================
        # {"tipo": "titulo", "texto": "Gabarito comentado"},

        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "1. **A** - m = ρ × V = 850 kg/m³ × 0,5 m³ = 425 kg\n\n"
        #         "2. **D** - F₂ = F₁ × (A₂/A₁) = 200 × (500/5) = 200 × 100 = 20.000 N = 20 kN\n\n"
        #         "3. **D** - P = P₀ + ρgh = 1,01×10⁵ + 1000×10×30 = 1,01×10⁵ + 3×10⁵ = 4,01×10⁵ Pa ≈ 4 atm\n\n"
        #         "4. **C** - Empuxo = Peso → ρ_água × g × A_sub = ρ_madeira × g × A_total → h_sub = (ρ_madeira/ρ_água) × h_total = 0,6 × 0,5 = 0,30 m\n\n"
        #         "5. **C** - A pressão hidrostática depende apenas da profundidade, não do volume ou formato.\n\n"
        #         "6. **D** - F₂ = F₁ × (A₂/A₁) = 150 × (12/3) = 150 × 4 = 600 N\n\n"
        #         "7. **B** - ρ = m/V = 2/0,0025 = 800 kg/m³, menor que 1000 kg/m³, portanto flutua.\n\n"
        #         "8. **C** - P = ρgh = 1000 × 9,8 × 15 = 147.000 Pa = 1,47 × 10⁵ Pa\n\n"
        #         "9. **D** - E = ρ × g × V = 1030 × 10 × 500 = 5.150.000 N = 5,15 × 10⁶ N\n\n"
        #         "10. **C** - P = ρ_óleo × g × h_óleo + ρ_água × g × h_água = (800×10×2) + (1000×10×3) = 16.000 + 30.000 = 46.000 Pa = 4,6 × 10⁴ Pa"
        #     ),
        # },

    ]