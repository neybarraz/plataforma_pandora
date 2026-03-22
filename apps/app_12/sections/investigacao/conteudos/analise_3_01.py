from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Execução da Análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "Agora é o momento de aplicar, na prática, o plano investigativo construído nas etapas anteriores. "
                "Nesta etapa, você deve executar a análise de forma consciente, levantando os dados do motor e do circuito "
                "de alimentação, registrando o que foi considerado, o que foi calculado e o que foi verificado."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo não é apenas realizar cálculos isolados, mas produzir um registro técnico claro, "
                "organizado e útil para a interpretação posterior. Para isso, organize os dados por bloco de análise "
                "e descreva, com precisão, como a verificação do dimensionamento dos condutores foi conduzida."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Antes de iniciar a execução",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_000",
            "pergunta": (
                "Antes de iniciar os cálculos, o que você pretende verificar no sistema e quais aspectos do circuito serão analisados?"
            ),
            "placeholder": (
                "Indique o que será verificado e quais características do sistema serão analisadas..."
            ),
            "altura": 120,
        },
        {
            "tipo": "subtitulo",
            "texto": "Bloco 1 — Dados do motor",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_001",
            "pergunta": (
                "Descreva as características elétricas do motor consideradas na análise."
            ),
            "placeholder": (
                "Explique quais dados nominais do motor foram utilizados, como potência, tensão e corrente..."
            ),
            "altura": 100,
        },
        {
            "tipo": "subtitulo",
            "texto": "Levantamento dos dados nominais",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_002",
            "pergunta": "Potência nominal do motor:",
            "placeholder": "Registre o valor da potência do motor em W, kW ou CV...",
            "altura": 80,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_003",
            "pergunta": "Tensão nominal de operação do motor:",
            "placeholder": "Registre o valor da tensão nominal em volts (V)...",
            "altura": 80,
        },
        {
            "tipo": "subtitulo",
            "texto": "Dados complementares do motor",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_004",
            "pergunta": "Corrente nominal do motor (se disponível):",
            "placeholder": "Registre o valor da corrente nominal em ampères (A)...",
            "altura": 80,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_005",
            "pergunta": "Tipo de alimentação do motor:",
            "placeholder": "Indique se o sistema é monofásico ou trifásico...",
            "altura": 80,
        },
        {
            "tipo": "subtitulo",
            "texto": "Verificação inicial",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_006",
            "pergunta": (
                "Descreva, com base nesses dados, a demanda elétrica esperada do motor."
            ),
            "placeholder": (
                "Explique como os dados do motor ajudam a entender a corrente exigida pelo sistema..."
            ),
            "altura": 120,
        },
        {
            "tipo": "subtitulo",
            "texto": "Bloco 2 — Dados do circuito de alimentação",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_007",
            "pergunta": (
                "Descreva as características do circuito de alimentação consideradas na análise."
            ),
            "placeholder": (
                "Explique como o circuito foi caracterizado antes dos cálculos..."
            ),
            "altura": 100,
        },
        {
            "tipo": "subtitulo",
            "texto": "Levantamento dos condutores",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_008",
            "pergunta": "Seção dos condutores instalados:",
            "placeholder": "Registre a seção transversal dos cabos em mm²...",
            "altura": 80,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_009",
            "pergunta": "Material dos condutores:",
            "placeholder": "Indique o material do condutor, como cobre ou alumínio...",
            "altura": 80,
        },
        {
            "tipo": "subtitulo",
            "texto": "Dados do percurso elétrico",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_010",
            "pergunta": "Comprimento do circuito de alimentação:",
            "placeholder": "Registre o comprimento considerado no circuito em metros (m)...",
            "altura": 80,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_011",
            "pergunta": "Condição ou método de instalação dos condutores (se aplicável):",
            "placeholder": "Descreva a forma de instalação considerada na análise...",
            "altura": 80,
        },
        {
            "tipo": "subtitulo",
            "texto": "Aplicação dos cálculos",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_012",
            "pergunta": (
                "Descreva quais cálculos ou verificações foram realizados para avaliar o circuito."
            ),
            "placeholder": (
                "Exemplo: cálculo da corrente, verificação da capacidade de condução, queda de tensão..."
            ),
            "altura": 120,
        },
        {
            "tipo": "subtitulo",
            "texto": "Observação dos resultados da análise",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_013",
            "pergunta": (
                "O que foi observado ao comparar a corrente exigida pelo motor com as características dos condutores?"
            ),
            "placeholder": (
                "Descreva se houve compatibilidade, limite de operação, indício de subdimensionamento ou outra condição relevante..."
            ),
            "altura": 140,
        },
        {
            "tipo": "subtitulo",
            "texto": "Registro sintético da execução",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_3_01_q_014",
            "pergunta": (
                "Com base no que foi levantado, calculado e verificado, descreva resumidamente como a análise foi executada."
            ),
            "placeholder": (
                "Explique quais dados foram utilizados, quais verificações foram feitas e como a análise foi conduzida..."
            ),
            "altura": 200,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: primeiro registre os dados do motor e do circuito. Depois apresente, com objetividade, "
                "quais cálculos foram realizados e o que foi verificado em relação ao dimensionamento dos condutores."
            ),
        },
    ]