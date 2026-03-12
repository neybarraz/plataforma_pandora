from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Pergunta norteadora",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a análise do contexto do ambiente e a definição do foco do problema, "
                "é necessário formular a pergunta que orientará toda a investigação. "
                "A pergunta norteadora funciona como o eixo central do estudo: ela organiza "
                "o processo de coleta de dados, direciona a análise das medições e orienta "
                "a interpretação física do fenômeno observado."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, a investigação busca compreender se o comportamento térmico "
                "da sala é compatível com condições adequadas de conforto para os ocupantes. "
                "Para responder a essa questão, será necessário observar como a temperatura "
                "se distribui no ambiente e como a temperatura do ar se relaciona com a "
                "temperatura das superfícies presentes na sala."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Assim, a pergunta que orienta a análise é:\n\n"
                "A distribuição de temperatura na sala e a relação entre as temperaturas do "
                "ar e das superfícies proporcionam condições adequadas de conforto térmico "
                "para os ocupantes?\n\n"
                "Responder a essa pergunta exigirá observar as medições realizadas no "
                "ambiente, interpretar o campo térmico da sala e relacionar os resultados "
                "obtidos com os conceitos de transferência de calor e conforto térmico."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_014",
            "pergunta": (
                "Qual é a função da pergunta norteadora em um estudo baseado em investigação?"
            ),
            "alternativas": {
                "a": "Substituir a necessidade de medições experimentais",
                "b": "Organizar e orientar o processo de investigação e análise do problema",
                "c": "Definir a solução final antes da coleta de dados",
                "d": "Limitar a análise apenas à temperatura externa",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A pergunta norteadora orienta todo o processo de investigação científica. "
                "Ela define qual fenômeno deve ser observado, quais dados precisam ser "
                "coletados e como esses dados devem ser interpretados. No contexto deste "
                "estudo, a pergunta conecta as medições de temperatura do ar e das superfícies "
                "com a análise do conforto térmico no ambiente."
            ),
        },
    ]