# apps/app_01/sections/problema/conteudos/conteudo_2_01.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Tensão central do sistema",
        },
        {
            "tipo": "texto",
            "texto": (
                "A tensão central deste problema está na necessidade de compreender como um "
                "sistema eletrônico relativamente simples consegue continuar alimentando uma "
                "carga mesmo quando a fonte principal de energia é interrompida. Em situações "
                "cotidianas, espera-se que um dispositivo pare de funcionar quando a fonte "
                "de alimentação é desligada.\n\n"
                "No entanto, no sistema didático analisado, observa-se que a carga representada "
                "pela placa de LED permanece em funcionamento mesmo após a retirada da fonte "
                "externa. Esse comportamento indica que existe um mecanismo interno capaz "
                "de armazenar energia e reorganizar sua distribuição no circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa situação revela a tensão central do problema: explicar como fenômenos "
                "do eletromagnetismo — como corrente elétrica, diferença de potencial, "
                "armazenamento de energia e interação entre campos elétricos e magnéticos — "
                "permitem que o circuito mantenha a operação da carga.\n\n"
                "Assim, o desafio da investigação não está apenas em observar o funcionamento "
                "do sistema, mas em compreender quais processos físicos tornam possível essa "
                "continuidade de operação."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_011",
            "pergunta": (
                "Qual situação representa melhor a tensão central do sistema de energia de reserva?"
            ),
            "alternativas": {
                "a": "O LED funciona apenas quando a fonte externa está conectada",
                "b": "O circuito continua alimentando a carga mesmo após a retirada da fonte principal",
                "c": "A bateria funciona apenas como suporte estrutural do circuito",
                "d": "O conversor de tensão elimina completamente a corrente elétrica",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A tensão central está associada ao fato de que o sistema mantém o funcionamento "
                "da carga mesmo sem a fonte principal de energia. Esse comportamento indica que "
                "o circuito não depende apenas da energia fornecida no instante de operação, "
                "mas também da energia previamente armazenada.\n\n"
                "A bateria, o módulo de carregamento e o conversor de tensão formam um conjunto "
                "capaz de organizar a transferência de energia no circuito. Entender como essa "
                "organização ocorre é o núcleo investigativo do problema."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_012",
            "pergunta": (
                "Explique, com suas palavras, por que o fato de a carga continuar funcionando "
                "sem a fonte principal pode ser considerado a tensão central deste problema."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]