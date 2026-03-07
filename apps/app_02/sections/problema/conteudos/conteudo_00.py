from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Formalização do problema",
        },
        {
            "tipo": "texto",
            "texto": (
                "<b>Objetivo desta etapa:</b><br>"
                "<i>Descrever o cenário do sistema de bombeamento e registrar os dados técnicos "
                "mínimos necessários para modelar o problema elétrico. Nesta etapa ocorre o "
                "levantamento e organização das informações do sistema. A análise detalhada e "
                "os cálculos elétricos serão desenvolvidos posteriormente, na etapa de "
                "<b>Investigação</b>.</i><br><br>"

                "Aqui você realizará a <b>formalização do problema de engenharia</b>. A situação "
                "real do sistema de bombeamento do Bloco dos Professores será convertida em um "
                "problema técnico claramente delimitado, permitindo sua análise de forma "
                "estruturada. Para isso, você deverá:<br><br>"

                "1. Descrever o contexto e os dados iniciais do sistema;<br>"
                "2. Definir o recorte do problema com foco elétrico;<br>"
                "3. Formular a pergunta norteadora que orientará a investigação;<br>"
                "4. Construir um modelo sistêmico do problema (entradas → processamento → saídas);<br>"
                "5. Verificar se a descrição do problema está coerente, completa e tecnicamente consistente.<br><br>"

                "O foco deste conteúdo limita-se ao <b>dimensionamento da alimentação elétrica do motor</b>, "
                "considerando grandezas como potência, tensão, corrente, fator de potência, rendimento, "
                "seção transversal dos condutores e queda de tensão. Nesta fase <b>não devem ser considerados</b> "
                "critérios normativos de instalação nem dispositivos de proteção, pois o objetivo é compreender "
                "primeiramente os fundamentos elétricos envolvidos no funcionamento do sistema."
            ),
        },
    ]