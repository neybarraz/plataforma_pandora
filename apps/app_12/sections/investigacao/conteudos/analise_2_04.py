from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Método de investigação",
        },
        {
            "tipo": "texto",
            "texto": (
                "Depois de definir o plano de análise e as variáveis de controle, é necessário "
                "estabelecer como os dados serão obtidos. Nesta etapa, você deve descrever o "
                "procedimento técnico que permitirá avaliar o dimensionamento dos condutores "
                "no circuito de alimentação do motor da bomba."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O método de investigação corresponde ao conjunto de ações que permitirá levantar "
                "os dados do motor, caracterizar o circuito elétrico e aplicar os cálculos necessários. "
                "Em outras palavras, é aqui que você transforma o plano de análise em um procedimento "
                "operacional estruturado."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Observe o que precisa ser feito",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_02_04_q_0001",
            "pergunta": (
                "Quais procedimentos precisam ser realizados para analisar o circuito de alimentação "
                "do motor e verificar o dimensionamento dos condutores?"
            ),
            "placeholder": (
                "Descreva as etapas necessárias para levantar os dados e realizar a análise do circuito..."
            ),
            "altura": 150,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_02_04_q_0002",
            "pergunta": (
                "Quais grandezas elétricas devem ser determinadas ou calculadas e quais informações do sistema são necessárias para isso?"
            ),
            "placeholder": (
                "Indique quais dados devem ser obtidos, como potência, tensão, corrente, comprimento do circuito, seção dos cabos..."
            ),
            "altura": 170,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_02_04_q_0003",
            "pergunta": (
                "Em quais condições ou etapas da análise esses dados devem ser obtidos e organizados?"
            ),
            "placeholder": (
                "Explique em que momento cada informação deve ser levantada ou calculada durante a análise..."
            ),
            "altura": 150,
        },
        {
            "tipo": "texto",
            "texto": (
                "Um método de investigação bem estruturado deve deixar claro: "
                "quais dados serão levantados, quais cálculos serão realizados, "
                "em que sequência isso ocorrerá e como os resultados serão organizados."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Elementos que podem compor seu método",
        },
        {
            "tipo": "lista",
            "itens": [
                "levantamento dos dados nominais do motor (potência, tensão, corrente)",
                "identificação do tipo de alimentação elétrica (monofásica ou trifásica)",
                "determinação da corrente elétrica do motor",
                "levantamento do comprimento do circuito de alimentação",
                "identificação da seção e do material dos condutores instalados",
                "cálculo da capacidade de condução de corrente dos cabos",
                "verificação da queda de tensão no circuito",
                "organização dos resultados para comparação entre valores calculados e valores admissíveis",
            ],
        },
        {
            "tipo": "texto",
            "texto": (
                "Esses elementos não substituem sua resposta. Eles funcionam como apoio para ajudar você "
                "a construir um procedimento técnico claro, coerente e executável."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Formule seu método de investigação",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_02_04_q_0004",
            "pergunta": (
                "Escreva, com suas palavras, o método de investigação que será utilizado. "
                "Explique como os dados do motor e do circuito serão obtidos, quais cálculos serão realizados, "
                "em que ordem a análise será conduzida e como os resultados permitirão avaliar o dimensionamento dos condutores."
            ),
            "placeholder": (
                "Escreva aqui seu método de investigação..."
            ),
            "altura": 240,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: descreva o procedimento em sequência lógica. Seu texto deve permitir que outra pessoa "
                "compreenda como a análise será realizada passo a passo."
            ),
        },
    ]