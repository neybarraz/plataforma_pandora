from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Cenário do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa será realizada a <strong>formalização do problema de engenharia</strong> "
                "associado ao sistema de bombeamento. A proposta é converter a situação real observada "
                "no sistema em um problema técnico claramente delimitado, de modo que sua análise possa "
                "ser desenvolvida de forma estruturada ao longo da disciplina.\n\n"
                "Esse movimento de formalização é importante porque, em contextos reais, o sistema não "
                "aparece inicialmente como um problema pronto. Antes dos cálculos e das verificações "
                "técnicas, é necessário identificar quais informações são relevantes, definir o recorte "
                "da análise e organizar os dados mínimos que permitem construir uma interpretação "
                "consistente do funcionamento elétrico do conjunto."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo desta etapa é <strong>descrever o cenário do sistema de bombeamento e registrar "
                "os dados técnicos mínimos necessários para modelar o problema elétrico</strong>. "
                "Aqui ocorre o levantamento e a organização das informações iniciais do sistema. "
                "A análise detalhada e os cálculos elétricos serão desenvolvidos posteriormente, "
                "na etapa de investigação.\n\n"
                "Nesse processo, será necessário descrever o contexto de funcionamento do sistema, "
                "definir o recorte do problema com foco elétrico, formular a pergunta norteadora "
                "que orientará a investigação e construir um modelo sistêmico capaz de representar "
                "as relações entre entradas, processamento e saídas."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O foco deste conteúdo está limitado ao <strong>dimensionamento da alimentação elétrica do motor</strong>, "
                "considerando grandezas como potência, tensão, corrente, fator de potência, rendimento, "
                "seção transversal dos condutores e queda de tensão. O interesse, neste momento, "
                "é compreender quais variáveis elétricas definem o problema e como elas se articulam "
                "na caracterização técnica do sistema.\n\n"
                "Por esse motivo, nesta fase não serão considerados critérios normativos de instalação "
                "nem dispositivos de proteção. Esses elementos são importantes em uma análise completa, "
                "mas o recorte adotado aqui prioriza a compreensão dos fundamentos elétricos envolvidos "
                "no funcionamento do sistema e na definição inicial do problema de engenharia."
            ),
        },
    ]