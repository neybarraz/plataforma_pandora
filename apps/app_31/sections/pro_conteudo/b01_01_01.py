import streamlit as st

# CAPTAR OS DADOS PREENCHIDOS
def _get_valor_limpo(qid: str) -> float | None:
    chave = f"problema_{qid}"
    valor_bruto = st.session_state.get(chave)

    if valor_bruto is None or str(valor_bruto).strip() in ["", "—", "None"]:
        return None

    try:
        return float(str(valor_bruto).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None

# GERA A TABELA DE ENTREGA
def _gerar_tabela_parametros() -> str:
    campos = {
        "Potência": ("problema.01.001.0001", "kW"),
        "Tensão nominal": ("problema.01.001.0002", "V"),
        "Fator de potência": ("problema.01.001.0003", "—"),
        "Rendimento": ("problema.01.001.0004", "—"),
        "Distância": ("problema.01.001.0005", "m"),
        "Temperatura ambiente": ("problema.01.001.0006", "°C"),
        "Bitola instalada": ("problema.01.001.0007", "mm²"),
        "Tensão medida": ("problema.01.001.0008", "V"),
        "Corrente medida": ("problema.01.001.0009", "A"),
        "Número de circuitos": ("problema.01.001.0010", "—"),
    }
    
    tabela = "Dados Coletados\n\n"
    tabela += "| Parâmetro | Valor Identificado | Unidade |\n"
    tabela += "| :--- | :---: | :---: |\n"
    
    for label, (qid, unid) in campos.items():
        valor = _get_valor_limpo(qid)
        val_str = f"{valor}" if valor is not None else "—"
        tabela += f"| **{label}** | {val_str} | {unid} |\n"
    
    return tabela + "<br>"

# GERA O TEXTO NO LAYOUT
def get_blocos() -> list[dict]:
    return [
        # ========================================================
        {"tipo": "titulo", "texto":"1. Caracterização do sistema eletromecânico"},

        {"tipo":"texto", "texto": (
            "O sistema analisado é responsável pelo bombeamento de água do reservatório inferior "
            "para o reservatório superior por meio de uma motobomba acionada por motor elétrico. "            
            "Para realizar essa função, o motor fornece energia mecânica à bomba, permitindo vencer "
            "a carga hidráulica do sistema e elevar a água até o nível desejado."
        )},

        {"tipo":"texto", "texto": (
            "Essa função hidráulica está diretamente associada a uma demanda elétrica. "
            "Quanto maior o esforço exigido da bomba, maior será a potência requerida do motor "
            "e, consequentemente, a corrente solicitada da rede elétrica. "
            "Compreender essa relação é essencial para analisar o dimensionamento da alimentação do motor."
        )},

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=PSuVujxAcOg"},

        # {"tipo":"texto", "texto": (
        #     "Pergunta técnica do problema:\n\n"
            
        #     # "O condutor instalado entre o quadro de comando e o motor é capaz de suportar "
        #     # "corretamente a carga elétrica exigida pelo sistema?"
        # )},

        {"tipo":"subtitulo", "texto": (            
            "O condutor instalado entre o quadro de comando e o motor é capaz de suportar "
            "corretamente a carga elétrica exigida pelo sistema?"
        )},

        {"tipo": "texto", "texto": (
            "Para responder à questão, o primeiro passo consiste em converter o sistema físico em um conjunto estruturado de grandezas técnicas. "
            "No âmbito da engenharia, o dimensionamento não se limita à aplicação de fórmulas, mas à tradução da realidade física em parâmetros numéricos rastreáveis e confiáveis. "
            "Diante de um sistema já instalado, a análise inicia-se anteriormente à fase de cálculo. "
            "É necessário verificar a conformidade do executado com os critérios de segurança e desempenho estabelecidos. "
            "A validade da análise depende diretamente da precisão dos dados coletados. "
            "Dados imprecisos implicam modelo inválido e decisão técnica comprometida. "
        )},
        {"tipo": "texto", "texto": (
            "Nesta etapa, o objetivo não é calcular, mas observar, medir e registrar com rigor metrológico."
        )},

        # ========================================================
        # 2. Grandezas que devem ser levantadas
        # ========================================================
        {"tipo": "titulo", "texto":"2. Levantamento das grandezas para dimensionamento",},
        {"tipo": "texto", "texto": (
            "O dimensionamento de um circuito elétrico não parte de suposições, mas de dados estruturados. "
            "Nesta etapa, você irá levantar as grandezas fundamentais que descrevem o sistema sob três perspectivas:\n\n"
            
            "- dados nominais do motor (condições de projeto)\n"
            "- parâmetros físicos do circuito (meio de transmissão)\n"
            "- medições reais de operação (comportamento em campo)\n\n"
            
            "A qualidade dessas informações determina diretamente a confiabilidade do dimensionamento. "
            "Erros na coleta ou interpretação dos dados comprometem todas as etapas seguintes do projeto."
        )},        # ________________________________________________________
        {"tipo": "video", "titulo": "Dados nominais do motor", "descricao": (
            "Antes de registrar qualquer dado, você precisa saber exatamente o que está lendo. "
            "A placa de identificação não é apenas informativa, ela é o documento técnico que define "
            "as condições nominais de operação do motor. Assista ao vídeo com foco na identificação "
            "dos quatro parâmetros críticos do dimensionamento: potência (P), tensão (V), fator de potência (cos φ)"
            "e rendimento (η).\n\n"
            "<br>"
            
            "Durante o vídeo, observe:\n"
            "- onde cada informação aparece na placa\n"
            "- como ela é representada (unidades, símbolos, variações)\n"
            "- possíveis diferenças entre motores\n\n"
            
            "Essa etapa desenvolve a capacidade de leitura técnica."
        ),
        "url": "https://www.youtube.com/watch?v=ZLV_MHFdmWk",
        },

        {"tipo": "texto", "texto": (
            "Após compreender a leitura da placa, inicie a coleta dos dados nominais do motor. "            
            "Esses valores representam as condições de operação para as quais o equipamento foi projetado "
            "e constituem a base de todo o dimensionamento elétrico.\n\n"
            "<br>"

            "A partir desses dados, você irá determinar a demanda elétrica do sistema. "
            "Qualquer erro na identificação ou no registro compromete diretamente o cálculo da corrente "
            "e, consequentemente, a escolha dos condutores.\n\n"
            
            "Realize a leitura diretamente na placa do motor e registre, com precisão, os valores:"
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0001",
            "rotulo": "Potência Nominal (P)", "unidade": "kW", "placeholder": "Ex: 5.5"},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0002",
            "rotulo": "Tensão Nominal (V)", "unidade": "V", "placeholder": "Ex: 380" },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0003",
            "rotulo": "Fator de Potência (cos φ)", "unidade": "0 a 1", "placeholder": "Ex: 0.86" },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0004",
            "rotulo": "Rendimento (η)", "unidade": "0 a 1", "placeholder": "Ex: 0.88"},

        {"tipo": "texto", "texto":(
            "Essas grandezas definem a demanda elétrica real do motor e serão utilizadas diretamente "
            "no cálculo da corrente de projeto.\n\n"

            "- Potência (P): Representa a potência mecânica útil entregue no eixo do motor. "
            "É a quantidade de energia efetivamente convertida em trabalho. "
            "Quanto maior a potência, maior será a corrente exigida da rede.\n\n"

            "- Tensão (V): Define o nível de alimentação elétrica do sistema. "
            "Para uma mesma potência, tensões mais baixas implicam correntes mais elevadas. "
            "Portanto, a tensão influencia diretamente o dimensionamento dos condutores.\n\n"

            "- Fator de Potência (cos φ): Indica a relação entre a potência ativa (útil) e a potência aparente fornecida pela rede. "
            "Valores menores significam maior circulação de potência reativa, aumentando a corrente total sem aumento de potência útil.\n\n"

            "- Rendimento (η): Expressa a eficiência do motor na conversão de energia elétrica em energia mecânica. "
            "Parte da energia é perdida (principalmente em forma de calor). "
            "Quanto menor o rendimento, maior será a potência elétrica exigida para entregar a mesma potência mecânica.\n\n"

            "Em conjunto, fator de potência e rendimento corrigem a potência nominal, permitindo determinar "
            "a potência elétrica real absorvida da rede. Sem essas grandezas, não é possível calcular a corrente de projeto de forma confiável."
        )},

        # ________________________________________________________
        {"tipo": "subtitulo", "texto":"Parâmetros físicos do circuito de alimentação"},
        {"tipo": "texto", "texto": (
            "Até aqui, o foco estava no motor. Agora, o foco muda para o caminho da energia. "
            "A energia elétrica não é transferida instantaneamente, ela percorre um condutor físico "
            "que apresenta resistência e está sujeito a aquecimento.\n\n"
            "<br>"

            "Esse percurso introduz dois efeitos fundamentais:\n\n"
            "- perda de energia ao longo do cabo (queda de tensão)\n"
            "- aquecimento do condutor devido à circulação de corrente\n\n"
            
            "Portanto, além da carga (motor), o meio físico por onde a energia circula passa a influenciar "
            "diretamente o desempenho e a segurança do sistema. Para caracterizar o circuito elétrico, "
            "é necessário levantar os parâmetros físicos da instalação. Esses dados determinam como o "
            "condutor se comporta em operação real e serão utilizados nas etapas de verificação de "
            "queda de tensão e análise térmica.\n\n"
            
            "Realize a medição ou estimativa em campo e registre os valores:"
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0005",
            "rotulo": "Distância entre quadro e motor", "unidade": "m", "placeholder": "Ex: 45"},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0006",
            "rotulo": "Temperatura Ambiente Estimada", "unidade": "°C", "placeholder": "Ex: 30" },

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0007",
            "rotulo": "Bitola (Seção) Atual do Cabo", "unidade": "mm²", "placeholder": "Ex: 6"},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.001.0010",
            "rotulo": "Número de circuitos", "unidade": "--", "placeholder": "Ex: 6"},

        {"tipo": "texto", "texto": (
            "Esses parâmetros descrevem o comportamento físico do circuito e influenciam diretamente os resultados do dimensionamento.\n\n"
            
            "- Distância (L): determina o comprimento do percurso da corrente. "
            "Quanto maior a distância, maior a resistência elétrica total do circuito e maior a queda de tensão.\n\n"
            
            "- Temperatura ambiente: afeta a capacidade de dissipação térmica do condutor. "
            "Temperaturas mais elevadas reduzem a corrente admissível do cabo.\n\n"
            
            "- Seção do condutor (mm²): define a capacidade de condução de corrente e a resistência elétrica do cabo. "
            "Seções menores aumentam perdas e aquecimento; seções maiores reduzem esses efeitos.\n\n"
            
            "Em conjunto, esses dados permitem avaliar o impacto do circuito sobre o desempenho elétrico e a segurança térmica da instalação."
        )},
        # ________________________________________________________
        {"tipo": "subtitulo", "texto":"Medições reais de operação"},

        {"tipo": "texto", "texto": (
            "Até aqui, você trabalhou com dados nominais e condições ideais de projeto. "
            "Agora, o foco muda para o comportamento real do sistema em operação. "
            "Na prática, o motor pode operar em condições diferentes das especificadas na placa. "
            "Variações na rede elétrica, carregamento mecânico e condições de instalação "
            "alteram diretamente a tensão e a corrente do circuito. "
            "Essas medições permitem verificar como o sistema está realmente se comportando "
            "e servem como base para validação do modelo teórico."
        )},

        {"tipo": "texto", "texto": (
            "Realize as medições diretamente no motor em operação, utilizando instrumentos adequados:\n\n"
            
            "- Alicate amperímetro, para medir a corrente em carga;\n"
            "- Voltímetro, para medir a tensão nos terminais do motor.\n\n"

            "Esses dados serão utilizados para comparar o valor calculado com o valor real, "
            "permitindo identificar desvios e possíveis problemas na instalação.\n\n"

            "Registre os valores medidos:"
        )},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.001.0008",
            "rotulo": "Tensão medida nos terminais do motor", "unidade": "V", "placeholder": "Ex: 365"},

        { "tipo": "entrada_numerica_inline", "id": "problema.01.001.0009",
            "rotulo": "Corrente real medida em operação", "unidade": "A", "placeholder": "Ex: 12.5"},

        {"tipo": "texto", "texto": (
            "Essas medições representam o comportamento real do sistema sob carga.\n\n"
            
            "- Tensão medida: indica o nível efetivo de alimentação nos terminais do motor. "
            "Diferenças em relação à tensão nominal podem evidenciar queda de tensão no circuito.\n\n"
            
            "- Corrente medida: representa o esforço elétrico real do motor em operação. "
            "Valores acima do esperado podem indicar sobrecarga, baixo rendimento ou problemas na instalação.\n\n"
            
            "A comparação entre valores medidos e valores calculados é fundamental para validar o dimensionamento "
            "e garantir que o sistema opere dentro de condições seguras e eficientes."
        )},


        # ========================================================
        {"tipo": "titulo", "texto":"3. Fundamento da demanda elétrica"},
        {"tipo": "texto", "texto": (
            "Nesta etapa, o conceito central é a relação entre potência elétrica e demanda energética do sistema. "
            "O motor não consome tensão de forma isolada. Ele demanda potência para realizar trabalho mecânico. "
            "Essa potência é fornecida pela rede elétrica na forma de potência elétrica."
        )},

        {"tipo": "texto", "texto": (
            "Para atender a essa demanda, o sistema elétrico responde por meio de um conjunto de grandezas interdependentes:\n\n"
            
            "- tensão (V);\n"
            "- corrente (I);\n"
            "- fator de potência (cosφ);\n"
            "- rendimento (η).\n\n"
            
            "Essas variáveis não atuam de forma independente. Elas estão fisicamente conectadas e, em conjunto, "
            "determinam o esforço elétrico necessário para o funcionamento do motor."
        )},

        {"tipo": "texto", "texto": (
            "A potência mecânica exigida pela carga define a potência elétrica que deve ser fornecida. "
            "A partir dessa relação, a corrente do circuito será determinada nas próximas etapas."
        )},
        {"tipo": "texto", "texto": (
            "Neste momento, você ainda não realiza cálculos. "
            "O objetivo é reconhecer as grandezas envolvidas e compreender como elas se relacionam dentro do sistema. "
            "Você está construindo a base conceitual necessária para o dimensionamento."
        )},


        # ========================================================
        {"tipo": "titulo", "texto":"4. Erros críticos na coleta de dados"},

        {"tipo": "texto", "texto": (
            "A etapa de coleta de dados define a qualidade de todo o dimensionamento. "
            "Erros nessa fase não são pontuais — eles se propagam para todas as etapas seguintes do projeto. "
            "Antes de prosseguir, é necessário reconhecer os erros mais frequentes e suas consequências técnicas."
        )},

        {"tipo": "texto", "texto": (
            "Erros recorrentes na coleta:\n\n"
            
            "- Potência anotada incorretamente (ex: confundir CV com kW);\n"
            "- Tensão considerada igual à de placa, sem verificação em campo;\n"
            "- Comprimento do circuito estimado visualmente, sem medição;\n"
            "- Temperatura ambiente ignorada ou subestimada;\n"
            "- Valores copiados sem conferência direta no equipamento.\n\n"
            
            "Esses erros geralmente ocorrem por pressa ou interpretação inadequada dos dados disponíveis."
        )},

        {"tipo": "texto", "texto": (
            "Impacto técnico dos erros de coleta:\n\n"
            
            "- Corrente de projeto calculada incorretamente;\n"
            "- Subdimensionamento ou superdimensionamento dos condutores;\n"
            "- Queda de tensão fora dos limites normativos;\n"
            "- Aquecimento excessivo e redução da vida útil da instalação.\n\n"
            
            "Um erro na entrada de dados compromete a validade de todo o modelo."
        )},

        # {"tipo": "texto", "texto": (
        #     "Regra fundamental:\n\n"
            
        #     "Não existe dimensionamento confiável sem dados confiáveis.\n\n"
            
        #     "A precisão na coleta não é uma etapa operacional, é uma responsabilidade técnica."
        # )},


        # ========================================================
        {"tipo": "titulo", "texto":"5. Entrega técnica: Dados Coletados",},

        {"tipo": "texto", "texto": (
            "Nesta etapa, os dados coletados são organizados em uma estrutura única e consistente. "
            "Essa consolidação transforma medições isoladas em uma base técnica utilizável para o dimensionamento elétrico. "
            "A tabela a seguir reúne os parâmetros nominais do motor, as condições físicas do circuito "
            "e as medições reais de operação."
        )},

        {"tipo": "texto", "texto": _gerar_tabela_parametros()},

        {"tipo": "texto", "texto": (
            "Essa base de dados será utilizada diretamente nas próximas etapas do projeto, incluindo:\n\n"
            
            "- cálculo da corrente de projeto\n"
            "- verificação da capacidade de condução\n"
            "- análise de queda de tensão\n"
            "- avaliação térmica do condutor\n\n"
            
            "Sem uma base numérica confiável, não existe cálculo válido."
        )},

        # ========================================================
        {"tipo": "titulo", "texto":"Fechamento da etapa",},
        {"tipo": "texto", "texto": (            
            "Neste momento, ainda não é possível afirmar se o condutor está corretamente dimensionado.\n\n"
            
            "No entanto, você já possui:\n"
            "- dados reais do sistema\n"
            "- informações organizadas\n"
            "- base numérica consistente\n\n"
            
            "A estrutura apresentada é condição necessária para o dimensionamento. A acurácia da coleta define "
            "a confiabilidade das etapas seguintes. A transição ocorre da observação para o projeto."
        )},
   
    ]