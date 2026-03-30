from __future__ import annotations
import streamlit as st

def _get_valor_limpo(qid: str) -> float | None:
    chave = f"problema_{qid}"
    valor_bruto = st.session_state.get(chave)

    if valor_bruto is None or str(valor_bruto).strip() in ["", "—", "None"]:
        return None

    try:
        return float(str(valor_bruto).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None

def _comparativo_correntes() -> str:
    # 1. Coleta os valores (Certifique-se que os IDs batem com o get_blocos)
    i_medida = _get_valor_limpo("problema.01.001.0013")  # Coletado na Etapa 1
    i_calculada = _get_valor_limpo("problema.01.002.0001")  # Calculado na Etapa 2

    # 2. Só executa se ambos os valores existirem
    if i_medida is not None and i_calculada is not None:
        # Cálculo da diferença absoluta e percentual para o diagnóstico
        diferenca = round(i_medida - i_calculada, 2)
        # Evita divisão por zero se i_calculada for 0
        porcentagem = round((diferenca / i_calculada) * 100, 1) if i_calculada != 0 else 0

        # Define um status simplificado para o aluno
        if i_medida > i_calculada:
            status = "⚠️ **Atenção:** Corrente medida acima da nominal (Possível Sobrecarga)."
        else:
            status = "✅ **Normal:** Corrente medida dentro dos limites nominais."

        return (
            f"Diagnóstico Comparativo\n\n"
            f"| Parâmetro | Valor Registrado | Unidade |\n"
            f"| :--- | :---: | :---: |\n"
            f"| Corrente Nominal Calculada | **{i_calculada}** | A |\n"
            f"| Corrente Real Medica | **{i_medida}** | A |\n\n"
            f"**Análise Técnica:**\n"
            f"- Diferença absoluta: **{diferenca} A**\n"
            f"- Desvio percentual: **{porcentagem}%**\n\n"
            f"{status}"
        )

    # 3. Mensagem caso os dados ainda não tenham sido preenchidos
    return (
        "### ⏳ Aguardando Dados para Comparação\n"
        "Para visualizar o diagnóstico, preencha a **Corrente Real** (Etapa 1) "
        "e o **Valor Calculado** da Corrente Nominal acima."
    )

def _comparativo_bitola() -> str:
    # 1. Coleta os valores (IDs exatos do seu get_blocos)
    bitola_atual = _get_valor_limpo("problema.01.001.0010")  # mm² (Etapa 1)
    i_calculada = _get_valor_limpo("problema.01.002.0001")   # A (Etapa 2)

    # 2. Só executa se ambos os valores existirem
    if bitola_atual is not None and i_calculada is not None:
        
        # Tabela de referência mental (Dicionário Simples)
        # Chave: Bitola (mm²) -> Valor: Capacidade aproximada (A)
        referencias = {
            1.5: 15.5,
            2.5: 21.0,
            4.0: 28.0,
            6.0: 36.0,
            10.0: 50.0,
            16.0: 68.0
        }

        # Busca a capacidade estimada para a bitola informada
        capacidade_est = referencias.get(bitola_atual, "Não mapeado")

        # Lógica de diagnóstico preliminar
        if isinstance(capacidade_est, float):
            if i_calculada > capacidade_est:
                status = "⚠️ **Risco:** Corrente nominal acima da capacidade estimada do cabo atual."
            elif i_calculada > (capacidade_est * 0.9):
                status = "🟡 **Limite:** Cabo operando muito próximo da capacidade máxima."
            else:
                status = "✅ **Folga:** A bitola atual parece comportar a corrente nominal."
        else:
            status = "**Análise:** Bitola fora da tabela de referência rápida. Verifique as tabelas da NBR 5410."

        return (
            f"Confronto Preliminar: Carga vs. Condutor\n\n"
            f"| Parâmetro | Valor Identificado | Unidade |\n"
            f"| :--- | :---: | :---: |\n"
            f"| **Corrente Nominal ($I_n$)** | {i_calculada} | A |\n"
            f"| **Bitola Instalada** | {bitola_atual} | mm² |\n\n"
            f" <br>"
        )

    # 3. Mensagem de espera
    return (
        "⏳ Aguardando Dados\n"
        "Preencha a **Bitola Atual** (Etapa 1) e calcule a **Corrente Nominal** acima para ver o diagnóstico."
    )


def get_blocos() -> list[dict]:
    return [


        # ============================================================
        # ETAPA 2 — DIMENSIONAMENTO E CÁLCULO
        # ============================================================
        { "tipo": "titulo", "texto": "ETAPA 2 — Cálculo da Corrente de Projeto" },

        { "tipo": "texto", "texto": (
            "Na Etapa 1, seu foco foi a inspeção e a coleta de dados. Agora, iniciamos a modelagem matemática. "
            "A pergunta fundamental que guiará esta fase é:\n\n " 
            "Qual é a corrente exata que este motor deve solicitar da rede em condições nominais de operação?\n\n"
            "Sem esta resposta, é impossível selecionar condutores ou dispositivos de proteção de forma técnica. "
            "O dimensionamento começa com a definição precisa da carga."
            )
        },

        { "tipo": "titulo",  "texto": "1. A Equação da Corrente Trifásica" },

        { "tipo": "texto", "texto": (
            "Para um sistema trifásico equilibrado, a corrente nominal (In) é o resultado da potência mecânica "
            "solicitada no eixo, corrigida pelas perdas elétricas (fator de potência) e mecânicas (rendimento). "
            "A relação fundamental é dada por:"
        )},

        { "tipo": "equacao",
            "latex": r"I_{n} = \frac{P}{\sqrt{3} \cdot V \cdot \cos\phi \cdot \eta}"
        },

        { "tipo": "texto", "texto": (
                "Onde:\n\n"
                "- P: Potência ativa do motor (em Watts)\n"
                "- V: Tensão nominal de linha (V)\n"
                "- cos φ: Fator de potência\n"
                "- η: Rendimento do motor\n\n"
                "Atenção ao detalhe técnico: Os motores geralmente apresentam a potência em kW. "
                "Para que a equação funcione corretamente, você deve converter esse valor para Watts (1 kW = 1000 W) "
                "antes de realizar a divisão."
            )
        },

        # ============================================================
        # SUBSTITUIÇÃO E CÁLCULO REAL
        # ============================================================
        { "tipo": "titulo", "texto": "2. Substituição dos Dados Reais"},

        { "tipo": "texto", "texto": (
            "Neste momento, a teoria se conecta aos dados que você extraiu diretamente da placa do motor na Etapa 1. "
            "A precisão do seu dimensionamento depende da fidelidade com que esses valores são aplicados na equação. "
            "Substitua os parâmetros nominais (Potência, Tensão, Fator de Potência e Rendimento) conforme o modelo abaixo, "
            "utilizando os valores reais registrados no seu levantamento de campo:"
        )},

        { "tipo": "equacao",
            "latex": r"I_{n} = \frac{P_{real}}{\sqrt{3} \cdot V_{nominal} \cdot \cos\phi \cdot \eta}"
        },

        { "tipo": "texto", "texto": (
            "Recomendação Técnica:\n\n"
            "- Evite arredondamentos prematuros durante as etapas intermediárias do cálculo.\n "
            "- Mantenha o maior número de casas decimais possível até chegar ao resultado final da Corrente Nominal (In).\n \n"
            "Isso garante que a margem de erro não se acumule, algo crítico quando passarmos para a escolha dos dispositivos de proteção."
        )},
        
        { "tipo": "entrada_numerica_inline", "id": "problema.01.002.0001",
            "rotulo": "Valor calculado de Corrente Nominal (In)", 
            "unidade": "A", 
            "placeholder": "Ex: 12.5"
        },

        # ============================================================
        # 3. CONFRONTO COM A MEDIÇÃO REAL
        # ============================================================
        { "tipo": "titulo", "texto": "3. Diagnóstico: Corrente Calculada vs. Medida" },

        { "tipo": "texto", "texto": (
                "Na Etapa 1, você utilizou o alicate amperímetro para registrar a corrente real em plena operação. "
                "Agora, coloque o valor calculado (I_n) lado a lado com o valor medido (I_medida)."
                "Em um cenário ideal, a corrente medida deve ser próxima ou ligeiramente inferior à nominal, "
                "indicando que o motor trabalha dentro de sua zona de eficiência. Valores muito discrepantes "
                "podem sinalizar subdimensionamento de cabos (queda de tensão), problemas mecânicos na bomba "
                "ou oscilações severas na rede elétrica."
        )},

        { "tipo": "texto", "texto": _comparativo_correntes() },

       { "tipo": "texto", "texto": (
                "Lembre-se: Se I_{medida} > I_{n}, o motor está operando em regime de sobrecarga, "
                "o que reduz drasticamente a vida útil do isolamento dos enrolamentos devido ao calor excessivo."
        )},

        {
            "tipo": "questao_texto",
            "id": "problema.01.002.0002",
            "pergunta": (
                "Análise Técnica: A corrente medida em campo é coerente com a nominal calculada? "
                "Justifique comparando os valores e aponte possíveis causas para a diferença encontrada."
            )
        },
        
        { "tipo": "texto", "texto": (
                "Lembre-se: Se I_{medida} > I_{n}, o motor está operando em regime de sobrecarga, "
                "o que reduz drasticamente a vida útil do isolamento dos enrolamentos devido ao calor excessivo."
        )},
 

        # ============================================================
        # 5. LEITURA FÍSICA E SENSIBILIDADE DO CÁLCULO
        # ============================================================
        { "tipo": "titulo", "texto": "5. Análise de Sensibilidade: A Física do Condutor" },

        { "tipo": "texto", "texto": (
            "Um erro comum é olhar para a equação da corrente apenas como um procedimento matemático. "
            "Para o engenheiro, essa fórmula revela como as ineficiências do sistema impactam diretamente "
            "o custo e a segurança da instalação. Observe as relações de proporcionalidade:"
        )},

        { "tipo": "equacao",
            "latex": r"I_{n} = \frac{P \uparrow}{\sqrt{3} \cdot V \downarrow \cdot \cos\phi \downarrow \cdot \eta \downarrow} \implies I_{n} \uparrow \uparrow"
        },

        { "tipo": "texto", "texto": (
            "Note que a corrente (I_n) é o 'ajuste de contas' do sistema. Se a qualidade da energia ou do motor cai, "
            "o fluxo de elétrons precisa aumentar para entregar a mesma potência mecânica no eixo:\n\n"
            "* **Queda de Tensão ($V$):** se a rede entrega menos tensão, a corrente sobe para compensar.\n"
            "* **Baixo Fator de Potência ($\cos\phi$):** exige mais corrente circulante para realizar o mesmo trabalho.\n"
            "* **Baixo Rendimento ($\eta$):** o calor perdido dentro do motor precisa ser pago com mais corrente da rede.\n\n"
                "**O Impacto no Condutor:**\n"
                "Corrente elevada não é apenas um número; é uma solicitação física severa que gera:\n\n"
                "1. **Efeito Joule ($I^2R$):** o aquecimento do cabo sobe com o **quadrado** da corrente. Dobrar a corrente quadruplica o calor.\n"
                "2. **Queda de Tensão Progressiva:** quanto maior a corrente, maior a perda de tensão no cabo, gerando um ciclo vicioso.\n"
                "3. **Degradação Térmica:** O isolamento do cabo (PVC/XLPE) possui um limite de temperatura. Superar esse limite reduz drasticamente a vida útil da instalação."
            )
        },

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=urzRRrJuagE",},
        {"tipo": "video", "url": "https://www.youtube.com/watch?v=RlKngsvhs1w",},
        {"tipo": "video", "url": "https://www.youtube.com/watch?v=HHpZWMVLIyQ",},


        { "tipo": "questao_multipla_escolha", "id": "problema.01.002.0003",
            "pergunta": "Por que um motor com baixo rendimento (η) exige um condutor com bitola maior?",
            "alternativas": {
                "a": "Porque o baixo rendimento aumenta a tensão nos terminais do motor.",
                "b": "Porque para compensar as perdas internas do motor, ele solicita uma corrente maior da rede para entregar a potência no eixo.",
                "c": "Porque o rendimento altera a resistência interna dos cabos de cobre.",
                "d": "Porque motores de baixo rendimento operam obrigatoriamente em tensões mais elevadas."
            },
            "alternativa_correta": "b"
        },

        # ============================================================
        # 6. VERIFICAÇÃO PRELIMINAR: O OLHAR CLÍNICO
        # ============================================================
        { "tipo": "titulo",  "texto": "6. Verificação Preliminar: Confronto com a Instalação Atual"},

        { "tipo": "texto", "texto": (
            "Antes de consultarmos as tabelas normativas de capacidade de condução (NBR 5410), um bom projetista"
            "realiza uma análise de ordem de grandeza. O objetivo aqui é identificar se a instalação atual possui "
            "erros grosseiros ou se está dentro de uma faixa de operação razoável."
        )},

        { "tipo": "texto", "texto": (
            "Considere o seguinte raciocínio rápido:\n\n"
            "* **Subdimensionamento crítico:** se a sua corrente calculada ($I_{n}$) é de 25 A e o cabo "
            "instalado em campo é de 1,5 mm², você já tem um indício matemático de risco de incêndio.\n"
            "* **Superdimensionamento:** se a corrente é de 5 A e o cabo é de 16 mm², há um desperdício "
            "financeiro evidente no projeto original."
            )
        },

        { "tipo": "texto", "texto": _comparativo_bitola() },

        { "tipo": "texto", "texto": (
                "Dica Técnica: Na prática, condutores de 2,5 mm² costumam suportar correntes na faixa de 20 A a 24 A "
                "em condições ideais. Use essa referência mental para avaliar o sistema que você está auditando."
        )},  

        { "tipo": "questao_texto", "id": "problema.01.002.0004",
            "pergunta": (
                "Análise de Compatibilidade: Com base na sua experiência e nos valores calculados, "
                "a bitola encontrada no local (mm²) parece ser tecnicamente compatível com a corrente "
                "solicitada pelo motor? Justifique sua suspeita sem utilizar tabelas por enquanto."
            )
        },

        # ============================================================
        # SÍNTESE DA ETAPA 2: A TRANSIÇÃO PARA A NORMA
        # ============================================================
        { "tipo": "titulo", "texto": "Recapitulação Técnica: Consolidação do Diagnóstico" },

        { "tipo": "texto",  "texto": (
            "Nesta etapa, você deixou de lado as suposições e construiu a base matemática do seu projeto. "
            "Ao converter a potência mecânica em corrente elétrica real, você concluiu as seguintes ações críticas:\n\n"
            "* **Modelagem Trifásica:** aplicou a equação fundamental considerando as perdas de FP e Rendimento.\n"
            "* **Confronto de Grandezas:** validou se a corrente que 'deveria' existir (teórica) é compatível com a que 'realmente' circula (medida).\n"
            "* **Análise de Sensibilidade:** identificou como as ineficiências do sistema elevam o esforço térmico nos cabos.\n"
            "* **Diagnóstico Preliminar:** confrontou a carga com a bitola instalada, gerando suas primeiras hipóteses de engenharia."
        )},

        { "tipo": "texto", "texto": (
                "O que muda a partir de agora?\n\n"
                "Até aqui, trabalhamos com a física pura. Na próxima etapa, entraremos no rigor da **NBR 5410**. "
                "A Corrente Nominal ($I_{n}$) que você calculou será agora submetida aos **Fatores de Correção Ambiental** "
                "(temperatura e agrupamento), transformando-se na **Corrente de Projeto ($I_{b}$)**. "
                "A partir deste ponto, as suas decisões não serão mais baseadas em 'feeling', mas em critérios normativos de segurança e capacidade de condução."
            )
        },

        {"tipo": "texto", "texto": (
            "⏭️ Próximo Passo: Dimensionamento por Capacidade de Condução\n"
            "Prepare-se para selecionar a seção mínima do condutor aplicando as tabelas de métodos de instalação e fatores de correção."
        )},
    ]