# apps/app_01/sections/problema/conteudos/conteudo_4_02.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Processos elétricos e magnéticos",
        },
        {
            "tipo": "texto",
            "texto": (
                "Depois de identificar as entradas do sistema, é necessário compreender quais "
                "processos físicos explicam como a energia elétrica é armazenada, transformada "
                "e transferida no circuito. Esses processos constituem o núcleo do modelo "
                "sistêmico do problema.\n\n"
                "No sistema analisado, destacam-se a circulação de corrente elétrica, a "
                "diferença de potencial entre os componentes, o armazenamento de energia "
                "na bateria, o campo magnético no indutor do conversor e o campo elétrico "
                "associado aos capacitores."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Corrente elétrica no circuito",
        },
        {
            "tipo": "texto",
            "texto": (
                "A corrente elétrica corresponde ao movimento organizado de cargas elétricas "
                "ao longo dos condutores do circuito. É ela que transporta energia entre a "
                "fonte, o carregador, a bateria, o conversor e a carga.\n\n"
                "Sem corrente elétrica, a energia não poderia circular pelo sistema. Por isso, "
                "a análise do funcionamento do circuito começa pela compreensão de como as "
                "cargas se deslocam e alimentam os diferentes componentes."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_022",
            "pergunta": (
                "Qual fenômeno físico permite o transporte de energia ao longo dos condutores do circuito?"
            ),
            "alternativas": {
                "a": "Corrente elétrica",
                "b": "Radiação térmica",
                "c": "Pressão elétrica",
                "d": "Massa magnética",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "titulo",
            "texto": "Diferença de potencial e armazenamento na bateria",
        },
        {
            "tipo": "texto",
            "texto": (
                "A corrente elétrica só pode existir quando há diferença de potencial entre "
                "dois pontos do circuito. Essa diferença organiza o movimento das cargas e "
                "estabelece as condições para a transferência de energia.\n\n"
                "No sistema estudado, a bateria atua como elemento de armazenamento. Enquanto "
                "a fonte externa está disponível, a energia elétrica é transferida para a "
                "bateria. Depois, essa energia pode ser liberada para manter a carga funcionando "
                "quando a fonte principal é removida."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Campo magnético no indutor",
        },
        {
            "tipo": "texto",
            "texto": (
                "No conversor de tensão, o indutor desempenha papel importante no controle "
                "da corrente e da transferência de energia. Quando a corrente elétrica passa "
                "por ele, forma-se um campo magnético ao redor do enrolamento.\n\n"
                "Esse comportamento pode ser interpretado com base na Lei de Ampère, que "
                "descreve a relação entre corrente elétrica e geração de campo magnético. "
                "Assim, o indutor mostra que o funcionamento do conversor depende diretamente "
                "de fenômenos magnéticos."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_023",
            "pergunta": (
                "Qual conceito físico ajuda a explicar a formação de campo magnético no indutor?"
            ),
            "alternativas": {
                "a": "Lei de Ampère",
                "b": "Lei da Gravitação",
                "c": "Reflexão da luz",
                "d": "Pressão atmosférica",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "titulo",
            "texto": "Campo elétrico nos capacitores e indução no conversor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Os capacitores presentes no conversor participam do armazenamento temporário "
                "de energia elétrica, associado à formação de campo elétrico entre suas placas. "
                "Esse processo contribui para suavizar a tensão de saída e estabilizar o "
                "funcionamento da carga.\n\n"
                "Além disso, as variações de corrente no indutor estão associadas a efeitos "
                "de indução eletromagnética, interpretados pela Lei de Faraday. Isso mostra "
                "que o conversor não atua apenas como um regulador eletrônico, mas como um "
                "dispositivo cujo funcionamento depende da interação entre campos elétricos "
                "e magnéticos."
            ),
        },
        {
            "tipo": "simulador_conversor",
            "id": "sim_conv_001",
            "titulo": "Simulador didático do conversor",
            "descricao": (
                "Explore como a corrente no indutor, o campo magnético, a carga no capacitor "
                "e a tensão de saída variam quando os parâmetros do conversor são modificados. "
                "Use o simulador para visualizar processos que não podem ser observados "
                "diretamente no circuito real."
            ),
            "arquivo": "simulador_conversor_didatico.py",
            # "pergunta_guiada": (
            #     "Ao alterar a tensão da bateria, a indutância e a capacitância, o que muda "
            #     "na estabilidade da saída e por que isso acontece fisicamente?"
            # ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_024",
            "pergunta": (
                "Qual é o papel físico dos capacitores no conversor de tensão?"
            ),
            "alternativas": {
                "a": "Armazenar temporariamente energia associada a campo elétrico",
                "b": "Produzir corrente sem diferença de potencial",
                "c": "Substituir a bateria como fonte principal",
                "d": "Eliminar o indutor do circuito",
            },
            "alternativa_correta": "a",
        },
        {
            "tipo": "texto",
            "texto": (
                "Os processos analisados mostram que o sistema funciona por meio da ação "
                "coordenada de diferentes fenômenos físicos. Corrente elétrica, diferença "
                "de potencial, armazenamento de energia, campo magnético e campo elétrico "
                "atuam de forma integrada no circuito. É essa articulação que torna possível "
                "carregar a bateria, regular a tensão e manter a carga em funcionamento."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_025",
            "pergunta": (
                "Explique, com suas palavras, como corrente elétrica, bateria, indutor e "
                "capacitores participam juntos do funcionamento do sistema de energia de reserva."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]