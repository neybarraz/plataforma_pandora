from __future__ import annotations
import streamlit as st


def _get_valor_limpo(qid: str) -> float | None:
    chave = f"problema_{qid}"
    valor_bruto = st.session_state.get(chave)

    if valor_bruto is None or str(valor_bruto).strip() in ["", "—", "None"]:
        return None

    try:
        return float(str(valor_bruto).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None


def _status_dado(qid: str, unidade: str = "") -> str:
    valor = _get_valor_limpo(qid)

    if valor is None:
        return '<span style="color:#dc2626;">✖ Não informado</span>'

    return f'<span style="color:#16a34a;">{valor} {unidade}</span>'


def get_blocos() -> list[dict]:
    return [

        # ========================================================
        {"tipo": "titulo", "texto": "1. Consolidação dos critérios de dimensionamento"},

        {"tipo": "texto", "texto": (
            "Nas etapas anteriores, o sistema foi analisado sob diferentes critérios técnicos, "
            "cada um avaliando um aspecto específico do comportamento da instalação elétrica. "
            "Esses critérios não são independentes. Todos eles devem ser atendidos simultaneamente "
            "para que a instalação seja considerada tecnicamente correta. "
            "Nesta etapa, o objetivo não é recalcular, mas consolidar os resultados obtidos "
            "e interpretar o sistema como um todo."
        )},

        {"tipo": "texto", "texto": (
            "Critérios avaliados:\n\n"

            f"- corrente de projeto: **{_status_dado('problema.01.002.0001', 'A')}**;\n"
            f"- corrente admissível: **{_status_dado('problema.01.003.0004', 'A')}**;\n"
            f"- queda de tensão percentual: **{_status_dado('problema.01.004.0007', '%')}**;\n"
            f"- desvio entre modelo e realidade: **{_status_dado('problema.01.006.0001', '%')}**."
        )},


        # ========================================================
        {"tipo": "titulo", "texto": "2. Princípio do critério mais restritivo"},

        {"tipo": "texto", "texto": (
            "O dimensionamento de condutores não é definido por um único critério isolado. "
            "Cada verificação impõe uma exigência mínima ao sistema. "
            "A condição final de projeto deve atender simultaneamente a todas essas exigências. "
            "Portanto, a seção do condutor deve ser definida pelo critério mais restritivo entre:\n\n"

            "- capacidade de condução de corrente (critério térmico);\n"
            "- limite de queda de tensão (critério de desempenho);\n"
            "- coerência com comportamento real (validação experimental).\n\n"

            "Isso significa que, mesmo que um critério seja atendido, a instalação será considerada inadequada "
            "se qualquer outro critério for violado."
        )},


        # ========================================================
        {"tipo": "titulo", "texto": "3. Interpretação integrada da instalação"},

        {"tipo": "texto", "texto": (
            "A análise técnica deve ser feita de forma integrada, considerando o comportamento físico, "
            "os limites normativos e os dados reais de operação.\n\n<br>"

            "Leitura técnica do sistema:\n\n"

            "- A corrente define o esforço elétrico imposto ao condutor;\n"
            "- A queda de tensão indica a qualidade do fornecimento de energia;\n"
            "- A verificação térmica garante a integridade da isolação ao longo do tempo;\n"
            "- A validação experimental confirma se o modelo representa a realidade.\n\n"

            "A decisão técnica resulta da coerência entre esses quatro aspectos."
        )},


        # ========================================================
        {"tipo": "titulo", "texto": "4. Critério decisório"},

        {"tipo": "texto", "texto": (
            "A instalação será considerada tecnicamente e normativamente adequada quando todas as condições abaixo forem atendidas:\n\n"

            "- I_projeto ≤ I_admissível (segurança térmica);\n"
            "- queda de tensão dentro do limite normativo;\n"
            "- desvio entre modelo e medição dentro de faixa aceitável.\n\n"

            "Caso qualquer uma dessas condições não seja atendida, a instalação deve ser considerada inadequada "
            "e necessita de intervenção técnica."
        )},


        # ========================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.007.0001",
            "pergunta": (
                "Se apenas um dos critérios (corrente, queda de tensão ou validação) não for atendido, "
                "qual deve ser a decisão técnica?"
            ),
            "alternativas": {
                "a": "A instalação pode ser considerada adequada",
                "b": "Apenas o critério mais importante deve ser considerado",
                "c": "A instalação deve ser considerada inadequada",
                "d": "O critério pode ser ignorado se o sistema estiver funcionando"
            },
            "alternativa_correta": "c",
        },


        {
            "tipo": "questao_texto",
            "id": "problema.01.007.0002",
            "pergunta": (
                "Com base nos critérios analisados, a instalação está tecnicamente e normativamente correta? "
                "Justifique sua resposta considerando todos os critérios avaliados."
            )
        },


        # ========================================================
        {"tipo": "titulo", "texto": "5. Entrega técnica: decisão final do projeto"},

        {"tipo": "texto", "texto": (
            "Síntese da análise:\n\n"

            f"- corrente de projeto: **{_status_dado('problema.01.002.0001', 'A')}**;\n"
            f"- corrente admissível: **{_status_dado('problema.01.003.0004', 'A')}**;\n"
            f"- queda de tensão: **{_status_dado('problema.01.004.0007', '%')}**;\n"
            f"- desvio modelo × campo: **{_status_dado('problema.01.006.0001', '%')}**.\n\n"

            "Conclusão técnica:\n\n"

            "- **A instalação atende aos critérios normativos:** quando todos os limites são respeitados;\n"
            "- **A instalação não atende:** quando qualquer critério é violado.\n\n"

            "Recomendação técnica:\n\n"

            "- Em caso de não conformidade, deve-se redimensionar o condutor ou revisar as condições de instalação;\n"
            "- Em caso de conformidade, a instalação pode ser considerada segura e adequada para operação contínua.\n\n"

            "Essa decisão representa a responsabilidade técnica sobre o sistema analisado."
        )},


        # ========================================================
        {"tipo": "subtitulo", "texto": "Fechamento da etapa"},

        {"tipo": "texto", "texto": (
            "A decisão técnica encerra o processo de dimensionamento.\n\n"

            "A partir deste ponto, não se trata mais de calcular, mas de concluir. "
            "Com base nos resultados obtidos nas etapas anteriores, você deve emitir um julgamento técnico objetivo "
            "sobre a condição da instalação.\n\n"

            "Isso implica responder, de forma inequívoca:\n\n"

            "- a instalação atende a todos os critérios normativos?\n"
            "- existe alguma condição de risco ou não conformidade?\n"
            "- é necessário redimensionamento ou intervenção?\n\n"

            "A decisão deve ser fundamentada nos dados analisados, sem suposições ou aproximações informais. "
            "Cada critério avaliado contribui para essa conclusão, e a não conformidade em qualquer um deles "
            "compromete a validade técnica da instalação.\n\n"

            "Neste momento, você assume o papel de responsável técnico, sendo capaz de interpretar os resultados "
            "e emitir uma conclusão clara, justificável e tecnicamente defensável."
        )}

    ]