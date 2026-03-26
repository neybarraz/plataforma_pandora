from __future__ import annotations

import streamlit as st


BASE_ID = "analise_1_07"

Q_D_001 = f"{BASE_ID}_001"
Q_D_002 = f"{BASE_ID}_002"
Q_F_001 = f"{BASE_ID}_003"
Q_F_002 = f"{BASE_ID}_004"


DIAG_QUESTOES = (Q_D_001, Q_D_002)
DIAG_CORRETAS = {
    Q_D_001: "c",
    Q_D_002: "b",
}


def _get_widget_value(question_id: str):
    return st.session_state.get(f"analise_widget_{question_id}")


def _normalizar_resposta(valor) -> str:
    if valor is None:
        return ""
    return str(valor).strip().lower()


def _respostas_diagnostico() -> dict[str, str]:
    return {
        qid: _normalizar_resposta(_get_widget_value(qid))
        for qid in DIAG_QUESTOES
    }


def _questoes_pendentes() -> list[str]:
    respostas = _respostas_diagnostico()
    return [qid for qid in DIAG_QUESTOES if not respostas[qid]]


def _diagnostico_respondido() -> bool:
    return len(_questoes_pendentes()) == 0


def _resultado_diagnostico() -> dict:
    respostas = _respostas_diagnostico()
    pendentes = _questoes_pendentes()

    corretas: list[str] = []
    erradas: list[str] = []

    for qid in DIAG_QUESTOES:
        resposta = respostas[qid]
        if not resposta:
            continue

        if resposta == DIAG_CORRETAS[qid]:
            corretas.append(qid)
        else:
            erradas.append(qid)

    total_acertos = len(corretas)
    respondido = len(pendentes) == 0
    acertou_tudo = respondido and total_acertos == len(DIAG_QUESTOES)
    precisa_reforco = respondido and total_acertos < len(DIAG_QUESTOES)

    return {
        "respondido": respondido,
        "pendentes": pendentes,
        "respostas": respostas,
        "corretas": corretas,
        "erradas": erradas,
        "q1_correta": Q_D_001 in corretas,
        "q2_correta": Q_D_002 in corretas,
        "total_acertos": total_acertos,
        "acertou_tudo": acertou_tudo,
        "precisa_reforco": precisa_reforco,
    }


def _bloco_diagnostico_q1() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_001,
        "pergunta": (
            "Em um circuito que alimenta um motor elétrico, a queda de tensão ao longo dos condutores "
            "deve ser limitada porque valores elevados podem comprometer a tensão efetivamente aplicada "
            "nos terminais da carga. Do ponto de vista físico, conclui-se que:"
        ),
        "alternativas": {
            "a": "A queda de tensão depende apenas da potência mecânica do motor, independentemente do circuito",
            "b": "A queda de tensão deixa de existir quando o condutor é de cobre",
            "c": "A queda de tensão resulta da circulação de corrente em condutores com resistência elétrica finita",
            "d": "A queda de tensão é causada exclusivamente pelo fator de potência do motor",
        },
        "alternativa_correta": "c",
    }


def _bloco_diagnostico_q2() -> dict:
    return {
        "tipo": "questao_multipla_escolha",
        "id": Q_D_002,
        "pergunta": (
            "Ao analisar a influência do comprimento do circuito na alimentação elétrica de um motor, "
            "assinale a interpretação correta:"
        ),
        "alternativas": {
            "a": "O comprimento do circuito não interfere na resistência elétrica dos condutores",
            "b": "Quanto maior o comprimento do circuito, maior tende a ser a resistência total e, portanto, maior a queda de tensão",
            "c": "A influência do comprimento existe apenas em circuitos trifásicos",
            "d": "O comprimento do circuito afeta apenas a corrente nominal do motor, sem alterar o comportamento dos condutores",
        },
        "alternativa_correta": "b",
    }


def _mapa_blocos_diagnostico() -> dict[str, dict]:
    return {
        Q_D_001: _bloco_diagnostico_q1(),
        Q_D_002: _bloco_diagnostico_q2(),
    }


def _blocos_diagnostico_completo() -> list[dict]:
    return [
        _bloco_diagnostico_q1(),
        _bloco_diagnostico_q2(),
    ]


def _blocos_diagnostico_pendentes() -> list[dict]:
    resultado = _resultado_diagnostico()
    pendentes = resultado["pendentes"]
    mapa = _mapa_blocos_diagnostico()

    blocos: list[dict] = [
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Você já iniciou o diagnóstico. Responda apenas as questões que ainda estão pendentes."
            ),
        }
    ]

    for qid in pendentes:
        if qid in mapa:
            blocos.append(mapa[qid])

    return blocos


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre relações fundamentais de circuitos aplicadas à "
                "queda de tensão e à influência do comprimento dos condutores. "
                "Este conteúdo pode ser considerado concluído nesta etapa."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Ao salvar ou concluir esta etapa, você poderá seguir para o próximo conteúdo."
            ),
        },
    ]


def _blocos_correcao_diagnostico() -> list[dict]:
    resultado = _resultado_diagnostico()

    blocos: list[dict] = [
        {
            "tipo": "alerta",
            "nivel": "warning",
            "texto": (
                "Você errou uma ou mais questões do diagnóstico. "
                "Antes de seguir, revise os pontos principais abaixo."
            ),
        },
        {
            "tipo": "subtitulo",
            "texto": "Correção do diagnóstico",
        },
    ]

    if not resultado.get("q1_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 1, a resposta correta é **c**. Em um circuito real, os condutores apresentam "
                    "resistência elétrica não nula. Quando a corrente elétrica percorre esse condutor, surge uma "
                    "diferença de potencial ao longo do seu comprimento, descrita pela relação **ΔV = R\\,I**. "
                    "Assim, parte da tensão disponível na fonte é dissipada ao longo da linha, reduzindo a tensão "
                    "efetivamente entregue ao motor. Esse fenômeno não depende apenas da existência da carga, mas "
                    "da interação entre corrente elétrica e resistência dos condutores."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **b**. A resistência elétrica de um condutor é dada por "
                    "**R = \\rho\\,L/A**, em que **\\rho** é a resistividade do material, **L** é o comprimento "
                    "do percurso elétrico e **A** é a área da seção transversal. Portanto, quando o comprimento "
                    "aumenta, a resistência total do circuito também aumenta. Como a queda de tensão está associada "
                    "à relação **ΔV = R\\,I**, comprimentos maiores tendem a produzir quedas de tensão mais elevadas, "
                    "especialmente em circuitos com correntes significativas."
                ),
            }
        )

    return blocos


def _blocos_reforco() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Reforço do conteúdo",
        },
        {
            "tipo": "texto",
            "texto": (
                "Em circuitos elétricos aplicados à alimentação de motores, a análise não se limita à corrente "
                "admissível do condutor. Também é necessário verificar se a tensão que chega à carga permanece "
                "suficientemente próxima da tensão nominal do sistema. Essa exigência decorre do fato de que os "
                "condutores possuem resistência elétrica finita e, portanto, parte da energia elétrica fornecida "
                "pela fonte é dissipada ao longo do percurso."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A base teórica inicial está na combinação entre a Lei de Ohm e a expressão da resistência elétrica "
                "de um condutor uniforme. Pela Lei de Ohm, a queda de tensão ao longo de um trecho resistivo pode "
                "ser escrita como:\n\n"
                "$$ \\Delta V = R\\,I $$\n\n"
                "em que **ΔV** é a queda de tensão, **R** é a resistência elétrica do trecho e **I** é a corrente "
                "que o percorre. Já a resistência do condutor pode ser representada por:\n\n"
                "$$ R = \\rho\\,\\frac{L}{A} $$\n\n"
                "em que **\\rho** é a resistividade elétrica do material, **L** é o comprimento do condutor e "
                "**A** é a área da seção transversal."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Substituindo a expressão da resistência na Lei de Ohm, obtém-se uma forma direta de interpretar "
                "o comportamento físico do circuito:\n\n"
                "$$ \\Delta V = \\rho\\,\\frac{L}{A}\\,I $$\n\n"
                "Essa equação mostra que a queda de tensão cresce com o aumento da corrente elétrica e com o "
                "aumento do comprimento do circuito, enquanto diminui quando se aumenta a seção transversal do "
                "condutor. Em termos de projeto, isso significa que circuitos mais longos e mais carregados exigem "
                "maior atenção ao dimensionamento dos cabos."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em instalações de alimentação de motores, a queda de tensão excessiva pode produzir consequências "
                "técnicas relevantes, como redução da tensão nos terminais do motor, aumento da corrente em certas "
                "condições operacionais, dificuldade de partida, aquecimento adicional e perda de desempenho do "
                "equipamento. Por isso, a análise da queda de tensão não é apenas uma verificação complementar, "
                "mas um critério funcional essencial na avaliação do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "O comprimento do circuito exerce papel central nessa análise. Em termos físicos, quanto maior o "
                "percurso elétrico entre a fonte e o motor, maior a resistência total associada aos condutores. "
                "Em circuitos reais, deve-se considerar o percurso efetivo da corrente, o que torna o comprimento "
                "um parâmetro determinante para a estimativa da queda de tensão. Em linhas extensas, mesmo correntes "
                "moderadas podem gerar reduções significativas de tensão caso a seção do cabo seja insuficiente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Em aplicações de engenharia, é comum expressar a queda de tensão também em termos percentuais, "
                "o que facilita a comparação com limites técnicos adotados em projeto:\n\n"
                "$$ \\Delta V_{\\%} = \\frac{\\Delta V}{V_n} \\times 100 $$\n\n"
                "em que **V_n** é a tensão nominal do circuito. Essa forma permite avaliar de maneira objetiva se "
                "a tensão entregue ao motor permanece dentro da faixa aceitável de operação."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=-zCx4Y3I99o",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=ulrdK7I_FDI",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema de bombeamento em análise, essas relações são aplicadas diretamente ao circuito de "
                "alimentação elétrica do motor. A potência requerida pelo motor define a corrente demandada, e essa "
                "corrente percorre condutores com comprimento, material e seção determinados. Assim, o desempenho "
                "elétrico do sistema depende não apenas da existência de alimentação, mas da qualidade dessa "
                "alimentação ao longo do circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Se o percurso entre a fonte e o motor for longo, a resistência equivalente dos condutores cresce. "
                "Se, além disso, a seção for reduzida, a queda de tensão pode atingir valores incompatíveis com o "
                "funcionamento adequado do motor. Portanto, a relação entre comprimento do circuito e seção do "
                "condutor é decisiva para garantir que a tensão disponível nos terminais do equipamento seja "
                "compatível com sua condição nominal de operação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Do ponto de vista de projeto, esse conteúdo conecta diretamente os fundamentos da teoria de "
                "circuitos à prática de dimensionamento em instalações prediais e sistemas de bombeamento. "
                "Não basta saber que o motor consome potência; é necessário compreender como essa exigência "
                "se traduz em corrente, como essa corrente interage com a resistência dos condutores e como "
                "isso afeta a tensão efetivamente disponível na carga."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "A queda de tensão em condutores decorre da resistência elétrica do circuito.",
                "A relação fundamental é dada por ΔV = R·I.",
                "A resistência do condutor depende de resistividade, comprimento e seção: R = ρL/A.",
                "Comprimentos maiores elevam a resistência total e tendem a aumentar a queda de tensão.",
                "Seções maiores reduzem a resistência e ajudam a limitar a queda de tensão.",
                "No circuito do motor da bomba, esses fatores afetam diretamente a qualidade da alimentação elétrica.",
            ],
        },
    ]


def _blocos_reflexao_final() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Reflexão final",
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Nesta etapa final, suas respostas serão registradas para análise. "
                "Não será exibido feedback imediato de certo ou errado."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_001,
            "pergunta": (
                "Em um circuito que alimenta um motor, mantendo-se a mesma corrente e o mesmo material do condutor, "
                "qual alteração tende a reduzir a queda de tensão ao longo da linha?"
            ),
            "alternativas": {
                "a": "Aumentar o comprimento do circuito",
                "b": "Reduzir a seção transversal do condutor",
                "c": "Aumentar a seção transversal do condutor",
                "d": "Aumentar a resistência elétrica do trecho",
            },
            "alternativa_correta": "c",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Em uma instalação de bombeamento, dois circuitos alimentam motores idênticos sob a mesma corrente. "
                "O circuito A é significativamente mais longo que o circuito B. A interpretação mais adequada é que:"
            ),
            "alternativas": {
                "a": "O circuito A tende a apresentar maior resistência total e maior queda de tensão",
                "b": "O circuito A necessariamente terá menor queda de tensão por dissipar melhor o calor",
                "c": "O comprimento do circuito não altera a tensão nos terminais do motor",
                "d": "A influência do comprimento só existe se a rede for monofásica",
            },
            "alternativa_correta": "a",
        },
    ]


def get_blocos() -> list[dict]:
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAG_QUESTOES):
            return _blocos_diagnostico_pendentes()
        return _blocos_diagnostico_completo()

    if resultado["acertou_tudo"]:
        return _blocos_sucesso_diagnostico()

    return (
        _blocos_correcao_diagnostico()
        + _blocos_reforco()
        + _blocos_reflexao_final()
    )


def render_controles_especiais() -> None:
    resultado = _resultado_diagnostico()

    if not resultado["respondido"]:
        if resultado["pendentes"] and len(resultado["pendentes"]) < len(DIAG_QUESTOES):
            st.info("Diagnóstico em andamento. Responda apenas as questões pendentes.")
        else:
            st.info("Responda às duas questões iniciais. O reforço será liberado automaticamente se necessário.")
        return

    if resultado["acertou_tudo"]:
        st.success("Diagnóstico concluído com domínio.")
        return

    st.warning("Diagnóstico concluído. O bloco de reforço foi liberado com base nas suas respostas.")