# apps/app_01/sections/problema/conteudos/conteudo_1_03.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Objetivo da investigação",
        },
        {
            "tipo": "texto",
            "texto": (
                "O objetivo desta investigação é compreender como um sistema didático de energia "
                "de reserva consegue manter uma carga alimentada mesmo quando a fonte externa é "
                "interrompida. Para isso, o circuito será analisado como um sistema eletromagnético "
                "no qual diferentes componentes desempenham funções específicas no armazenamento, "
                "controle e transferência de energia.\n\n"
                "A investigação não se limita a observar se o LED permanece aceso. O foco está em "
                "entender quais fenômenos físicos tornam esse comportamento possível e como bateria, "
                "carregador, conversor e carga se relacionam durante a operação do sistema."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesse contexto, será necessário interpretar o papel da diferença de potencial no "
                "movimento de cargas elétricas, a função da bateria como elemento de armazenamento "
                "de energia e a atuação do conversor de tensão como dispositivo que reorganiza a "
                "energia elétrica para adequá-la à carga.\n\n"
                "Ao final, pretende-se construir uma explicação física coerente para o funcionamento "
                "do sistema, relacionando corrente elétrica, tensão, campo magnético no indutor e "
                "armazenamento de energia nos elementos do circuito."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=lHxoOfbIXZM",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_004",
            "pergunta": (
                "Qual é o objetivo principal da investigação proposta para o sistema didático "
                "de energia de reserva?"
            ),
            "alternativas": {
                "a": "Verificar apenas se o LED acende quando conectado ao circuito",
                "b": "Compreender como os fenômenos físicos explicam o armazenamento e a transferência de energia no sistema",
                "c": "Analisar somente o formato da placa eletrônica e dos conectores",
                "d": "Medir apenas a corrente da bateria sem interpretar o circuito como sistema",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Investigar esse sistema significa ir além da observação do funcionamento aparente. "
                "O LED aceso é apenas um efeito visível de processos físicos internos que envolvem "
                "movimento de cargas, diferença de potencial, armazenamento de energia e regulação "
                "de tensão. Por isso, o objetivo da análise é compreender o circuito como um sistema "
                "organizado e não apenas como um conjunto de peças conectadas.\n\n"
                "Essa abordagem permite interpretar cada componente em função de seu papel físico. "
                "A bateria armazena energia, o módulo de carregamento controla a reposição dessa "
                "energia e o conversor ajusta a forma como ela é entregue à carga. A investigação, "
                "portanto, busca explicar tecnicamente o comportamento do sistema com base em "
                "conceitos de eletromagnetismo."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_005",
            "pergunta": (
                "Explique, com suas palavras, por que investigar esse sistema exige mais do que "
                "apenas observar o LED aceso, envolvendo também a análise dos fenômenos físicos "
                "que ocorrem no circuito."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]