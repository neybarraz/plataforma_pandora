from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
# ========================================================
{"tipo": "titulo", "texto":"Estrutura do laudo técnico — orientação de elaboração"},

{"tipo": "texto", "texto": (
    "Nesta etapa, você deverá elaborar um laudo técnico completo fora do sistema. "
    "O objetivo não é repetir cálculos, mas organizar, interpretar e comunicar tecnicamente os resultados obtidos. "
    "A seguir, está a estrutura que o laudo deve conter, com orientações sobre como cada parte deve ser construída."
)},


# ========================================================
{"tipo": "titulo", "texto":"1. Identificação"},

{"tipo": "texto", "texto": (
    "A identificação define o contexto técnico do sistema analisado. "
    "Você deve descrever, de forma objetiva:\n\n"

    "- qual é o sistema (ex: motor, bomba, circuito);\n"
    "- qual é a finalidade da instalação;\n"
    "- qual o tipo de alimentação elétrica.\n\n"

    "Evite termos genéricos. O texto deve permitir entender claramente o que está sendo analisado. "
    "Não inclua cálculos ou análises nesta parte."
)},


# ========================================================
{"tipo": "titulo", "texto":"2. Objetivo do laudo"},

{"tipo": "texto", "texto": (
    "O objetivo define a finalidade técnica do documento. Você deve indicar claramente:\n\n"

    "- o que está sendo verificado;\n"
    "- qual é o objeto da análise (ex: condutor, circuito);\n"
    "- qual critério será utilizado (ex: NBR 5410).\n\n"

    "O texto deve ser direto e técnico, iniciando com verbos como: verificar, avaliar ou analisar."
)},


# ========================================================
{"tipo": "titulo", "texto":"3. Descrição do sistema"},

{"tipo": "texto", "texto": (
    "Nesta parte, você deve descrever como o sistema funciona. Inclua:\n\n"

    "- tipo de carga (motor, resistiva, etc.);\n"
    "- forma de operação (contínua, intermitente);\n"
    "- características relevantes do comportamento elétrico.\n\n"

    "Não inclua valores numéricos ou cálculos. "
    "O foco é explicar o funcionamento físico do sistema."
)},


# ========================================================
{"tipo": "titulo", "texto":"4. Dados de entrada"},

{"tipo": "texto", "texto": (
    "Apresente todos os dados utilizados na análise. Os dados devem ser organizados, preferencialmente em tabela, contendo:\n\n"

    "- potência;\n"
    "- tensão;\n"
    "- fator de potência;\n"
    "- rendimento;\n"
    "- comprimento do circuito;\n"
    "- temperatura ambiente;\n"
    "- seção do condutor.\n\n"

    "Todos os valores utilizados nos cálculos devem aparecer aqui. Não inclua resultados ou interpretações."
)},


# ========================================================
{"tipo": "titulo", "texto":"5. Metodologia e critérios adotados"},

{"tipo": "texto", "texto": (
    "Explique como a análise foi realizada. Você deve indicar:\n\n"

    "- quais equações foram utilizadas;\n"
    "- quais normas foram aplicadas;\n"
    "- quais critérios técnicos foram considerados.\n\n"

    "Essa parte deve mostrar o caminho lógico da análise, "
    "sem apresentar resultados numéricos."
)},


# ========================================================
{"tipo": "titulo", "texto":"6. Memorial de cálculo"},

{"tipo": "texto", "texto": (
    "Apresente os cálculos realizados de forma estruturada. Para cada cálculo, você deve:\n\n"

    "- apresentar a equação;\n"
    "- substituir os valores;\n"
    "- indicar o resultado com unidade.\n\n"

    "Não omita etapas. O memorial deve permitir que outro profissional reproduza os resultados."
)},


# ========================================================
{"tipo": "titulo", "texto":"7. Verificações técnicas"},

{"tipo": "texto", "texto": (
    "Nesta parte, você deve comparar os resultados com critérios técnicos. Inclua, no mínimo:\n\n"

    "- verificação de corrente (I_projeto ≤ I_admissível);\n"
    "- verificação da queda de tensão (%ΔV ≤ limite normativo).\n\n"

    "Para cada verificação:\n\n"

    "- apresente o valor obtido;\n"
    "- compare com o limite;\n"
    "- indique se atende ou não atende.\n\n"

    "Cada critério deve ser analisado separadamente."
)},


# ========================================================
{"tipo": "titulo", "texto":"8. Análise técnica"},

{"tipo": "texto", "texto": (
    "Aqui você deve interpretar os resultados obtidos. Responda, com base nos dados:\n\n"

    "- o sistema apresenta comportamento adequado?\n"
    "- existe margem de segurança?\n"
    "- há risco de falha ou degradação?\n\n"

    "Não repita valores. O foco é interpretação técnica, não cálculo."
)},


# ========================================================
{"tipo": "titulo", "texto":"9. Decisão técnica"},

{"tipo": "texto", "texto": (
    "Apresente a conclusão final do laudo. A resposta deve ser objetiva:\n\n"

    "- o sistema atende aos critérios normativos;\n"
    "ou\n"
    "- o sistema não atende aos critérios normativos.\n\n"

    "A decisão deve estar fundamentada nas verificações realizadas. Evite respostas vagas ou ambíguas."
)},


# ========================================================
{"tipo": "titulo", "texto":"10. Recomendação técnica"},

{"tipo": "texto", "texto": (
    "Indique a ação necessária com base na decisão. Exemplos:\n\n"

    "- manter a instalação;\n"
    "- redimensionar o condutor;\n"
    "- corrigir condições de instalação.\n\n"

    "A recomendação deve ser coerente com a análise realizada e aplicável na prática."
)},


# ========================================================
{"tipo": "titulo", "texto":"11. Fechamento técnico"},

{"tipo": "texto", "texto": (
    "Finalize o laudo com um texto breve reforçando:\n\n"

    "- que a análise foi baseada em critérios técnicos e normativos;\n"
    "- que os resultados representam as condições avaliadas.\n\n"

    "O fechamento deve transmitir clareza e responsabilidade técnica."
)},
    ]