from __future__ import annotations

import streamlit as st


def _get_valor(qid: str, fallback: str = "—") -> str:
    key = f"problema_{qid}"
    valor = st.session_state.get(key)

    if valor is None or str(valor).strip() == "":
        return fallback

    return str(valor).strip()


def _texto_contexto() -> str:
    potencia = _get_valor("problema.01.001.0001", "uma potência")
    tensao = _get_valor("problema.01.001.0002", "uma tensão")
    distancia = _get_valor("problema.01.001.0006", "uma distância")

    return (
        f"Você coletou os dados do sistema: motor de {potencia} kW, alimentado em {tensao} V, "
        f"com distância de aproximadamente {distancia} m entre o quadro e o motor. "
        "Antes de calcular qualquer coisa, é possível prever o comportamento do sistema. "
        "Essa etapa é importante porque força o raciocínio físico antes da matemática."
    )


def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Resposta guiada: antecipando o comportamento do sistema",
        },

        {
            "tipo": "texto",
            "texto": _texto_contexto(),
        },

        {
            "tipo": "texto",
            "texto": (
                "Agora você deve tomar decisões com base na intuição física.\n\n"
                "Não calcule ainda.\n"
                "Responda com base no comportamento esperado do sistema."
            ),
        },

        # -------------------------------------------------
        # ESTIMATIVA 1 — CORRENTE
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Estimativa 1: exigência do motor",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0001",
            "pergunta": (
                "Um motor com maior potência elétrica tende a exigir:"
            ),
            "alternativas": {
                "a": "Menor corrente",
                "b": "A mesma corrente",
                "c": "Maior corrente",
                "d": "Corrente zero",
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "texto",
            "texto": (
                "A potência define a quantidade de energia que precisa ser transferida. "
                "Mais potência exige maior fluxo de energia, ou seja, maior corrente."
            ),
        },

        # -------------------------------------------------
        # ESTIMATIVA 2 — DISTÂNCIA
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Estimativa 2: efeito da distância",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0002",
            "pergunta": (
                "Com base na distância medida, o efeito do cabo sobre o sistema tende a ser:"
            ),
            "alternativas": {
                "a": "Desprezível",
                "b": "Moderado",
                "c": "Relevante",
                "d": "Inexistente",
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "texto",
            "texto": (
                "Quanto maior a distância, maior a resistência do cabo e maior a queda de tensão.\n"
                "Em sistemas longos, o cabo deixa de ser apenas um condutor e passa a influenciar o funcionamento."
            ),
        },

        # -------------------------------------------------
        # ESTIMATIVA 3 — CABO FINO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Estimativa 3: efeito de um cabo subdimensionado",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0003",
            "pergunta": (
                "Se o cabo for mais fino do que o necessário, qual efeito tende a aparecer primeiro?"
            ),
            "alternativas": {
                "a": "Aumento da tensão no motor",
                "b": "Redução da queda de tensão",
                "c": "Aumento da queda de tensão",
                "d": "Eliminação da corrente",
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "texto",
            "texto": (
                "Cabos mais finos possuem maior resistência elétrica. "
                "Isso aumenta a queda de tensão e reduz a energia disponível no motor."
            ),
        },

        # -------------------------------------------------
        # ESTIMATIVA 4 — IMPACTO NO MOTOR
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Estimativa 4: impacto no funcionamento do motor",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0004",
            "pergunta": (
                "Se a tensão no motor diminuir, o comportamento mais provável é:"
            ),
            "alternativas": {
                "a": "O motor melhora o desempenho",
                "b": "A corrente pode aumentar",
                "c": "O sistema se estabiliza automaticamente",
                "d": "Nada muda",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "Para manter a potência, o sistema tende a aumentar a corrente quando a tensão cai. "
                "Isso aumenta o aquecimento e o esforço elétrico."
            ),
        },

        # -------------------------------------------------
        # COMPARAÇÃO — CURTO VS LONGO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Comparação: circuito curto vs circuito longo",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0005",
            "pergunta": (
                "Qual situação tende a apresentar menor queda de tensão?"
            ),
            "alternativas": {
                "a": "Cabo longo",
                "b": "Cabo curto",
                "c": "Ambos iguais",
                "d": "Depende apenas da potência",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "A queda de tensão cresce com o comprimento do circuito. "
                "Por isso, sistemas mais curtos tendem a ser menos críticos."
            ),
        },

        # -------------------------------------------------
        # VALIDAÇÃO — RACIOCÍNIO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Validação do raciocínio",
        },

        {
            "tipo": "questao_texto",
            "id": "problema.01.003.0006",
            "pergunta": (
                "Explique, com suas palavras, por que a distância e a seção do cabo "
                "influenciam diretamente o funcionamento do motor."
            ),
        },

        # -------------------------------------------------
        # PRÉ-DIAGNÓSTICO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Pré-diagnóstico do sistema",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.003.0007",
            "pergunta": (
                "Antes dos cálculos, qual é a hipótese mais provável para um sistema com cabo longo e possível subdimensionamento?"
            ),
            "alternativas": {
                "a": "Sistema ideal sem perdas",
                "b": "Queda de tensão relevante",
                "c": "Tensão aumentando ao longo do cabo",
                "d": "Corrente nula",
            },
            "alternativa_correta": "b",
        },

        {
            "tipo": "texto",
            "texto": (
                "Você acabou de construir uma hipótese física do sistema.\n\n"
                "Agora o problema já não é mais desconhecido.\n"
                "Na próxima etapa, essa hipótese será testada com equações e cálculos reais."
            ),
        },

        # -------------------------------------------------
        # FECHAMENTO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Síntese da etapa",
        },

        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você não calculou — você antecipou.\n\n"
                "Isso é essencial em engenharia:\n\n"
                "- prever antes de calcular\n"
                "- entender antes de aplicar fórmula\n\n"
                "Agora você já sabe o que esperar do sistema.\n"
                "O próximo passo é verificar se essa previsão está correta."
            ),
        },

    ]