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

        return (
            f" <br>\n\n"
            f"| Parâmetro | Valor Registrado | Unidade |\n"
            f"| :--- | :---: | :---: |\n"
            f"| Corrente Nominal Calculada | **{i_calculada}** | A |\n"
            f"| Corrente Real Medica | **{i_medida}** | A |\n\n"
            f"<br>"
        )

    # 3. Mensagem caso os dados ainda não tenham sido preenchidos
    return (
        "### ⏳ Aguardando Dados para Comparação\n"
        "Para visualizar o diagnóstico, preencha a **Corrente Real** (Etapa 1) "
        "e o **Valor Calculado** da Corrente Nominal acima."
    )

def get_blocos() -> list[dict]:
    return [
        # ============================================================
        # ETAPA 3 — DIMENSIONAMENTO NORMATIVO (NBR 5410)
        # ============================================================
        { "tipo": "titulo", "texto": "ETAPA 3 — Dimensionamento por Capacidade de Condução" },

        { "tipo": "texto", "texto": (
            "Até este ponto, sua análise foi baseada na observação e na física do motor. Você calculou a corrente "
            "nominal (I_n), comparou com a realidade do campo e validou o esforço do sistema. "
            "Agora, deixamos o campo das hipóteses e entramos no campo da Responsabilidade Técnica. "
            "Dimensionar um condutor não é apenas escolher um fio que 'funcione'; é selecionar uma seção "
            "transversal que garanta a integridade do isolamento contra o sobreaquecimento, conforme as diretrizes da NBR 5410."
        )},

        { "tipo": "texto", "texto": (
                "A Pergunta de Ouro da Engenharia:\n\n"
                "Qual seção de condutor suporta esta corrente com segurança absoluta durante toda a vida útil da instalação?\n\n"
                "Para responder, você não usará opinião ou 'regras de bolso'. Você aplicará os critérios normativos "
                "de capacidade de condução de corrente, considerando o método de instalação e as influências externas."
            )
        },

        # ============================================================
        # 1. O RIGOR DA NBR 5410
        # ============================================================
        { "tipo": "titulo", "texto": "1. Critérios de Dimensionamento (NBR 5410)" },

        { "tipo": "texto", "texto": (
            "Na engenharia elétrica, a seção de um condutor não é definida por 'costume' ou 'padrão de obra'. "
            "A NBR 5410 estabelece que a capacidade de condução de corrente (I_z) é uma propriedade "
            "variável, que depende diretamente das condições de instalação e do ambiente. "
            "Para determinar a bitola correta, você deve considerar cinco pilares fundamentais:"
        )},

        { "tipo": "texto", "texto": (
            "1. Método de instalação: o cabo está embutido, aparente ou enterrado? Isso dita a troca térmica.\n\n"
            "2. Temperatura ambiente: o ar ao redor está a 30°C ou o cabo está próximo a uma fonte de calor?\n"
            "3. Agrupamento: há outros circuitos no mesmo eletroduto gerando calor simultâneo?\n"
            "4. Constituição do cabo: o material é cobre ou alumínio? A isolação é PVC (70°C) ou EPR/XLPE (90°C)?\n"
            "5. Número de condutores carregados: em sistemas trifásicos, quantos condutores dissipam energia?"
            )
        },

        { "tipo": "texto", "texto": (
            "A NBR 5410 não enxerga o cabo apenas como um condutor de elétrons, mas como um trocador de calor. "
            "O limite de corrente de um fio não é fixo; ele é determinado pela temperatura máxima que a sua isolação "
            "pode suportar sem derreter ou degradar prematuramente (70°C para PVC e 90°C para EPR/XLPE). "
            "Para garantir a segurança, a norma organiza o dimensionamento em três grandes pilares:"
        )},

        { "tipo": "texto", "texto": (
            "Lembre-se: A tabela da norma é o seu porto seguro. Consultá-la é o que garante que o "
            "projeto seja tecnicamente inquestionável e seguro contra incêndios."
        )},

        # METODO DE INSTALACAO
        { "tipo": "subtitulo", "texto": "Métodos de Instalação (Referência de Troca Térmica)" },

        { "tipo": "texto",  "texto": (
                "A norma classifica como o cabo está acondicionado para entender a dissipação térmica:\n\n"
                "* **Método A -- Condutores em eletroduto embutido em parede isolante:** É a pior condição de troca térmica. O calor fica 'preso'.\n"
                "* **Método B -- Eletroduto aparente ou embutido em alvenaria:** Condição intermediária. A alvenaria ajuda a dissipar um pouco de calor.\n"
                "* **Método C -- Cabo unipolar ou multipolar sobre parede:** Troca térmica direta com o ar, permitindo correntes maiores.\n"
                "* **Método D -- Cabos enterrados:** A troca depende da umidade e do tipo de solo ao redor do eletroduto."
        )},

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=5on0eGBgigA",},

        { "tipo": "questao_multipla_escolha", "id": "problema.01.003.0001",
            "pergunta": "Por que o 'Método de Instalação' altera a capacidade de corrente de um mesmo cabo?",
            "alternativas": {
                "a": "Porque altera a resistência ôhmica do cobre.",
                "b": "Porque influencia a capacidade do cabo de dissipar o calor gerado pelo Efeito Joule para o ambiente.",
                "c": "Porque muda a tensão nominal que o cabo pode suportar.",
                "d": "Porque o método de instalação altera a frequência da rede elétrica."
            },
            "alternativa_correta": "b"
        },      

        # INFLUENCIAS AMBIENTAIS
        { "tipo": "subtitulo", "texto": "Influências Ambientais (Fatores de Correção)" },

        { "tipo": "texto", "texto": (
            "A capacidade da tabela da norma é calculada para 30°C (ar) ou 20°C (solo). Se o ambiente da motobomba for mais quente, "
            "devemos aplicar o Fator de Temperatura (f_t). Se houver muitos circuitos juntos, aplicamos o Fator de Agrupamento (f_g), "
            "pois um cabo aquece o outro. O cobre conduz melhor que o alumínio, e a isolação em EPR ou XLPE suporta mais calor que o PVC. "
            "Por isso, um cabo de 2,5 mm² em EPR pode carregar mais corrente que um de 2,5 mm² em PVC nas mesmas condições. \n"
            "<br><br>"
            "Conceito de Engenheiro: Dimensionar pela NBR 5410 é garantir que a temperatura do cabo  nunca ultrapasse o limite da sua isolação em regime permanente."
            )
        },

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=Bdwo6oXQdyc",},

        { "tipo": "questao_multipla_escolha", "id": "problema.01.003.0002",
            "pergunta": "Em uma instalação onde vários circuitos compartilham o mesmo eletroduto, por que é necessário reduzir a corrente máxima permitida em cada cabo (aplicar fator de agrupamento)?",
            "alternativas": {
                "a": "Porque o agrupamento aumenta a tensão nominal disponível para o motor.",
                "b": "Porque a proximidade de outros cabos carregados dificulta a dissipação de calor, podendo levar a isolação a ultrapassar seu limite térmico.",
                "c": "Porque o campo magnético dos cabos vizinhos altera a composição química do cobre.",
                "d": "Porque a NBR 5410 exige o uso de alumínio em vez de cobre para circuitos agrupados."
            },
            "alternativa_correta": "b"
        },


        # ============================================================
        # CONSTITUIÇÃO DO CABO: MATERIAL E ISOLAÇÃO
        # ============================================================
        { "tipo": "subtitulo", "texto": "Constituição do Cabo (Material e Isolação)" },

        { "tipo": "texto", "texto": (
            "A capacidade de um cabo é determinada pelo binômio  Condutor + Isolação. "
            "Enquanto o condutor dita a facilidade com que a corrente passa, a isolação dita o limite de temperatura "
            "que o conjunto suporta antes de derreter ou sofrer degradação química. "
            "<br><br>"
            
            "1. Material do Condutor (Cobre vs. Alumínio):\n\n"
            "* O **Cobre** é o padrão para instalações internas devido à sua alta condutividade e flexibilidade.\n"
            "* O **Alumínio** possui menor condutividade (exige bitolas maiores para a mesma corrente), sendo permitido pela norma apenas em condições específicas (como seções acima de 50 mm² em certas instalações).\n\n"
            
            "**2. Tipo de Isolação (O Limite Térmico):**\n\n"
            "* **PVC (Policloreto de Vinila):** Suporta até **70°C** em regime permanente. É o mais comum e econômico.\n"
            "* **EPR / XLPE (Etileno-Propileno / Polietileno Reticulado):** São isolações termofixas que suportam até **90°C**. "
            "Como aguentam mais calor, um cabo de 2,5 mm² com isolação de 90°C 'carrega' mais corrente que um de 70°C, pois demora mais para atingir seu limite crítico."
        )},
        
        {"tipo": "video", "url": "https://www.youtube.com/watch?v=ILtQC2S3-Zg"}, 

        { "tipo": "questao_multipla_escolha", "id": "problema.01.003.0003",
            "pergunta": "Se substituirmos um cabo com isolação em PVC (70°C) por um de mesma bitola com isolação em EPR (90°C), o que acontece com a capacidade de condução de corrente?",
            "alternativas": {
                "a": "A capacidade diminui, pois o EPR oferece maior resistência à passagem dos elétrons.",
                "b": "A capacidade permanece a mesma, pois a seção de cobre não foi alterada.",
                "c": "A capacidade aumenta, pois o material da isolação permite que o condutor opere em uma temperatura mais elevada sem danos.",
                "d": "O cabo deixará de conduzir corrente, pois o EPR é um material semicondutor."
            },
            "alternativa_correta": "c"
        },

        # ============================================================
        # NÚMERO DE CONDUTORES CARREGADOS
        # ============================================================
        { "tipo": "subtitulo", "texto": "Número de Condutores Carregados" },

        { "tipo": "texto", "texto": (
            "Para a norma, o que importa não é quantos fios existem, mas quantos deles estão dissipando calor simultaneamente. "
            "Isso impacta diretamente a temperatura interna do eletroduto.\n\n"
            "**1. Circuito Monofásico (Fase + Neutro):**\n"
            "temos **2 condutores carregados**. A corrente que vai pela fase volta pelo neutro; ambos aquecem.\n\n"
            
            "**2. Circuito Trifásico (3 Fases sem Neutro):**\n"
            "temos **3 condutores carregados**. As três fases equilibram a carga e dissipam calor.\n\n"
            
            "**3. Circuito Trifásico com Neutro:**\n"
            "* Se as cargas forem equilibradas (ex: um motor trifásico), a corrente no neutro é zero. Logo, são **3 condutores carregados**.\n"
            "* O neutro só será considerado carregado se houver desequilíbrio significativo ou presença de harmônicos (cargas eletrônicas).\n\n"
            
            "**Importante:** O condutor de proteção (**PE - Terra**) nunca é contado como condutor carregado, pois só circula corrente por ele em caso de falha."
            )
        },

        {"tipo": "video", "url": "https://www.youtube.com/watch?v=y-54HxWFozU"},

        # {"tipo": "video", "url": "https://www.youtube.com/watch?v=afqVd02oYlY"},
        { "tipo": "questao_multipla_escolha", "id": "problema.01.003.0004",
            "pergunta": "Ao dimensionar o circuito de alimentação trifásico de um motor (3 Fases + Terra), quantos 'condutores carregados' devemos considerar para consultar a tabela da NBR 5410?",
            "alternativas": {
                "a": "2 condutores carregados, pois o motor é uma carga indutiva.",
                "b": "3 condutores carregados, correspondentes às três fases que alimentam o motor.",
                "c": "4 condutores carregados, pois o condutor de proteção (terra) também deve ser contado.",
                "d": "1 condutor carregado, pois as fases se anulam vetorialmente."
            },
            "alternativa_correta": "b"
        },

        # ============================================================
        # 2. DEFINIÇÃO DA CORRENTE DE PROJETO (Ib)
        # ============================================================

        { "tipo": "titulo", "texto": "2. Corrente de Projeto (I_b) como Ponto de Partida" },

        { "tipo": "texto", "texto": (
            "O dimensionamento normativo não admite aproximações. O seu ponto de partida agora é a "
            "Corrente de Projeto (I_b). Este valor representa a carga real que o condutor deve suportar continuamente sem degradar a isolação. "
            "Sua 'missão' nas tabelas da NBR 5410 será encontrar um condutor cuja capacidade de condução (I_z) seja maior ou igual ao "
            "valor que você calculou na Etapa 2."
        )},

        { "tipo": "texto", "texto": _comparativo_correntes() },

        { "tipo": "texto", "texto": (
                "🔍 Filtros para a Consulta Técnica:\n\n"
                "Para não errar a coluna na norma, você deve fixar estas três premissas:\n\n"
                "1. **Material:** Condutores de Cobre.\n"
                "2. **Isolação:** Use o tipo identificado na inspeção (PVC para 70°C ou EPR/XLPE para 90°C).\n"
                "3. **Nº de Condutores Carregados:** Selecione a coluna **'3'** (Circuitos Trifásicos)."
        )},

        # ============================================================
        # 3. NAVEGAÇÃO NA NORMA
        # ============================================================
        {
            "tipo": "titulo",
            "texto": "3. Mapa de Navegação: Tabelas Mestras (NBR 5410)"
        },

        {
            "tipo": "texto",
            "texto": (
                "Não procure a seção 'por instinto'. Siga este roteiro técnico dentro da norma para encontrar a seção nominal (mm²) correta:\n\n"
                "* **Passo 1 (pág. 88):** Na **Tabela 33**, identifique a letra do seu **Método de Referência** (ex: B1, C ou D).\n"
                "* **Passo 2 (pág. 101):** Acesse a **Tabela 36** se o cabo for de **PVC**.\n"
                "* **Passo 3 (pág. 102):** Acesse a **Tabela 37** se o cabo for de **EPR ou XLPE**.\n\n"
                "**⚠️ Nota Importante:** O condutor de proteção (terra) não dissipa calor em regime normal, portanto, **não conta** como condutor carregado."
            )
        },

        {
            "tipo": "texto",
            "texto": (
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
        
        {
            "tipo": "questao_texto",
            "id": "problema.01.003.0005",
            "pergunta": (
                "Consulta à Norma: Localize na tabela da NBR 5410 a primeira bitola que suporta a sua corrente "
                "de projeto, considerando o método de instalação e o tipo de isolação. Qual seção (mm²) você encontrou?"
            )
        },

        # ============================================================
        # 4. APLICAÇÃO DOS FATORES DE CORREÇÃO (O MUNDO REAL)
        # ============================================================
        { "tipo": "titulo", "texto": "4. Refino Térmico: Fatores de Correção (f_t e f_g)" },

        {"tipo": "texto", "texto": (
            "A capacidade que você encontrou na tabela anterior assume condições ideais (30°C e cabo isolado). "
            "Como a motobomba opera em condições reais, devemos aplicar os 'redutores' de capacidade:\n\n "
            "1. **Fator de Temperatura ($$f_{t}$$):** Se o ambiente for mais quente que 30°C, o cabo dissipa menos calor.\n"
            "2. **Fator de Agrupamento ($$f_{g}$$):** Se houver outros circuitos no mesmo duto, um cabo aquece o outro.\n\n"
            "A **Corrente Admissível Corrigida ($$I_{z}$$)** é calculada pela fórmula:"
        )},

        { "tipo": "equacao",
            "latex": r"I_{z} = I_{tabela} \times f_{t} \times f_{g}"
        },

        { "tipo": "texto", "texto": (
            "Critério de Validação: Para o projeto ser seguro, a nova corrente corrigida (I_z) "
            "deve continuar sendo maior ou igual à sua Corrente de Projeto (I_b)."
        )},


        # ============================================================
        # ENTREGA 3 - CONSOLIDAÇÃO DO DIMENSIONAMENTO
        # ============================================================
        { "tipo": "titulo", "texto": "📋 ENTREGA 3: Memorial de Cálculo da Seção Transversal" },

        { "tipo": "texto", "texto": (
            "Com base nas suas consultas à NBR 5410, preencha o memorial abaixo para validar a seção do condutor."
        )},

        { "tipo": "questao_texto", "id": "problema.01.003.0006",
            "pergunta": "Corrente de Projeto ($I_{b}$) calculada (A):"
        },

        { "tipo": "questao_texto", "id": "problema.01.003.0007",
            "pergunta": "Seção Nominal Candidata (mm²) e Corrente da Tabela ($I_{tabela}$):"
        },

        { "tipo": "questao_texto", "id": "problema.01.003.0008",
            "pergunta": "Fatores Aplicados (Temperatura $f_{t}$ e Agrupamento $f_{g}$):"
        },

        { "tipo": "questao_texto", "id": "problema.01.003.0009",
            "pergunta": "Resultado Final: Qual é a SEÇÃO MÍNIMA (mm²) que atende com segurança após as correções?"
        },

        { "tipo": "texto", "texto": (
            "💡 Dica de Engenheiro: Se após aplicar os fatores a corrente corrigida ficar menor que a de projeto, "
                "você deve subir para a próxima bitola comercial e repetir o teste!"
            )
        },

        # ============================================================
        # 5. CRITÉRIO DE DECISÃO: O VEREDITO TÉCNICO
        # ============================================================
        { "tipo": "titulo", "texto": "5. O Veredito: Validação da Seção por Capacidade Térmica" },

        { "tipo": "texto", "texto": (
            "Agora você deve confrontar a Capacidade Corrigida (I_z) com a sua Corrente de Projeto (I_b). "
            "Esta é a regra de ouro da segurança elétrica na NBR 5410:\n\n"
            "-- O condutor deve ser capaz de transportar a carga sem que a temperatura da isolação ultrapasse o limite crítico."
        )},

        { "tipo": "equacao",
            "latex": r"I_{corrigida} < I_{projeto} \implies \text{Seção Insuficiente}"
        },

        { "tipo": "equacao",
            "latex": r"I_{corrigida} \geq I_{projeto} \implies \text{Seção Preliminar Aceita}"
        },
       
        {
            "tipo": "texto",
            "texto": (
                "Cuidado! \n\n Mesmo que a seção passe no critério térmico, ela ainda não é definitiva. "
                "Em circuitos longos, o condutor pode ser aprovado no calor, mas reprovado na Queda de Tensão (ΔV)."
                "Se a tensão cair demais no trajeto, o motor perderá torque, aquecerá excessivamente e poderá queimar, "
                "mesmo que o cabo esteja 'frio'."
            )
        },

        { "tipo": "questao_multipla_escolha", "id": "problema.01.003.0010",
            "pergunta": "Se após aplicar os fatores de correção você descobrir que I_z < I_b, qual deve ser sua conduta técnica?",
            "alternativas": {
                "a": "Manter a bitola, pois os fatores de correção são apenas sugestões de segurança.",
                "b": "Trocar o motor por um de menor potência para reduzir a corrente de projeto.",
                "c": "Selecionar o condutor de seção nominal imediatamente superior na tabela e repetir a verificação.",
                "d": "Ignorar a NBR 5410 e utilizar o método do 'costume de obra'."
            },
            "alternativa_correta": "c"
        },


        # ============================================================
        # 6. LEITURA CRÍTICA: O CONDUTOR ALÉM DO CALOR
        # ============================================================
        { "tipo": "titulo", "texto": "6. Análise Crítica: O Condutor Além do Calor"  },

        # { "tipo": "texto", "texto": (
        #     "É fundamental compreender que um condutor aprovado pelo critério da corrente admissível (I_z < I_b) garante apenas que o cabo não irá derreter. "
        #     "No entanto, ele ainda pode falhar por outros motivos técnicos invisíveis ao olhar leigo, como:\n\n"
        #     "* **Queda de Tensão Excessiva:** a energia 'se perde' no caminho devido à resistência do fio.\n"
        #     "* **Aquecimento Acumulado:** percursos longos ou agrupamentos severos que degradam a isolação precocemente.\n\n"
        #     "**Conclusão:** Esta é a primeira barreira normativa. O projeto ainda não está blindado."
        # )},

        # ============================================================
        # 7. CONFRONTO: TEORIA (NORMA) VS. REALIDADE (CAMPO)
        # ============================================================
        {"tipo": "titulo", "texto": "7. Diagnóstico: Norma x Instalação Atual" },

        # { "tipo": "texto", "texto": (
        #     "Agora é o momento do confronto final desta etapa. Compare a Bitola Instalada "
        #     "que você verificou na inspeção física com a Bitola Mínima exigida pela NBR 5410."
        # )},

        # {
        #     "tipo": "equacao",
        #     "latex": r"\text{Seção}_{\text{Instalada}} \geq \text{Seção}_{\text{Normativa}} \implies \text{Conformidade Preliminar}"
        # },

        # {
        #     "tipo": "questao_multipla_escolha",
        #     "id": "problema.01.003.0011",
        #     "pergunta": "Com base na sua análise, o condutor atualmente instalado no motor atende ao critério de corrente admissível da NBR 5410?",
        #     "alternativas": {
        #         "a": "Sim, a seção instalada é igual ou superior à exigida pela norma.",
        #         "b": "Não, a seção instalada é inferior à exigida, caracterizando uma Não Conformidade Grave.",
        #         "c": "Não é possível afirmar sem medir a distância do cabo primeiro.",
        #         "d": "Sim, pois se o motor está ligando, o cabo é adequado."
        #     },
        #     "alternativa_correta": "a" # O sistema deve validar conforme o input anterior do aluno
        # },

        # {
        #     "tipo": "texto",
        #     "texto": (
        #         "### Próximos Passos:\n"
        #         "* **Se você marcou 'Não' (Opção B):** Você acabou de detectar um risco real de incêndio ou falha prematura. Registre isso no seu relatório técnico.\n"
        #         "* **Se você marcou 'Sim' (Opção A):** Excelente. O sistema está seguro termicamente, mas agora precisamos verificar se a **Queda de Tensão** não irá subalimentar o motor."
        #     )
        # },

        # { "tipo": "espacador", "pixels": 30 }

# =========================
        # 6. Leitura crítica

        # Observe algo importante:

        # Um cabo pode suportar corrente suficiente,
        # mas ainda falhar por:

        # queda de tensão excessiva
        # aquecimento acumulado
        # percurso longo

        # Ou seja:

        # Essa é apenas a primeira verificação normativa.

        # Não é decisão final.

# =========================
        # 7. Confronto com a bitola instalada

        # Agora compare:

        # Bitola instalada em campo
        # versus
        # Bitola mínima exigida pela norma

        # Pergunta direta:

        # O condutor atualmente instalado atende ao critério de corrente admissível?

        # Se não atender:

        # → já existe não conformidade.

        # Se atender:

        # → prossiga para a verificação de queda de tensão.


# ====================================
    {"tipo": "titulo", "texto": "Recapitulação Técnica: " },
        # Síntese da Etapa 3

        # Nesta etapa você:

        # Aplicou a NBR 5410 corretamente
        # Selecionou seção mínima por corrente
        # Aplicou fatores de correção
        # Confrontou com instalação real

        # Agora você tem:

        # Seção preliminar por corrente admissível.

        # Mas isso não encerra o dimensionamento.

        # Na próxima etapa:

        # → você vai verificar se essa seção também atende ao limite de queda de tensão.

        # É aqui que muitos projetos falham.
    ]






# Perfeito. Agora entramos na parte normativa.
# Aqui o aluno deixa de apenas calcular corrente e passa a **tomar decisão baseada em norma técnica**.

# Abaixo está o texto estruturado para o app — didático, progressivo e com entregas claras.

# ---

# # ETAPA 3 — Seleção Preliminar pela Corrente Admissível

# ## Aplicação da NBR 5410

# Até aqui você já possui:

# * Corrente de projeto do motor
# * Dados de instalação
# * Temperatura ambiente
# * Tipo de percurso do cabo

# Agora começa a parte normativa.

# A pergunta deixa de ser:

# > Quanto o motor consome?

# E passa a ser:

# > O cabo consegue conduzir essa corrente com segurança?

# Essa resposta não vem da física pura.
# Ela vem da norma.

# ---

# ## 1. O que significa “corrente admissível”?

# Corrente admissível é:

# > A máxima corrente que um condutor pode transportar continuamente sem ultrapassar o limite térmico da isolação.

# Se o cabo conduz corrente acima desse limite:

# * A isolação envelhece
# * A vida útil diminui
# * Pode ocorrer falha elétrica
# * Existe risco de incêndio

# Dimensionar por corrente é, antes de tudo, proteger o sistema.

# ---

# ## 2. Consulta à Tabela da NBR 5410

# Agora você deve abrir a tabela de capacidade de condução de corrente da norma.

# Mas atenção:
# Você não pode simplesmente olhar um número.

# Você precisa considerar:

# * Método de instalação (eletroduto embutido? bandeja? enterrado?)
# * Temperatura ambiente real
# * Número de condutores carregados no mesmo eletroduto

# Esses fatores alteram a capacidade do cabo.

# ---

# ## 3. Aplicação de Fatores de Correção

# A norma fornece valores de corrente admissível em condições padrão.

# Se sua instalação estiver fora do padrão (exemplo: ambiente 40°C), você deve aplicar fator de correção térmico.

# Corrente admissível corrigida:

# [
# I_{corrigida} = I_{tabela} \cdot F_{temperatura} \cdot F_{agrupamento}
# ]

# Onde:

# * ( F_{temperatura} ) < 1 se ambiente quente
# * ( F_{agrupamento} ) < 1 se houver vários cabos juntos

# Isso significa que a capacidade real do cabo pode ser menor que a da tabela.

# ---

# ## 4. Procedimento Técnico

# Agora execute a sequência correta:

# 1. Identifique método de instalação.
# 2. Localize na norma a tabela correspondente.
# 3. Escolha material do condutor (cobre ou alumínio).
# 4. Verifique capacidade de corrente para cada seção.
# 5. Aplique fatores de correção.
# 6. Compare com a corrente de projeto.

# A regra é objetiva:

# [
# I_{admissível} \geq I_{projeto}
# ]

# Se não atender, aumente a seção.

# ---

# ## 5. Exemplo Didático

# Suponha:

# Corrente de projeto = 12 A

# Tabela (condições padrão):

# 1,5 mm² → 15 A
# 2,5 mm² → 21 A

# Se a temperatura for elevada e houver fator 0,9:

# 1,5 mm² → 15 × 0,9 = 13,5 A
# 2,5 mm² → 21 × 0,9 = 18,9 A

# Agora compare:

# 12 A < 13,5 A

# Tecnicamente, 1,5 mm² ainda atenderia.

# Mas engenharia não trabalha no limite mínimo.

# Aplicando margem de segurança operacional:

# → seção preliminar adotada: 2,5 mm²

# ---

# ## 6. Entrega Técnica

# Agora você deve responder formalmente:

# * Qual é a corrente de projeto?
# * Qual é o método de instalação?
# * Qual fator de correção foi aplicado?
# * Qual é a corrente admissível corrigida?
# * Qual seção atende o critério?

# ENTREGA 3:

# Declare:

# “A seção mínima exigida pelo critério de corrente admissível é ___ mm².”

# Sem considerar ainda queda de tensão.

# ---

# ## 7. Leitura Crítica

# Pergunta importante:

# Se a bitola instalada atualmente for menor que a encontrada aqui, o que isso significa?

# Significa que o sistema já pode estar operando acima da capacidade térmica do cabo.

# Se for maior, pode estar superdimensionado.

# Mas atenção:

# Atender ao critério de corrente não significa que o dimensionamento está concluído.

# Ainda falta:

# * Verificação de queda de tensão
# * Verificação térmica completa
# * Confronto com medições reais

# ---

# ## Síntese da Etapa 3

# Você acabou de aplicar:

# * Norma técnica
# * Critério térmico
# * Fatores de correção
# * Tomada de decisão preliminar

# Agora existe uma seção candidata.

# Mas ainda não existe conclusão final.

# A engenharia só termina quando todos os critérios são atendidos simultaneamente.

# Na próxima etapa você vai verificar se essa seção também atende à queda de tensão.

# É aqui que muitos projetos falham.

# ---

# Se quiser, posso agora montar:

# * A etapa completa de verificação de queda de tensão
# * Ou já integrar essa etapa no formato pronto para o `get_blocos()` do seu app
