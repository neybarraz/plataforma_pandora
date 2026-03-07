from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Pergunta norteadora do problema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após identificar o contexto do sistema, levantar os dados iniciais "
                "e definir o foco da análise, é necessário formular uma pergunta que "
                "oriente toda a investigação técnica. Essa pergunta é chamada de "
                "pergunta norteadora.\n\n"
                "Em atividades de engenharia, a pergunta norteadora funciona como "
                "o ponto central do problema. Ela direciona quais dados devem ser "
                "analisados, quais cálculos precisam ser realizados e quais decisões "
                "técnicas devem ser tomadas ao longo do estudo."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_025",
            "pergunta": (
                "Qual das alternativas representa corretamente a pergunta que "
                "orienta a análise do sistema de bombeamento estudado?"
            ),
            "alternativas": {
                "a": "Como aumentar a quantidade de água armazenada no reservatório superior?",
                "b": "Como dimensionar corretamente a alimentação elétrica do motor da bomba?",
                "c": "Como modificar o sistema hidráulico do reservatório?",
                "d": "Como alterar a estrutura do prédio para instalar uma nova bomba?",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, a pergunta norteadora está relacionada ao "
                "dimensionamento da alimentação elétrica do motor que aciona a "
                "motobomba do Bloco dos Professores. A partir dessa pergunta, a investigação "
                "será direcionada para compreender como as grandezas elétricas "
                "do sistema se relacionam e quais cálculos são necessários para "
                "garantir o funcionamento adequado do equipamento.\n\n"
                "Assim, a pergunta que orienta a análise pode ser formulada da "
                "seguinte forma:\n\n"
                "Como dimensionar corretamente a alimentação elétrica do motor "
                "da bomba do Bloco dos Professores, garantindo operação adequada dentro dos "
                "fundamentos básicos da eletricidade?"
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_026",
            "pergunta": (
                "Explique, com suas palavras, por que a definição de uma pergunta "
                "norteadora é importante para orientar a investigação de um "
                "problema técnico em engenharia."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]