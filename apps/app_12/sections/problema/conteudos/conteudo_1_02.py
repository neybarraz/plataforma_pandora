# apps/app_01/sections/problema/conteudos/conteudo_1_02.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "O que é energia de reserva?",
        },
        {
            "tipo": "texto",
            "texto": (
                "Em sistemas eletrônicos, a energia de reserva corresponde à capacidade de manter "
                "uma carga em funcionamento quando a fonte principal deixa de fornecer energia. "
                "Esse tipo de arranjo é comum em dispositivos que não podem ser desligados "
                "imediatamente, como sistemas de segurança, roteadores, equipamentos médicos e "
                "no-breaks.\n\n"
                "No sistema estudado, essa ideia aparece de forma simplificada: a bateria armazena "
                "energia enquanto a fonte externa está disponível e, quando essa fonte é removida, "
                "passa a alimentar o circuito. Assim, o sistema não depende apenas da presença "
                "instantânea de energia, mas também da possibilidade de armazená-la e utilizá-la "
                "posteriormente."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=_m0YqcfwpE0",
            "caption": "Um exemplo desse tipo de sistema é o NOBREAK, um dispositivo que fornece energia de emergência quando ocorre uma falha na rede elétrica. Utilizando uma bateria interna, ele mantém os equipamentos funcionando por um curto período após a interrupção da fonte principal.",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_003",
            "pergunta": (
                "Do ponto de vista físico, quando se pode afirmar que um sistema atua como "
                "energia de reserva?"
            ),
            "alternativas": {
                "a": "Quando o circuito funciona apenas enquanto a fonte externa está ligada",
                "b": "Quando o sistema consegue armazenar energia e fornecê-la à carga na ausência da fonte principal",
                "c": "Quando a tensão do circuito é sempre igual à tensão da bateria",
                "d": "Quando o LED acende independentemente da existência de corrente elétrica",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A energia de reserva depende de dois processos físicos articulados: armazenamento "
                "de energia e posterior fornecimento dessa energia à carga. No sistema didático, "
                "a bateria é o elemento que permite essa continuidade de funcionamento. Enquanto a "
                "fonte externa está presente, parte da energia é utilizada para alimentar o circuito "
                "e parte é armazenada na bateria.\n\n"
                "Quando a fonte é retirada, a bateria assume o papel de fonte de energia, permitindo "
                "que a corrente continue circulando. Isso mostra que a função de reserva não está "
                "ligada apenas ao componente em si, mas à organização do sistema como um todo. "
                "O carregador, a bateria e o conversor de tensão formam um arranjo que garante "
                "continuidade de alimentação e estabilidade de operação da carga."
            ),
        },
    ]