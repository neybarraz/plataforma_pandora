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
# Aqui vamos estruturar a **Etapa 7 — Decisão Técnica Final** no formato ideal para o app: objetivo, direto, formador de projetista, com entrega concreta.

# ---

# # ETAPA 7 — Decisão Técnica Final

# ## Agora você decide como engenheiro

# Você já:

# * coletou dados reais
# * calculou corrente de projeto
# * consultou tabela de capacidade de condução
# * verificou queda de tensão
# * analisou condições térmicas
# * comparou teoria com medições reais

# Agora não há mais cálculo novo.

# Há decisão.

# E decisão técnica exige justificativa.

# ---

# # 1. Revisão estruturada antes da decisão

# Antes de escrever sua conclusão, responda objetivamente:

# ### ✔ Qual é a seção atualmente instalada?

# Registre o valor encontrado em campo.

# ---

# ### ✔ Qual é a seção mínima exigida pelo critério de corrente admissível?

# Com base na corrente de projeto e na tabela da NBR 5410, considerando:

# * método de instalação
# * temperatura ambiente
# * fatores de correção

# Qual foi a menor seção que atendeu a corrente?

# ---

# ### ✔ Qual seção atende ao critério de queda de tensão?

# Você calculou a queda percentual.

# Pergunta objetiva:

# A seção preliminar manteve a queda dentro do limite normativo (ex: 4%)?

# Se não manteve:

# Qual seção passou a atender?

# ---

# ### ✔ Qual seção atende ao critério térmico?

# Considerando:

# * potência dissipada (I²R)
# * temperatura ambiente
# * método de instalação

# Existe risco de aquecimento excessivo?

# A seção instalada suporta a dissipação esperada?

# ---

# # 2. Comparação consolidada

# Agora organize mentalmente (ou em tabela):

# | Critério            | Seção mínima exigida |
# | ------------------- | -------------------- |
# | Corrente admissível | ___ mm²              |
# | Queda de tensão     | ___ mm²              |
# | Aquecimento         | ___ mm²              |

# Regra prática de engenharia:

# > A seção adotada deve ser a MAIOR entre as exigidas pelos critérios.

# Se um critério exigir 6 mm²
# e outro exigir 10 mm²

# A seção final não é média.
# É 10 mm².

# ---

# # 3. Confronto com a seção instalada

# Agora compare:

# Seção instalada em campo: ___ mm²
# Seção mínima necessária após verificação completa: ___ mm²

# Existem três possibilidades:

# ### 1️⃣ Adequado

# A seção instalada é igual ou maior que a mínima exigida.

# ### 2️⃣ Subdimensionado

# A seção instalada é menor que a mínima exigida.

# Risco:

# * aquecimento
# * queda de tensão excessiva
# * redução de vida útil
# * possível não conformidade normativa

# ### 3️⃣ Superdimensionado

# A seção instalada é muito maior que o necessário.

# Consequência:

# * custo elevado
# * tecnicamente seguro
# * economicamente questionável

# ---

# # 4. ENTREGA 7 — Conclusão Técnica Formal

# Agora redija como engenheiro responsável.

# Modelo esperado:

# > “O condutor de ___ mm² está (adequado / subdimensionado / superdimensionado), pois atende (ou não atende) aos critérios de corrente admissível, queda de tensão e condições térmicas conforme NBR 5410.”

# Se estiver inadequado:

# > “Recomenda-se a substituição por condutor de ___ mm² para garantir conformidade normativa e segurança operacional.”

# Essa não é uma resposta de prova.

# É uma justificativa técnica.

# ---

# # 5. Leitura crítica final

# Antes de encerrar, responda mentalmente:

# * A corrente medida em campo confirma o modelo?
# * A tensão medida confirma o cálculo de queda?
# * O sistema apresenta indícios práticos de aquecimento?
# * Existe margem de segurança razoável?

# Engenharia não é apenas passar na norma.

# É garantir desempenho e durabilidade.

# ---

# # Síntese Final

# Você acabou de executar:

# ✔ levantamento de dados
# ✔ modelagem elétrica
# ✔ aplicação normativa
# ✔ verificação quantitativa
# ✔ validação experimental
# ✔ tomada de decisão técnica

# Isso é engenharia elétrica aplicada.

# Não é “entender eletricidade”.

# É decidir sob restrição técnica, com responsabilidade.

# ---

# Se você quiser, posso agora:

# * transformar isso em blocos `get_blocos()` prontos para o app
# * incluir um exemplo completo com números reais resolvidos
# * incluir um checklist visual final estilo “laudo técnico”

# Agora sim estamos formando alguém capaz de assinar projeto.
