from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Saídas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Depois de identificar as entradas do sistema e de analisar as relações "
                "elétricas envolvidas no problema, é necessário compreender quais resultados "
                "são produzidos por essa investigação. Esses resultados correspondem às "
                "saídas do sistema, isto é, às informações técnicas obtidas a partir da "
                "análise realizada.\n\n"
                "No estudo do sistema de bombeamento, as saídas não representam apenas números "
                "ou respostas finais. Elas expressam conclusões técnicas que permitem avaliar "
                "as condições de alimentação do motor e definir parâmetros importantes para "
                "o dimensionamento do circuito elétrico."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Resultados obtidos na análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "Entre as principais saídas produzidas neste estudo estão a corrente do circuito, "
                "a seção adequada dos condutores elétricos e a forma de ligação do motor. "
                "Esses resultados decorrem da interpretação das variáveis de entrada e da "
                "aplicação das relações elétricas utilizadas ao longo da investigação.\n\n"
                "Ao serem obtidas, essas grandezas permitem passar de uma descrição inicial "
                "do sistema para uma avaliação técnica mais precisa, mostrando quais condições "
                "devem ser atendidas para que a alimentação elétrica do motor seja coerente "
                "com seu funcionamento."
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
            "tipo": "titulo",
            "texto": "Seção do condutor e tabelas técnicas",
        },
        {
            "tipo": "texto",
            "texto": (
                "Entre as saídas mais importantes da análise está a definição da seção adequada "
                "do condutor. Para isso, é comum utilizar tabelas técnicas que relacionam a "
                "capacidade de condução de corrente dos cabos elétricos com sua seção transversal "
                "e com determinadas condições de instalação.\n\n"
                "Essas tabelas permitem interpretar, de forma aplicada, se um condutor é capaz "
                "de conduzir a corrente do circuito sem comprometer suas condições térmicas de "
                "operação. Desse modo, a análise deixa de ser apenas teórica e passa a dialogar "
                "com critérios técnicos utilizados em situações reais de dimensionamento."
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
                "A tabela apresentada organiza a relação entre a seção do condutor, expressa "
                "em milímetros quadrados (mm²), e a corrente máxima que esse condutor pode "
                "suportar em determinadas condições de instalação. Essa relação é fundamental "
                "para compreender como os resultados da análise elétrica se traduzem em decisões "
                "técnicas concretas.\n\n"
                "Na prática, esse tipo de informação é utilizado para selecionar condutores "
                "compatíveis com a corrente do circuito. Assim, a saída do sistema não é apenas "
                "um valor calculado, mas uma referência para a escolha de elementos reais da "
                "instalação elétrica."
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
            "tipo": "texto",
            "texto": (
                "Quando se relacionam a corrente do circuito e a seção do condutor, torna-se "
                "possível compreender uma parte central do problema de dimensionamento elétrico. "
                "Quanto maior a corrente que circula no circuito, maiores tendem a ser as "
                "exigências impostas ao condutor, tanto do ponto de vista térmico quanto do "
                "ponto de vista operacional.\n\n"
                "Por isso, as saídas da análise elétrica devem ser interpretadas de forma "
                "articulada. Corrente, seção do condutor e condições de alimentação não são "
                "resultados independentes, mas elementos conectados que permitem construir uma "
                "avaliação técnica coerente do sistema estudado."
            ),
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