from __future__ import annotations
import streamlit as st
from typing import Dict, Optional, Tuple

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










def calcular_diagnosticos_sala() -> Dict[str, Dict[str, Optional[float]]]:
    """
    Calcula as médias das temperaturas e ΔT para todas as paredes da sala.
    
    Retorna um dicionário com a estrutura:
    {
        "norte": {
            "T_parede_medio": float or None,
            "T_ar_medio": float or None,
            "delta_T": float or None,
            "T_parede_N1": float or None,
            "T_parede_N2": float or None,
            "T_ar_NO": float or None,
            "T_ar_NE": float or None
        },
        "sul": {...},
        "leste": {...},
        "oeste": {...}
    }
    """
    
    # Mapeamento dos IDs para cada parede
    paredes_config = {
        "norte": {
            "parede_1": "problema.01.001.1007",  # N1
            "parede_2": "problema.01.001.1008",  # N2
            "ar_1": "problema.01.001.1002",      # NO
            "ar_2": "problema.01.001.1003"       # NE
        },
        "sul": {
            "parede_1": "problema.01.001.1011",  # S1
            "parede_2": "problema.01.001.1012",  # S2
            "ar_1": "problema.01.001.1004",      # SO
            "ar_2": "problema.01.001.1005"       # SE
        },
        "leste": {
            "parede_1": "problema.01.001.1009",  # L1
            "parede_2": "problema.01.001.1010",  # L2
            "ar_1": "problema.01.001.1003",      # NE
            "ar_2": "problema.01.001.1005"       # SE
        },
        "oeste": {
            "parede_1": "problema.01.001.1013",  # O1
            "parede_2": "problema.01.001.1014",  # O2
            "ar_1": "problema.01.001.1002",      # NO
            "ar_2": "problema.01.001.1004"       # SO
        }
    }
    
    resultados = {}
    
    for parede, ids in paredes_config.items():
        # Obter valores brutos
        T_parede_1 = _get_valor_limpo(ids["parede_1"])
        T_parede_2 = _get_valor_limpo(ids["parede_2"])
        T_ar_1 = _get_valor_limpo(ids["ar_1"])
        T_ar_2 = _get_valor_limpo(ids["ar_2"])
        
        # Calcular médias
        if T_parede_1 is not None and T_parede_2 is not None:
            T_parede_medio = (T_parede_1 + T_parede_2) / 2
        else:
            T_parede_medio = None
        
        if T_ar_1 is not None and T_ar_2 is not None:
            T_ar_medio = (T_ar_1 + T_ar_2) / 2
        else:
            T_ar_medio = None
        
        # Calcular ΔT
        if T_parede_medio is not None and T_ar_medio is not None:
            delta_T = T_parede_medio - T_ar_medio
        else:
            delta_T = None
        
        # Armazenar resultados
        resultados[parede] = {
            "T_parede_1": T_parede_1,
            "T_parede_2": T_parede_2,
            "T_ar_1": T_ar_1,
            "T_ar_2": T_ar_2,
            "T_parede_medio": T_parede_medio,
            "T_ar_medio": T_ar_medio,
            "delta_T": delta_T
        }
    
    return resultados


def get_blocos() -> list[dict]:
    # Chamar a função uma vez no início da seção
    diagnosticos = calcular_diagnosticos_sala()

    # Exemplo para parede Norte
    norte = diagnosticos["norte"]
    sul = diagnosticos["sul"]
    leste = diagnosticos["leste"]
    oeste = diagnosticos["oeste"]
    return [
# ========================================================
# 1. Calor: energia em trânsito
# ========================================================
        {"tipo": "titulo", "texto": "1. Calor: energia em trânsito"},

        {"tipo": "texto", "texto": (
            "Na etapa anterior, vimos que a temperatura do ar não é suficiente para descrever o comportamento térmico do ambiente. "
            "Precisamos agora analisar não apenas o estado térmico, mas o processo de troca de energia.\n\n<br>"
            "Introduz-se o conceito de calor: energia em trânsito, sempre associada a uma diferença de temperatura. "
            "Diferente da temperatura, que é uma propriedade do sistema, o calor não é armazenado. "
            "Ele representa a transferência de energia entre regiões com diferentes níveis térmicos."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0001",
            "pergunta": "Do ponto de vista termodinâmico, o calor pode ser definido como:",
            "alternativas": {
                "a": "Uma propriedade armazenada no sistema.",
                "b": "A energia total contida em um corpo.",
                "c": "Energia em trânsito devido a uma diferença de temperatura.",
                "d": "Uma forma de temperatura elevada."
            },
            "alternativa_correta": "c"
        },

# ========================================================
# 2. Os três mecanismos fundamentais
# ========================================================
        {"tipo": "titulo", "texto": "2. Os três mecanismos fundamentais"},

        {"tipo": "texto", "texto": (
            "A transferência de calor ocorre por três mecanismos fundamentais:\n\n"
            "- Condução: transferência através de um meio material sem transporte macroscópico de massa.\n"
            "- Convecção: transferência associada ao movimento de um fluido.\n"
            "- Radiação: transferência por emissão de ondas eletromagnéticas, mesmo no vácuo.\n\n"
            "Em sistemas reais, esses mecanismos atuam simultaneamente, mas um deles geralmente predomina em cada região."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0002",
            "pergunta": "Qual mecanismo de transferência de calor pode ocorrer mesmo na ausência total de meio material?",
            "alternativas": {
                "a": "Condução",
                "b": "Convecção",
                "c": "Radiação",
                "d": "Nenhum deles"
            },
            "alternativa_correta": "c"
        },
# ========================================================
# 3. Condução: fluxo por gradiente térmico (Lei de Fourier)
# ========================================================
        {"tipo": "titulo", "texto": "3. Condução: fluxo por gradiente térmico (Lei de Fourier)"},

        {"tipo": "texto", "texto": (
            "Na condução térmica, o calor se propaga devido ao gradiente de temperatura dentro de um material. "
            "Para uma parede plana em regime estacionário, a taxa de transferência de calor é dada por:"
        )},
        {"tipo": "equacao", "latex": r"q = -k \cdot A \cdot \frac{dT}{dx}"},
        {"tipo": "texto", "texto": (
            "onde: k é a condutividade térmica do material; A é a área de transferência; e dT/dx é o gradiente de temperatura. "
            "O sinal negativo indica que o fluxo ocorre no sentido de temperaturas decrescentes."
        )},

       {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0003",
            "pergunta": "Na Lei de Fourier, o que representa a condutividade térmica (k)?",
            "alternativas": {
                "a": "A capacidade do material de armazenar calor.",
                "b": "A resistência elétrica do material.",
                "c": "A capacidade do material de conduzir calor.",
                "d": "A variação de temperatura do sistema."
            },
            "alternativa_correta": "c"
        },
        {"tipo": "subtitulo", "texto": "Conexão com a sala"},

        {"tipo": "texto", "texto": (
            "Na sala analisada, a temperatura da parede Sul e a temperatura do ar no ponto SO podem ser comparadas. "
            "Se houver diferença significativa, há um gradiente térmico. "
            "Nesse caso, a condução entre a parede e o ar adjacente contribui para o desconforto térmico próximo à parede Sul. "
            f"Vamos calcular a taxa de transferência de calor por condução através da parede Sul da sala.\n\n<br>"
            f"**Dados disponíveis:**\n"
            f"- Temperatura da face interna da parede Sul (S1): {_get_valor_limpo('problema.01.001.1011') or '50'} °C \n"
            f"- Temperatura do ar interno (ponto SO): {_get_valor_limpo('problema.01.001.1004') or '24'} °C \n"
            f"- Condutividade térmica da parede (tijolo): 1,2 W/(m·K)\n"
            f"- Largura da parede Sul: {_get_valor_limpo('problema.01.001.0102') or '8,0'} m\n"
            f"- Altura da parede Sul: {_get_valor_limpo('problema.01.001.0103') or '2,7'} m\n"
            f"- Espessura da parede: 0,15 m (valor típico)\n\n"
            "**Passo 1:** Calcule a área da parede Sul (largura × altura)."
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.002.0004", "rotulo": "Área da parede Sul", "unidade": "m²"},

        {"tipo": "texto", "texto": (
            "\n\n**Passo 2:** Aplique a Lei de Fourier para encontrar a potência térmica (taxa de transferência de calor):"
        )},

        {"tipo": "equacao", "latex": r"q = -k \cdot A \cdot \frac{dT}{dx}"},

        {"tipo": "texto", "texto": (
            "O gradiente dT/dx pode ser aproximado por (T_ar - T_parede) / L, onde L é a espessura da parede.\n\n<br>"
            "O sinal indica a direção do fluxo:\n"
            "- Se T_parede > T_ar → dT/dx < 0 → calor flui da parede para o ar;\n"
            "- Se T_parede < T_ar → dT/dx > 0 → calor flui do ar para a parede;\n"
            "- Se T_parede ≈ T_ar → dT/dx ≈ 0 → condução desprezível."
        )},

        {"tipo": "equacao", "latex": r"\frac{dT}{dx} \approx \frac{T_{ar} - T_{parede}}{L}"},

        {"tipo": "texto", "texto": (
            "\n\n**Passo 3:** Substitua os valores na equação e calcule q (em watts). "
            "O resultado representa a potência térmica total transferida através de toda a parede."
        )},

        {"tipo": "entrada_numerica_inline", "id": "problema.01.002.0005", "rotulo": "Potência térmica (condução)", "unidade": "W"},

        {"tipo": "texto", "texto": (
            "\n\n**Interpretação:** \n\n"
            "- se o valor calculado for positivo, o calor está entrando na sala através da parede;\n "
            "- se o valor calculado for negativo, está saindo.\n\n "
            "Quanto maior o valor absoluto, maior o impacto da parede no desconforto térmico."
        )},

 


# ========================================================
# 4. Convecção: fluxo entre superfície e fluido (Lei de Newton)
# ========================================================
        {"tipo": "titulo", "texto": "4. Convecção: fluxo entre superfície e fluido (Lei de Newton)"},
        {"tipo": "texto", "texto": (
            "Na convecção, o calor é transferido entre uma superfície sólida (como uma parede) e um fluido em movimento (como o ar da sala). "
            "Diferente da condução, que ocorre dentro de um material, a convecção envolve o transporte de energia pelo movimento do fluido. "
            "A taxa de transferência de calor por convecção é modelada pela Lei de Newton:"
        )},
        {"tipo": "equacao", "latex": r"q = h \cdot A \cdot (T_s - T_\infty)"},

        {"tipo": "texto", "texto": (
            "onde:\n\n"
            "- q: taxa de transferência de calor (W);\n"
            "- h: coeficiente convectivo (W/(m²·K)); <br> Depende das condições de escoamento, geometria e propriedades do fluido\n"
            "- A: área de contato entre a superfície e o fluido (m²);\n"
            "- T_s: temperatura da superfície (°C ou K);\n"
            "- T_∞: temperatura do fluido longe da superfície (°C ou K)."
        )},

        {"tipo": "subtitulo", "texto": "Conexão com a sala"},
        {"tipo": "texto", "texto": (
            f"Na sala analisada, a convecção ocorre entre as paredes e o ar interno. "
            f"Considere a parede Sul com temperatura T_s = {_get_valor_limpo('problema.01.001.1011') or '50'} °C e "
            f"o ar interno a T_∞ = {_get_valor_limpo('problema.01.001.1004') or '24'} °C (ponto SO). "
            "A diferença de temperatura (T_s - T_∞) é o potencial motriz para a convecção. "
            "Quanto maior essa diferença, maior a taxa de transferência de calor.\n\n<br>"
            "O coeficiente convectivo h depende de fatores como:\n"
            "- Velocidade do ar (ar parado vs. ar em movimento);\n"
            "- Posição da superfície (parede vertical, horizontal, etc.);\n"
            "- Propriedades do ar (viscosidade, condutividade térmica).\n\n"
            "Na sala real, a circulação de ar causada por pessoas, aberturas ou sistemas de ventilação afeta h e, consequentemente, o desconforto térmico."
        )},

        {"tipo": "simulador_conveccao"},
        {"tipo": "texto", "texto": (
            "A ventilação não atua diretamente como mecanismo de aquecimento ou resfriamento. "
            "Ela aumenta o coeficiente convectivo (h) e, com isso, intensifica a troca de energia "
            "entre a superfície e o ar.\n\n<br>"

            "O efeito térmico depende do sinal da diferença de temperatura (ΔT = T_s - T_ar):\n\n"
            "- Se ΔT > 0 (superfície mais quente que o ar): calor flui da parede para o ar → o ambiente é aquecido.\n"
            "- Se ΔT < 0 (superfície mais fria que o ar): calor flui do ar para a parede → o ambiente é resfriado.\n\n"

            "Ao aumentar a ventilação, o valor de |q| aumenta, ou seja, a troca de calor se intensifica, "
            "mas o sentido do fluxo não muda. "
            "Portanto, a ventilação amplifica o processo térmico já existente: "
           "ela pode tanto melhorar quanto piorar o conforto térmico, dependendo das condições do ambiente."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0006",
            "pergunta": ("Em uma sala com parede quente (T_s > T_ar), o que acontece com o conforto térmico se a ventilação for aumentada?"),
            "alternativas": {
                "a": "Melhora, pois a ventilação resfria o ambiente diretamente.",
                "b": "Piora, pois a ventilação aumenta a transferência de calor da parede para o ar.",
                "c": "Não se altera, pois a ventilação não afeta a diferença de temperatura.",
                "d": "Melhora se a ventilação for natural, piora se for forçada."
            },
            "alternativa_correta": "b"
        },
        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0007",
            "pergunta": ("Duas salas idênticas têm a mesma diferença de temperatura entre a parede Sul e o ar (ΔT = 26°C). Na Sala A, o ar está parado (h = 5 W/m²·K). "
            "Na Sala B, há um ventilador (h = 25 W/m²·K). Comparando a taxa de transferência de calor por convecção:"),
            "alternativas": {
                "a": "É igual nas duas salas.",
                "b": "Na Sala B é 5 vezes maior.",
                "c": "Na Sala B é 20 vezes maior.",
                "d": "Na Sala B é 25 vezes maior."
            },
            "alternativa_correta": "b"
        },
# ========================================================
# 5. Radiação: fluxo por ondas eletromagnéticas (Stefan-Boltzmann)
# ========================================================
        {"tipo": "titulo", "texto": "5. Radiação: fluxo por ondas eletromagnéticas (Stefan-Boltzmann)"},
        {"tipo": "texto", "texto": (
            "Diferente da condução e da convecção, a radiação térmica não precisa de um meio material para se propagar. "
            "Ela ocorre pela emissão de ondas eletromagnéticas, podendo transferir calor mesmo no vácuo. "
            "Por isso, por exemplo, sentimos o calor do Sol mesmo através do espaço. "
            "Para superfícies opacas e cinzentas, a taxa de transferência de calor por radiação é estimada por:"
        )},

        {"tipo": "equacao", "latex": r"q = \varepsilon \cdot \sigma \cdot A \cdot (T_s^4 - T_{\infty}^4)"},

        {"tipo": "texto", "texto": (
            "Onde:\n\n"
            "- q: taxa de transferência de calor por radiação (W);\n"
            "- ε: emissividade da superfície (adimensional, entre 0 e 1);\n"
            "- σ: constante de Stefan-Boltzmann (≈ 5,67 × 10⁻⁸ W/m²·K⁴);\n"
            "- A: área da superfície (m²);\n"
            "- T_s: temperatura absoluta da superfície (K);\n"
            "- T_∞: temperatura absoluta do ambiente ao redor (K).\n\n"
            "A presença da quarta potência (T⁴) significa que a radiação se torna cada vez mais relevante em temperaturas elevadas, "
            "podendo superar a convecção em superfícies muito quentes."
        )},

        {"tipo": "subtitulo", "texto": "Conexão com a sala"},

                {"tipo": "simulador_radiacao"},

        {"tipo": "texto", "texto": (
                "\n\n**Interpretação:**\n\n"
                "- Quando a parede está **mais quente que o corpo**, você ganha calor por radiação (sensação de calor).\n"
                "- Quando a parede está **mais fria que o corpo**, você perde calor para a parede (sensação de frio).\n"
                "- A **temperatura do ar** não influencia diretamente a radiação — apenas a convecção.\n\n"
                "Por isso, a sensação térmica não depende apenas da temperatura do ar. Uma parede fria pode causar frio mesmo em um ambiente com ar quente, e uma parede quente pode causar calor mesmo com ar frio."
        )},

        {"tipo": "questao_multipla_escolha", "id": "problema.01.002.0008",
            "pergunta": "Uma parede de uma sala está a 47°C (320 K) e o corpo humano a 34°C (307 K). A emissividade efetiva do sistema parede-corpo é ε = 0,95. Se a temperatura da parede aumentar para 67°C (340 K), o que ocorre com a taxa de transferência de calor por radiação entre a parede e o corpo?",
            "alternativas": {
                "a": "Aumenta cerca de 20%, pois a diferença de temperatura aumentou 20°C.",
                "b": "Aumenta cerca de 70%, pois a radiação depende linearmente da temperatura.",
                "c": "Aumenta cerca de 130%, pois a radiação é proporcional a T⁴.",
                "d": "Permanece a mesma, pois a temperatura do corpo não mudou."
            },
            "alternativa_correta": "c"
        },



# ========================================================
# 6. Aplicação: diagnóstico dos fluxos na sala
# ========================================================
        {"tipo": "titulo", "texto": "6. Aplicação: diagnóstico dos fluxos na sala"},
        {"tipo": "texto", "texto": (
            "Agora que conhecemos os três mecanismos de transferência de calor, vamos aplicá-los ao diagnóstico da sala analisada. "
            "Cada superfície e região da sala pode ser dominada por um mecanismo diferente, dependendo das condições de contorno."
        )},

        {"tipo": "subtitulo", "texto": "Procedimento de análise"},
        {"tipo": "texto", "texto": (
            "Para diagnosticar os fluxos de calor na sala, siga estas etapas:\n\n"
            "1. **Identifique as superfícies críticas:** Compare a temperatura de cada parede (Sul, Norte, Leste, Oeste) com a temperatura do ar interno.\n"
            "2. **Calcule a diferença:** ΔT = T_parede - T_ar para cada superfície.\n"
            "3. **Classifique o sinal:**\n"
            "   - Se ΔT > 0 → a parede está mais quente que o ar\n"
            "   - Se ΔT < 0 → a parede está mais fria que o ar\n"
            "   - Se ΔT ≈ 0 → fluxos desprezíveis\n"
            "4. **Quanto maior |ΔT|, maior a intensidade da troca térmica.**"
        )},

        {"tipo": "subtitulo", "texto": "Análise por mecanismo"},
        {"tipo": "texto", "texto": (
            "Para cada superfície identificada, os mecanismos atuam da seguinte forma:\n\n<br>"
            "**Convecção:** Ocorre entre a superfície e o ar adjacente. O fluxo é dado por q = h·A·ΔT.\n"
            "   - Se ΔT > 0: calor flui da parede para o ar (ambiente aquecido).\n"
            "   - Se ΔT < 0: calor flui do ar para a parede (ambiente resfriado).\n\n"
            "**Radiação:** Ocorre entre a superfície e os ocupantes. Depende de T⁴ e da emissividade.\n"
            "   - Se T_parede > T_corpo: parede aquece o ocupante.\n"
            "   - Se T_parede < T_corpo: ocupante perde calor para a parede.\n\n"
            "**Condução:** Transferência de calor através da espessura da parede (do exterior para o interior ou vice-versa).\n\n"
            "O desconforto térmico próximo a uma parede é causado pela **combinação** da radiação direta e da convecção do ar adjacente."
        )},

        {"tipo": "subtitulo", "texto": "Interpretação conforme o caso"},
        {"tipo": "texto", "texto": (
            "A partir dos seus dados, analise:\n\n"
            "- **Parede(s) com maior ΔT positivo:** Provocam aquecimento local por convecção e radiação.\n"
            "- **Parede(s) com maior ΔT negativo:** Provocam resfriamento local (sensação de frio radiante).\n"
            "- **Paredes com ΔT próximo de zero:** Impacto térmico desprezível.\n\n"
            "A parede crítica é aquela com o maior valor absoluto de ΔT, pois será a principal responsável pelo desconforto térmico localizado."
        )},

        {"tipo": "subtitulo", "texto": "Janelas e superfícies envidraçadas"},
        {"tipo": "texto", "texto": (
            "Caso a sala possua janelas, considere mecanismos adicionais:\n\n"
            "- **Radiação solar direta:** Pode ser o mecanismo dominante em fachadas ensolaradas.\n"
            "- **Condução através do vidro:** Geralmente menor resistência térmica que a parede.\n"
            "- **Convecção na superfície do vidro:** Pode estar fria (inverno) ou quente (verão)."
        )},

        {"tipo": "subtitulo", "texto": "Consolidação"},

# ========================================================
# Parede Norte
# ========================================================
{"tipo": "texto", "texto": (
    f"""
| Norte | Ponto 1 (°C) | Ponto 2 (°C) | Média (°C) |
|--------|---------------|---------------|-------------|
| Parede  | {norte['T_parede_1'] if norte['T_parede_1'] is not None else '--'} | {norte['T_parede_2'] if norte['T_parede_2'] is not None else '--'} | {f"{norte['T_parede_medio']:.1f}" if norte['T_parede_medio'] is not None else '--'} |
| Ar | {norte['T_ar_1'] if norte['T_ar_1'] is not None else '--'} | {norte['T_ar_2'] if norte['T_ar_2'] is not None else '--'} | {f"{norte['T_ar_medio']:.1f}" if norte['T_ar_medio'] is not None else '--'} |

**ΔT = {f"{norte['delta_T']:.1f}" if norte['delta_T'] is not None else '--'} °C** (parede - ar)
<br>"""
)},

{"tipo": "questao_multipla_escolha", "id": "problema.01.002.0009",
    "pergunta": "Com base no ΔT calculado para a parede Norte, qual é o mecanismo predominante e seu efeito no conforto térmico?",
    "alternativas": {
        "a": "Condução apenas — sem efeito no conforto.",
        "b": "Convecção e radiação — a parede aquece o ambiente (sensação de calor).",
        "c": "Convecção e radiação — a parede resfria o ambiente (sensação de frio).",
        "d": "Radiação solar direta — ganho de calor intenso."
    },
    "alternativa_correta": "depende_do_ΔT"
},

# ========================================================
# Parede Sul
# ========================================================
{"tipo": "texto", "texto": (
    f"""
| Sul | Ponto 1 (°C) | Ponto 2 (°C) | Média (°C) |
|--------|---------------|---------------|-------------|
| Parede  | {sul['T_parede_1'] if sul['T_parede_1'] is not None else '--'} | {sul['T_parede_2'] if sul['T_parede_2'] is not None else '--'} | {f"{sul['T_parede_medio']:.1f}" if sul['T_parede_medio'] is not None else '--'} |
| Ar | {sul['T_ar_1'] if sul['T_ar_1'] is not None else '--'} | {sul['T_ar_2'] if sul['T_ar_2'] is not None else '--'} | {f"{sul['T_ar_medio']:.1f}" if sul['T_ar_medio'] is not None else '--'} |

**ΔT = {f"{sul['delta_T']:.1f}" if sul['delta_T'] is not None else '--'} °C** (parede - ar)
<br>"""
)},

{"tipo": "questao_multipla_escolha", "id": "problema.01.002.0010",
    "pergunta": "Com base no ΔT calculado para a parede Sul, qual é o mecanismo predominante e seu efeito no conforto térmico?",
    "alternativas": {
        "a": "Condução apenas — sem efeito no conforto.",
        "b": "Convecção e radiação — a parede aquece o ambiente (sensação de calor).",
        "c": "Convecção e radiação — a parede resfria o ambiente (sensação de frio).",
        "d": "Radiação solar direta — ganho de calor intenso."
    },
    "alternativa_correta": "depende_do_ΔT"
},

# ========================================================
# Parede Leste
# ========================================================
{"tipo": "texto", "texto": (
    f"""
| Leste | Ponto 1 (°C) | Ponto 2 (°C) | Média (°C) |
|--------|---------------|---------------|-------------|
| Parede  | {leste['T_parede_1'] if leste['T_parede_1'] is not None else '--'} | {leste['T_parede_2'] if leste['T_parede_2'] is not None else '--'} | {f"{leste['T_parede_medio']:.1f}" if leste['T_parede_medio'] is not None else '--'} |
| Ar | {leste['T_ar_1'] if leste['T_ar_1'] is not None else '--'} | {leste['T_ar_2'] if leste['T_ar_2'] is not None else '--'} | {f"{leste['T_ar_medio']:.1f}" if leste['T_ar_medio'] is not None else '--'} |

**ΔT = {f"{leste['delta_T']:.1f}" if leste['delta_T'] is not None else '--'} °C** (parede - ar)
<br>"""
)},

{"tipo": "questao_multipla_escolha", "id": "problema.01.002.0011",
    "pergunta": "Com base no ΔT calculado para a parede Leste, qual é o mecanismo predominante e seu efeito no conforto térmico?",
    "alternativas": {
        "a": "Condução apenas — sem efeito no conforto.",
        "b": "Convecção e radiação — a parede aquece o ambiente (sensação de calor).",
        "c": "Convecção e radiação — a parede resfria o ambiente (sensação de frio).",
        "d": "Radiação solar direta — ganho de calor intenso."
    },
    "alternativa_correta": "depende_do_ΔT"
},

# ========================================================
# Parede Oeste
# ========================================================
{"tipo": "texto", "texto": (
    f"""
| Oeste | Ponto 1 (°C) | Ponto 2 (°C) | Média (°C) |
|--------|---------------|---------------|-------------|
| Parede  | {oeste['T_parede_1'] if oeste['T_parede_1'] is not None else '--'} | {oeste['T_parede_2'] if oeste['T_parede_2'] is not None else '--'} | {f"{oeste['T_parede_medio']:.1f}" if oeste['T_parede_medio'] is not None else '--'} |
| Ar | {oeste['T_ar_1'] if oeste['T_ar_1'] is not None else '--'} | {oeste['T_ar_2'] if oeste['T_ar_2'] is not None else '--'} | {f"{oeste['T_ar_medio']:.1f}" if oeste['T_ar_medio'] is not None else '--'} |

**ΔT = {f"{oeste['delta_T']:.1f}" if oeste['delta_T'] is not None else '--'} °C** (parede - ar)
<br>"""
)},

{"tipo": "questao_multipla_escolha", "id": "problema.01.002.0012",
    "pergunta": "Com base no ΔT calculado para a parede Oeste, qual é o mecanismo predominante e seu efeito no conforto térmico?",
    "alternativas": {
        "a": "Condução apenas — sem efeito no conforto.",
        "b": "Convecção e radiação — a parede aquece o ambiente (sensação de calor).",
        "c": "Convecção e radiação — a parede resfria o ambiente (sensação de frio).",
        "d": "Radiação solar direta — ganho de calor intenso."
    },
    "alternativa_correta": "depende_do_ΔT"
},

{"tipo": "texto", "texto": (
    "O desconforto térmico não depende apenas da temperatura do ar, mas da combinação "
    "desses mecanismos atuando simultaneamente. A parede com maior |ΔT| será a principal fonte de desconforto localizado."
)},

# ========================================================
# 7. Mini-entrega: mapa dos fluxos de calor
# ========================================================
{"tipo": "titulo", "texto": "7. Mini-entrega: mapa dos fluxos de calor"},
{"tipo": "texto", "texto": (
    "\n\nNesta etapa, você deve construir um **esquema físico da sala** representando os fluxos de calor identificados.\n\n"
    "**Instruções para a mini-entrega:**\n\n"
    "1. Desenhe (ou descreva detalhadamente) a planta baixa ou um corte esquemático da sala, indicando as quatro orientações (Norte, Sul, Leste, Oeste).\n\n"
    "2. Identifique e destaque as seguintes superfícies:\n"
    "   - Todas as paredes (Norte, Sul, Leste, Oeste)\n"
    "   - Piso e teto\n"
    "   - Janelas (se houver na sala analisada)\n"
    "   - Posição aproximada dos ocupantes\n\n"
    "3. Com base nos ΔT calculados para cada parede, classifique:\n"
    "   - **Parede crítica:** aquela com maior |ΔT| (destaque com cor diferente)\n"
    "   - **Demais paredes:** classifique conforme o sinal de ΔT\n\n"
    "4. Para cada superfície, indique:\n"
    "   - Mecanismo(s) de transferência predominante(s) (convecção, radiação, condução)\n"
    "   - Direção do fluxo de calor (setas: → para fluxo da parede para o ar, ← para fluxo do ar para a parede)\n"
    "   - Intensidade relativa (alta para parede crítica, média para ΔT moderado, baixa para ΔT próximo de zero)\n\n"
    "**Exemplo de legenda:**\n"
    "- 🔴 Radiação: fluxo por ondas eletromagnéticas (representar com linhas onduladas)\n"
    "- 🔵 Convecção: fluxo pelo movimento do ar (representar com setas curvas)\n"
    "- ⚫ Condução: fluxo através da parede (representar com setas retas)\n\n"
    "**Critérios de avaliação:**\n\n"
    "| Critério | Peso | Descrição |\n"
    "|----------|------|-----------|\n"
    "| Identificação correta dos mecanismos | 40% | Radiação, convecção e condução associados corretamente a cada superfície |\n"
    "| Direção dos fluxos | 20% | Setas indicando sentido correto (baseado no sinal de ΔT) |\n"
    "| Identificação da parede crítica | 20% | Destaque para a parede com maior |ΔT| |\n"
    "| Clareza e organização | 20% | Esquema legível, legendas, cores |\n\n"
    "O objetivo não é apenas descrever, mas **interpretar o sistema como um problema de engenharia térmica**. "
    "Cada região deve ser analisada com base nos conceitos apresentados e nos valores de ΔT calculados, evitando descrições genéricas."
)},
# {"tipo": "subtitulo", "texto": "Critérios de avaliação"},

# {"tipo": "texto", "texto": (
#     "A mini-entrega será avaliada com base em:\n\n"
#     "| Critério | Peso | Descrição |\n"
#     "|----------|------|-----------|\n"
#     "| Identificação correta dos mecanismos | 40% | Radiação, convecção e condução corretamente associados |\n"
#     "| Direção dos fluxos | 20% | Setas indicando sentido correto do calor |\n"
#     "| Diferenciação de intensidade | 20% | Destaque para parede Sul como região crítica |\n"
#     "| Clareza e organização | 20% | Esquema legível, legendas, cores |\n\n<br>"
# )},

{"tipo": "subtitulo", "texto": "Competências desenvolvidas"},

{"tipo": "texto", "texto": (
    "Ao final desta etapa, o aluno deve ser capaz de:\n\n"
    "- Diferenciar os mecanismos de transferência de calor em um caso real;\n"
    "- Interpretar fisicamente equações de fluxo térmico aplicadas ao ambiente construído;\n"
    "- Relacionar fenômenos observados (desconforto próximo à parede Sul) com modelos físicos;\n"
    "- Construir um mapa conceitual dos fluxos de calor;\n"
    "- Preparar a base para a modelagem energética da sala (próxima etapa)."
)},
    ]
