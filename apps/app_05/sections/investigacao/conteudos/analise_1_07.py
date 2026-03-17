from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "relacoes_fundamentais_circuitos_queda_tensao_comprimento"

NUM_D_1 = 1
NUM_D_2 = 2
NUM_F_1 = 3
NUM_F_2 = 4

Q_D_001 = f"q_d_{CONTEUDO_ID}_{NUM_D_1:03d}"
Q_D_002 = f"q_d_{CONTEUDO_ID}_{NUM_D_2:03d}"
Q_F_001 = f"q_f_{CONTEUDO_ID}_{NUM_F_1:03d}"
Q_F_002 = f"q_f_{CONTEUDO_ID}_{NUM_F_2:03d}"

DIAG_STATUS_KEY = f"analise_diag_status_{CONTEUDO_ID}"
DIAG_RESULT_KEY = f"analise_diag_result_{CONTEUDO_ID}"


def _get_widget_value(question_id: str):
    return st.session_state.get(f"analise_widget_{question_id}")


def _diagnostico_respondido() -> bool:
    return _get_widget_value(Q_D_001) is not None and _get_widget_value(Q_D_002) is not None


def _acertou(question_id: str, correta: str) -> bool:
    valor = _get_widget_value(question_id)
    return valor is not None and str(valor).strip().lower() == correta.strip().lower()


def _get_diag_status() -> str:
    return str(st.session_state.get(DIAG_STATUS_KEY, "nao_iniciado"))


def _set_diag_status(status: str) -> None:
    st.session_state[DIAG_STATUS_KEY] = status


def _get_diag_result() -> dict:
    valor = st.session_state.get(DIAG_RESULT_KEY, {})
    return valor if isinstance(valor, dict) else {}


def _set_diag_result(resultado: dict) -> None:
    st.session_state[DIAG_RESULT_KEY] = resultado


def _finalizar_diagnostico() -> None:
    if not _diagnostico_respondido():
        return

    acerto_q1 = _acertou(Q_D_001, "c")
    acerto_q2 = _acertou(Q_D_002, "b")
    total_acertos = int(acerto_q1) + int(acerto_q2)

    resultado = {
        "resposta_q1": _get_widget_value(Q_D_001),
        "resposta_q2": _get_widget_value(Q_D_002),
        "q1_correta": acerto_q1,
        "q2_correta": acerto_q2,
        "total_acertos": total_acertos,
        "acertou_tudo": total_acertos == 2,
    }

    _set_diag_result(resultado)

    if total_acertos == 2:
        _set_diag_status("concluido_com_dominio")
    else:
        _set_diag_status("concluido_com_reforco")

    st.rerun()


def _blocos_diagnostico() -> list[dict]:
    return [
        {
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
        },
        {
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
        },
    ]


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre relações fundamentais de circuitos aplicadas à "
                "queda de tensão e à influência do comprimento dos condutores. Este conteúdo pode ser "
                "considerado concluído nesta etapa."
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
    resultado = _get_diag_result()

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


def _blocos_verificacao_final() -> list[dict]:
    return [
        {
            "tipo": "subtitulo",
            "texto": "Verificação final",
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
    blocos: list[dict] = []
    status = _get_diag_status()

    if status == "nao_iniciado":
        blocos.extend(_blocos_diagnostico())
        return blocos

    if status == "concluido_com_dominio":
        blocos.extend(_blocos_sucesso_diagnostico())
        return blocos

    if status == "concluido_com_reforco":
        blocos.extend(_blocos_correcao_diagnostico())
        blocos.extend(_blocos_reforco())
        blocos.extend(_blocos_verificacao_final())
        return blocos

    return blocos


def render_controles_especiais() -> None:
    status = _get_diag_status()

    if status != "nao_iniciado":
        return

    if not _diagnostico_respondido():
        st.info("Responda as duas questões para verificar o diagnóstico.")
        return

    if st.button(
        "Verificar diagnóstico",
        key=f"btn_verificar_diag_{CONTEUDO_ID}",
        use_container_width=False,
    ):
        _finalizar_diagnostico()