# apps/app_01/sections/problema/conteudos/conteudo_3_01.py
from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Pergunta norteadora",
        },
        {
            "tipo": "texto",
            "texto": (
                "Após a análise do sistema e a definição do foco da investigação, é necessário "
                "formular a pergunta que orientará todo o estudo. A pergunta norteadora funciona "
                "como o eixo central da investigação: ela organiza a observação do sistema, "
                "orienta a coleta de dados e direciona a interpretação dos fenômenos físicos "
                "presentes no circuito.\n\n"
                "No caso do sistema didático de energia de reserva, a simples observação do "
                "funcionamento do circuito não é suficiente. O fato de a carga continuar "
                "funcionando quando a fonte externa é removida indica que existem processos "
                "físicos responsáveis por armazenar, transformar e transferir energia "
                "dentro do sistema."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Para compreender esse comportamento, é necessário analisar o circuito à luz "
                "dos conceitos de eletromagnetismo. Corrente elétrica, diferença de potencial, "
                "campos elétricos, campos magnéticos e processos de indução eletromagnética "
                "participam do funcionamento do sistema.\n\n"
                "Esses fenômenos estão presentes em diferentes componentes do circuito, como "
                "a bateria, o módulo de carregamento, o conversor de tensão e os elementos "
                "internos do conversor, como indutores e capacitores."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "<div style='padding:14px; border-radius:8px; "
                "border-left:6px solid #14B8A6; margin:12px 0;'>"
                "<strong>Pergunta norteadora:</strong><br><br>"
                "Como os fenômenos do eletromagnetismo explicam o funcionamento de um sistema "
                "didático de energia de reserva baseado em bateria, carregador e conversor "
                "de tensão?"
                "</div>"
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Essa é a pergunta que orienta esta investigação. Respondê-la exigirá observar "
                "o comportamento do circuito, interpretar as medições elétricas realizadas no "
                "sistema e relacionar esses resultados com os conceitos fundamentais do "
                "eletromagnetismo."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_016",
            "pergunta": (
                "Qual é a principal função da pergunta norteadora em uma investigação científica?"
            ),
            "alternativas": {
                "a": "Substituir a necessidade de observação do sistema",
                "b": "Organizar e orientar o processo de investigação do fenômeno",
                "c": "Definir automaticamente a solução final do problema",
                "d": "Eliminar a necessidade de análise conceitual",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A pergunta norteadora tem a função de organizar o processo de investigação. "
                "Ela define qual fenômeno deve ser compreendido e orienta a coleta e a "
                "interpretação das evidências observadas no sistema.\n\n"
                "No caso deste estudo, a pergunta conecta o funcionamento do circuito "
                "com os conceitos de eletromagnetismo. A análise da corrente elétrica, "
                "da diferença de potencial, do armazenamento de energia na bateria e "
                "da atuação do indutor e dos capacitores no conversor permite construir "
                "uma explicação física coerente para o funcionamento do sistema de "
                "energia de reserva."
            ),
        },
        {
            "tipo": "questao_texto",
            "id": "q_017",
            "pergunta": (
                "Explique, com suas palavras, como os conceitos de corrente elétrica, "
                "diferença de potencial e armazenamento de energia podem ajudar a "
                "explicar o funcionamento do sistema didático de energia de reserva."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]