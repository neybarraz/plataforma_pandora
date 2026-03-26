from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Pergunta central da análise",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a análise inicial do sistema, o levantamento dos dados disponíveis "
                "e a definição do foco da investigação, torna-se necessário formular a "
                "pergunta que orientará todo o estudo. A pergunta norteadora funciona "
                "como o eixo central da investigação: ela delimita o problema, organiza "
                "a observação do sistema e direciona a análise das grandezas envolvidas.\n\n"
                "No contexto deste estudo, essa etapa é fundamental porque a simples "
                "descrição do sistema de bombeamento não é suficiente para produzir uma "
                "análise técnica consistente. É preciso definir com clareza qual aspecto "
                "do sistema será investigado e qual problema de engenharia se pretende compreender."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em problemas de engenharia, a pergunta norteadora não apenas orienta a "
                "coleta de informações, mas também define quais relações físicas e técnicas "
                "devem ser examinadas ao longo da investigação. Ela indica quais dados "
                "precisam ser analisados, quais cálculos se tornam relevantes e quais "
                "decisões técnicas deverão ser justificadas com base nos resultados obtidos.\n\n"
                "No caso do sistema de bombeamento estudado, o foco está na alimentação "
                "elétrica do motor que aciona a motobomba. Isso significa que a investigação "
                "deve ser orientada para a compreensão das grandezas elétricas associadas "
                "ao funcionamento do motor e para a análise das condições necessárias ao "
                "seu dimensionamento básico."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "<div style='padding:14px; border-radius:8px; "
                "border-left:6px solid #14B8A6; margin:12px 0;'>"
                "<strong>Pergunta norteadora:</strong><br><br>"
                "Como dimensionar corretamente a alimentação elétrica do motor da bomba "
                "do Bloco dos Professores, garantindo operação adequada com base nos "
                "fundamentos básicos da eletricidade?"
                "</div>"
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa é a pergunta que orienta esta investigação. Respondê-la exigirá "
                "interpretar os dados técnicos do motor, analisar as relações entre "
                "potência, tensão e corrente elétrica, e avaliar como essas grandezas "
                "participam da definição das condições de alimentação do equipamento.\n\n"
                "Ao longo do estudo, essa pergunta servirá como referência para a "
                "organização dos dados, para a realização dos cálculos e para a "
                "construção de uma explicação tecnicamente coerente sobre o problema."
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
                "A alternativa correta identifica o foco real da investigação. O objetivo "
                "não é alterar o sistema hidráulico nem propor mudanças estruturais na instalação, "
                "mas compreender como deve ser analisada a alimentação elétrica do motor "
                "da motobomba.\n\n"
                "A pergunta norteadora organiza essa análise ao concentrar a atenção nas "
                "grandezas elétricas que caracterizam o problema, como potência, tensão, "
                "corrente e condições de alimentação. Dessa forma, ela transforma a situação "
                "real observada em um problema técnico investigável, permitindo que a análise "
                "seja conduzida de modo estruturado e fundamentado."
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