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


def _calcular_corrente_admissivel():
    i_projeto = _get_valor_limpo("problema.01.002.0001")  # corrente nominal
    i_tabela = _get_valor_limpo("problema.01.003.0001")
    f_temp = _get_valor_limpo("problema.01.003.0002")
    f_agrup = _get_valor_limpo("problema.01.003.0003")

    if None in (i_projeto, i_tabela, f_temp, f_agrup):
        return None

    i_corrigida = i_tabela * f_temp * f_agrup

    return {
        "i_projeto": i_projeto,
        "i_tabela": i_tabela,
        "f_temp": f_temp,
        "f_agrup": f_agrup,
        "i_corrigida": i_corrigida,
    }


# def _interpretacao_corrente_admissivel():
#     i_adm = _get_valor_limpo("problema.01.003.0004")
#     i_proj =  _get_valor_limpo("problema.01.002.0001")
#     if resultado is None:
#         return "Preencha os dados para visualizar a interpretação."

#     i_proj = resultado["i_projeto"]
#     i_adm = resultado["i_corrigida"]

#     if i_adm >= i_proj:
#         return (
#             "A corrente admissível corrigida é maior ou igual à corrente de projeto. "
#             "A seção analisada atende ao critério de condução em regime permanente."
#         )
#     else:
#         return (
#             "A corrente admissível corrigida é inferior à corrente de projeto. "
#             "A seção é insuficiente e pode operar em sobrecarga térmica contínua."
#         )


def _tabela_corrente_admissivel():
    resultado = _calcular_corrente_admissivel()

    if resultado is None:
        return "Preencha os valores para visualizar a tabela."

    tabela = "Verificação da corrente admissível\n\n"
    tabela += "| Parâmetro | Valor | Unidade |\n"
    tabela += "| :--- | :---: | :---: |\n"
    tabela += f"| Corrente de projeto | **{resultado['i_projeto']:.2f}** | A |\n"
    tabela += f"| Corrente da tabela | **{resultado['i_tabela']:.2f}** | A |\n"
    tabela += f"| Fator temperatura | **{resultado['f_temp']:.2f}** | — |\n"
    tabela += f"| Fator agrupamento | **{resultado['f_agrup']:.2f}** | — |\n"
    # tabela += f"| Corrente admissível corrigida | **{resultado['i_corrigida']:.2f}** | A |\n"

    # interpretacao = _interpretacao_corrente_admissivel()

    return tabela + "\n\n<br>"# + interpretacao



def get_blocos() -> list[dict]:
    return [

        # ========================================================
        {"tipo": "titulo", "texto":"1. Seleção da capacidade de condução do condutor"},

        {"tipo": "texto", "texto": (
            "Na etapa anterior, foi determinada a corrente nominal do motor, representando o esforço elétrico exigido pelo sistema. "
            "Agora, o problema se desloca do comportamento da carga para a capacidade do condutor."
        )},

        {"tipo": "texto", "texto": (
            "A pergunta técnica desta etapa é:\n\n"
            "Qual seção de condutor é capaz de conduzir essa corrente de forma contínua e segura, "
            "sem comprometer sua integridade térmica?"
        )},

        {"tipo": "texto", "texto": (
            "A partir deste ponto, o dimensionamento deixa de ser apenas modelagem física e passa a ser "
            "aplicação normativa. A decisão não depende de tentativa ou experiência empírica, mas do uso correto "
            "dos critérios estabelecidos em norma técnica."
        )},

        # ========================================================
        {"tipo": "titulo", "texto":"2. Fundamento térmico da condução elétrica"},

        {"tipo": "texto", "texto": (
            "Todo condutor elétrico aquece quando conduz corrente. Esse aquecimento é consequência direta do efeito Joule, "
            "no qual parte da energia elétrica é dissipada em forma de calor."
        )},

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=urzRRrJuagE",},

        {"tipo": "texto", "texto": (
            "A capacidade de condução de corrente de um cabo não é ilimitada. Ela é definida pela máxima temperatura "
            "que o material condutor e sua isolação podem suportar sem degradação."
        )},

        {"tipo": "texto", "texto": (
            "Essa capacidade depende de fatores como:\n\n"
            
            "- material do condutor (cobre ou alumínio): define a resistividade elétrica. "
            "Condutores com menor resistividade (como o cobre) dissipam menos energia em forma de calor "
            "para a mesma corrente, permitindo maior capacidade de condução;\n\n"
            
            "- tipo de isolação: define a temperatura máxima admissível de operação. "
            "Isolações como PVC (70°C) suportam menos aquecimento, enquanto materiais como XLPE/EPR (90°C) "
            "permitem maiores correntes antes de atingir o limite térmico;\n\n"
            
            "- método de instalação: determina a capacidade de dissipação térmica. "
            "Instalações confinadas (eletroduto embutido) dificultam a troca de calor, "
            "reduzindo a corrente admissível, enquanto instalações expostas aumentam a dissipação;\n\n"
            
            "- temperatura ambiente: influencia diretamente o gradiente térmico entre o cabo e o meio. "
            "Quanto maior a temperatura ambiente, menor a capacidade de dissipar calor, "
            "reduzindo a corrente admissível;\n\n"
            
            "- agrupamento de circuitos: provoca acúmulo de calor entre condutores próximos. "
            "Cada cabo aquece o outro, reduzindo a capacidade individual de condução.\n\n"
            
            "A corrente admissível é, portanto, um limite térmico imposto pela capacidade do sistema de "
            "dissipar o calor gerado pelo efeito Joule."
        )},


        # ========================================================
        {"tipo": "titulo", "texto":"3. Aplicação da norma (NBR 5410)"},

        {"tipo": "texto", "texto": (
            "A determinação da corrente admissível deve ser realizada com base nas tabelas da NBR 5410. "
            "Essas tabelas fornecem valores padronizados considerando condições específicas de instalação."
        )},

        { "tipo": "texto", "texto": (
                '<div style="margin-top: 20px;">'
                '<a href="https://universidadeniltonlins.com.br/wp-content/uploads/2019/04/NBR-5410.pdf" '
                'target="_blank" '
                'style="text-decoration: none; border: 2px solid #ff4b4b; color: white; background-color: #ff4b4b; '
                'padding: 12px 24px; border-radius: 8px; font-weight: bold; display: inline-block;">'
                '📖 Abrir NBR 5410:2004 (PDF)'
                '</a>'
                '</div>'
            )
        },
                
        {"tipo": "texto", "texto": (
            "A corrente obtida diretamente das tabelas da NBR 5410 representa uma condição padronizada de ensaio "
            "(tipicamente 30°C para instalação ao ar e sem agrupamento). "
            "No entanto, instalações reais raramente operam nessas condições ideais."
        )},

        {"tipo": "texto", "texto": (  
            "Por esse motivo, a norma exige a aplicação de fatores de correção que ajustam a capacidade de condução "
            "do condutor às condições reais de operação, garantindo que a temperatura da isolação não ultrapasse o limite admissível."
        )},

        {"tipo": "equacao",
        "latex": r"I_{z} = I_{tabela} \cdot f_{t} \cdot f_{g}"
        },


        # =======================================================
        {"tipo": "titulo", "texto": "4. Aplicação da NBR 5410 ao problema"},

        {"tipo": "texto", "texto": (
            "Nesta etapa, você irá aplicar a norma diretamente aos dados do seu problema. "
            "O objetivo é verificar se o condutor analisado é capaz de conduzir a corrente nominal "
            "em condições reais de operação.\n\n<br>"

            "A verificação é feita a partir da corrente admissível corrigida, definida por:"
        )},

        {"tipo": "equacao",
        "latex": r"I_{z} = I_{tabela} \cdot f_{t} \cdot f_{g}"
        },

        {"tipo": "texto", "texto": (
            "Cada termo dessa equação deve ser obtido diretamente da norma, a partir das condições reais da instalação."
        )},


        # =======================================================
        {"tipo": "subtitulo", "texto": "Corrente (Tabela 37 — NBR 5410)"},

        {"tipo": "texto", "texto": (
            "A corrente utilizada no dimensionamento é a corrente nominal determinada anteriormente. "

            "Esse valor representa a condição real de operação do sistema e será utilizado como referência "
            "para verificar se o condutor suporta o regime permanente."
        )},

        {"tipo": "texto", "texto": (
            f"Corrente nominal considerada: {_get_valor_limpo('problema.01.002.0001') or '—'} A"
        )},

        {
            "tipo": "imagem",
            "arquivo": "tab_37.png",
            "legenda": "Tabela 37 — Capacidade de condução de corrente (NBR 5410)",
            "fonte": "NBR 5410"
        },

        {"tipo": "texto", "texto": (
        "A Tabela 37 apresenta a capacidade de condução de corrente em condições padrão. "
        "Esse valor não depende do circuito em si, mas sim da seção transversal do condutor "
        "e do método de instalação adotado.\n\n<br>"

        "Para auxiliar na escolha, os métodos de instalação podem ser interpretados da seguinte "
        "forma: os métodos A1 e A2 referem-se a condutores instalados em eletroduto embutido, "
        "onde a dissipação térmica é menor; os métodos B1 e B2 representam condutores em eletroduto "
        "aparente ou embutido em alvenaria, sendo esta a condição mais comum em projetos; "
        "o método C corresponde a condutores instalados ao ar livre, que proporcionam maior "
        "dissipação térmica; já o método D aplica-se a condutores enterrados, cuja capacidade "
        "depende das características do solo.\n\n<br>"

        "O procedimento prático é simples: primeiro, escolhe-se uma seção de condutor; em seguida, "
        "identifica-se o método de instalação utilizado (A1, B1, B2, etc.); por fim, localiza-se "
        "na tabela o valor correspondente à combinação desses dois parâmetros.\n\n<br>"

        "O valor obtido representa a capacidade base do condutor, ou seja, seu desempenho antes "
        "da aplicação de quaisquer fatores de correção."
        )},

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.003.0001",
            "rotulo": r"Corrente da tabela ($I_{tabela}$)",
            "unidade": "A"
        },


        # =======================================================
        {"tipo": "subtitulo", "texto": "Fator de temperatura (Tabela 40 — NBR 5410)"},

        {
            "tipo": "imagem",
            "arquivo": "tab_40.png",
            "legenda": "Tabela 40 — Fator de correção por temperatura",
            "fonte": "NBR 5410"
        },

        {"tipo": "texto", "texto": (
            "A temperatura ambiente altera diretamente a capacidade de dissipação térmica do condutor. "
            "Quanto maior a temperatura, menor a corrente admissível. "
        )},

        {"tipo": "texto", "texto": (
            f"Temperatura ambiente considerada: {_get_valor_limpo('problema.01.001.0006') or '—'} °C"
        )},

        {"tipo": "texto", "texto": (
            "Utilize a temperatura medida no local e consulte a Tabela 40 para obter o fator de correção."
        )},
        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.003.0002",
            "rotulo": r"Fator de temperatura ($f_t$)",
            "unidade": "—"
        },


        # =======================================================
        {"tipo": "subtitulo", "texto": "Fator de agrupamento (Tabela 42 — NBR 5410)"},

        {
            "tipo": "imagem",
            "arquivo": "tab_42.png",
            "legenda": "Tabela 42 — Fator de correção por agrupamento",
            "fonte": "NBR 5410"
        },

        {"tipo": "texto", "texto": (
            "Quando múltiplos circuitos estão agrupados, ocorre acúmulo de calor entre os condutores. "

            "Esse efeito reduz a capacidade de condução e deve ser corrigido.\n\n"

            "Utilize o número de circuitos agrupados e consulte a Tabela 42."
        )},

        {"tipo": "texto", "texto": (
            f"Número de circuitos agrupados: {_get_valor_limpo('problema.01.001.0010') or '—'}"
        )},

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.003.0003",
            "rotulo": r"Fator de agrupamento ($f_g$)",
            "unidade": "—"
        },


        # =======================================================
        {"tipo": "subtitulo", "texto": "Cálculo da corrente admissível corrigida"},

        {"tipo": "texto", "texto": (
            "Com todos os valores coletados, calcule a corrente admissível corrigida."
        )},

        {"tipo": "equacao",
        "latex": r"I_{z} = I_{tabela} \cdot f_t \cdot f_g"
        },

        {"tipo": "texto", "texto": _tabela_corrente_admissivel()},

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.003.0004",
            "rotulo": "Corrente admissível corrigida",
            "unidade": "A"
        },

        {"tipo": "texto", "texto": (
            "Esse valor representa a real capacidade do condutor nas condições do problema."
        )},

        # =======================================================
        {"tipo": "subtitulo", "texto": "Critério de dimensionamento"},

        {"tipo": "texto", "texto": (
            "Para verificar se o condutor atende ao critério de dimensionamento, "
            "utilize os valores obtidos nas etapas anteriores."
        )},

        {"tipo": "texto", "texto": (
            f"Corrente nominal (I_n): {_get_valor_limpo('problema.01.002.0001') or '--'} A\n\n"
            f"Corrente admissível do condutor (I_z): {_get_valor_limpo('problema.01.003.0004') or '--'} A"
        )},


        {"tipo": "equacao",
        "latex": r"I_{z} \ge I_{nominal}"
        },

        {"tipo": "texto", "texto": (
            "O critério estabelece que a corrente admissível do condutor (I_z) "
            "deve ser maior ou igual à corrente nominal (I_n)."
        )},

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0005",
            "pergunta": (
                "Comparando os valores obtidos, qual é a conclusão correta sobre o dimensionamento do condutor?"
            ),
            "alternativas": {
                "a": "Não é possível concluir sem recalcular os fatores de correção",
                "b": "O condutor está subdimensionado, pois I_z < I_n",
                "c": "O condutor está corretamente dimensionado, pois I_z ≥ I_n",
                "d": "O critério correto seria I_n ≥ I_z"
            },
            "alternativa_correta": "c",
        },





        # {"tipo": "equacao",
        # "latex": r"I_{z} \ge I_{nominal}"
        # },

        # {"tipo": "texto", "texto": (
        #     "Interpretação técnica:\n\n"

        #     "- Se I_z ≥ I_nominal → a seção é adequada;\n"
        #     "- Se I_z < I_nominal → a seção é insuficiente.\n\n"

        #     "Caso não atenda, deve-se selecionar uma nova seção e repetir o processo."
        # )},

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0006",
            "pergunta": (
                "Se a corrente admissível corrigida for menor que a corrente nominal do circuito, "
                "qual é a consequência?"
            ),
            "alternativas": {
                "a": "O sistema opera normalmente",
                "b": "O cabo terá maior eficiência",
                "c": "Não há impacto relevante",
                "d": "O condutor pode operar em sobreaquecimento contínuo"
            },
            "alternativa_correta": "d",
        },


        # =======================================================
        {"tipo": "titulo", "texto": "5. Seção nominal do condutor"},

        {"tipo": "texto", "texto": (
            "Após determinar a corrente admissível corrigida (I_z), o problema passa a ser invertido. "
            "Não se trata mais de calcular a capacidade do condutor, mas de selecionar, a partir da norma, "
            "qual seção nominal é capaz de atender a essa corrente."
        )},

        {"tipo": "texto", "texto": (
            "Esse processo consiste em retornar à Tabela 37 da NBR 5410 e identificar a menor seção "
            "cuja capacidade de condução seja maior ou igual à corrente admissível calculada."
        )},

        {"tipo": "texto", "texto": (
            f"Corrente admissível corrigida (I_z): {_get_valor_limpo('problema.01.003.0004') or '--'} A"
        )},

        {
            "tipo": "imagem",
            "arquivo": "tab_37.png",
            "legenda": "Tabela 37 — Capacidade de condução de corrente (NBR 5410)",
            "fonte": "NBR 5410"
        },

        {"tipo": "texto", "texto": (
            "Procedimento técnico:\n\n"
            
            "- localizar, na tabela, as correntes admissíveis para o método de instalação adotado;\n"
            "- identificar a primeira seção cuja corrente tabelada seja maior ou igual a I_z;\n"
            "- essa seção corresponde à seção mínima admissível pelo critério de corrente.\n\n"
            
            "A escolha não deve ser arbitrária. Sempre deve ser selecionada a menor seção que atenda ao critério."
        )},

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.003.0007",
            "rotulo": "Seção nominal do condutor selecionada",
            "unidade": "mm²"
        },

        {"tipo": "texto", "texto": (
            "O valor informado representa a seção mínima que atende ao critério térmico de condução de corrente."
        )},


        # =======================================================
        {"tipo": "titulo", "texto": "6. Entrega técnica: Seção por critério de corrente"},

        {"tipo": "texto", "texto": (
            "Nesta etapa, o dimensionamento é consolidado a partir da aplicação direta da norma. "
            "A análise realizada permitiu determinar a seção mínima do condutor capaz de operar "
            "em regime permanente sem ultrapassar seus limites térmicos."
            "A tabela a seguir organiza os principais parâmetros utilizados na verificação do critério de corrente."
        )},

        {"tipo": "texto", "texto": (
            "Verificação do dimensionamento por corrente\n\n"
            "| Parâmetro | Valor | Unidade |\n"
            "| :--- | :---: | :---: |\n"
            f"| Corrente de projeto (I_n) | **{_get_valor_limpo('problema.01.002.0001') or '--'}** | A |\n"
            f"| Corrente da tabela (I_tabela) | **{_get_valor_limpo('problema.01.003.0001') or '--'}** | A |\n"
            f"| Fator de temperatura (f_t) | **{_get_valor_limpo('problema.01.003.0002') or '--'}** | — |\n"
            f"| Fator de agrupamento (f_g) | **{_get_valor_limpo('problema.01.003.0003') or '--'}** | — |\n"
            f"| Corrente admissível corrigida (I_z) | **{_get_valor_limpo('problema.01.003.0004') or '--'}** | A |\n"
            f"| Seção nominal selecionada | **{_get_valor_limpo('problema.01.003.0007') or '--'}** | mm² |\n <br>"
        )},

        {"tipo": "texto", "texto": (
            "Resultado técnico:\n\n"
            
            "A seção nominal obtida representa a mínima seção admissível que atende ao critério de condução de corrente, "
            "garantindo que o condutor opere dentro dos limites térmicos estabelecidos pela norma.\n\n"
            
            "Esse resultado constitui a primeira restrição do dimensionamento elétrico. "
            "A seção selecionada é válida sob o ponto de vista térmico, mas ainda deve ser verificada "
            "em relação a outros critérios de desempenho do circuito."
        )},


        # ========================================================
        {"tipo": "titulo", "texto":"Fechamento da etapa"},

        {"tipo": "texto", "texto": (
            "Neste ponto, o dimensionamento passa a ser conduzido por critérios normativos consolidados.\n\n"
            
            "Você já estabeleceu:\n"
            "- a corrente de projeto do sistema;\n"
            "- a corrente admissível corrigida do condutor;\n"
            "- a verificação do critério térmico (I_z ≥ I_n);\n"
            "- a seleção da seção nominal mínima a partir da Tabela 37.\n\n"
            
            "A seção definida nesta etapa representa a condição mínima segura de operação térmica do condutor.\n\n"
            
            "No entanto, o dimensionamento ainda não está concluído. "
            "A seção selecionada deve agora ser verificada quanto ao desempenho elétrico do circuito.\n\n"
            
            "Na próxima etapa, será analisada a queda de tensão, "
            "avaliando se a energia elétrica chega ao motor dentro dos limites aceitáveis de operação."
        )},

        #         {"tipo": "video", "url": "https://www.youtube.com/watch?v=RlKngsvhs1w",},
        # {"tipo": "video", "url": "https://www.youtube.com/watch?v=HHpZWMVLIyQ",},
    ]




