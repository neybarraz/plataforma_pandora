
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


def _status_dado(qid: str, unidade: str = "") -> str:
    valor = _get_valor_limpo(qid)

    if valor is None:
        return '<span style="color:#dc2626;">✖ Não informado</span>'

    return f'<span style="color:#16a34a;">{valor} {unidade}</span>'
# ================================================
# BLOCO DE TEXTO
# ================================================
def get_blocos() -> list[dict]:
    return [
# O raciocínio é:
# 1. o motor exige uma certa **corrente**
# 2. essa corrente circula por um cabo com **resistência** e, em alguns casos, **reatância**
# 3. ao longo do percurso, parte da tensão se perde no cabo
# 4. essa perda é a **queda de tensão**
# A forma prática de calcular depende de o circuito ser monofásico ou trifásico e do nível de precisão desejado.
        # ========================================================
        {"tipo": "titulo", "texto":"1. Avaliação da tensão nos terminais da carga"},

        {"tipo": "texto", "texto": (
            "Na etapa anterior, foi determinada a corrente nominal do motor, "
            "representando o esforço elétrico exigido pelo sistema em regime permanente. "
            "Esse valor define quanto de corrente precisa circular no circuito para que o motor funcione corretamente."
        )},

        {"tipo": "subtitulo", "texto": (
            "O que acontece com essa corrente ao longo do cabo?"
        )},

        {"tipo": "texto", "texto": (
            "A corrente elétrica não é transferida instantaneamente entre a fonte e o motor. "
            "Ela percorre um caminho físico (o condutor) que apresenta propriedades elétricas próprias."
            "Todo condutor possui resistência elétrica e, dependendo da configuração do circuito, "
            "também pode apresentar reatância. Essas grandezas representam a oposição à passagem da corrente elétrica."
            "Quando a corrente circula por esse meio físico, ocorre dissipação de energia ao longo do percurso. "
            "Parte da energia fornecida pela fonte não chega ao motor, sendo convertida em calor no condutor."
        )},

        # ========================================================
        {"tipo": "subtitulo", "texto":"Raciocínio físico da queda de tensão"},

        {"tipo": "texto", "texto": (
            "O fenômeno da queda de tensão pode ser compreendido a partir de uma sequência lógica simples:\n\n"
            "1. O motor exige uma determinada corrente elétrica, definida na etapa anterior;\n"
            "2. Essa corrente percorre um condutor que possui resistência elétrica (e, em alguns casos, reatância);\n"
            "3. Ao longo do percurso, ocorre dissipação de energia devido ao efeito Joule;\n"
            "4. Como consequência, a tensão disponível no final do circuito é menor do que a tensão na origem.\n\n"
            
            "Essa diferença entre a tensão de alimentação e a tensão nos terminais do motor é chamada de queda de tensão."
            "Portanto, a queda de tensão não é um erro do sistema, mas um fenômeno físico inevitável. "
            "O objetivo do dimensionamento não é eliminá-la, mas garantir que ela permaneça dentro de limites aceitáveis."
        )},


## 1. O que precisa ter para calcular
    # Os dados mais importantes são:
    #     **Do motor / carga**
    #         * potência
    #         * tensão nominal
    #         * fator de potência
    #         * rendimento
    #         * tipo de alimentação: monofásico ou trifásico
    #     **Do circuito**
    #         * comprimento do cabo
    #         * seção do condutor em mm²
    #         * material do condutor, normalmente cobre ou alumínio
    #         * método de instalação, quando for usar valores tabelados mais completos
    #     **Para cálculo mais detalhado**
    #         * resistividade do material ou resistência elétrica do cabo
    #         * reatância do cabo, se quiser um cálculo mais completo
    #         * temperatura de operação, porque ela altera a resistência


        # ========================================================
        {"tipo": "titulo", "texto":"2. Parâmetros necessários para modelagem da queda de tensão"},

        {"tipo": "texto", "texto": (
            "O cálculo da queda de tensão não depende de uma única grandeza isolada. "
            "Ele resulta da interação entre a carga (motor) e o circuito elétrico que transporta a energia."
            "Para que a análise seja tecnicamente consistente, é necessário organizar os dados em três grupos: "
            "parâmetros da carga, características do circuito e propriedades elétricas do condutor."
        )},

        {"tipo": "texto", "texto": (
            "Dados do motor (carga):\n\n"
            f"- potência do motor:               **{_status_dado('problema.01.001.0001', 'kW') or '--'}**;\n"
            f"- tensão nominal de alimentação:   **{_status_dado('problema.01.001.0002', 'V') or '--'}**;\n"
            f"- fator de potência (cosφ):        **{_status_dado('problema.01.001.0003') or '--'}**;\n"
            f"- rendimento (η):                  **{_status_dado('problema.01.001.0004') or '--'}**;\n"
            "- tipo de alimentação (monofásico ou trifásico): ❌"
        )},

        {"tipo": "texto", "texto": (
            "Dados do circuito elétrico:\n\n"
            f"- comprimento do circuito (distância entre fonte e carga): **{_status_dado('problema.01.001.0005', 'm') or '--'}**;\n"
            f"- seção do condutor: **{_status_dado('problema.01.001.0007', 'mm²') or '--'}**;\n"
            "- material do condutor (cobre ou alumínio): ❌\n"
            "- método de instalação: ❌"
        )},

        {"tipo": "texto", "texto": (
            "Dados elétricos do condutor:\n\n"
            "- resistividade elétrica do material (ou resistência por unidade de comprimento): ❌\n"
            "- reatância do cabo (em circuitos onde o efeito indutivo é relevante): ❌\n"
            "- temperatura de operação, que altera a resistência elétrica do condutor: ❌"
        )},


## 2. Primeiro passo: calcular a corrente do motor
    # Antes da queda de tensão, normalmente você precisa da corrente.
    ### Motor monofásico    [I = \frac{P}{V \cdot \cos\varphi \cdot \eta}]
    ### Motor trifásico     [I = \frac{P}{\sqrt{3}\cdot V \cdot \cos\varphi \cdot \eta}]



        # ========================================================
        {"tipo": "subtitulo", "texto": "3. Cálculo da corrente do motor"},

        {"tipo": "texto", "texto": (
            "Nas etapas anteriores, foram determinadas duas grandezas fundamentais do problema: "
            "a corrente nominal do motor e a corrente admissível do condutor. "
            "Neste ponto, não será necessário recalcular esses valores, mas compreender o papel de cada um no dimensionamento. \n\n<br>"
    
            "A corrente nominal é obtida a partir dos dados do motor: potência, tensão, fator de potência e rendimento. "
            "Ela representa o esforço elétrico exigido pelo sistema em condições normais de operação. "
            "Já a corrente admissível é definida com base na NBR 5410, considerando as condições reais de instalação, "
            "como temperatura ambiente e agrupamento de circuitos. "
            "Ela representa o limite térmico seguro do condutor. \n\n"

            "Para a análise de queda de tensão, a grandeza relevante é a corrente que efetivamente circula no circuito. "
            "Esse valor corresponde à corrente nominal do motor, previamente calculada."
        )},

        {"tipo": "texto", "texto": (
            f"Corrente considerada no circuito: {_status_dado('problema.01.002.0001', 'A') or '--'}"
        )},

        {"tipo": "texto", "texto": (
            "Essa corrente será utilizada como entrada no cálculo da queda de tensão, "
            "pois é ela que percorre o condutor e determina o nível de perdas elétricas ao longo do circuito."
        )},




## 3. Calcular a resistência do cabo
    # A resistência elétrica do condutor pode ser obtida por: [R = \rho \cdot \frac{L}{S}]
    # Para cobre, usa-se com frequência:  [\rho \approx 0{,}0175 \ \Omega \cdot mm^2/m]
    # Para alumínio:                      [\rho \approx 0{,}028 \ \Omega \cdot mm^2/m]


        # ========================================================
        {"tipo": "subtitulo", "texto": "4. Cálculo da resistência elétrica do condutor"},

        {"tipo": "texto", "texto": (
            "A queda de tensão ao longo do circuito está diretamente associada à resistência elétrica do condutor. "
            "Quanto maior a resistência, maior será a perda de tensão para uma mesma corrente. "
            "A resistência elétrica do condutor (R, unidade Ω) do cabo depende de três fatores principais: ρ, resistividade do material (Ω·mm²/m); "
            "L, comprimento do circuito (m); e S, seção do condutor (mm²). "
            "Essas grandezas se relacionam pela seguinte expressão:"
        )},

        {"tipo": "equacao",
        "latex": r"R = \rho \cdot \frac{L}{S}"
        },

        {"tipo": "texto", "texto": (
            "A resistividade depende do material do condutor. "
            "Na prática, utilizam-se valores padronizados para facilitar o cálculo."
        )},

        {"tipo": "texto", "texto": (
            "Valores usuais:\n\n"
            
            "- cobre: ρ ≈ 0,0175 Ω·mm²/m;\n"
            "- alumínio: ρ ≈ 0,028 Ω·mm²/m."
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.004.0001",
            "rotulo": "Resistividade do material (ρ)",  "unidade": "Ω·mm²/m", "placeholder": "Ex: 0.0175 (cobre)"
        },


        {"tipo": "texto", "texto": (
            "Os valores de comprimento e seção do condutor já foram definidos nas etapas anteriores e serão reutilizados neste cálculo."
        )},

        {"tipo": "texto", "texto": (
            f"Comprimento do circuito (L): {_status_dado('problema.01.001.0005', 'm') or '--'}\n\n"
            f"Seção do condutor (S): {_status_dado('problema.01.001.0007', 'mm²') or '--'}"
        )},


        {"tipo": "texto", "texto": (
            "Substitua os valores na equação e determine a resistência elétrica do condutor."
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.004.1002",
            "rotulo": "Resistência elétrica do condutor", "unidade": "Ω", "placeholder": "Ex: 550"
        },

        {"tipo": "texto", "texto": (
            "Esse valor representa a oposição à passagem da corrente ao longo do cabo "
            "e será utilizado diretamente no cálculo da queda de tensão."
        )},



        # ========================================================
        {"tipo": "subtitulo", "texto": "5. Cálculo da reatância do condutor"},

        {"tipo": "texto", "texto": (
            "Além da resistência elétrica, condutores percorridos por corrente alternada também apresentam reatância. "
            "A reatância está associada aos efeitos magnéticos gerados pela variação da corrente no tempo, "
            "especialmente em circuitos com maior comprimento ou em sistemas trifásicos.\n\n"
            
            "Embora, em muitos casos práticos, a resistência seja predominante, a reatância deve ser considerada "
            "para uma análise mais completa da queda de tensão."
        )},

        {"tipo": "texto", "texto": (
            "A reatância do cabo depende principalmente do comprimento do circuito e das características construtivas do condutor. "
            "Ela representa a oposição adicional à passagem da corrente alternada, associada aos efeitos magnéticos no entorno do condutor. "
            "De forma simplificada, a reatância total (X), expressa em ohms (Ω), pode ser determinada a partir do produto entre a reatância por unidade de comprimento (x, em Ω/m) "
            "e o comprimento do circuito (L, em metros). Essa relação pode ser expressa por:"
        )},
                
        {"tipo": "equacao",
        "latex": r"X = x \cdot L"
        },

        {"tipo": "texto", "texto": (
            "A reatância por unidade de comprimento depende do tipo de cabo e da forma de instalação. "
            "Na prática, para circuitos de baixa tensão, utilizam-se valores aproximados."
        )},

        {"tipo": "texto", "texto": (
            "Valor típico:\n\n"
            
            "- cabos de baixa tensão: x ≈ 0,08 mΩ/m (0,00008 Ω/m)\n\n"
            
            "Esse valor típico utilizado para reatância em cabos de baixa tensão. "
            "Para maior precisão, devem ser utilizados valores tabelados conforme a NBR 5410 ou catálogos de fabricantes."
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.004.0003",
            "rotulo": "Reatância por unidade de comprimento", "unidade": "Ω/m", "placeholder": "Ex: 0.00008"
        },

        {"tipo": "texto", "texto": (
            "O comprimento do circuito já foi definido anteriormente e será reutilizado neste cálculo. "
            f"Comprimento do circuito (L): {_status_dado('problema.01.001.0005', 'm') or '--'}. "
            "Substitua os valores na equação e determine a reatância total do condutor."
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.004.0004",
            "rotulo": "Reatância do condutor", "unidade": "Ω"
        },

        {"tipo": "texto", "texto": (
            "Esse valor representa a oposição adicional à passagem da corrente alternada no condutor "
            "e será utilizado no cálculo completo da queda de tensão."
        )},

## 4. Fórmulas da queda de tensão
    ### Caso simplificado — monofásico      [\Delta V = 2 \cdot I \cdot R]
        # O fator 2 aparece porque a corrente percorre ida e volta.
    ### Caso simplificado — trifásico       [\Delta V = \sqrt{3}\cdot I \cdot R]

    ### Forma mais completa — com resistência e reatância
        #### Monofásico                     [\Delta V = 2 \cdot I \cdot (R\cos\varphi + X\sin\varphi)]
        #### Trifásico                      [\Delta V = \sqrt{3}\cdot I \cdot (R\cos\varphi + X\sin\varphi)]
            # Onde:
            #     * (R) = resistência do cabo
            #     * (X) = reatância do cabo
            # Esse modelo é mais técnico e mais fiel, principalmente em circuitos maiores.

        # ========================================================
        {"tipo": "subtitulo", "texto": "6. Cálculo da queda de tensão no circuito"},

        {"tipo": "texto", "texto": (
            "Com a corrente do circuito e os parâmetros elétricos do condutor já definidos, "
            "é possível determinar a queda de tensão ao longo do percurso entre a fonte e o motor."
            "A queda de tensão resulta da interação entre a corrente elétrica e as características do condutor. "
            "Dois efeitos físicos estão envolvidos nesse processo: a resistência elétrica, associada à dissipação de energia em forma de calor, "
            "e a reatância, associada aos efeitos magnéticos da corrente alternada.\n\n<br>"

            "Para representar esses dois efeitos de forma conjunta, utiliza-se um modelo mais completo, "
            "no qual a queda de tensão depende da resistência do cabo (R), da reatância (X), "
            "da corrente do circuito (I) e do fator de potência da carga (cosφ).\n\n"

            "Para circuitos monofásicos, a queda de tensão é dada por:"
        )},

        {"tipo": "equacao",
        "latex": r"\Delta V = 2 \cdot I \cdot (R\cos\varphi + X\sin\varphi)"
        },

        {"tipo": "texto", "texto": (
            "Para circuitos trifásicos, a queda de tensão é dada por:"
        )},

        {"tipo": "equacao",
        "latex": r"\Delta V = \sqrt{3} \cdot I \cdot (R\cos\varphi + X\sin\varphi)"
        },
        {"tipo": "texto", "texto": (
            "Nessas expressões, ΔV representa a queda de tensão no circuito (em volts), "
            "I é a corrente de projeto previamente determinada, R é a resistência do condutor e X é a reatância do cabo. "
            "O termo (R·cosφ + X·senφ) expressa a contribuição combinada dos efeitos resistivos e indutivos do circuito, "
            "considerando a defasagem entre tensão e corrente.\n\n<br>"

            "Para a aplicação prática da equação, é necessário conhecer tanto o valor do cosseno quanto do seno do ângulo φ. "
            "Normalmente, o fator de potência (cosφ) é fornecido nos dados do motor, mas o seno não é apresentado diretamente. "
            "Para obtê-lo, utiliza-se a relação trigonométrica fundamental:"
        )},

        {"tipo": "equacao",
        "latex": r"\cos^2\varphi + \sin^2\varphi = 1"
        },

        {"tipo": "texto", "texto": (
            "A partir dessa identidade, é possível determinar o valor do seno do ângulo φ a partir do fator de potência:"
        )},

        {"tipo": "equacao",
        "latex": r"\sin \varphi = \sqrt{1 - \cos^2\varphi}"
        },

        {"tipo": "texto", "texto": (
            "Com isso, torna-se possível calcular completamente o termo (R·cosφ + X·senφ) "
            "e aplicar a equação da queda de tensão de forma consistente.\n\n<br>"

            # "Esse modelo é mais completo e fornece uma representação mais fiel do comportamento real do circuito, "
            # "especialmente em instalações com maiores comprimentos ou em sistemas trifásicos, "
            # "onde os efeitos indutivos se tornam mais relevantes."
        )},

        {"tipo": "texto", "texto": (
            f"Utilizando o Fator de Potência encontrada para o motor: {_status_dado('problema.01.001.0003') or '--'} "
            "Encontre o valor para o fator de potência reativo."
        )},


        { "tipo": "entrada_numerica_inline",  "id": "problema.01.004.0005",
            "rotulo": "Fator de Potência reativo", "unidade": "--"
        },

        {"tipo": "texto", "texto": (
            "Com todos os dados necessários, listado abaixo, calcula a queda de tensão."
        )},

        {"tipo": "texto", "texto": (
            "Parâmetros do sistema\n\n"
            "| Parâmetro | Valor | Unidade |\n"
            "| :--- | :---: | :---: |\n"
            f"| Resistência do material | **{_get_valor_limpo('problema.01.004.1002') or '--'}** | — |\n"
            f"| Reatância do condutor   | **{_get_valor_limpo('problema.01.004.0004') or '--'}** | — |\n"
            f"| Fator de potência | **{_get_valor_limpo('problema.01.001.0003') or '--'}** | — |\n"
            f"| Fator de potência reativo | **{_get_valor_limpo('problema.01.004.0005') or '--'}** | — |\n"
            f"| Corrente nominal | **{_get_valor_limpo('problema.01.002.0001') or '--'}** | A |\n <br>"
        )},

                { "tipo": "entrada_numerica_inline",  "id": "problema.01.004.0006",
                    "rotulo": "Queda de tensão", "unidade": "V"
                },


## 5. Percentual de queda de tensão
    # Depois de achar (\Delta V), calcula-se:     [%\Delta V = \frac{\Delta V}{V} \cdot 100]
    # Isso mostra quanto da tensão nominal foi perdido no cabo.

        # ========================================================
        {"tipo": "subtitulo", "texto": "7. Cálculo do percentual de queda de tensão"},

        {"tipo": "texto", "texto": (
            "Após determinar a queda de tensão em volts (ΔV), é necessário avaliar o seu impacto em relação à tensão nominal do sistema. "
            "Essa análise é feita por meio do cálculo percentual da queda de tensão."
            "O percentual de queda de tensão indica quanto da tensão de alimentação é perdido ao longo do circuito, "
            "permitindo avaliar a qualidade do fornecimento de energia ao motor."
        )},

        {"tipo": "equacao",
        "latex": r" \Delta V \%= \frac{\Delta V}{V} \cdot 100\%"
        },

        {"tipo": "texto", "texto": (
            "Organize os dados necessários para o cálculo:"
        )},

        {"tipo": "texto", "texto": (
            "Parâmetros do sistema\n\n"
            "| Parâmetro | Valor | Unidade |\n"
            "| :--- | :---: | :---: |\n"
            f"| Queda de tensão (ΔV) | **{_get_valor_limpo('problema.01.004.0006') or '--'}** | V |\n"
            f"| Tensão nominal (V) | **{_get_valor_limpo('problema.01.001.0002') or '--'}** | V |\n <br>"
        )},

        {"tipo": "texto", "texto": (
            "Substitua os valores na equação e determine o percentual de queda de tensão do circuito."
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.004.0007",
        "rotulo": "Percentual de queda de tensão",
        "unidade": "%"
        },

        {"tipo": "texto", "texto": (
            "Esse valor representa a proporção da tensão de alimentação que é perdida ao longo do condutor. "
            "Na etapa seguinte, esse resultado será comparado com os limites estabelecidos em norma "
            "para verificar a adequação do dimensionamento do circuito."
        )},

        # ========================================================
        # ========================================================
        {"tipo": "subtitulo", "texto": "8. Verificação na NBR 5410"},

        {"tipo": "texto", "texto": (
            "Após determinar o percentual de queda de tensão do circuito, é necessário verificar se esse valor "
            "atende aos limites estabelecidos pela NBR 5410. Essa verificação garante que a tensão disponível nos "
            "terminais do motor seja adequada para seu funcionamento."
        )},

        {"tipo": "texto", "texto": (
            "Consulte o trecho da norma apresentado a seguir e identifique o limite admissível aplicável ao tipo de circuito analisado."
        )},

        {
            "tipo": "imagem",
            "arquivo": "nbr5410_6272.png",
            "legenda": "6.2.7 Quedas de tensão da NBR 5410",
            "fonte": "NBR 5410"
        },

        {"tipo": "texto", "texto": (
            "A partir da leitura da norma, registre o valor limite de queda de tensão correspondente:"
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.004.0008",
        "rotulo": "Limite de queda de tensão segundo a NBR 5410",
        "unidade": "%"
        },

        # ========================================================
        {"tipo": "subtitulo", "texto": "Verificação do critério"},

        {"tipo": "texto", "texto": (
            "Com o limite normativo identificado, compare-o com o valor percentual calculado para o circuito."
        )},

        {"tipo": "texto", "texto": (
            "Parâmetros de verificação\n\n"
            "| Parâmetro | Valor | Unidade |\n"
            "| :--- | :---: | :---: |\n"
            f"| Queda de tensão (%) | **{_get_valor_limpo('problema.01.004.0007') or '--'}** | % |\n"
            f"| Limite normativo | **{_get_valor_limpo('problema.01.004.0008') or '--'}** | % |\n <br>"
        )},

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.004.0009",
            "pergunta": (
                "Comparando o valor calculado com o limite da NBR 5410, qual é a conclusão sobre o circuito?"
            ),
            "alternativas": {
                "a": "O circuito atende ao critério de queda de tensão",
                "b": "O circuito não atende ao critério e deve ser redimensionado",
                "c": "Não é possível concluir",
                "d": "O critério não se aplica ao circuito"
            },
            "alternativa_correta": "a",
        },

        {"tipo": "texto", "texto": (
            "A verificação consiste em comparar diretamente os dois valores:\n\n"
            
            "- Se %ΔV ≤ limite → o circuito atende à norma;\n"
            "- Se %ΔV > limite → o circuito não atende e deve ser corrigido.\n\n"
            
            "Quando o limite não é atendido, é necessário reduzir a queda de tensão no circuito."
        )},

        # ========================================================
        {"tipo": "subtitulo", "texto": "Impacto e ações corretivas"},

        {"tipo": "texto", "texto": (
            "Uma queda de tensão acima do limite normativo compromete o desempenho do sistema. "
            "O motor passa a operar com tensão inferior à nominal, o que resulta em redução de torque, "
            "aumento da corrente elétrica e elevação da temperatura de operação.\n\n"
            
            "Para corrigir essa condição, as ações mais comuns são:\n"
            "- aumento da seção do condutor;\n"
            "- redução do comprimento do circuito;\n"
            "- revisão da configuração da instalação."
        )},

        {"tipo": "questao_multipla_escolha",
        "id": "problema.01.004.0010",
        "pergunta": (
            "Qual fator tem maior impacto direto no aumento da queda de tensão?"
        ),
        "alternativas": {
            "a": "Redução da corrente",
            "b": "Aumento da seção do condutor",
            "c": "Aumento do comprimento do circuito",
            "d": "Aumento da tensão nominal"
        },
        "alternativa_correta": "c",
        },

          # 
          # 
          #       
# Exemplo detalhado
    # Vou fazer um exemplo trifásico, que é o caso mais comum em motores.
    # ## Dados do motor
    #     * potência: (5{,}5 , kW)
    #     * tensão: (380 , V)
    #     * fator de potência: (0{,}86)
    #     * rendimento: (0{,}88)
    # ## Dados do cabo
    #     * material: cobre
    #     * comprimento: (45 , m)
    #     * seção: (6 , mm^2)

    ## Passo 1: converter potência  [P = 5{,}5 , kW = 5500 , W]
    ## Passo 2: calcular a corrente do motor        [I = \frac{5500}{\sqrt{3}\cdot 380 \cdot 0{,}86 \cdot 0{,}88}]
    # Sabendo que:        [\sqrt{3} \approx 1{,}732]
    # Então:              [I = \frac{5500}{1{,}732 \cdot 380 \cdot 0{,}86 \cdot 0{,}88}]
    #                     [I = \frac{5500}{498{,}4}]
    #                     [I \approx 11{,}03 , A]
    ## Passo 3: calcular a resistência do cabo  [R = \rho \cdot \frac{L}{S}]
                                                # [R = 0{,}0175 \cdot \frac{45}{6}]
                                                # [R = 0{,}0175 \cdot 7{,}5]
                                                # [R = 0{,}13125 , \Omega]
    ## Passo 4: calcular a queda de tensão trifásica simplificada
        # [\Delta V = \sqrt{3}\cdot I \cdot R]
        # [\Delta V = 1{,}732 \cdot 11{,}03 \cdot 0{,}13125]
        # [\Delta V \approx 2{,}51 , V]
    ## Passo 5: calcular o percentual de queda
        # [%\Delta V = \frac{2{,}51}{380}\cdot 100]
        # [%\Delta V \approx 0{,}66%]

    ## Resultado final do exemplo
        # * corrente do motor: **11,03 A**
        # * queda de tensão: **2,51 V**
        # * queda percentual: **0,66%**
        # Isso indica que, nesse exemplo, a queda de tensão é baixa e o circuito está, em princípio, adequado sob esse critério.

    # Interpretação física
        # A queda de tensão depende principalmente de quatro coisas:
        ### 1. Corrente: Quanto maior a corrente, maior a queda de tensão.
        ### 2. Comprimento: Quanto maior o cabo, maior a resistência e maior a queda.
        ### 3. Seção do cabo: Quanto maior a seção, menor a resistência e menor a queda.
        ### 4. Material: Cobre tem menor resistividade que alumínio, então tende a apresentar menor queda para a mesma seção.

    # Os erros mais comuns são:
    #     * usar potência em kW sem converter para W
    #     * esquecer fator de potência e rendimento no cálculo da corrente
    #     * usar fórmula monofásica em circuito trifásico
    #     * esquecer que no monofásico existe ida e volta
    #     * usar comprimento estimado errado
    #     * confundir bitola instalada com bitola calculada
    #     * ignorar que a resistência varia com a temperatura


# ======================================================== 
{"tipo": "titulo", "texto":"7. Entrega técnica: Conformidade de tensão"},

{"tipo": "texto", "texto": (
    "Nesta etapa, foi realizada a verificação da conformidade do circuito quanto ao critério de queda de tensão, "
    "conforme estabelecido pela NBR 5410. "
    "A análise consistiu na determinação da queda de tensão ao longo do circuito e na sua comparação com o limite normativo aplicável. "
    "A partir dos dados do sistema, foram obtidos os seguintes resultados:\n\n"

    f"- Corrente do circuito: **{_get_valor_limpo('problema.01.002.0001') or '--'} A**;\n"
    f"- Queda de tensão: **{_get_valor_limpo('problema.01.004.0006') or '--'} V**;\n"
    f"- Queda de tensão percentual: **{_get_valor_limpo('problema.01.004.0007') or '--'} %**;\n"
    f"- Limite normativo: **{_get_valor_limpo('problema.01.004.0008') or '--'} %**.\n\n"

    "Critério normativo aplicado:\n\n"

    "- Se %ΔV ≤ limite → o circuito atende ao critério de queda de tensão;\n"
    "- Se %ΔV > limite → o circuito não atende ao critério.\n\n"

    "Resultado da verificação:\n\n"

    "A comparação entre o valor calculado e o limite normativo permite avaliar diretamente "
    "a conformidade do circuito quanto ao desempenho elétrico.\n\n"

    "Quando o critério é atendido, garante-se que a tensão nos terminais do motor permanece "
    "dentro de uma faixa adequada de operação, assegurando o desempenho e a eficiência do sistema. "
    "Caso contrário, a instalação pode apresentar redução de torque, aumento de corrente e aquecimento excessivo.\n\n"

    "Conclusão técnica:\n\n"

    "O circuito foi avaliado com base no critério de queda de tensão estabelecido pela NBR 5410, "
    "permitindo verificar sua adequação quanto à qualidade da energia fornecida à carga.\n\n"

    "Este resultado complementa o dimensionamento obtido anteriormente pelo critério de corrente. "
    "A seção do condutor somente é considerada adequada quando atende simultaneamente aos critérios térmico "
    "e de queda de tensão."
)},
 
        # {"tipo": "texto", "texto": (
        #     "Parâmetros de verificação\n\n"
        #     "| Parâmetro | Valor | Unidade |\n"
        #     "| :--- | :---: | :---: |\n"
            
        #     f"| Corrente do circuito (I) | **{_get_valor_limpo('problema.01.002.0001') or '--'}** | A |\n"
        #     f"| Comprimento do circuito (L) | **{_get_valor_limpo('problema.01.001.0005') or '--'}** | m |\n"
        #     f"| Seção do condutor (S) | **{_get_valor_limpo('problema.01.001.0007') or '--'}** | mm² |\n"
            
        #     f"| Resistência do condutor (R) | **{_get_valor_limpo('problema.01.004.1002') or '--'}** | Ω |\n"
        #     f"| Reatância do condutor (X) | **{_get_valor_limpo('problema.01.004.0004') or '--'}** | Ω |\n"
            
        #     f"| Queda de tensão (ΔV) | **{_get_valor_limpo('problema.01.004.0006') or '--'}** | V |\n"
        #     f"| Queda de tensão (%) | **{_get_valor_limpo('problema.01.004.0007') or '--'}** | % |\n"
            
        #     f"| Limite normativo | **{_get_valor_limpo('problema.01.004.0008') or '--'}** | % |\n"
            
        #     "<br>"
        # )},

        # ========================================================
        {"tipo": "subtitulo", "texto":"Fechamento da etapa"},

        {"tipo": "texto", "texto": (
            "Neste ponto, você já avaliou se o sistema entrega energia com qualidade adequada.\n\n"
            
            "Você já possui:\n"
            "- verificação da queda de tensão;\n"
            "- comparação com limite normativo;\n"
            "- diagnóstico de desempenho elétrico.\n\n"
            
            "Caso o sistema não esteja conforme, a seção do condutor deve ser revista.\n\n"
            
            "Na próxima etapa, será analisado o comportamento térmico do circuito, "
            "considerando as perdas por efeito Joule ao longo do tempo."
        )},
    ]