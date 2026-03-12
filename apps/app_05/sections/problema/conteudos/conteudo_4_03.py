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
            "id": "q_026",
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
            "tipo": "questao_multipla_escolha",
            "id": "q_027",
            "pergunta": (
                "Qual é a função física principal da bateria no sistema analisado?"
            ),
            "alternativas": {
                "a": "Gerar luz diretamente para o LED",
                "b": "Armazenar energia que poderá ser usada posteriormente pelo circuito",
                "c": "Substituir o papel do indutor",
                "d": "Eliminar a diferença de potencial no sistema",
            },
            "alternativa_correta": "b",
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
            "id": "q_028",
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
            "tipo": "questao_multipla_escolha",
            "id": "q_029",
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
            "tipo": "titulo",
            "texto": "Visualização dinâmica do conversor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Para compreender melhor esses processos, é útil observar uma representação "
                "visual do funcionamento do conversor. Nessa visualização, a corrente no "
                "indutor varia ao longo do tempo, o campo magnético associado cresce e diminui, "
                "e os capacitores participam da estabilização da tensão de saída.\n\n"
                "Essa representação ajuda a perceber que o conversor não apenas altera o valor "
                "da tensão. Ele realiza essa função por meio de processos físicos associados "
                "à circulação de corrente, à formação de campos e ao armazenamento temporário "
                "de energia."
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "im_05_02.png",
            "caption": (
                "Representação do conversor DC-DC mostrando a circulação de corrente, "
                "o campo magnético no indutor e o campo elétrico no capacitor."
            ),
        },
        {
            "tipo": "titulo",
            "texto": "Corrente no indutor e tensão de saída",
        },
        {
            "tipo": "texto",
            "texto": (
                "Outra forma de compreender o funcionamento do conversor é observar como "
                "algumas grandezas elétricas variam ao longo do tempo. No gráfico a seguir "
                "aparecem dois comportamentos importantes.\n\n"
                "Na parte superior observa-se a corrente no indutor. Ela cresce e diminui "
                "continuamente, formando uma variação aproximadamente triangular. Esse "
                "comportamento indica que o indutor está alternadamente armazenando e "
                "liberando energia.\n\n"
                "Na parte inferior aparece a tensão de saída do conversor. Mesmo que a "
                "tensão da bateria seja menor, o processo de armazenamento e liberação "
                "de energia no indutor permite que o circuito mantenha uma tensão "
                "estável na carga, próxima de 5 V."
            ),
        },
        {
            "tipo": "imagem",
            "arquivo": "im_05_03.png",
            "caption": (
                "Variação da corrente no indutor ao longo do tempo (gráfico superior) e "
                "tensão estabilizada na saída do conversor (gráfico inferior). O processo "
                "de armazenamento e liberação de energia no indutor permite manter a "
                "tensão de saída próxima de 5 V mesmo quando a tensão da bateria é menor."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_030",
            "pergunta": (
                "O que a variação triangular da corrente no indutor indica sobre o funcionamento do conversor?"
            ),
            "alternativas": {
                "a": "Que não existe armazenamento de energia no circuito",
                "b": "Que o indutor alterna entre armazenar e liberar energia elétrica",
                "c": "Que a corrente elétrica desaparece no conversor",
                "d": "Que a bateria fornece sempre a mesma corrente ao circuito",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "Quando o aluno observa a variação da corrente no indutor e a atuação dos "
                "capacitores, torna-se mais fácil relacionar o comportamento do circuito "
                "com os conceitos de eletromagnetismo. O indutor evidencia a ligação entre "
                "corrente elétrica e campo magnético, enquanto os capacitores mostram como "
                "a energia elétrica pode ser armazenada temporariamente em campo elétrico.\n\n"
                "Assim, processos que normalmente não são visíveis em um circuito eletrônico "
                "tornam-se interpretáveis por meio de representações gráficas."
            ),
        },
    ]