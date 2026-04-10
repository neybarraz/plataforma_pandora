from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Módulo do Professor: Produção de Material Didático sobre o TP4056",
        },
        {
            "tipo": "texto",
            "texto": (
                "Este módulo é um guia para você, futuro professor de Física, produzir um "
                "material didático para seus alunos. O tema é o carregamento de baterias "
                "Li-ion usando o módulo TP4056, abordando conceitos de eletricidade e "
                "modelagem científica. "
                "O material que você produzirá deverá ser didático, acessível a alunos do "
                "Ensino Médio, e baseado nos conceitos apresentados nesta sequência."
            ),
        },

        # -------------------------------------------------
        # OBJETIVO DO MATERIAL
        # -------------------------------------------------
        {
            "tipo": "subtitulo",
            "texto": "Objetivo do material didático",
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao final deste módulo, você deverá ser capaz de produzir um texto "
                "de 4 a 6 páginas que:\n\n"
                "1. Apresente uma situação-problema motivadora.\n"
                "2. Explique a diferença entre tensão e corrente no contexto de carregamento.\n"
                "3. Descreva o modelo CC/CV (Corrente Constante / Tensão Constante).\n"
                "4. Proponha um roteiro experimental simples de verificação.\n"
                "5. Discuta os limites do modelo (aquecimento, degradação da bateria).\n"
                "6. Inclua perguntas de fixação para os alunos."
            ),
        },

        # -------------------------------------------------
        # ESTRUTURA OBRIGATÓRIA
        # -------------------------------------------------
        {
            "tipo": "titulo",
            "texto": "Estrutura obrigatória do seu material",
        },

        {
            "tipo": "subtitulo",
            "texto": "1. Título e situação-problema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Sugestão de título: 'Será que a bateria está carregando? Um estudo de caso com o TP4056'\n\n"
                "A situação-problema deve partir de uma questão concreta:\n"
                "'O LED do módulo acendeu, mas como ter certeza de que a bateria está realmente recebendo carga?'\n\n"
                "Instrução para você: Peça que seus alunos escrevam uma hipótese inicial antes de continuar."
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "2. Grandezas físicas essenciais",
        },
        {
            "tipo": "texto",
            "texto": (
                "Você deve explicar duas grandezas fundamentais:\n\n"
                "- Tensão (V): indica o nível de energia armazenada na bateria. Uma bateria Li-ion totalmente carregada atinge cerca de 4,2 V.\n"
                "- Corrente (I): indica o fluxo real de cargas elétricas. Sem corrente, não há carregamento efetivo.\n\n"
                "Pergunta didática para incluir: 'Se a tensão é 3,8 V mas a corrente é zero, a bateria está carregando? Por quê?'\n\n"
                "Conceito de Física em destaque: diferença entre potencial elétrico (tensão) e movimento de cargas (corrente)."
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "3. O modelo CC/CV (Corrente Constante / Tensão Constante)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Apresente as duas fases de funcionamento do TP4056:\n\n"
                "🔹 Fase CC (Corrente Constante):\n"
                "   - O carregador impõe uma corrente fixa (ex: 1A).\n"
                "   - A tensão da bateria aumenta gradualmente.\n"
                "   - Analogia didática: 'Encher uma piscina com mangueira de vazão fixa — o nível da água sobe de forma constante.'\n\n"
                "🔹 Fase CV (Tensão Constante):\n"
                "   - Quando a tensão atinge 4,2 V, o carregador fixa a tensão nesse valor.\n"
                "   - A corrente diminui gradualmente até quase zero.\n"
                "   - Analogia didática: 'Ao final do enchimento, a torneira fecha sozinha para não transbordar.'\n\n"
                "Modelo elétrico simplificado (inclua um pequeno diagrama descritivo):\n\n"
                "   [Fonte TP4056] → (I) → [Resistência interna] → [Bateria como tensão variável]\n\n"
                "Equação opcional para alunos mais avançados: "
                "\n   $I = \\frac{(V_{carregador} - V_{bateria})}{R_{interna}}$"
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "4. Roteiro experimental para verificação",
        },
        {
            "tipo": "texto",
            "texto": (
                "Proponha um roteiro simples e seguro:\n\n"
                "Materiais: Multímetro, módulo TP4056, bateria Li-ion (3,7 V), fonte USB 5V.\n\n"
                "Passo a passo:\n"
                "1. Meça a tensão da bateria antes de conectá-la ao módulo.\n"
                "2. Conecte a bateria ao TP4056 e ligue a fonte.\n"
                "3. Meça a corrente de carga (multímetro em série com a bateria).\n"
                "4. Aguarde 5 minutos e meça novamente tensão e corrente.\n"
                "5. Anote os dados em uma tabela.\n\n"
                "Tabela sugerida:\n"
                "| Instante | Tensão (V) | Corrente (A) | Fase (CC ou CV?) |\n"
                "|----------|------------|--------------|------------------|\n"
                "| Início   |            |              |                  |\n"
                "| 5 min    |            |              |                  |\n\n"
                "Pergunta de análise: 'Os dados obtidos seguem o comportamento esperado do modelo CC/CV? Justifique.'"
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "5. Limites do modelo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Discuta com seus alunos que nenhum modelo é perfeito. Exemplos:\n\n"
                "• Aquecimento: O TP4056 é linear e dissipa potência como calor:\n"
                "  P = (V_entrada - V_bateria) × I. Se esquentar demais, reduz a corrente automaticamente.\n\n"
                "• Bateria degradada: Resistência interna alta impede que a tensão atinja 4,2 V corretamente.\n\n"
                "• Conexões ruins ou fonte instável: Alteram o comportamento observado.\n\n"
                "Pergunta desafiadora: 'O modelo está errado ou o sistema é mais complexo?'\n\n"
                "Conceito de Ciência destacado: Modelos são ferramentas de interpretação, válidos dentro de certas hipóteses. Reconhecer seus limites é um passo de maturidade técnica."
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "6. Conclusão e perguntas de fixação",
        },
        {
            "tipo": "texto",
            "texto": (
                "Síntese em 3 frases para encerrar o material:\n\n"
                "1. Medir apenas a tensão não é suficiente; a corrente é a evidência direta do carregamento.\n"
                "2. O TP4056 alterna entre controlar corrente (fase CC) e controlar tensão (fase CV) para proteger a bateria.\n"
                "3. Comparar medições reais com o modelo permite identificar se o sistema opera normalmente ou se há falhas/limitações.\n\n"
                "Perguntas de fixação (inclua no final do material):\n\n"
                "1. Por que o TP4056 não pode continuar com corrente constante quando a bateria atinge 4,2 V?\n"
                "   (Resposta esperada: risco de sobrecarga e dano químico à bateria.)\n\n"
                "2. Se a corrente medida for 0,5 A mas a corrente programada é 1 A, liste duas possíveis causas.\n"
                "   (Respostas esperadas: aquecimento do chip, bateria operando em fase CV, resistor PROG errado, fonte insuficiente.)\n\n"
                "3. O que significa, fisicamente, a corrente diminuir na fase CV?\n"
                "   (Resposta esperada: a diferença de potencial entre o carregador e a bateria está diminuindo.)"
            ),
        },

        # -------------------------------------------------
        # RUBRICA DE AUTOAVALIAÇÃO
        # -------------------------------------------------
        {
            "tipo": "titulo",
            "texto": "Rubrica de autoavaliação para o professor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Antes de entregar seu material, verifique se ele atende aos seguintes critérios:\n\n"
                "- Clareza conceitual: Tensão e corrente são claramente diferenciadas, com exemplos.\n"
                "- Didática do modelo CC/CV: As duas fases são explicadas com analogias ou figuras.\n"
                "- Rigor científico: Os limites do modelo são discutidos (aquecimento, degradação, etc.).\n"
                "- Estrutura adequada: O material segue a sequência proposta (problema → conceitos → modelo → experimento → limites → fixação).\n"
                "- Linguagem acessível: O texto é compreensível para alunos do Ensino Médio.\n\n"
                "Se todos os itens estiverem marcados, seu material está pronto para ser utilizado em sala de aula."
            ),
        },

        # -------------------------------------------------
        # EXEMPLO DE ANALOGIA PARA INCLUIR
        # -------------------------------------------------
        {
            "tipo": "titulo",
            "texto": "Exemplos prontos para usar no seu material",
        },

        {
            "tipo": "subtitulo",
            "texto": "Analogia da piscina (fase CC)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Imagine que você está enchendo uma piscina com uma mangueira que tem vazão constante (ex: 10 litros por minuto).\n\n"
                "- A vazão constante da água é análoga à corrente constante (fase CC).\n"
                "- O nível da água subindo é análogo à tensão da bateria aumentando.\n\n"
                "Essa analogia ajuda os alunos a entenderem por que a tensão sobe enquanto a corrente permanece fixa."
            ),
        },

        {
            "tipo": "subtitulo",
            "texto": "Analogia do freio automático (fase CV)",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando a piscina está quase cheia, você reduz a vazão da mangueira para não transbordar.\n"
                "\n- A tensão se estabiliza no nível máximo seguro (4,2 V).\n"
                "- A corrente diminui gradualmente, como a vazão que diminui até quase zero.\n\n"
                "Essa analogia explica por que a corrente cai na fase CV."
            ),
        },

        # -------------------------------------------------
        # SUGESTÃO DE FIGURAS/DESENHOS
        # -------------------------------------------------
        {
            "tipo": "subtitulo",
            "texto": "Sugestões de figuras para incluir",
        },
        {
            "tipo": "texto",
            "texto": (
                "Seu material pode ser enriquecido com desenhos simples como:\n\n"
                "1. Diagrama do circuito: Fonte 5V → TP4056 → Bateria (com multímetros indicando onde medir tensão e corrente).\n"
                "2. Gráfico tensão × tempo: Curva subindo de ~3,0V até 4,2V, depois estabilizando.\n"
                "3. Gráfico corrente × tempo: Patamar constante (CC) seguido de decaimento exponencial (CV).\n\n"
                "Essas figuras podem ser feitas à mão ou com ferramentas simples como o draw.io."
            ),
        },

        # -------------------------------------------------
        # INSTRUÇÃO FINAL
        # -------------------------------------------------
        {
            "tipo": "titulo",
            "texto": "Instrução final",
        },
        {
            "tipo": "texto",
            "texto": (
                "Agora é com você! Utilize este guia como referência para produzir seu material didático. "
                "Lembre-se: seu material será avaliado não apenas pela correção técnica, mas pela capacidade de tornar a Física compreensível e investigativa para alunos do Ensino Médio.\n\n"
                "Bom trabalho, professor!"
            ),
        },
    ]
