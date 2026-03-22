# apps/app_01/sections/problema/conteudos/conteudo_1_06.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Instrumentos de medição",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para investigar o funcionamento do sistema didático de energia de reserva, é "
                "necessário utilizar instrumentos capazes de registrar grandezas elétricas em "
                "diferentes pontos do circuito. Nesse estudo, o multímetro digital tem papel "
                "central, pois permite medir tensão e corrente e comparar o comportamento dos "
                "componentes em diferentes condições de operação.\n\n"
                "A medição não deve se limitar a um único ponto do circuito. É importante observar "
                "a tensão na bateria, a tensão de saída do conversor e, quando possível, a corrente "
                "associada ao funcionamento da carga. Essas medições ajudam a interpretar como a "
                "energia é armazenada, transformada e entregue ao LED."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Além do valor medido, o momento da coleta também é relevante. As medições devem "
                "ser realizadas em estados bem definidos do sistema: com a fonte externa conectada, "
                "durante o processo de carga, e após a remoção da fonte, quando a bateria assume "
                "a alimentação da carga. Comparar esses estados permite relacionar os dados "
                "experimentais com a pergunta central da investigação.\n\n"
                "Assim, o sistema de medição não serve apenas para obter números, mas para revelar "
                "como o circuito responde a diferentes condições de funcionamento."
            ),
        },
        # {
        #     "tipo": "imagem",
        #     "arquivo": "medicao_sistema_01.png",
        #     "caption": (
        #         "Exemplo de medição de tensão em diferentes pontos do sistema didático de energia "
        #         "de reserva com auxílio de multímetro digital."
        #     ),
        # },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=1WIWrmc-rBk",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_009",
            "pergunta": (
                "Qual é a principal finalidade das medições elétricas realizadas no sistema "
                "didático de energia de reserva?"
            ),
            "alternativas": {
                "a": "Medir apenas a aparência física dos componentes",
                "b": "Comparar tensão e corrente em diferentes pontos e estados de operação do circuito",
                "c": "Substituir o funcionamento real do sistema por valores teóricos fixos",
                "d": "Eliminar a necessidade de interpretar conceitos físicos",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A principal função das medições elétricas é fornecer evidências do comportamento "
                "real do circuito. Ao medir a tensão da bateria, por exemplo, é possível observar "
                "a condição de armazenamento de energia. Ao medir a saída do conversor, torna-se "
                "possível verificar como a tensão é regulada para alimentar a carga.\n\n"
                "Quando essas medições são comparadas em diferentes estados do sistema, a análise "
                "ganha sentido físico. Os valores obtidos deixam de ser apenas dados isolados e "
                "passam a indicar como a energia circula, onde ela é armazenada e de que forma o "
                "circuito mantém a carga operando. Assim, medir é também interpretar o sistema."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_010",
            "pergunta": (
                "Explique, com suas palavras, por que medir tensão e corrente em diferentes pontos "
                "do circuito ajuda a compreender o funcionamento físico do sistema de energia de reserva."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]