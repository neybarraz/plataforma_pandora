from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Controle de Variáveis",
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao realizar uma investigação técnica em um circuito elétrico, não basta apenas analisar os valores obtidos. "
                "Para que a verificação do dimensionamento dos condutores seja válida, é necessário garantir que os parâmetros "
                "do sistema não sofram variações que comprometam a análise."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No seu plano de análise, você definiu que serão realizados cálculos e verificações com base nas características "
                "do motor e do circuito elétrico. Agora, é necessário garantir que essas análises não sejam influenciadas por "
                "alterações indevidas nos dados ou nas condições consideradas."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Observe o sistema",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_03_q_0001",
            "pergunta": (
                "Ao avaliar o circuito de alimentação do motor, quais fatores poderiam variar ou ser considerados de forma inconsistente "
                "e prejudicar a análise do dimensionamento dos condutores?"
            ),
            "placeholder": (
                "Pense em parâmetros do sistema que, se considerados de forma diferente, poderiam alterar os resultados..."
            ),
            "altura": 150,
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_03_q_0002",
            "pergunta": (
                "Por que essas possíveis variações poderiam comprometer a interpretação dos resultados da análise?"
            ),
            "placeholder": (
                "Explique como inconsistências nos dados ou nas condições poderiam levar a conclusões incorretas..."
            ),
            "altura": 140,
        },
        {
            "tipo": "texto",
            "texto": (
                "Para que a análise seja confiável, é necessário manter consistentes todos os parâmetros que influenciam diretamente "
                "o comportamento elétrico do circuito. Isso garante que os resultados obtidos representem corretamente a relação entre "
                "a corrente do motor e a capacidade dos condutores."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Definição das variáveis de controle",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_03_q_0003",
            "pergunta": (
                "Quais parâmetros do sistema devem ser mantidos consistentes durante a análise para garantir que os resultados sejam válidos?"
            ),
            "placeholder": (
                "Liste os parâmetros que não devem variar ou que devem ser considerados de forma fixa na análise..."
            ),
            "altura": 180,
        },
        {
            "tipo": "texto",
            "texto": (
                "Em um sistema como o analisado, alguns parâmetros costumam precisar ser mantidos consistentes para evitar distorções nos resultados:"
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "tensão nominal de alimentação do motor",
                "potência nominal do motor",
                "tipo de sistema elétrico (monofásico ou trifásico)",
                "material do condutor (cobre ou alumínio)",
                "comprimento do circuito considerado nos cálculos",
                "condições de instalação dos condutores",
            ],
        },
        {
            "tipo": "texto",
            "texto": (
                "Esses itens não são uma resposta pronta, mas indicam o tipo de controle necessário para garantir uma análise técnica consistente."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Síntese do controle de variáveis",
        },
        {
            "tipo": "questao_texto",
            "id": "analise_2_03_q_0004",
            "pergunta": (
                "Explique, com suas palavras, como você garantirá a consistência dos parâmetros durante a análise do circuito."
            ),
            "placeholder": (
                "Descreva como você manterá os dados e condições coerentes ao longo da investigação..."
            ),
            "altura": 200,
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Dica: o controle de variáveis garante que os resultados da análise sejam confiáveis. "
                "Sem esse controle, não é possível afirmar se as conclusões refletem o comportamento real do sistema."
            ),
        },
    ]