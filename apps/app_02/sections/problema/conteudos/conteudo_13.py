from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Validação do problema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a definição do contexto, do foco da análise, da pergunta "
                "norteadora e da construção do modelo sistêmico, é importante "
                "realizar uma verificação final da estrutura do problema.\n\n"
                "Essa etapa tem como objetivo avaliar se o problema foi "
                "formulado de forma coerente e se o modelo construído "
                "representa adequadamente o sistema elétrico analisado. "
                "Antes de iniciar os cálculos e a investigação técnica, "
                "é necessário confirmar que as variáveis relevantes foram "
                "identificadas e que a pergunta norteadora pode ser "
                "respondida a partir do modelo proposto."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_035",
            "pergunta": (
                "Ao validar a estrutura do problema, qual aspecto deve ser "
                "verificado antes de iniciar a investigação técnica?"
            ),
            "alternativas": {
                "a": "Se o reservatório possui capacidade suficiente de água",
                "b": "Se o modelo inclui as variáveis elétricas necessárias para a análise",
                "c": "Se a tubulação do sistema hidráulico foi substituída recentemente",
                "d": "Se o prédio possui mais de um reservatório superior",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A validação do problema permite confirmar que a estrutura "
                "definida até aqui é suficiente para orientar a investigação. "
                "Se as entradas do sistema estiverem bem identificadas, "
                "se as etapas de processamento forem coerentes e se as "
                "saídas representarem os resultados esperados da análise, "
                "então o problema está adequadamente formulado.\n\n"
                "Com essa verificação concluída, torna-se possível avançar "
                "para a etapa de investigação, na qual os cálculos elétricos "
                "serão realizados para responder à pergunta norteadora do estudo."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_036",
            "pergunta": (
                "Explique, com suas palavras, por que a validação do problema "
                "é importante antes de iniciar os cálculos elétricos da "
                "investigação."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]
