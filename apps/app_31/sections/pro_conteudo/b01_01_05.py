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


def _status_dado(qid: str, unidade: str = "") -> str:
    valor = _get_valor_limpo(qid)

    if valor is None:
        return '<span style="color:#dc2626;">✖ Não informado</span>'

    return f'<span style="color:#16a34a;">{valor} {unidade}</span>'

def get_blocos() -> list[dict]:
    return [
        {"tipo": "titulo", "texto":"1. Verificação térmica do condutor"},

        {"tipo": "texto", "texto": (
            "Nas etapas anteriores, foi verificado que o condutor atende aos critérios de condução de corrente "
            "e de queda de tensão, garantindo o funcionamento elétrico adequado do circuito. "
            "A partir deste ponto, o problema deixa de ser apenas elétrico e passa a incorporar uma análise térmica. "
            "Não basta que o cabo conduza corrente: é necessário garantir que essa operação ocorra sem comprometer "
            "sua integridade física ao longo do tempo.\n\n<br>"

            "**Mesmo atendendo aos critérios de corrente e queda de tensão, o cabo operará termicamente de forma segura?**\n\n<br>"

            "A passagem de corrente elétrica pelo condutor provoca aquecimento, decorrente das perdas por efeito Joule. "
            "Esse aquecimento eleva a temperatura do material e, principalmente, da isolação que o envolve. "
            "Se a temperatura de operação ultrapassar os limites admissíveis, ocorre degradação progressiva da isolação, "
            "reduzindo a vida útil do condutor e podendo levar a falhas elétricas.\n\n<br>"
            
            "Nesta etapa, o objetivo é verificar se o calor gerado durante a operação pode ser dissipado adequadamente, "
            "mantendo a temperatura do condutor dentro dos limites seguros estabelecidos em norma."
        )},

        # ========================================================
        {"tipo": "titulo", "texto":"2. Parâmetros para análise térmica do condutor"},

        {"tipo": "texto", "texto": (
            "A verificação térmica do condutor não é realizada diretamente a partir da temperatura ou da potência dissipada, "
            "mas sim por meio da comparação entre a corrente de operação e a capacidade térmica admissível do cabo. "
            "Para isso, é necessário reunir os parâmetros que representam, de um lado, o esforço elétrico imposto ao condutor "
            "e, de outro, sua capacidade de suportar esse esforço sem degradação da isolação. "
            "Além disso, a resistência elétrica é considerada para interpretar o nível de aquecimento gerado no circuito. "
            "Esses parâmetros permitem estabelecer uma leitura técnica consistente sobre a condição térmica de operação."
        )},

        {"tipo": "texto", "texto": (
            f"\n\n- corrente de projeto: **{_status_dado('problema.01.002.0001', 'A')}**;\n"
            f"- corrente admissível corrigida: **{_status_dado('problema.01.003.0004', 'A')}**;\n"
            f"- resistência do condutor: **{_status_dado('problema.01.004.1002', 'Ω')}**."
        )},


        # ========================================================
        {"tipo": "titulo", "texto":"3. Quantificação do aquecimento do condutor"},

        {"tipo": "texto", "texto": (
            "Quando a corrente elétrica percorre um condutor, parte da energia é inevitavelmente dissipada na forma de calor, "
            "devido à resistência elétrica do material. Esse fenômeno, conhecido como efeito Joule, é o responsável direto "
            "pelo aquecimento dos cabos em operação. "
            "A intensidade desse aquecimento depende de duas grandezas fundamentais: a corrente que circula no circuito e "
            "a resistência do condutor. Essa relação é expressa pela potência dissipada:"
        )},

        {"tipo": "equacao", "latex": r"P_{perda} = I^2 \cdot R"},

        {"tipo": "texto", "texto": (
            "Essa equação mostra que o aquecimento cresce com o quadrado da corrente. "
            "Isso significa que pequenos aumentos de corrente provocam aumentos significativos na geração de calor, "
            "tornando o controle da corrente essencial para a segurança térmica do sistema. \n\n<br>"
            "A quantificação dessa potência permite responder objetivamente: "
            "quanto calor o cabo está gerando durante a operação. "
            "Embora esse valor não seja utilizado diretamente como critério normativo, ele é fundamental para compreender "
            "o nível de esforço térmico imposto ao condutor e justificar a necessidade da verificação térmica baseada na norma.\n\n<br>"

            "Substitua os valores na equação e determine a potência dissipada no condutor:"
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.005.0001",
            "rotulo": "Potência dissipada", "unidade": "W"
        },

        {"tipo": "texto", "texto": (
            "O valor obtido representa a taxa de geração de calor no cabo. "
            "Esse resultado será utilizado na etapa seguinte para interpretar se a condição de operação é compatível "
            "com os limites térmicos admissíveis da isolação."
        )},

        # ========================================================
        {"tipo": "titulo", "texto":"4. Critério de verificação térmica"},

        {"tipo": "texto", "texto": (
            "Na etapa anterior, foi determinada a corrente de projeto do sistema, que representa o esforço elétrico "
            "exigido pelo motor em operação. "
            "Agora, essa corrente deixa de ser apenas um resultado e passa a ser um critério de verificação. "
            "A norma estabelece um limite máximo de corrente que o condutor pode suportar sem ultrapassar "
            "a temperatura admissível da isolação. Esse limite é representado pela corrente admissível (I_admissível).\n\n<br>"

            "Portanto, o problema técnico passa a ser:\n\n"
            "**comparar a corrente exigida pelo sistema com a capacidade térmica do condutor.**"
        )},

        {"tipo": "equacao", "latex": r"I_{projeto} \le I_{admissível}"},

        {"tipo": "texto", "texto": (
            "Interpretação física:\n\n"

            "- A corrente que circula no cabo gera calor (efeito Joule);\n"
            "- Esse calor precisa ser dissipado para o ambiente;\n"
            "- O condutor possui um limite térmico definido pela isolação;\n"
            "- A norma traduz esse limite em uma corrente máxima admissível.\n\n"

            "Assim, não é necessário calcular diretamente a temperatura do cabo, "
            "pois a NBR 5410 já incorpora esse comportamento térmico nos valores de corrente admissível."
        )},

        {"tipo": "texto", "texto": (
            "Critério de segurança:\n\n"

            "- Se I_projeto ≤ I_admissível → o condutor opera dentro do limite térmico;\n"
            "- Se I_projeto > I_admissível → há risco de sobreaquecimento e degradação da isolação.\n\n"

            "Essa verificação estabelece se o condutor é capaz de suportar continuamente "
            "a carga elétrica imposta pelo sistema."
        )},

        {"tipo": "subtitulo", "texto": "Análise crítica da condição térmica"},

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.005.0002",
            "pergunta": (
                "Por que a verificação térmica do condutor é feita comparando correntes "
                "e não diretamente a potência dissipada (I²R)?"
            ),
            "alternativas": {
                "a": "Porque a potência dissipada não influencia o aquecimento do condutor.",
                "b": "Porque a norma já incorpora os efeitos térmicos na corrente admissível.",
                "c": "Porque a resistência do condutor é constante.",
                "d": "Porque a corrente não depende da potência."
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "questao_texto",
            "id": "problema.01.005.0003",
            "pergunta": (
                "Se a corrente de projeto estiver muito próxima da corrente admissível, "
                "mesmo atendendo ao critério I_projeto ≤ I_admissível, "
                "isso representa uma condição tecnicamente segura? Justifique."
            )
        },
# ========================================================
{"tipo": "titulo", "texto":"5. Entrega técnica: verificação térmica"},

{"tipo": "texto", "texto": (
    "Resumo da análise:\n\n"
    f"- corrente de projeto: **{_status_dado('problema.01.002.0001', 'A')}**;\n"
    f"- corrente admissível: **{_status_dado('problema.01.003.0004', 'A')}**;\n"
    f"- potência dissipada: **{_status_dado('problema.01.005.0001', 'W')}**.\n"

    "- **Interpretação:** a potência dissipada representa o calor gerado no condutor devido à circulação de corrente. "
    "Esse valor permite compreender o esforço térmico imposto ao cabo, mas não é utilizado "
    "diretamente como critério de dimensionamento.\n"
    "- **Conclusão:** se a corrente admissível for maior ou igual à corrente de projeto, "
    "o condutor opera dentro dos limites térmicos seguros estabelecidos pela norma."
)},


# ========================================================
{"tipo": "subtitulo", "texto":"Fechamento da etapa"},

{"tipo": "texto", "texto": (
    "A verificação térmica garante que o condutor não apenas conduz corrente, "
    "mas opera de forma segura ao longo do tempo. "
    "Com isso, o dimensionamento atende simultaneamente aos critérios elétricos e térmicos da instalação."
)}

    ]














#         # ========================================================
#         { "tipo": "titulo", "texto": "3. Fundamento físico do aquecimento do condutor" },


#     { "tipo": "texto", "texto": (
#         "\n\n- **Interpretação física do fenômeno:** a corrente elétrica percorre o condutor para alimentar a carga, "
#         "mas o condutor oferece resistência à passagem dessas cargas. Essa resistência converte parte da "
#         "energia elétrica em calor, que se acumula no condutor e eleva sua temperatura. Ou seja, o aquecimento "
#         "não é um efeito colateral qualquer, mas uma consequência inevitável da condução de corrente.\n\n"

#         "- **Influência da corrente no aquecimento:** o aquecimento é proporcional ao quadrado da corrente (I²), "
#         "o que significa que pequenas variações na corrente provocam grandes variações térmicas. "
#         "Por exemplo, se a corrente dobra, a potência dissipada aumenta quatro vezes; "
#         "se a corrente aumenta 20%, o aquecimento aumenta cerca de 44%. Essa relação torna o controle da "
#         "corrente essencial para a segurança térmica do sistema.\n\n"

#         "- **Conclusão física da etapa:** o condutor aquece porque dissipa energia elétrica na forma de calor. "
#         "A intensidade desse aquecimento depende diretamente da corrente que circula e da resistência do cabo. "
#         "Assim, quanto maior a corrente ou a resistência, maior será a geração de calor. A análise térmica, "
#         "portanto, consiste em verificar se esse calor consegue ser dissipado sem elevar a temperatura do "
#         "condutor além do limite suportado pela isolação."
#     )},



# # ## 4. Calcular a potência dissipada no cabo
#     # Primeiro produto físico da etapa: [P_{perda} = I^2 \cdot R]
#     # Isso responde:
#         # **quanto calor o cabo gera eletricamente**
#         # Esse valor não é utilizado diretamente como critério normativo,
#         # mas permite compreender fisicamente o aquecimento do condutor.

#         # ========================================================
#         {"tipo": "titulo", "texto":"4. Quantificação da potência dissipada no condutor"},

#         {"tipo": "texto", "texto": (
#             "A partir do fundamento físico estabelecido anteriormente, é possível quantificar o aquecimento do condutor. "
#             "Até este ponto, foi compreendido que a circulação de corrente em um meio resistivo gera calor. "
#             "Agora, o objetivo é determinar quanto calor está sendo efetivamente gerado no cabo em operação. "
#             "Essa quantificação é realizada por meio da potência dissipada por efeito Joule, que representa a energia elétrica "
#             "convertida em calor ao longo do condutor."
#         )},

#         {"tipo": "equacao",
#         "latex": r"P_{perda} = I^2 \cdot R"
#         },

#         {"tipo": "texto", "texto": (
#             "Substituindo os valores do problema:\n\n"
#             f"- corrente de projeto: **{_status_dado('problema.01.002.0001', 'A') or '--'}**;\n"
#             f"- resistência do condutor: **{_status_dado('problema.01.004.1002', 'Ω') or '--'}**.\n\n"
            
#             "A partir desses valores, aplique a equação do efeito Joule para determinar a potência dissipada no condutor."
#         )},
#         { "tipo": "entrada_numerica_inline", "id": "problema.01.005.0001",
#             "rotulo": "Potência dissipada pelo cabo", "unidade": "W"
#         },
#         { "tipo": "texto", "texto": (
#             "A potência calculada representa a taxa de geração de calor no condutor, ou seja, "
#             "quanta energia elétrica está sendo transformada em calor a cada instante. "
#             "A norma não estabelece limites diretos para esse valor, mas ele é essencial para compreender "
#             "o comportamento térmico do sistema."
    
#             "\n\n - **Interpretação técnica:** a potência dissipada traduz diretamente o esforço térmico imposto ao condutor. "
#             "Valores elevados indicam maior tendência de aquecimento, especialmente porque a corrente entra ao quadrado na equação."
 
#             "\n\n - **Conclusão:** com esse valor, a análise deixa de ser apenas elétrica e passa a considerar se o calor "
#             "gerado pode ser dissipado sem elevar a temperatura do condutor acima dos limites da isolação. "
#             "Essa verificação será realizada na próxima etapa."
#         )},

# # ## 5. Relacionar geração de calor com condição térmica
#     # Agora entra a pergunta de segurança:
#     # **esse calor gerado consegue ser dissipado sem elevar a temperatura do cabo acima do limite da isolação?**

#     # A capacidade de dissipação térmica do cabo não é analisada diretamente por meio de potência,
#     # mas sim por critérios normativos definidos na NBR 5410.
    
#     # A norma já incorpora os efeitos térmicos por meio:
#         # * da capacidade de condução de corrente
#         # * dos fatores de correção (temperatura, agrupamento, instalação)

#     # Portanto, a análise térmica consiste em interpretar o aquecimento pelo efeito Joule
#     # e verificar se a condição de operação permanece dentro dos limites seguros definidos pela norma.

#     # ========================================================
#         {"tipo": "titulo", "texto":"5. Relação entre geração de calor e condição térmica do condutor"},

#         {"tipo": "texto", "texto": (
#             "A partir da potência dissipada calculada, foi possível quantificar o calor gerado no condutor durante a operação. "
#             "No entanto, a análise térmica não se limita à geração de calor. "
#             "A questão central passa a ser:\n\n<br>"
            
#             "**Esse calor consegue ser dissipado sem elevar a temperatura do cabo acima do limite suportado pela isolação?**\n\n<br>"

#             "O aquecimento do condutor depende de dois fatores simultâneos:\n\n"
            
#             "- a quantidade de calor gerada (determinada por I²R);\n"
#             "- a capacidade do sistema de dissipar esse calor para o ambiente.\n\n"
            
#             "Se a geração de calor for maior que a capacidade de dissipação, a temperatura do condutor se eleva progressivamente, "
#             "podendo ultrapassar os limites térmicos da isolação."
#             "Entretanto, na prática de engenharia, essa verificação não é realizada diretamente por meio da potência dissipada. "
#             "A capacidade térmica do condutor é tratada de forma indireta por meio de critérios normativos estabelecidos na NBR 5410."
#         )},

#         {"tipo": "texto", "texto": (
#             "A norma já incorpora os efeitos térmicos do aquecimento por meio de parâmetros que limitam a operação do condutor, como:\n\n"
            
#             "- capacidade de condução de corrente (obtida em tabelas);\n"
#             "- fatores de correção por temperatura ambiente;\n"
#             "- fatores de correção por agrupamento de circuitos;\n"
#             "- condições de instalação do cabo.\n\n"
            
#             "Esses fatores ajustam a corrente admissível do condutor de modo a garantir que a temperatura de operação "
#             "não ultrapasse o limite da isolação."
#         )},

#         {"tipo": "texto", "texto": (
#             "Dessa forma, a análise térmica não consiste em comparar diretamente a potência dissipada com um valor limite, "
#             "mas em verificar se a corrente de operação do circuito está dentro da capacidade admissível corrigida do condutor."
#         )},

#         {"tipo": "texto", "texto": (
#             "Conclusão técnica da etapa:\n\n"
            
#             "O aquecimento do condutor é explicado pelo efeito Joule (I²R), mas a verificação de segurança térmica é realizada "
#             "por meio da corrente admissível definida pela norma.\n\n"
            
#             "Assim, se a corrente de projeto for menor ou igual à corrente admissível corrigida, o calor gerado será dissipado "
#             "sem comprometer a isolação. Caso contrário, o condutor poderá operar em sobreaquecimento."
#         )},

# # ## 6. Critério técnico da etapa
#     # A etapa precisa terminar com um critério binário.

#     # Critério principal:
#         # **A operação é considerada termicamente segura quando a corrente de projeto não excede
#         # a capacidade de condução corrigida do condutor.**

#     # Interpretação:
#         # * Se I_projeto ≤ I_admissível → condição térmica segura
#         # * Se I_projeto > I_admissível → risco de sobreaquecimento

#     # Interpretação física:
#         # * o aquecimento do cabo é proporcional a I²R
#         # * a NBR já garante que, dentro da corrente admissível, esse aquecimento não compromete a isolação

# # ## 7. Produto calculado da etapa
#         # * **Potência dissipada no cabo (I²R)**
#         # * **Interpretação do aquecimento do condutor**
#         # * **Verificação da condição térmica pela norma**
#         # * **Conclusão sobre a segurança térmica da isolação**

#     # Tabela com:
#         # * corrente de projeto
#         # * corrente admissível
#         # * resistência do cabo
#         # * potência dissipada
#         # * temperatura ambiente
#         # * seção adotada
#         # * conclusão térmica (atende / não atende)

#     # Fechamento
#         # O condutor não deve apenas conduzir corrente e manter a tensão adequada,
#         # mas também operar sem degradação térmica ao longo do tempo.
        
#         # A verificação térmica assegura que o calor gerado no cabo é compatível com sua capacidade de dissipação,
#         # garantindo a integridade da isolação e a confiabilidade da instalação elétrica.




 


#         # ========================================================
#         {"tipo": "titulo", "texto":"4. Interpretação térmica pela norma"},

#         {"tipo": "texto", "texto": (
#             "A verificação térmica não é feita diretamente pela potência dissipada, "
#             "mas sim pela capacidade de condução de corrente definida na NBR 5410.\n\n"

#             "Essa capacidade já considera:\n\n"
#             "- limites térmicos da isolação;\n"
#             "- condições de instalação;\n"
#             "- temperatura ambiente;\n"
#             "- efeitos de agrupamento.\n\n"

#             "Portanto, a norma garante que, se o condutor operar dentro da corrente admissível, "
#             "o aquecimento não comprometerá a isolação."
#         )},

#         # ========================================================
#         {"tipo": "titulo", "texto":"5. Critério de verificação térmica"},

#         {"tipo": "equacao",
#          "latex": r"I_{z} \ge I_{projeto}"
#         },

#         {"tipo": "texto", "texto": (
#             "A condição térmica segura é atendida quando a corrente admissível do condutor "
#             "é maior ou igual à corrente de projeto.\n\n"

#             "Interpretação:\n\n"
#             "- Se I_z ≥ I → operação segura\n"
#             "- Se I_z < I → risco de sobreaquecimento\n\n"

#             "Esse critério assegura que o calor gerado (I²R) pode ser dissipado "
#             "sem elevar a temperatura acima do limite da isolação."
#         )},

#         {
#             "tipo": "questao_multipla_escolha",
#             "id": "problema.01.004.0002",
#             "pergunta": (
#                 "Se a corrente de projeto for maior que a corrente admissível do condutor, "
#                 "qual é a consequência térmica?"
#             ),
#             "alternativas": {
#                 "a": "O cabo opera normalmente",
#                 "b": "O cabo dissipa calor sem risco",
#                 "c": "O condutor pode sofrer sobreaquecimento e degradação da isolação",
#                 "d": "Não há impacto térmico relevante"
#             },
#             "alternativa_correta": "c",
#         },

#         # ========================================================
#         {"tipo": "titulo", "texto":"6. Entrega técnica: Verificação térmica"},

#         {"tipo": "texto", "texto": (
#             "Nesta etapa, foi analisado o comportamento térmico do condutor com base "
#             "no efeito Joule e nos critérios da norma.\n\n"

#             "Resumo da análise:\n\n"
#             f"- Corrente de projeto: {_get_valor_limpo('problema.01.002.0001') or '--'} A\n"
#             f"- Corrente admissível: {_get_valor_limpo('problema.01.003.0004') or '--'} A\n\n"

#             "Conclusão:\n\n"
#             "Se a corrente admissível for maior ou igual à corrente de projeto, "
#             "o condutor opera dentro dos limites térmicos seguros."
#         )},

#         # ========================================================
#         {"tipo": "titulo", "texto":"Fechamento da etapa"},

#         {"tipo": "texto", "texto": (
#             "A verificação térmica confirma que o condutor não apenas conduz corrente, "
#             "mas também mantém sua integridade ao longo do tempo.\n\n"

#             "Essa etapa garante que o aquecimento gerado não compromete a isolação, "
#             "assegurando segurança, durabilidade e confiabilidade da instalação.\n\n"

#             "Na sequência, o dimensionamento será consolidado a partir da análise conjunta "
#             "de todos os critérios técnicos."
#         )},











#         # # ========================================================
#         # {"tipo": "titulo", "texto":"1. Verificação da integridade térmica do condutor"},

#         # {"tipo": "texto", "texto": (
#         #     "Nas etapas anteriores, o sistema já foi analisado quanto à corrente suportada pelo condutor "
#         #     "e quanto ao desempenho elétrico no ponto de carga. Agora, a análise se desloca para a segurança térmica."
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "A pergunta técnica desta etapa é:\n\n"
#         #     "O condutor suportará o aquecimento ao longo do tempo sem comprometer sua integridade térmica?"
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "Aqui, o problema deixa de ser apenas normativo ou funcional e passa a envolver durabilidade, "
#         #     "margem de segurança e risco de degradação da instalação."
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "Projeto seguro não é apenas aquele que funciona. "
#         #     "É aquele que mantém estabilidade térmica ao longo do regime de operação."
#         # )},

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"2. Conceito central: efeito Joule"},

#         # {"tipo": "texto", "texto": (
#         #     "Sempre que uma corrente elétrica percorre um condutor, parte da energia é dissipada em forma de calor. "
#         #     "Esse fenômeno é conhecido como efeito Joule."
#         # )},

#         # {"tipo": "equacao",
#         #     "latex": r"P_{perda} = I^2 \cdot R"
#         # },

#         # {"tipo": "texto", "texto": (
#         #     "A potência dissipada cresce com o quadrado da corrente. "
#         #     "Isso significa que pequenas variações de corrente podem provocar aumentos térmicos significativos."
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "Portanto, a análise térmica não depende apenas da existência de corrente, "
#         #     "mas da sua intensidade, do tempo de permanência e da resistência elétrica do trecho."
#         # )},

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"3. Grandezas calculadas da etapa"},

#         # {"tipo": "texto", "texto": (
#         #     "Nesta etapa, devem ser determinados os seguintes parâmetros:\n\n"
#         #     "- resistência elétrica do trecho;\n"
#         #     "- potência dissipada por efeito Joule;\n"
#         #     "- elevação térmica estimada do condutor.\n\n"
#         #     "Essas grandezas permitem avaliar se a operação ocorre com margem térmica adequada."
#         # )},

#         # {"tipo": "entrada_numerica_inline",
#         #     "id": "problema.01.005.0001",
#         #     "rotulo": "Resistividade do material (ρ)",
#         #     "unidade": "Ω·mm²/m",
#         #     "placeholder": "Ex: 0.0175"
#         # },

#         # {"tipo": "entrada_numerica_inline",
#         #     "id": "problema.01.005.0002",
#         #     "rotulo": "Coeficiente térmico simplificado",
#         #     "unidade": "°C/W",
#         #     "placeholder": "Ex: 0.40"
#         # },

#         # {"tipo": "entrada_numerica_inline",
#         #     "id": "problema.01.005.0003",
#         #     "rotulo": "Fator de regime térmico",
#         #     "unidade": "—",
#         #     "placeholder": "Ex: 1.00"
#         # },

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"4. Referência normativa e condições reais"},

#         # {"tipo": "texto", "texto": (
#         #     "A NBR 5410 impõe limites térmicos de forma indireta por meio da corrente admissível, "
#         #     "considerando fatores como temperatura ambiente, tipo de isolação, agrupamento e método de instalação."
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "No entanto, a conformidade normativa depende de condições específicas. "
#         #     "Quando as condições reais se afastam dessas hipóteses, o risco térmico pode aumentar."
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "Por isso, a verificação térmica complementa a análise normativa, reforçando a leitura crítica do sistema."
#         # )},

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"5. Variável sensível: intensidade da corrente ao longo do tempo"},

#         # {"tipo": "texto", "texto": (
#         #     "O aquecimento do condutor não depende apenas do valor nominal da corrente, "
#         #     "mas também do regime de operação ao longo do tempo."
#         # )},

#         # {"tipo": "texto", "texto": (
#         #     "Perguntas relevantes para essa análise incluem:\n\n"
#         #     "- o motor opera continuamente?\n"
#         #     "- há partidas frequentes?\n"
#         #     "- o regime é intermitente ou permanente?\n\n"
#         #     "Quanto maior a permanência de corrente elevada, maior tende a ser o aquecimento acumulado."
#         # )},

#         # {"tipo": "questao_multipla_escolha", "id": "problema.01.005.0004",
#         #     "pergunta": (
#         #         "Por que pequenas elevações na corrente podem causar aumentos térmicos significativos no condutor?"
#         #     ),
#         #     "alternativas": {
#         #         "a": "Porque a temperatura depende apenas do comprimento do cabo.",
#         #         "b": "Porque a dissipação térmica cresce linearmente com a tensão.",
#         #         "c": "Porque a potência dissipada depende de I²R, crescendo com o quadrado da corrente.",
#         #         "d": "Porque o aquecimento do cabo independe da resistência elétrica."
#         #     },
#         #     "alternativa_correta": "c",
#         # },

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"6. Cálculo e avaliação do regime térmico"},

#         # {"tipo": "texto", "texto": (
#         #     "Com base nos dados do circuito e nas hipóteses adotadas para o regime de operação, "
#         #     "determine a resistência do trecho, a potência dissipada e a elevação térmica estimada."
#         # )},

#         # {"tipo": "texto", "texto": _texto_substituicao_termica()},

#         # {"tipo": "texto", "texto": _texto_interpretacao_termica()},

#         # {"tipo": "questao_texto", "id": "problema.01.005.0005",
#         #     "pergunta": (
#         #         "Se a elevação térmica estimada for elevada, quais medidas técnicas podem ser adotadas "
#         #         "para reduzir o risco térmico do circuito?"
#         #     )
#         # },

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"7. Entrega técnica: Relatório de avaliação térmica"},

#         # {"tipo": "texto", "texto": (
#         #     "Nesta etapa, a segurança térmica do circuito é avaliada a partir das perdas elétricas "
#         #     "e do aquecimento estimado no condutor."
#         # )},

#         # {"tipo": "texto", "texto": _tabela_verificacao_termica()},

#         # {"tipo": "texto", "texto": (
#         #     "Essa análise permite verificar se o sistema opera com margem térmica confortável "
#         #     "ou se está sujeito a risco de aquecimento excessivo e degradação da isolação."
#         # )},

#         # # ========================================================
#         # {"tipo": "titulo", "texto":"Fechamento da etapa"},

#         # {"tipo": "texto", "texto": (
#         #     "Neste ponto, o condutor já foi analisado quanto à sua capacidade de condução, "
#         #     "ao desempenho elétrico e à segurança térmica.\n\n"
            
#         #     "Você já possui:\n"
#         #     "- verificação da corrente admissível;\n"
#         #     "- análise de queda de tensão;\n"
#         #     "- estimativa do aquecimento por efeito Joule.\n\n"
            
#         #     "Esses três filtros consolidam a avaliação técnica do condutor sob a perspectiva do projeto.\n\n"
            
#         #     "Na próxima etapa, o modelo será confrontado com medições reais, "
#         #     "iniciando a validação experimental do sistema."
#         # )},
#     ]

# # from __future__ import annotations
# # import streamlit as st

# # def get_blocos() -> list[dict]:
# #     return [
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"Etapa 5 — Verificação Térmica",},
# # # # ETAPA 5 — VERIFICAÇÃO TÉRMICA

# # # ## Garantir integridade térmica do condutor

# # # Até agora você verificou:

# # # * se o cabo suporta a corrente (critério normativo)
# # # * se a tensão chega dentro do limite aceitável

# # # Agora surge a pergunta crítica:

# # # > O condutor suportará o aquecimento ao longo do tempo sem comprometer sua integridade?

# # # Esta etapa trata de segurança e durabilidade.

# # # ---

# # # Avaliação de risco térmico.

# # # Aqui você começa a pensar como responsável técnico:

# # # * Existe margem térmica confortável?
# # # * Ou o cabo opera constantemente próximo ao limite?

# # # Projeto bom não é aquele que “aguenta”.
# # # É aquele que opera com segurança.

# # # ---

# # # ## 7. Evolução do aluno

# # # Você deixa de ser apenas verificador de desempenho elétrico.

# # # Agora você se torna:

# # # Analista de risco.

# # # Você passa a enxergar:

# # # * Vida útil da isolação
# # # * Confiabilidade da instalação
# # # * Impacto do tempo sobre o sistema

# # # ## 1. Finalidade da etapa
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"1. Finalidade da Etapa",},

# # # Garantir que o cabo opere dentro de sua faixa térmica segura durante regime permanente.

# # # Não basta atender tabela.
# # # É necessário compreender o comportamento térmico real.

# # # ---

# # # ## 2. Fundamento físico envolvido
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"2. Conceito central",},

# # # O conceito central é:

# # # **Efeito Joule.**

# # # Sempre que corrente percorre um condutor, ocorre dissipação de energia em forma de calor:

# # # [
# # # P_{perda} = I^2 R
# # # ]

# # # Quanto maior a corrente:

# # # → maior o aquecimento (crescimento quadrático).

# # # Isso significa que pequenas variações na corrente geram grandes variações térmicas.

# # # ---


# # # ## 3. Grandezas calculadas
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"3. Grandezas caluladas",},
# # # Você deve determinar:

# # # * Resistência do trecho (R)
# # # * Potência dissipada (P_perda)
# # # * Estimativa de elevação de temperatura (ΔT)

# # # Mesmo que a norma já imponha limites indiretos via tabelas, compreender o aquecimento reforça a análise crítica.

# # # ---

# # # ## 4. Norma aplicada
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"4. Norma Aplicada",},

# # # A NBR 5410 considera:

# # # * Temperatura ambiente
# # # * Tipo de isolação (PVC, XLPE…)
# # # * Agrupamento de cabos
# # # * Método de instalação

# # # Esses fatores alteram a capacidade térmica do sistema.

# # # A corrente admissível da tabela já incorpora limites térmicos — mas apenas sob condições específicas.

# # # Se as condições reais forem diferentes, o risco aumenta.

# # # ---

# # # ## 5. Variável sensível da etapa
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"5. Variável sensível da etapa",},

# # # Intensidade da corrente ao longo do tempo.

# # # Não é apenas o valor nominal.

# # # Perguntas importantes:

# # # * O motor opera continuamente?
# # # * Há picos frequentes de partida?
# # # * Existe regime intermitente?

# # # O aquecimento acumulado depende do regime de operação.

# # # ---



# # # ## 8. Consequência prática se errar
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"6. Consequência prática se errar",},

# # # Se o aquecimento for subestimado:

# # # * isolação envelhece prematuramente
# # # * surgem falhas por ressecamento
# # # * aumenta risco de curto-circuito
# # # * pode ocorrer incêndio

# # # O erro térmico não aparece imediatamente.

# # # Ele aparece meses ou anos depois.

# # # ---

# # # ## 9. Produto gerado
# #         # ========================================================
# #         {"tipo": "titulo", "texto":"7. Produto gerado",},

# # # Você deve apresentar:

# # # * Cálculo de P_perda (I²R)
# # # * Análise qualitativa do regime térmico
# # # * Verificação se há margem de segurança
# # # * Conclusão técnica sobre integridade térmica

# # # Essa análise consolida a segurança do projeto.

# # # ---

# # # ## Fechamento da Etapa 5

# # # Agora você verificou:

# # # * Corrente admissível
# # # * Queda de tensão
# # # * Segurança térmica

# # # O cabo já passou por três filtros técnicos.

# # # Mas ainda falta um passo fundamental:

# # # Comparar modelo e realidade.

# # # Na próxima etapa, você valida tudo contra medições reais.

# # # Aqui começa a auditoria técnica do sistema.

# #     ]
