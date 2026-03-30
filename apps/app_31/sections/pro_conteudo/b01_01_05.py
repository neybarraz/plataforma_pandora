from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Etapa em desenvolvimento. "
                "O material será incorporado após a definição final do modelo "
                "analítico e dos critérios de verificação aplicáveis."
            ),
        }



# Perfeito. Agora entramos em uma etapa decisiva do dimensionamento.

# Aqui o aluno deixa de olhar apenas corrente e queda de tensão e passa a avaliar **segurança térmica do condutor**.

# Abaixo está o texto estruturado para uso direto no app.

# ---

# # ETAPA 5 — Verificação Térmica do Condutor

# ## O cabo suporta o aquecimento gerado pela corrente?

# Até agora você:

# * Calculou a corrente de projeto
# * Selecionou uma seção preliminar
# * Verificou a queda de tensão

# Agora surge uma pergunta crítica:

# > O cabo consegue dissipar o calor gerado pela corrente sem comprometer a isolação?

# Se a resposta for negativa, o dimensionamento está incorreto — mesmo que a queda de tensão esteja dentro do limite.

# ---

# ## 1. Entendendo a origem do aquecimento

# Todo condutor possui resistência elétrica.

# Quando a corrente circula, ocorre dissipação de energia sob a forma de calor.

# A potência dissipada no trecho é dada por:

# [
# P_{perda} = I^2 \cdot R
# ]

# Onde:

# * ( I ) = corrente que percorre o cabo
# * ( R ) = resistência elétrica do trecho

# Observe um ponto fundamental:

# O aquecimento cresce com o **quadrado da corrente**.

# Isso significa que um pequeno aumento na corrente gera um aumento significativo na dissipação térmica.

# ---

# ## 2. Cálculo da potência dissipada

# Você já conhece:

# * Corrente de projeto (A)
# * Comprimento do cabo (m)
# * Seção escolhida (mm²)

# A resistência do trecho pode ser estimada por:

# [
# R = \rho \frac{L}{A}
# ]

# Onde:

# * ( \rho ) = resistividade do material (cobre ou alumínio)
# * ( L ) = comprimento do circuito (ida e volta)
# * ( A ) = área da seção do condutor

# Agora você deve calcular:

# 1. A resistência total do trecho
# 2. A potência dissipada no cabo

# ---

# ### ENTREGA 5 — Cálculo térmico

# Calcule:

# * Resistência do trecho (Ω)
# * Potência dissipada total (W)

# Depois responda:

# Esse valor é coerente com a instalação observada?

# Por exemplo:

# * O cabo está dentro de eletroduto embutido?
# * Está agrupado com outros condutores?
# * Está exposto ao sol?
# * O ambiente possui temperatura elevada?

# A dissipação térmica precisa ser compatível com a capacidade de resfriamento do sistema.

# ---

# ## 3. Fatores de correção térmica (norma)

# A NBR 5410 estabelece que a capacidade de condução de corrente depende:

# * Temperatura ambiente
# * Método de instalação
# * Agrupamento de cabos

# Se o ambiente estiver acima da temperatura de referência (normalmente 30°C), deve-se aplicar fator de correção.

# Se houver vários cabos agrupados, também se aplica fator redutor.

# Isso significa que:

# Mesmo que a seção suporte a corrente nominal em condição ideal,
# ela pode não suportar em condição real.

# ---

# ## 4. Leitura técnica do resultado

# Após calcular a potência dissipada e considerar fatores de correção, responda:

# * A seção escolhida ainda suporta a corrente corrigida?
# * O cabo opera com margem de segurança?
# * Existe risco de aquecimento excessivo?

# Se a perda for significativa, podem ocorrer:

# * Aquecimento excessivo do condutor
# * Envelhecimento prematuro da isolação
# * Redução da vida útil
# * Risco de falha elétrica
# * Possível disparo de proteção

# Engenharia não é apenas “funcionar hoje”.
# É funcionar com segurança ao longo do tempo.

# ---

# ## 5. Conexão com a medição real

# Agora confronte teoria com campo.

# Perguntas técnicas:

# * O cabo apresenta sinais de aquecimento?
# * Existe escurecimento ou ressecamento da isolação?
# * A corrente medida está acima da nominal?
# * A tensão no motor está reduzida (indicando possível compensação de corrente)?

# Se corrente real > corrente calculada, o aquecimento real será maior do que o previsto.

# Isso altera completamente a decisão.

# ---

# ## Síntese da Etapa

# Nesta etapa você:

# * Calculou a potência dissipada no cabo
# * Avaliou a influência da resistência elétrica
# * Aplicou fatores de correção térmica
# * Verificou compatibilidade com instalação real
# * Identificou riscos operacionais

# Agora você não está apenas dimensionando por corrente.

# Você está verificando segurança térmica.

# Na próxima etapa, a decisão técnica final será consolidada com base em:

# * Corrente admissível
# * Queda de tensão
# * Condição térmica

# Somente quando os três critérios forem atendidos simultaneamente, o condutor estará corretamente dimensionado.











    ]



