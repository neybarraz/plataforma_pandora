# apps/app_01/sections/problema/conteudos/conteudo_1_01.py
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
                "Em muitos equipamentos eletrônicos, quando a fonte principal de energia é "
                "desligada, o circuito simplesmente para de funcionar. Esse parece ser o comportamento "
                "mais esperado: sem fonte, não há funcionamento. No entanto, no sistema estudado "
                "nesta disciplina, ocorre algo que chama atenção logo no início da observação.\n\n"
                "Mesmo após a remoção da fonte externa, a placa de LED continua funcionando. "
                "Esse comportamento cria uma situação investigativa importante, porque indica que "
                "o circuito não depende apenas da energia presente no instante da alimentação. "
                "Há algum mecanismo interno permitindo que a energia continue sendo fornecida à carga."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esse sistema didático representa, em pequena escala, o funcionamento de um "
                "dispositivo de energia de reserva. O circuito é composto por uma bateria de "
                "telefone celular, um módulo de carregamento, um conversor de tensão e uma carga "
                "representada por uma placa de LED. Quando a fonte externa está conectada, o sistema "
                "carrega a bateria e alimenta o circuito. Quando a fonte é removida, a bateria passa "
                "a fornecer energia para manter o funcionamento da carga."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "É justamente esse comportamento que transforma o circuito em um problema físico "
                "interessante. Se a fonte foi retirada, por que o LED continua aceso? Responder "
                "a essa pergunta exige compreender o movimento de cargas elétricas, a diferença "
                "de potencial entre os componentes e a forma como a energia pode ser armazenada "
                "e depois transferida dentro do sistema."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=_iVj_x8wxkE",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "problema_01_001_q_0001",
            "pergunta": (
                "Se a fonte externa foi removida e o LED continua aceso, qual interpretação física "
                "é mais adequada para explicar esse comportamento?"
            ),
            "alternativas": {
                "a": "O LED produz energia suficiente para manter o circuito funcionando.",
                "b": "A bateria armazena energia elétrica e passa a fornecê-la ao circuito.",
                "c": "O conversor de tensão gera energia elétrica automaticamente.",
                "d": "A corrente elétrica desaparece temporariamente no circuito.",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A alternativa correta reconhece o papel da bateria como elemento de armazenamento "
                "de energia. Durante o funcionamento normal, a fonte externa fornece energia ao "
                "circuito e também carrega a bateria. Esse processo permite acumular energia no sistema.\n\n"
                "Quando a fonte é desligada, a bateria passa a atuar como fonte de energia, mantendo "
                "a circulação de corrente elétrica no circuito. Assim, o LED continua recebendo energia "
                "e permanece aceso. O que parecia contraditório no início passa a fazer sentido quando "
                "o sistema é interpretado como um arranjo capaz de armazenar e transferir energia entre "
                "seus componentes."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema didático analisado, a bateria Li-ion atua como o principal elemento "
                "de armazenamento de energia. O módulo de carregamento controla o processo de carga, "
                "enquanto o conversor de tensão ajusta a energia elétrica para que a carga funcione "
                "corretamente.\n\n"
                "Desse modo, o circuito deixa de ser apenas um conjunto de peças conectadas e passa "
                "a ser entendido como um sistema tecnológico em que corrente elétrica, diferença de "
                "potencial e armazenamento de energia explicam o funcionamento observado."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "problema_01_001_q_0002",
            "pergunta": (
                "Explique, com suas palavras, por que o fato de o LED continuar aceso após a remoção "
                "da fonte externa cria um problema físico interessante para investigar."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]