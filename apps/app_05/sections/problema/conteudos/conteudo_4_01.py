# apps/app_01/sections/problema/conteudos/conteudo_4_01.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Entradas do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para compreender o funcionamento do sistema didático de energia de reserva, "
                "é necessário identificar quais grandezas entram no sistema e alimentam seu "
                "comportamento elétrico. Essas grandezas são chamadas de entradas do sistema, "
                "pois representam as condições que permitem o carregamento da bateria e o "
                "funcionamento do circuito.\n\n"
                "Neste estudo, as entradas principais são a tensão fornecida pela fonte externa "
                "e a corrente elétrica disponibilizada por essa fonte. Essas grandezas definem "
                "como a energia elétrica chega ao circuito e em que condições ela pode ser "
                "armazenada e posteriormente utilizada."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Tensão da fonte externa",
        },
        {
            "tipo": "texto",
            "texto": (
                "A tensão da fonte externa é uma das entradas fundamentais do sistema. "
                "Ela estabelece a diferença de potencial necessária para que as cargas elétricas "
                "se movimentem no circuito e para que a bateria possa ser carregada.\n\n"
                "No sistema analisado, a fonte externa fornece energia elétrica ao módulo "
                "de carregamento, que controla a forma como essa energia é transferida para "
                "a bateria e para o restante do circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_018",
            "pergunta": (
                "Qual é o papel da tensão da fonte externa no sistema de energia de reserva?"
            ),
            "alternativas": {
                "a": "Substituir completamente a bateria",
                "b": "Fornecer a diferença de potencial necessária para alimentar e carregar o circuito",
                "c": "Eliminar a necessidade de corrente elétrica",
                "d": "Atuar apenas como suporte mecânico para os módulos",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "titulo",
            "texto": "Corrente fornecida pela fonte",
        },
        {
            "tipo": "texto",
            "texto": (
                "Além da tensão, a corrente fornecida pela fonte externa também é uma entrada "
                "importante do sistema. A corrente representa o fluxo de cargas elétricas que "
                "pode ser disponibilizado para o carregamento da bateria e para a alimentação "
                "dos componentes do circuito.\n\n"
                "Sem corrente elétrica, não há transferência efetiva de energia no sistema. "
                "Por isso, tensão e corrente devem ser analisadas em conjunto como condições "
                "de entrada do circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_019",
            "pergunta": (
                "Por que a corrente fornecida pela fonte externa é importante para o sistema?"
            ),
            "alternativas": {
                "a": "Porque representa o fluxo de cargas que transporta energia no circuito",
                "b": "Porque substitui o papel do conversor de tensão",
                "c": "Porque impede o armazenamento de energia na bateria",
                "d": "Porque elimina a diferença de potencial no circuito",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "titulo",
            "texto": "Dentro e fora do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao estruturar o problema como um sistema analisável, é necessário definir "
                "suas fronteiras. Dentro do sistema estão a bateria, o módulo de carregamento, "
                "o conversor de tensão, a carga LED e o fluxo de corrente elétrica entre "
                "esses componentes.\n\n"
                "Fora do sistema permanecem a rede elétrica externa e os detalhes internos "
                "mais complexos dos circuitos integrados. Essa delimitação permite concentrar "
                "a análise nas entradas, nos processos e nas saídas mais relevantes para a "
                "interpretação física do circuito."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_020",
            "pergunta": (
                "Qual conjunto representa corretamente os elementos considerados dentro do sistema?"
            ),
            "alternativas": {
                "a": "Rede elétrica externa e projeto industrial completo",
                "b": "Bateria, módulo de carregamento, conversor, carga LED e corrente no circuito",
                "c": "Apenas o LED e a carcaça do dispositivo",
                "d": "Somente os circuitos internos detalhados dos componentes integrados",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "As entradas do sistema — tensão e corrente fornecidas pela fonte externa — "
                "são as condições iniciais que permitem o funcionamento do circuito. Ao definir "
                "essas entradas e estabelecer as fronteiras do sistema, torna-se possível "
                "analisar de forma organizada como a energia elétrica entra, é processada e "
                "depois entregue à carga."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_021",
            "pergunta": (
                "Explique, com suas palavras, por que a tensão e a corrente da fonte externa "
                "podem ser tratadas como entradas do sistema de energia de reserva."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]