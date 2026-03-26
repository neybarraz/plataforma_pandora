from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Foco de análise física",
        },
        {
            "tipo": "texto",
            "texto": (
                "Depois de reconhecer a tensão central do problema, é preciso definir com mais "
                "clareza o que será observado no sistema. Nesta etapa, o foco da análise será "
                "construído de forma progressiva, começando pelos fenômenos mais visíveis no "
                "funcionamento do circuito e avançando, depois, para interpretações mais profundas.\n\n"
                "Primeiro, será necessário compreender como a energia elétrica circula no sistema. "
                "Depois, será possível entender como alguns componentes controlam essa circulação "
                "e armazenam energia de maneira temporária."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Movimento de cargas elétricas",
        },
        {
            "tipo": "texto",
            "texto": (
                "O ponto de partida da análise é o movimento de cargas elétricas ao longo dos "
                "condutores. Esse movimento constitui a corrente elétrica, responsável por transportar "
                "energia entre a fonte, a bateria, o conversor e a carga.\n\n"
                "Sem corrente elétrica, não há funcionamento do circuito. Por isso, compreender "
                "como essa corrente circula é a forma mais simples e direta de começar a interpretar "
                "o sistema."
            ),
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "q_013",
            "pergunta": (
                "Qual fenômeno físico descreve o movimento organizado de cargas elétricas em um circuito?"
            ),
            "alternativas": {
                "a": "Radiação térmica",
                "b": "Corrente elétrica",
                "c": "Pressão atmosférica",
                "d": "Gravidade elétrica",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "titulo",
            "texto": "Diferença de potencial no circuito",
        },
        {
            "tipo": "texto",
            "texto": (
                "A corrente elétrica não aparece de forma espontânea. Para que as cargas se movimentem, "
                "é necessário existir uma diferença de potencial entre dois pontos do circuito.\n\n"
                "No sistema analisado, essa diferença de potencial cria as condições para que a energia "
                "elétrica seja transferida e para que a carga receba alimentação. Assim, antes de falar "
                "de conversão e controle, é importante entender que o funcionamento básico do circuito "
                "depende da existência de tensão elétrica entre seus componentes."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Armazenamento de energia no sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Outro aspecto central da análise é o armazenamento de energia. O comportamento observado "
                "no sistema — especialmente o fato de o LED continuar funcionando após a retirada da fonte — "
                "mostra que a energia não está apenas circulando: ela também está sendo armazenada.\n\n"
                "Nesse nível inicial de análise, a bateria aparece como o principal elemento de armazenamento. "
                "Ela acumula energia enquanto a fonte externa está disponível e depois a fornece ao circuito "
                "quando necessário. Esse é o ponto mais importante para compreender, de forma simples, por que "
                "o sistema atua como energia de reserva."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Controle da energia no conversor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Depois de compreender corrente elétrica, diferença de potencial e armazenamento de energia, "
                "torna-se possível avançar para um nível mais profundo da análise. O conversor de tensão não "
                "apenas conduz energia: ele também controla a forma como essa energia é entregue à carga.\n\n"
                "Para isso, o circuito utiliza componentes como indutor e capacitores. Esses componentes "
                "permitem introduzir ideias mais abstratas, como campo magnético e campo elétrico, mas agora "
                "essas ideias aparecem conectadas a uma função concreta do sistema: regular tensão e estabilizar "
                "o funcionamento da carga."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Campos elétricos e magnéticos no sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "Em um nível mais avançado de interpretação, o foco da análise inclui os campos associados "
                "a alguns componentes do conversor. Quando a corrente passa pelo indutor, forma-se um campo "
                "magnético. Nos capacitores, a energia pode ser associada à formação de campo elétrico.\n\n"
                "Esses fenômenos mostram que o funcionamento do sistema depende não apenas de corrente e tensão, "
                "mas também da interação entre efeitos elétricos e magnéticos. Essa etapa aprofunda a análise, "
                "mas sem perder de vista o comportamento concreto do circuito."
            ),
        },
    ]