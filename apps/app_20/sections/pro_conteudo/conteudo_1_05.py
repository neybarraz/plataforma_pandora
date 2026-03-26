# apps/app_05/sections/problema/conteudos/conteudo_1_05.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Parâmetros e funcionamento observado",
        },
        {
            "tipo": "texto",
            "texto": (
                "As características observáveis do sistema de energia de reserva incluem a tensão "
                "nominal da bateria, a tensão fornecida pela fonte externa, a tensão de saída do "
                "conversor e o comportamento da carga durante a operação. Esses parâmetros ajudam "
                "a descrever o circuito em funcionamento e a identificar como a energia circula "
                "entre os componentes.\n\n"
                "No sistema estudado, a bateria opera em torno de 3,7 V, enquanto a carga LED "
                "é alimentada em aproximadamente 5 V por meio do conversor de tensão. Isso mostra "
                "que o circuito não apenas transfere energia, mas também modifica a forma como "
                "essa energia é entregue à carga."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Outro aspecto importante é o comportamento do sistema em dois estados distintos: "
                "com a fonte externa conectada e com a fonte removida. Em um caso, a bateria pode "
                "estar sendo carregada e o circuito alimentado ao mesmo tempo. No outro, a bateria "
                "assume a função de fonte de energia. Observar essa transição é fundamental para "
                "interpretar o sistema como uma tecnologia de reserva e não apenas como um circuito "
                "alimentado diretamente por uma fonte."
            ),
        },
        {
            "tipo": "simulacao_estado",
            "id": "sim_001",
            "titulo": "Simulação simples — estados de funcionamento do sistema",
            "descricao": (
                "Altere o estado da fonte e observe como o fluxo de energia no sistema muda. "
                "Compare o papel da fonte externa, da bateria e da carga em cada situação."
            ),
            "estado_inicial": "fonte_conectada",
            "estados": {
                "fonte_conectada": {
                    "titulo": "Fonte externa conectada",
                    "resumo": (
                        "A fonte externa fornece energia ao circuito. Nesse estado, a bateria pode "
                        "ser carregada enquanto a carga continua alimentada."
                    ),
                    "fluxos": [
                        "Fonte externa → módulo de carregamento",
                        "Módulo de carregamento → bateria",
                        "Fonte externa / sistema → conversor de tensão",
                        "Conversor de tensão → LED",
                    ],
                    "observacoes": [
                        "A bateria recebe energia",
                        "O LED permanece ligado",
                        "Há alimentação e carregamento simultâneos",
                    ],
                    "indicadores": {
                        "fonte": "ativa",
                        "bateria": "carregando",
                        "conversor": "regulando saída",
                        "led": "ligado",
                    },
                },
                "fonte_removida": {
                    "titulo": "Fonte externa removida",
                    "resumo": (
                        "A fonte externa deixa de fornecer energia. Nesse estado, a bateria assume "
                        "a alimentação do sistema e mantém a carga em funcionamento."
                    ),
                    "fluxos": [
                        "Bateria → conversor de tensão",
                        "Conversor de tensão → LED",
                    ],
                    "observacoes": [
                        "A bateria fornece energia ao circuito",
                        "O LED permanece ligado",
                        "O sistema atua como energia de reserva",
                    ],
                    "indicadores": {
                        "fonte": "inativa",
                        "bateria": "fornecendo energia",
                        "conversor": "regulando saída",
                        "led": "ligado",
                    },
                },
            },
            "pergunta_guiada": (
                "O que muda no caminho da energia quando a fonte externa é removida?"
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "im_05_01.png",
            "caption": (
                "Exemplo de pontos de observação de tensão e estados de funcionamento do sistema "
                "com fonte externa presente ou ausente."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_008",
            "pergunta": (
                "Por que é importante observar o sistema com a fonte externa ligada e também "
                "desligada?"
            ),
            "alternativas": {
                "a": "Porque a bateria só existe fisicamente quando a fonte está desligada",
                "b": "Porque o LED só pode funcionar em um dos dois estados",
                "c": "Porque a comparação entre os estados permite entender quando a bateria carrega e quando passa a alimentar a carga",
                "d": "Porque o conversor deixa de existir quando a fonte é conectada",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "texto",
            "texto": (
                "A comparação entre os dois estados de operação é decisiva para entender a função "
                "do sistema. Quando a fonte externa está ligada, existe energia disponível para "
                "carregar a bateria e alimentar o circuito. Quando a fonte é removida, a bateria "
                "assume o fornecimento de energia e mantém a carga em funcionamento.\n\n"
                "Essa mudança de condição mostra que o sistema não depende exclusivamente da fonte "
                "externa no instante de uso. Ele foi organizado para armazenar energia previamente "
                "e utilizá-la depois, característica central de um sistema de reserva. Observar "
                "tensão, corrente e comportamento da carga nesses dois estados permite transformar "
                "uma simples percepção de funcionamento em uma análise física estruturada."
            ),
        },
    ]