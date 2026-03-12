# apps/app_01/sections/problema/conteudos/conteudo_2_03.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Delimitação do escopo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após definir o foco da investigação, é necessário estabelecer também os limites "
                "do estudo. A delimitação do escopo indica quais aspectos do sistema serão "
                "analisados e quais permanecerão fora da investigação.\n\n"
                "Essa etapa é importante porque permite concentrar a análise nos fenômenos "
                "físicos essenciais para compreender o funcionamento do sistema de energia "
                "de reserva."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Neste estudo, o circuito será analisado principalmente do ponto de vista "
                "conceitual, buscando interpretar como corrente elétrica, diferença de potencial "
                "e campos eletromagnéticos participam do funcionamento do sistema.\n\n"
                "A investigação incluirá observações do comportamento do circuito e medições "
                "elétricas básicas, como tensão em diferentes pontos do sistema."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Por outro lado, alguns aspectos permanecerão fora da análise. O estudo não "
                "abordará o funcionamento detalhado dos circuitos internos dos componentes "
                "integrados, como o CI do conversor LM2596, nem realizará dimensionamentos "
                "eletrônicos completos ou análises de eficiência energética avançada.\n\n"
                "Essa delimitação permite tratar o sistema como um objeto de estudo para "
                "compreender conceitos fundamentais de eletromagnetismo aplicados a uma "
                "tecnologia real."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_014",
            "pergunta": (
                "Por que é importante delimitar o escopo da investigação do sistema?"
            ),
            "alternativas": {
                "a": "Para analisar todos os fenômenos possíveis sem organização",
                "b": "Para concentrar o estudo nos aspectos físicos mais relevantes",
                "c": "Para eliminar completamente as medições experimentais",
                "d": "Para substituir o circuito real por modelos teóricos complexos",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "Delimitar o escopo permite transformar um sistema tecnológico complexo em "
                "um problema investigável. Ao concentrar a análise nos fenômenos físicos "
                "mais relevantes — como corrente elétrica, diferença de potencial e interação "
                "entre campos elétricos e magnéticos — torna-se possível construir uma "
                "interpretação clara do funcionamento do circuito."
            ),
        },

        {
            "tipo": "questao_texto",
            "id": "q_015",
            "pergunta": (
                "Explique, com suas palavras, por que a investigação do sistema foi limitada "
                "à análise conceitual dos fenômenos eletromagnéticos e não ao projeto eletrônico completo."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]