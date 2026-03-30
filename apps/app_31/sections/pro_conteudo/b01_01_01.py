import streamlit as st
import math

def _get_valor_limpo(qid: str) -> float | None:
    chave = f"problema_{qid}"
    valor_bruto = st.session_state.get(chave)

    if valor_bruto is None or str(valor_bruto).strip() in ["", "—", "None"]:
        return None

    try:
        return float(str(valor_bruto).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None

def _calculo_corrente_nominal() -> str:
    # Coleta os dados usando a nova limpeza
    p = _get_valor_limpo("problema.01.001.0001")
    v = _get_valor_limpo("problema.01.001.0002")
    fp = _get_valor_limpo("problema.01.001.0003")
    n = _get_valor_limpo("problema.01.001.0004")

    # Só executa se os 4 pilares forem números válidos (não None)
    if all(x is not None for x in [p, v, fp, n]):
        try:
            # Cálculo da Corrente Nominal Trifásica
            # I = P / (sqrt(3) * V * cosphi * rend)
            i_nom = (p * 1000) / (math.sqrt(3) * v * fp * n)
            i_res = round(i_nom, 2)

            return (
                f"✅ Memorial de Cálculo\n\n"
                f"Com os dados de placa informados, o sistema calculou a corrente nominal:\n\n"
                f"$$I_{{n}} = \\frac{{{p} \\cdot 1000}}{{\\sqrt{{3}} \\cdot {v} \\cdot {fp} \\cdot {n}}} = {i_res} \\text{{ A}}$$"
            )
        except ZeroDivisionError:
            return "⚠️ **Erro:** Tensão, Fator de Potência ou Rendimento não podem ser zero."
    
    # Se ainda faltar algum número, mostra esta mensagem
    return (
        "### ⏳ Aguardando Dados da Placa\n"
        "Preencha a Potência, Tensão, FP e Rendimento acima para calcular a corrente nominal."
    )

def _tabela_resumo_tecnico() -> str:
    # Dicionário de mapeamento: Nome do Parâmetro -> (ID do Campo, Unidade)
    campos = {
        "Potência": ("problema.01.001.0001", "kW"),
        "Tensão nominal": ("problema.01.001.0002", "V"),
        "Fator de potência": ("problema.01.001.0003", "—"),
        "Rendimento": ("problema.01.001.0004", "—"),
        "Distância": ("problema.01.001.0006", "m"),
        "Temperatura ambiente": ("problema.01.001.0009", "°C"),
        "Bitola instalada": ("problema.01.001.0010", "mm²"),
        "Tensão medida": ("problema.01.001.0012", "V"),
        "Corrente medida": ("problema.01.001.0013", "A"),
    }

    # Cabeçalho da Tabela em Markdown (sem coluna Observação)
    tabela = "| Parâmetro | Valor | Unidade |\n"
    tabela += "| :--- | :---: | :---: |\n"

    for label, (qid, unid) in campos.items():
        valor = _get_valor_limpo(qid)
        val_str = f"{valor}" if valor is not None else "—"
        tabela += f"| {label} | **{val_str}** | {unid} |\n"
        tabela += f" <br>"

    return (
        "Agora você faz o que diferencia engenheiro de técnico improvisado. Você organiza os dados.\n\n"
        "#### Tabela de Parâmetros Coletados\n\n"
        f"{tabela}"
    )

def get_blocos() -> list[dict]:
    return [

        # ============================================================
        # ABERTURA
        # ============================================================
        {"tipo": "titulo", "texto":"Sistema de Bombeamento de Água",},

        {"tipo":"texto", "texto": (
                "O sistema analisado tem como finalidade realizar o bombeamento de água do reservatório inferior para o " 
                "reservatório superior por meio de uma motobomba acionada por motor elétrico. Para que esse transporte "
                "ocorra, o motor precisa fornecer energia mecânica à bomba, permitindo vencer a carga hidráulica do sistema "
                "e elevar a água até o nível desejado. Ao observar a finalidade do sistema, procure identificar a "
                "relação entre a função hidráulica desempenhada pela bomba e a demanda elétrica exigida do motor. Essa "
                "relação será fundamental para compreender, nas próximas etapas, o dimensionamento da alimentação elétrica "
                "do motor. Neste estudo, o desafio consiste em analisar o sistema de bombeamento e determinar como deve "
                "ser dimensionada a alimentação elétrica do motor da motobomba."
        ),},

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=PSuVujxAcOg",},

        #  ETAPA 1 
        {"tipo": "titulo", "texto": "ETAPA 1 — Levantamento de dados de campo",},
        {"tipo": "texto", "texto": (
            "Na engenharia, dimensionar não é apenas aplicar fórmulas; é traduzir a realidade física em parâmetros numéricos. "
            "Diante de um sistema de bombeamento — com motor, quadro e condutores já instalados — a pergunta fundamental precede "
            "o cálculo: o que foi executado é tecnicamente seguro e eficiente? Lembre-se: a qualidade da sua decisão é "
            "limitada pela qualidade dos seus dados. Se a coleta for imprecisa, o cálculo será inútil e a decisão, perigosa. "
            "Nesta etapa, sua prioridade não é a calculadora, mas a inspeção rigorosa. Antes de calcular, colete."
        ),},


        # ============================================================
        # DADOS DA PLACA DO MOTOR
        # ============================================================

        {"tipo": "titulo", "texto": "1. Dados da Placa do Motor"},
        {"tipo": "video", "titulo": "Inspeção Técnica: Como ler a placa do motor", "descricao": (
            "Antes de abrir a calculadora, você precisa dominar a leitura da placa de identificação. "
            "Assista ao vídeo e localize os quatro pilares do dimensionamento: Potência, Tensão, FP e Rendimento."
            ),
            "url": "https://www.youtube.com/watch?v=ZLV_MHFdmWk",
        },
        
        {"tipo": "texto", "texto": (
            "A placa de identificação é o documento oficial do motor. Ela define o 'carregamento' que o seu circuito "
            "elétrico deverá suportar. Registre os dados nominais coletados em campo:"
        ),},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0001",
            "rotulo": "Potência Nominal (P)", "unidade": "kW", "placeholder": "Ex: 5.5"},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0002",
            "rotulo": "Tensão Nominal (V)", "unidade": "V", "placeholder": "Ex: 380" },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0003",
            "rotulo": "Fator de Potência (cos φ)", "unidade": "0 a 1", "placeholder": "Ex: 0.86" },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0004",
            "rotulo": "Rendimento (η)", "unidade": "0 a 1", "placeholder": "Ex: 0.88"},

        {"tipo": "titulo", "texto": "A Física por trás do Condutor",},

        {"tipo": "texto", "texto": (
            "Para o engenheiro, a potência no eixo é uma exigência de fluxo de energia. Considerando um sistema "
            "trifásico equilibrado, a relação que dita o dimensionamento é:"
        ),},
        {"tipo": "equacao",
            "latex": r"I_{nominal} = \frac{P}{\sqrt{3} \cdot V \cdot \cos\phi \cdot \eta}",
        },
        {"tipo": "texto", "texto": (
            "Note que a Corrente (I) é diretamente proporcional à Potência (P). Em termos práticos:\n\n"
            "- Maior carga mecânica requer maior conversão de energia elétrica.\n"
            "- Como a tensão da rede é constante, o sistema 'puxa' mais elétrons por segundo.\n"
            "- Esse fluxo elevado gera calor (Efeito Joule), exigindo condutores com maior seção transversal."
        ),},

        {"tipo": "questao_texto", "id": "problema.01.001.0005",
            "pergunta": (
                "Conecte os pontos: Por que o aumento da potência nominal do motor "
                "obriga o projetista a escolher cabos com bitolas (seções) maiores?"
            ),
        },


        # ============================================================
        # DADOS DO CIRCUITO
        # ============================================================
        {"tipo": "titulo", "texto": "2. Dados do circuito elétrico",},

        {"tipo": "texto", "texto": (
            "A energia não se 'teleporta' do quadro ao motor; ela percorre um condutor físico sujeito a perdas. "
            "Agora, mude o foco do motor para o caminho: a infraestrutura elétrica. A distância impacta a queda "
            "de tensão, enquanto o ambiente e o método de instalação determinam a capacidade de dissipação térmica do cabo."
        ),},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0006",
            "rotulo": "Distância entre quadro e motor", "unidade": "m", "placeholder": "Ex: 45"},

        {"tipo": "titulo", "texto": "A Resistência Física: Segunda Lei de Ohm",},

        {"tipo": "texto", "texto": (
            "Se a Primeira Lei de Ohm foca na relação elétrica (V=RI), a Segunda Lei foca na constituição física do condutor. " 
            "Ela explica por que o comprimento e a bitola do cabo são determinantes no projeto. A resistência (R) que o cabo "
            "oferece ao fluxo de elétrons depende do material, do seu comprimento e da sua espessura:"
        ),},

        {"tipo": "equacao",
            "latex": r"R = \rho \cdot \frac{L}{A}",
        },

        {
            "tipo": "texto",
            "texto": (
                "Para o dimensionamento de sistemas de bombeamento, essa relação é crítica:\n\n"
                "- **Comprimento ($L$):** Quanto maior a distância entre o quadro e o motor, maior a resistência.\n"
                "- **Seção Transversal ($A$):** Quanto maior a bitola (área), menor a resistência oferecida.\n"
                "- **Resistividade ($\\rho$):** No nosso caso, o material é o cobre, que possui baixa oposição ao fluxo.\n\n"
                "Em resumo: cabos muito longos ou muito finos aumentam a resistência, o que gera perda de energia "
                "sob a forma de calor e queda de tensão no motor."
            ),
        },

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0007",
            "pergunta": (
                "Considerando a Segunda Lei de Ohm, se o comprimento do condutor aumenta, "
                "o que ocorre com a resistência elétrica e a queda de tensão?"
            ),
            "alternativas": {
                "a": "Ambas diminuem.",
                "b": "A resistência aumenta, elevando a queda de tensão.",
                "c": "A resistência aumenta, mas a queda de tensão permanece igual.",
                "d": "A resistência diminui, facilitando o fluxo."
            },
            "alternativa_correta": "b",
        },

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=yV9_Rt-ML4g",},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.001.0008",
            "pergunta": "Método de Instalação (Conforme NBR 5410):",
            "alternativas": {
                "a": "Eletroduto embutido em alvenaria",
                "b": "Eletroduto aparente (sobre parede)",
                "c": "Bandeja ou leito perfurado",
                "d": "Eletroduto enterrado"
            },
            "alternativa_correta": "a",
        },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0009",
            "rotulo": "Temperatura Ambiente Estimada", "unidade": "°C", "placeholder": "Ex: 30" },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0010",
            "rotulo": "Bitola (Seção) Atual do Cabo", "unidade": "mm²", "placeholder": "Ex: 6"},

        {"tipo": "questao_texto", "id": "problema.01.001.0011",
            "pergunta": (
                "Reflexão de Engenharia: A bitola encontrada em campo parece ser fruto de um cálculo técnico ou de um 'padrão de obra'? "
                "Justifique sua suspeita inicial antes de iniciarmos a validação matemática."
            ),
        },


        # ============================================================
        # MEDIÇÕES REAIS
        # ============================================================
        {"tipo": "titulo", "texto": "3. Diagnóstico de Campo: O Confronto com a Realidade",},

        {"tipo": "texto", "texto": (
            "Nesta etapa, a teoria encontra a prática. Utilizando o  Alicate Amperímetro e o Multímetro, " 
            "você deve coletar os valores reais de operação do sistema de bombeamento. Lembre-se: Se a tensão medida "
            "no motor for inferior à nominal, há uma queda de tensão excessiva. Se a corrente medida superar a de "
            "projeto, o motor está operando sob sobrecarga ou esforço indevido."
        ),},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.001.0012",
            "rotulo": "Tensão medida nos terminais do motor", "unidade": "V", "placeholder": "Ex: 365"},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.001.0013",
            "rotulo": "Corrente real medida em operação", "unidade": "A", "placeholder": "Ex: 12.5"},

        { "tipo": "titulo", "texto": "Análise Preliminar de Queda de Tensão",},

        {"tipo": "texto", "texto": (
            "Compare agora a Tensão Nominal (da placa) com a Tensão Medida no motor. A diferença entre esses dois valores "
            "representa a perda de potencial ao longo do condutor."
        ),},

        { "tipo": "equacao",
            "latex": r"\Delta V = V_{nominal} - V_{medida}",
        },

        { "tipo": "questao_multipla_escolha", "id": "problema.01.001.0014",
            "pergunta": (
                "Se você encontrou uma diferença de tensão significativa (maior que 5%), "
                "qual componente do circuito é o principal suspeito de estar subdimensionado?"
            ),
            "alternativas": {
                "a": "O motor elétrico.",
                "b": "O conjunto motobomba.",
                "c": "A seção (bitola) dos condutores elétricos.",
                "d": "O quadro de comando."
            },
            "alternativa_correta": "c",
        },

        { "tipo": "texto", "texto": _calculo_corrente_nominal(), },

        { "tipo": "questao_texto", "id": "problema.01.001.0015",
            "pergunta": (
                "Relatório de Campo: Compare a corrente medida (I_medida) com a corrente nominal "
                "calculada anteriormente. O motor está operando dentro da sua zona de eficiência? "
                "Justifique com base nos valores coletados."
            ),
        },


        # # ============================================================
        # # ORGANIZAÇÃO TÉCNICA
        # # ============================================================
        { "tipo": "titulo", "texto": "4. Organização dos dados", },

        {
            "tipo": "texto",
            "texto": _tabela_resumo_tecnico(),
        },

        {
            "tipo": "texto",
            "texto": (
                "Essa tabela será usada em todas as próximas etapas. Sem ela, não existe projeto."
            ),
        },

        { "tipo": "titulo", "texto": "5. Primeira leitura crítica (mini diagnóstico)" },

        { "tipo": "texto", "texto": (
                "Antes de avançar para os cálculos normativos, observe os dados coletados e registre suas impressões iniciais." 
                "O olhar clínico do engenheiro precede a calculadora. Considere os seguintes pontos:\n\n"
                # "• Análise de Carga: A corrente medida em operação está próxima, igual ou acima da nominal (In) calculada?\n"
                # "• Queda de Tensão: A tensão nos terminais do motor (V medida) apresenta uma diferença acentuada em relação aos 380V nominais?\n"
                # "• Relação Distância e Bitola: O comprimento do circuito parece adequado para a seção transversal do cabo instalado?\n"
                # "• Condições de Contorno: O método de instalação e a temperatura ambiente favorecem a dissipação térmica?\n\n"
                # "Nesta fase, você não precisa de conclusões definitivas. O objetivo é registrar hipóteses que serão validadas "
                # "matematicamente na próxima etapa. A sensibilidade técnica ajuda a identificar erros grosseiros antes mesmo do projeto começar."
        )},


        { "tipo": "questao_texto", "id": "problema.01.001.0016",
            "pergunta": (
                "Análise de Carga: A corrente medida em operação está próxima, igual ou acima da nominal (In) calculada?"
        ),},

        { "tipo": "questao_texto", "id": "problema.01.001.0017",
            "pergunta": (
                "Queda de Tensão: A tensão nos terminais do motor (V medida) apresenta uma diferença acentuada em relação aos 380V nominais?"
        ),},

        { "tipo": "questao_texto", "id": "problema.01.001.0018",
            "pergunta": (
                "Relação Distância e Bitola: O comprimento do circuito parece adequado para a seção transversal do cabo instalado?"
        ),},

        { "tipo": "questao_texto", "id": "problema.01.001.0019",
            "pergunta": (
                "Condições de Contorno: O método de instalação e a temperatura ambiente favorecem a dissipação térmica?"
        ),},

        { "tipo": "texto", "texto": (
                "Nesta fase, você não precisa de conclusões definitivas. O objetivo é registrar hipóteses que serão validadas "
                "matematicamente na próxima etapa. A sensibilidade técnica ajuda a identificar erros grosseiros antes mesmo do projeto começar."
        )},

        {
            "tipo": "titulo",
            "texto": "Recapitulação Técnica: Levantamento de dados de campo"
        },

        {
            "tipo": "texto",
            "texto": (
                "Você concluiu o levantamento de campo, transformando uma situação real em um modelo de dados técnicos estruturados. "
                "Até aqui, o trabalho foi de inspeção e registro. Agora, o sistema está pronto para ser submetido ao rigor da engenharia. "
                "Com as medições reais e os dados de infraestrutura organizados, você está habilitado para iniciar o dimensionamento. "
                "Na Etapa 2, utilizaremos este banco de dados para determinar:\n\n"
                "1. Corrente de projeto corrigida pelos fatores de agrupamento e temperatura.\n"
                "2. Capacidade de condução de corrente conforme a NBR 5410.\n"
                "3. Verificação da queda de tensão admissível para o regime de partida e operação.\n\n"
                "O diagnóstico visual termina aqui. A partir deste ponto, as decisões serão baseadas em cálculos e normas técnicas."
            )
        },
    ]