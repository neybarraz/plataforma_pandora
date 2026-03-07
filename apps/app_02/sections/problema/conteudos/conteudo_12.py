from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Modelo sistêmico – Saídas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a definição das entradas e a realização das etapas de "
                "processamento, o modelo sistêmico produz os resultados da "
                "análise. Esses resultados são chamados de saídas do sistema.\n\n"
                "No estudo do sistema de bombeamento, as saídas correspondem "
                "às informações obtidas a partir dos cálculos elétricos "
                "realizados durante a investigação. Esses resultados permitem "
                "avaliar se a alimentação elétrica do motor está adequada e "
                "quais parâmetros devem ser adotados no circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_031",
            "pergunta": (
                "No modelo sistêmico aplicado ao sistema elétrico da motobomba, "
                "qual das alternativas representa um exemplo de saída do sistema?"
            ),
            "alternativas": {
                "a": "A potência nominal indicada na placa do motor",
                "b": "A distância entre a fonte de energia e o motor",
                "c": "A seção adequada do condutor elétrico",
                "d": "A temperatura ambiente da instalação",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "texto",
            "texto": (
                "Entre as principais saídas obtidas neste estudo estão a "
                "corrente do circuito, a seção adequada dos condutores "
                "elétricos e a forma correta de ligação do motor. Esses "
                "resultados representam as conclusões técnicas derivadas "
                "da análise realizada.\n\n"
                "Para determinar a seção adequada do condutor, é comum utilizar "
                "tabelas técnicas que indicam a capacidade de condução de "
                "corrente dos cabos elétricos. Essas tabelas relacionam a "
                "seção do condutor com a corrente máxima que ele pode suportar "
                "em determinadas condições de instalação."
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "tabela_01.png",
            "caption": "Tabela de capacidade de condução de corrente para cabos elétricos",
        },
        {
            "tipo": "texto",
            "texto": (
                "Observe a tabela apresentada. Ela mostra a capacidade de condução "
                "de corrente de cabos elétricos instalados em diferentes condições. "
                "A seção do condutor é indicada em milímetros quadrados (mm²) e "
                "cada valor corresponde a uma corrente máxima que o cabo pode "
                "conduzir sem comprometer sua integridade térmica.\n\n"
                "Na prática, engenheiros e técnicos utilizam esse tipo de tabela "
                "para selecionar a seção adequada do condutor de acordo com a "
                "corrente do circuito e o método de instalação utilizado."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_032",
            "pergunta": (
                "Ao utilizar uma tabela de capacidade de condução de corrente, "
                "qual informação principal ela permite determinar?"
            ),
            "alternativas": {
                "a": "A potência do motor elétrico",
                "b": "A tensão da rede elétrica",
                "c": "A seção adequada do condutor para determinada corrente",
                "d": "O número de equipamentos conectados ao circuito",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_033",
            "pergunta": (
                "De acordo com a tabela apresentada, qual grandeza está "
                "relacionada diretamente à capacidade de condução de corrente "
                "de um cabo elétrico?"
            ),
            "alternativas": {
                "a": "A cor do isolamento do cabo",
                "b": "A seção transversal do condutor (mm²)",
                "c": "A marca do fabricante",
                "d": "A altura do reservatório",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_texto",
            "id": "q_034",
            "pergunta": (
                "Explique, com suas palavras, por que a corrente do circuito "
                "e a seção do condutor estão diretamente relacionadas no "
                "dimensionamento de uma instalação elétrica."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]