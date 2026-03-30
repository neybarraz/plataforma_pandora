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
    ]



# Perfeito.
# Agora entramos na parte mais formadora do processo: **validar modelo com realidade**.

# Abaixo está o texto estruturado para o app, didático, técnico e com entregas claras.

# ---

# # ETAPA 6 — Confronto com Medição Real

# ## A teoria explica o sistema ou o sistema desmente a teoria?

# Até aqui você:

# * Calculou corrente nominal
# * Selecionou seção preliminar
# * Verificou queda de tensão teórica
# * Aplicou critérios normativos

# Agora vem a pergunta que separa cálculo acadêmico de engenharia real:

# > O comportamento medido em campo confirma o modelo calculado?

# Se não confirmar, existe erro — e você precisa identificá-lo.

# ---

# ## 1. Revisão dos dados medidos

# Você já coletou:

# * Tensão no quadro (V_quadro)
# * Tensão no motor (V_motor)
# * Corrente real medida (I_real)

# Esses três valores são suficientes para iniciar a análise crítica.

# ---

# ## 2. Cálculo da queda de tensão real

# A queda real medida é:

# [
# \Delta V_{real} = V_{quadro} - V_{motor}
# ]

# Agora transforme em percentual:

# [
# % \Delta V_{real} = \frac{\Delta V_{real}}{V_{quadro}} \times 100
# ]

# ### ENTREGA 1

# Calcule:

# * ΔV_real (em volts)
# * %ΔV_real

# Registre os dois valores.

# ---

# ## 3. Comparação com a queda teórica

# Você já calculou anteriormente a queda de tensão prevista pelo modelo:

# [
# \Delta V_{teórica}
# ]

# Agora compare:

# | Tipo de queda | Valor |
# | ------------- | ----- |
# | Teórica       | ___ V |
# | Real medida   | ___ V |

# Pergunta direta:

# A queda real está próxima da teórica?

# ---

# ## 4. Interpretação técnica

# Agora começa a análise de engenharia.

# ### Caso 1 — Queda real ≈ Queda teórica

# Isso indica que:

# * O modelo está coerente
# * A resistência estimada está próxima da real
# * As conexões estão adequadas

# Conclusão: o comportamento elétrico está consistente com o cálculo.

# ---

# ### Caso 2 — Queda real maior que a teórica

# Isso indica que existe resistência adicional no sistema.

# Possíveis causas:

# * Conexões frouxas
# * Bornes oxidados
# * Emendas mal executadas
# * Cabo degradado
# * Condutor parcialmente danificado

# Aqui o cabo pode até estar corretamente dimensionado, mas o sistema está com problema de execução.

# ### ENTREGA 2

# Liste pelo menos duas hipóteses técnicas que expliquem a diferença observada.

# ---

# ## 5. Análise da corrente medida

# Agora compare:

# * Corrente nominal calculada
# * Corrente real medida

# Pergunta fundamental:

# A corrente real é maior que a nominal?

# Se SIM:

# Isso pode indicar:

# * Queda de tensão relevante
# * O motor tentando manter potência
# * Aumento do esforço elétrico
# * Possível aquecimento excessivo

# Quando a tensão cai, o motor tende a aumentar corrente para manter torque.

# Isso aumenta perdas:

# [
# P_{perda} = I^2 R
# ]

# Pequeno aumento de corrente → grande aumento de aquecimento.

# ### ENTREGA 3

# Explique, com base nos valores medidos, se o motor está operando sob esforço elétrico.

# ---

# ## 6. Coerência entre corrente e queda

# Agora conecte os dois fenômenos:

# Se queda de tensão aumenta → corrente pode aumentar.

# Se corrente aumenta → perdas aumentam.

# Se perdas aumentam → temperatura aumenta.

# Você consegue perceber o ciclo?

# Esse é o momento em que você deixa de aplicar fórmulas isoladas e começa a enxergar sistema elétrico como sistema físico integrado.

# ---

# ## 7. Decisão técnica parcial

# Com base nos dados reais, responda formalmente:

# 1. A queda de tensão está dentro do limite normativo?
# 2. A corrente real está coerente com a potência do motor?
# 3. O modelo teórico representa bem o sistema?
# 4. Existe indício de falha construtiva?
# 5. Existe indício de subdimensionamento?

# ### ENTREGA FINAL DA ETAPA

# Redija um parecer técnico curto:

# “O comportamento real (confirma / não confirma) o modelo teórico. A diferença observada pode ser explicada por ______. A instalação apresenta (ou não apresenta) indícios de inadequação.”

# ---

# ## Síntese da Etapa 6

# Nesta etapa você:

# * Calculou queda real
# * Comparou com previsão teórica
# * Avaliou coerência entre corrente e tensão
# * Identificou possíveis falhas ocultas
# * Produziu diagnóstico técnico

# Aqui você deixa de ser executor de fórmula.

# Você vira analista de sistema elétrico real.

# ---

# Se você quiser, posso agora:

# * Ajustar isso já no formato `get_blocos()` pronto para o app
# * Integrar automaticamente com os valores já coletados na Etapa 1
# * Montar a Etapa 7 (decisão final de dimensionamento) conectando tudo

# Agora o aluno realmente está praticando engenharia.
