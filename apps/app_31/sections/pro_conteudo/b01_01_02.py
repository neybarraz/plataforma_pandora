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

def _calcular_delta_percentual():
    i_calc = _get_valor_limpo("problema.01.002.0001")  # corrente calculada
    i_med = _get_valor_limpo("problema.01.001.0009")   # corrente medida

    if i_calc and i_med:
        delta = abs(i_med - i_calc)
        perc = (delta / i_calc) * 100
        return i_calc, i_med, delta, perc
    return None, None, None, None



def _calcular_delta_percentual():
    i_calc = _get_valor_limpo("problema.01.002.0001")
    i_med = _get_valor_limpo("problema.01.001.0009")

    if i_calc is None or i_med is None or i_calc == 0:
        return None

    delta = abs(i_med - i_calc)
    perc = (delta / i_calc) * 100
    return {
        "i_calc": i_calc,
        "i_med": i_med,
        "delta": delta,
        "perc": perc,
    }


def _texto_delta_percentual() -> str:
    resultado = _calcular_delta_percentual()

    if resultado is None:
        return (
            "Preencha a corrente nominal calculada e a corrente medida para visualizar "
            "a substituição numérica e a diferença percentual."
        )

    i_calc = resultado["i_calc"]
    i_med = resultado["i_med"]
    delta = resultado["delta"]
    perc = resultado["perc"]

    return (
        "Substituindo os valores obtidos:\n\n"
        f"- Corrente calculada: {i_calc:.2f} A\n"
        f"- Corrente medida: {i_med:.2f} A\n"
        f"- Diferença absoluta (ΔI): {delta:.2f} A\n"
        f"- Diferença percentual: {perc:.2f}%"
    )

def _texto_interpretacao_delta() -> str:
    resultado = _calcular_delta_percentual()

    if resultado is None:
        return "A interpretação será exibida após o preenchimento dos valores."

    perc = resultado["perc"]
    i_calc = resultado["i_calc"]
    i_med = resultado["i_med"]

    # determina direção
    if i_med > i_calc:
        direcao = "maior"
    elif i_med < i_calc:
        direcao = "menor"
    else:
        direcao = "igual"

    # classificação
    if perc < 10:
        classificacao = (
            "Diferença inferior a 10%: o modelo pode ser considerado coerente "
            "com o comportamento real do sistema."
        )

    elif perc <= 20:
        if direcao == "maior":
            classificacao = (
                "Diferença entre 10% e 20% com corrente medida maior que a calculada: "
                "indica possíveis perdas não consideradas, início de sobrecarga "
                "ou variações operacionais relevantes."
            )
        elif direcao == "menor":
            classificacao = (
                "Diferença entre 10% e 20% com corrente medida menor que a calculada: "
                "indica possível operação em carga parcial ou leve superestimação do modelo."
            )
        else:
            classificacao = (
                "Diferença entre 10% e 20%: variação moderada entre modelo e medição."
            )

    else:  # perc > 20
        if direcao == "maior":
            classificacao = (
                "Diferença superior a 20% com corrente medida maior que a calculada: "
                "condição crítica. Pode indicar sobrecarga, queda de tensão significativa "
                "ou erro nos dados utilizados no modelo."
            )
        elif direcao == "menor":
            classificacao = (
                "Diferença superior a 20% com corrente medida menor que a calculada: "
                "indica forte superestimação do modelo ou operação fora das condições nominais."
            )
        else:
            classificacao = (
                "Diferença superior a 20%: divergência significativa entre modelo e realidade."
            )

    return (
        "Interpretação técnica:\n\n"
        f"{classificacao}"
    )

def _comparativo_correntes() -> str:
    campos = {
        "Corrente medida": ("problema.01.001.0009", "A"),
        "Corrente calculada": ("problema.01.002.0001", "A"),
    }
    
    tabela = "Comparação das correntes\n\n"
    tabela += "| Parâmetro | Valor Identificado | Unidade |\n"
    tabela += "| :--- | :---: | :---: |\n"
    
    for label, (qid, unid) in campos.items():
        valor = _get_valor_limpo(qid)
        val_str = f"{valor}" if valor is not None else "—"
        tabela += f"| **{label}** | {val_str} | {unid} |\n"
    
    return tabela + "<br>"

def _gerar_tabela_parametros() -> str:
    campos = {
        "Potência": ("problema.01.001.0001", "kW"),
        "Tensão nominal": ("problema.01.001.0002", "V"),
        "Fator de potência": ("problema.01.001.0003", "—"),
        "Rendimento": ("problema.01.001.0004", "—"),
    }
    
    tabela = "Dados Coletados\n\n"
    tabela += "| Parâmetro | Valor Identificado | Unidade |\n"
    tabela += "| :--- | :---: | :---: |\n"
    
    for label, (qid, unid) in campos.items():
        valor = _get_valor_limpo(qid)
        val_str = f"{valor}" if valor is not None else "—"
        tabela += f"| **{label}** | {val_str} | {unid} |\n"
    
    return tabela + "<br>"






def _tabela_validacao_corrente() -> str:
    resultado = _calcular_delta_percentual()

    if resultado is None:
        return (
            "Tabela de validação da corrente\n\n"
            "Preencha a corrente nominal calculada e a corrente medida "
            "para visualizar os resultados."
        )

    i_calc = resultado["i_calc"]
    i_med = resultado["i_med"]
    delta = resultado["delta"]
    perc = resultado["perc"]

    # interpretação já existente
    interpretacao = _texto_interpretacao_delta().replace("Interpretação técnica:\n\n", "")

    tabela = "Validação da corrente nominal\n\n"
    tabela += "| Parâmetro | Valor | Unidade |\n"
    tabela += "| :--- | :---: | :---: |\n"
    tabela += f"| Corrente calculada | **{i_calc:.2f}** | A |\n"
    tabela += f"| Corrente medida | **{i_med:.2f}** | A |\n"
    tabela += f"| Diferença absoluta (ΔI) | **{delta:.2f}** | A |\n"
    tabela += f"| Diferença percentual | **{perc:.2f}** | % |\n"

    return (
        tabela +
        "\n\n**Interpretação técnica:**\n\n"
        f"{interpretacao}"
    )











def get_blocos() -> list[dict]:
    return [
        # ========================================================
        # ========================================================
        {"tipo": "titulo", "texto":"1. Determinação e validação da corrente nominal"},

        {"tipo": "texto", "texto": (
            "Na etapa anterior, foram levantados os dados fundamentais do sistema, "
            "incluindo potência, tensão, fator de potência e rendimento do motor. "
            "Essas grandezas constituem a base para a modelagem elétrica do problema."
        )},

        # >>> PERGUNTA CENTRAL (padrão do método)
        {"tipo": "subtitulo", "texto": (
            "Qual corrente o motor realmente exige?"
        )},

        {"tipo": "texto", "texto": (
            "A partir dos dados coletados, o problema passa a ser determinar o esforço elétrico "
            "necessário para o funcionamento do sistema em regime permanente."
        )},

        {"tipo": "texto", "texto": (
            "Essa grandeza é definida pela corrente nominal do motor, que representa a demanda elétrica "
            "real imposta à instalação."
        )},

        {"tipo": "texto", "texto": (
            "A corrente nominal estabelece a referência técnica para todas as verificações do circuito. "
            "Sem a sua determinação, não é possível avaliar:\n\n"
            
            "- a capacidade de condução dos condutores;\n"
            "- a adequação dos dispositivos de proteção;\n"
            "- o comportamento elétrico do circuito sob carga."
        )},

        {"tipo": "texto", "texto": (
            "Nesta etapa, os dados coletados deixam de ser informações isoladas e passam a ser "
            "integrados em um modelo elétrico. O objetivo é converter as características do sistema "
            "em um parâmetro mensurável e aplicável ao projeto.\n\n"

            "O valor obtido deve apresentar coerência física, consistência dimensional e compatibilidade "
            "com o comportamento esperado do motor em operação.\n\n"

            "A corrente nominal não é apenas um resultado intermediário — ela define a base técnica "
            "sobre a qual todas as decisões de dimensionamento serão tomadas."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0006",
            "pergunta": (
                "Dentro do processo de dimensionamento elétrico, qual é a função da corrente nominal do motor?"
            ),
            "alternativas": {
                "a": "Representa um valor auxiliar, utilizado apenas para conferência final.",
                "b": "Define o esforço elétrico do sistema e serve como referência para o dimensionamento do circuito.",
                "c": "Indica exclusivamente a potência mecânica fornecida pelo motor.",
                "d": "É utilizada apenas na verificação de queda de tensão."
            },
            "alternativa_correta": "b",
        },
        # ========================================================
        {"tipo": "titulo", "texto":"2. Fundamento elétrico da corrente nominal"},

        {"tipo": "texto", "texto": (
            "Nesta seção, o conceito principal é a relação entre potência elétrica e corrente no circuito. "
            "O motor não consome corrente de forma arbitrária. A corrente elétrica é consequência direta "
            "da potência que o motor precisa absorver para realizar trabalho mecânico."
        )},

        {"tipo": "texto", "texto": (
            "A carga mecânica imposta ao sistema define a potência no eixo do motor. "
            "Para sustentar essa potência, o motor deve receber potência elétrica da rede. "
            "Essa conversão, de potência elétrica em potência mecânica, estabelece o nível de corrente "
            "que circulará no circuito."
        )},

        {"tipo": "texto", "texto": (
            "A forma como essa relação se expressa depende do tipo de alimentação do motor. "
            "Motores podem operar em sistemas monofásicos ou trifásicos, e cada configuração possui "
            "uma expressão específica para o cálculo da corrente."
        )},

        {"tipo": "texto", "texto": (
            "Para sistemas monofásicos, a corrente é dada por:"
        )},

        {"tipo": "equacao", 
            "latex": r"I = \frac{P}{V \cdot cos\varphi \cdot \eta}"
        },

        {"tipo": "texto", "texto": (
            "Para sistemas trifásicos, a corrente é dada por:"
        )},

        {"tipo": "equacao", 
            "latex": r"I = \frac{P}{\sqrt{3} \cdot V \cdot cos\varphi \cdot \eta}"
        },

        {"tipo": "texto", "texto": (
            "Onde:\n\n"
            
            "- P: potência mecânica no eixo (W);\n"
            "- V: tensão de alimentação (V);\n"
            "- cosφ: fator de potência do motor;\n"
            "- η: rendimento do motor.\n\n"
            
            "A diferença entre as expressões está na forma como a potência é distribuída no sistema elétrico."
        )},

        {"tipo": "texto", "texto": (
            "A identificação correta do tipo de alimentação do motor é fundamental para o cálculo da corrente. "
            "Essa informação deve ser verificada na placa de identificação ou na configuração da instalação elétrica."
        )},

        {"tipo": "texto", "texto": (
            "Essas equações não são apenas ferramentas de cálculo. "
            "Elas representam a tradução do comportamento físico do sistema: "
            "a demanda energética da carga sendo convertida em esforço elétrico no circuito. "
            "A corrente obtida a partir dessas relações será utilizada como referência técnica "
            "para o dimensionamento dos condutores nas próximas etapas."
        )},


        # ========================================================
        {"tipo": "titulo", "texto":"3. Cálculo da corrente nominal do motor"},

        {"tipo": "texto", "texto": (
            "Com base nos dados levantados na etapa anterior, inicia-se agora a construção da corrente nominal. "
            "Essa etapa consiste em aplicar o modelo matemático ao sistema real, substituindo na equação "
            "os valores obtidos para determinar o esforço elétrico exigido pelo motor."
        )},

        {"tipo": "texto", "texto": (
            "Utilize a tabela de parâmetros coletados como referência para o cálculo:"
        )},

        {"tipo": "texto", "texto": _gerar_tabela_parametros()},

        {"tipo": "texto", "texto": (
            "A partir desses dados, selecione a expressão adequada (monofásica ou trifásica) "
            "e realize a substituição dos valores para determinar a corrente. "            
            "Esse processo transforma os dados do sistema em um parâmetro elétrico mensurável."
        )},

        {"tipo": "texto", "texto": (
            "Cuidados técnicos durante o cálculo:\n\n"
            
            "- Converter a potência de kW para W (multiplicar por 1000);\n"
            "- Utilizar a tensão nominal correta do sistema;\n"
            "- Considerar o fator de potência (cosφ);\n"
            "- Considerar o rendimento (η);\n"
            "- Verificar a coerência das unidades utilizadas.\n\n"
            
            "Cada termo da equação influencia diretamente o valor final da corrente. "
            "Após realizar o cálculo, registre o valor obtido para a corrente nominal:"
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.002.0001",
            "rotulo": "Corrente nominal calculada", "unidade": "A", "placeholder": "Ex: 4.5"},
       
        # ========================================================
        # ========================================================
        {"tipo": "titulo", "texto":"4. Validação da corrente nominal em campo"},

        {"tipo": "texto", "texto": (
            "A corrente nominal representa o esforço elétrico exigido pelo motor em condições de operação. "
            "Esse valor, obtido a partir do modelo, será utilizado como referência para análise do sistema real. "
            "A validade do dimensionamento depende diretamente da coerência entre o valor calculado "
            "e o comportamento observado em campo."
        )},

        {"tipo": "texto", "texto": (
            "Neste ponto, realiza-se o confronto entre:\n\n"
            "- corrente nominal calculada (modelo);\n"
            "- corrente medida em operação (campo).\n\n"
            
            "Essa comparação permite avaliar se o modelo representa adequadamente o sistema real."
        )},

        {"tipo": "texto", "texto": _comparativo_correntes()},


        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0002",
            "pergunta": (
                "Observe os valores apresentados e faça um julgamento inicial. A corrente medida está coerente com a corrente nominal calculada?"
            ),
            "alternativas": {
                "a": "Sim, os valores são compatíveis",
                "b": "Não, há diferença significativa",
                "c": "Não é possível avaliar",
                "d": "Os valores não têm relação"
            },
            "alternativa_correta": "a",
        },

        {"tipo": "texto", "texto": (
            "Para avaliar tecnicamente essa coerência, não basta observar os valores. "
            "É necessário quantificar a diferença entre eles."
        )},

        {"tipo": "equacao",
        "latex": r"\%\Delta I = \frac{|I_{medida} - I_{calculada}|}{I_{calculada}} \times 100"
        },

        {"tipo": "texto", "texto": _texto_delta_percentual()},

        {"tipo": "texto", "texto": _texto_interpretacao_delta()},

        {"tipo": "texto", "texto": (
            "A análise da diferença entre a corrente medida e a corrente calculada deve considerar dois fatores fundamentais:\n\n"
            
            "- a magnitude do desvio (diferença percentual);\n"
            "- o sentido da diferença (qual corrente é maior).\n\n"

            "Diferenças pequenas indicam boa aderência entre modelo e realidade. "
            "Diferenças elevadas indicam inconsistências que devem ser investigadas.\n\n"

            "Quando a corrente medida é maior que a calculada, há indícios de esforço elétrico acima do previsto, "
            "o que pode estar associado a sobrecarga, queda de tensão ou erros nos dados utilizados.\n\n"

            "Quando a corrente medida é menor que a calculada, o sistema pode estar operando em carga parcial "
            "ou o modelo pode ter superestimado a demanda.\n\n"

            "A interpretação correta exige sempre a análise conjunta desses dois aspectos."
        )},

        {"tipo": "questao_texto", "id": "problema.01.002.0003",
            "pergunta": (
                "Se a corrente nominal calculada for inferior à corrente medida em operação, "
                "o que isso indica sobre o modelo adotado e quais podem ser as consequências técnicas "
                "para o dimensionamento do circuito?"
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0004",
            "pergunta": (
                "Quando a corrente nominal calculada é aproximadamente igual à corrente medida em operação, "
                "qual é a interpretação técnica mais adequada?"
            ),
            "alternativas": {
                "a": "O modelo representa adequadamente o comportamento real do sistema.",
                "b": "O motor está operando acima da sua capacidade nominal.",
                "c": "O circuito está obrigatoriamente subdimensionado.",
                "d": "A tensão de alimentação está incorreta."
            },
            "alternativa_correta": "a",
        },

        {"tipo": "questao_texto", "id": "problema.01.002.0005",
            "pergunta": (
                "Se a corrente nominal calculada for superior à corrente medida em operação, "
                "quais hipóteses podem explicar essa diferença e quais são os impactos dessa condição "
                "no dimensionamento do circuito?"
        )},

        {"tipo": "texto", "texto": (
            "Essa análise marca o início da validação do modelo elétrico. "
            "A coerência entre valores calculados e medidos indica que a base de dados e o modelo adotado são confiáveis. "
            "A partir desse ponto, o dimensionamento passa a se apoiar em uma base técnica validada."
        )},

        # ========================================================
        # ========================================================
        {"tipo": "titulo", "texto":"5. Entrega técnica: Corrente nominal validada",},

        {"tipo": "texto", "texto": (
            "Nesta etapa, o modelo elétrico do sistema é consolidado a partir da determinação da corrente nominal "
            "e da sua comparação com os dados medidos em campo. "
            "Essa análise transforma o conjunto de dados coletados em um parâmetro elétrico validado, "
            "representativo do comportamento real do sistema. "
        )},
        
        {"tipo": "texto", "texto": (    
            "A tabela a seguir apresenta a comparação entre a corrente calculada e a corrente medida:"
        )},

        { "tipo": "texto", "texto": _tabela_validacao_corrente()},


        # ========================================================
        {"tipo": "titulo", "texto":"Fechamento da etapa",},

        {"tipo": "texto", "texto": (
            "Neste momento, o sistema deixa de ser apenas observado e passa a ser representado por um modelo elétrico validado.\n\n"
            
            "Você já possui:\n"
            "- corrente nominal determinada a partir dos dados coletados;\n"
            "- comparação entre modelo e comportamento real;\n"
            "- análise da coerência entre os valores.\n\n"
            
            "A qualidade dessa validação define a confiabilidade de todo o dimensionamento. "
            "A partir deste ponto, as decisões passam a ser baseadas em um parâmetro técnico consistente.\n\n"
            
            "Na próxima etapa, essa corrente será confrontada com a capacidade admissível dos condutores, "
            "conforme os critérios estabelecidos em norma."
        )},
    ]
