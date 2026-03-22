# apps/app_01/sections/problema/conteudos/conteudo_1_04.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Componentes do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para compreender o funcionamento de um sistema de energia de reserva, é necessário "
                "identificar os componentes que o formam e reconhecer que cada um participa de uma "
                "etapa do processo de armazenamento, controle ou fornecimento de energia. No sistema "
                "didático estudado, a bateria, o módulo de carregamento, o conversor de tensão e a "
                "placa de LED compõem um arranjo funcional integrado.\n\n"
                "Embora o circuito pareça simples, ele reúne componentes com funções distintas. "
                "A bateria armazena energia, o TP4056 controla seu carregamento, o LM2596 regula "
                "a tensão de saída e o LED atua como carga. A interpretação física do sistema "
                "depende de entender como esses elementos interagem."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além dos módulos visíveis, o conversor de tensão contém elementos internos como "
                "indutor, diodo e capacitores. Esses componentes são relevantes porque permitem "
                "discutir fenômenos que não são imediatamente perceptíveis, como formação de campo "
                "magnético, armazenamento temporário de energia e suavização da tensão de saída.\n\n"
                "Assim, a caracterização dos componentes não é apenas uma descrição técnica do "
                "circuito, mas uma etapa essencial para compreender quais conceitos físicos serão "
                "necessários para explicar seu comportamento."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=md-ooet0rHs",
        },

        # {
        #     "tipo": "imagem",
        #     "arquivo": "componentes_sistema_01.png",
        #     "caption": (
        #         "Principais componentes do sistema didático: bateria, módulo TP4056, conversor "
        #         "LM2596 e carga LED."
        #     ),
        # },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_006",
            "pergunta": (
                "Qual componente está mais diretamente associado ao armazenamento principal "
                "de energia no sistema estudado?"
            ),
            "alternativas": {
                "a": "Placa de LED",
                "b": "Bateria Li-ion",
                "c": "Conector USB",
                "d": "Diodo do conversor",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A bateria Li-ion é o principal elemento de armazenamento de energia do sistema. "
                "Ela permite acumular energia enquanto a fonte externa está disponível e, depois, "
                "fornecê-la ao circuito quando necessário. Os demais componentes também são "
                "importantes, mas cumprem outras funções: o TP4056 controla a carga da bateria, "
                "o LM2596 ajusta a tensão e a placa de LED consome a energia entregue à carga.\n\n"
                "Reconhecer o papel de cada componente é essencial porque a explicação física do "
                "sistema depende justamente da articulação dessas funções. O circuito só opera "
                "como energia de reserva porque armazenamento, controle e fornecimento de energia "
                "ocorrem de forma coordenada."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_007",
            "pergunta": (
                "Explique, com suas palavras, por que identificar o papel de cada componente "
                "é importante para compreender o funcionamento físico do sistema de energia de reserva."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]