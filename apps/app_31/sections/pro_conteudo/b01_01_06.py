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
        {"tipo": "titulo", "texto": "1. Validação experimental do modelo"},

        {"tipo": "texto", "texto": (
            "Nas etapas anteriores, foi construído um modelo técnico do sistema elétrico, "
            "com base em dados nominais, parâmetros do circuito e critérios normativos. "
            "Esse modelo permitiu estimar a corrente de operação, a queda de tensão e a condição térmica do condutor. "
            "Entretanto, um modelo só é tecnicamente válido quando representa o comportamento real do sistema. "
            "Por isso, esta etapa tem como objetivo verificar se os valores calculados são coerentes com os valores medidos em campo.\n\n<br> "

            "Pergunta central da etapa:\n\n"
            "**O comportamento real do sistema confirma o modelo teórico construído?**"
        )},


        # ========================================================
        {"tipo": "titulo", "texto": "2. Organização dos dados para comparação"},

        {"tipo": "texto", "texto": (
            "Para validar o modelo, é necessário comparar diretamente os valores calculados com os valores medidos. "
            "Essa comparação deve ser feita de forma estruturada, utilizando as mesmas grandezas físicas.\n\n <br>"

            "Grandezas analisadas:\n\n"
            f"- corrente calculada (modelo): **{_status_dado('problema.01.002.0001', 'A')}**;\n"
            f"- corrente medida (campo): **{_status_dado('problema.01.001.0009', 'A')}**;\n"
            f"- tensão nominal: **{_status_dado('problema.01.001.0002', 'V')}**;\n"
            f"- tensão medida nos terminais: **{_status_dado('problema.01.001.0008', 'V')}**."
        )},


        # ========================================================
        {"tipo": "titulo", "texto": "3. Cálculo do desvio percentual"},

        {"tipo": "texto", "texto": (
            "A validação não é feita apenas por comparação visual. "
            "É necessário quantificar a diferença entre o modelo e a realidade. "
            "O desvio percentual permite medir o erro relativo entre o valor calculado e o valor medido."
        )},

        {"tipo": "equacao", "latex": r"\text{D\%} = \frac{|I_{medido} - I_{calculado}|}{I_{calculado}} \cdot 100\%"},

        {"tipo": "texto", "texto": (
            "Calcule o desvio percentual para a corrente do sistema:"
        )},

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.006.0001",
            "rotulo": "Desvio percentual da corrente",
            "unidade": "%"
        },


        # ========================================================
        {"tipo": "titulo", "texto": "4. Interpretação técnica do desvio"},

        {"tipo": "texto", "texto": (
            "O desvio percentual indica o nível de aderência entre o modelo teórico e o comportamento real do sistema.\n\n<br>"

            "Interpretação técnica:\n\n"

            "- Desvios pequenos indicam que o modelo representa adequadamente a realidade;\n"
            "- Desvios moderados indicam que existem simplificações ou incertezas no modelo;\n"
            "- Desvios elevados indicam inconsistência entre o modelo e o sistema real.\n\n"

            "Causas possíveis de desvio:\n\n"

            "- variação da carga mecânica do motor;\n"
            "- tensão de alimentação diferente da nominal;\n"
            "- erros de medição;\n"
            "- simplificações adotadas no modelo;\n"
            "- condições reais diferentes das assumidas no projeto."
        )},


        # ========================================================
        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.006.0002",
            "pergunta": (
                "Se o desvio entre o valor calculado e o valor medido for elevado, qual é a interpretação mais adequada?"
            ),
            "alternativas": {
                "a": "O modelo está correto e a medição está errada",
                "b": "O modelo precisa ser revisado ou as condições reais não foram corretamente consideradas",
                "c": "O desvio não tem importância técnica",
                "d": "O sistema está necessariamente em falha"
            },
            "alternativa_correta": "b",
        },


        {
            "tipo": "questao_texto",
            "id": "problema.01.006.0003",
            "pergunta": (
                "Considerando o desvio obtido, o modelo pode ser considerado representativo do sistema real? "
                "Justifique tecnicamente sua resposta."
            )
        },


        # ========================================================
        {"tipo": "titulo", "texto": "5. Entrega técnica: validação do modelo"},

        {"tipo": "texto", "texto": (
            "Resumo da análise:\n\n"

            f"- corrente calculada: **{_status_dado('problema.01.002.0001', 'A')}**;\n"
            f"- corrente medida: **{_status_dado('problema.01.001.0009', 'A')}**;\n"
            f"- desvio percentual: **{_status_dado('problema.01.006.0001', '%')}**.\n\n"

            "- **Conclusão técnica:** se o desvio estiver dentro de uma faixa aceitável, o modelo pode ser considerado válido para representar o sistema. "
            "Caso contrário, é necessário revisar as hipóteses adotadas, os dados coletados ou as condições reais de operação."
        )},


        # ========================================================
        {"tipo": "subtitulo", "texto": "Fechamento da etapa"},

        {"tipo": "texto", "texto": (
            "A validação experimental encerra o ciclo de modelagem, conectando cálculo e realidade. "
            "Com isso, o projeto deixa de ser apenas uma estimativa teórica e passa a ter base técnica comprovada. "
            "Na próxima etapa, essa análise será consolidada em uma decisão técnica final, considerando todos os critérios avaliados."
        )}

    ]