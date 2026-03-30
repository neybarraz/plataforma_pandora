from __future__ import annotations


def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Fundamentos físicos do sistema de bombeamento",
        },



# Perfeito.
# Agora entramos no ponto onde muitos projetos falham: **queda de tensão**.

# Abaixo está o texto estruturado para o app, mantendo lógica progressiva, interação frequente e entrega técnica clara.

# ---

# # ETAPA 4 — Verificação de Queda de Tensão

# ## A seção escolhida realmente entrega energia suficiente ao motor?

# Você já calculou a corrente de projeto.
# Você já selecionou uma seção preliminar pela capacidade de condução de corrente.

# Mas ainda falta responder a pergunta mais crítica:

# > A tensão que sai do quadro chega ao motor dentro do limite aceitável?

# A norma (como a NBR 5410) normalmente limita a queda de tensão total do circuito a aproximadamente **4%**.

# Se ultrapassar esse valor, o motor pode:

# * perder desempenho
# * aquecer excessivamente
# * aumentar a corrente
# * reduzir vida útil

# Aqui começa a verificação real.

# ---

# ## 1. Entendendo o que está sendo calculado

# Queda de tensão é a diferença entre:

# Tensão no quadro
# menos
# Tensão que chega ao motor

# Ela acontece porque o cabo possui resistência elétrica.

# Quanto maior a resistência e quanto maior a corrente, maior será a queda.

# ---

# ## 2. Modelo de cálculo trifásico

# Para sistema trifásico, usamos:

# ΔV = √3 · I · R · L

# Onde:

# I = corrente de projeto (A)
# R = resistência do condutor (Ω/m)
# L = comprimento do circuito (m)

# Mas a resistência depende da seção do cabo:

# R = ρ · L / A

# Onde:

# ρ = resistividade do material (cobre ≈ 0,0175 Ω·mm²/m)
# L = comprimento (m)
# A = área da seção (mm²)

# Substituindo:

# ΔV = √3 · I · ρ · L² / A

# Essa expressão mostra algo importante:

# * Se a distância dobra, a queda cresce muito.
# * Se a seção aumenta, a queda diminui.
# * Se a corrente aumenta, a queda aumenta.

# Isso não é teoria.
# Isso é comportamento físico real.

# ---

# ## 3. Cálculo prático com seus dados

# Agora você deve usar:

# * Corrente de projeto calculada anteriormente
# * Distância medida em campo
# * Seção preliminar escolhida

# ### ENTREGA 4 — Cálculo da queda absoluta

# Calcule:

# ΔV (em volts)

# Depois calcule a queda percentual:

# %ΔV = (ΔV / V_nominal) × 100

# Onde V_nominal é a tensão da placa do motor.

# Esse valor percentual é o que será comparado com a norma.

# ---

# ## 4. Interpretação técnica

# Agora vem a pergunta decisiva:

# A queda percentual está abaixo de 4%?

# Se SIM:
# → A seção atende ao critério de queda de tensão.

# Se NÃO:
# → A seção está inadequada.
# → Você precisa aumentar a bitola.
# → Recalcular.
# → Verificar novamente.

# Aqui você entra em ciclo de decisão técnica.

# ---

# ## 5. Conexão com medição real

# Compare agora:

# Tensão nominal da placa
# Tensão medida no motor

# Calcule a queda real medida:

# ΔV_real = V_quadro − V_motor

# Calcule o percentual real medido.

# Pergunta importante:

# O valor medido se aproxima do valor teórico calculado?

# Se sim:
# → Modelo coerente.

# Se for muito maior:
# → Pode haver:

# * conexões ruins
# * emendas mal feitas
# * oxidação
# * cabo deteriorado

# Agora você não está apenas calculando.

# Você está validando o projeto com a realidade.

# ---

# ## 6. Leitura de engenharia

# Observe o impacto prático:

# Se a queda for alta:

# * O motor recebe menos tensão.
# * Para manter potência, tende a aumentar corrente.
# * A corrente maior aumenta aquecimento.
# * O aquecimento reduz vida útil.
# * O sistema se torna instável.

# Tudo começa com a queda de tensão.

# É aqui que muitos projetos aparentemente “funcionando” estão, na verdade, mal dimensionados.

# ---

# ## Síntese da Etapa 4

# Você:

# * Calculou a queda absoluta em volts
# * Calculou a queda percentual
# * Comparou com o limite normativo
# * Confrontou cálculo com medição real
# * Avaliou se a seção escolhida permanece válida

# Se a queda estiver dentro do limite, a seção sobrevive à primeira verificação.

# Se não estiver, você precisa ajustar.

# Essa é a diferença entre:

# Entender eletricidade
# e
# Projetar corretamente.

# ---

# Se você quiser, posso agora montar a próxima etapa:

# ETAPA 5 — Verificação térmica e fatores de correção

# Ou posso transformar isso em blocos prontos no formato do seu app.
















    ]