from __future__ import annotations

import streamlit as st


CONTEUDO_ID = "propriedades_eletricas_condutores_material_resistividade"

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

    acerto_q1 = _acertou(Q_D_001, "b")
    acerto_q2 = _acertou(Q_D_002, "c")
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
                "No circuito de alimentação de um motor de bomba, deseja-se comparar dois condutores "
                "de mesma seção e mesmo comprimento: um de cobre e outro de alumínio. "
                "Considerando condições equivalentes de instalação, a afirmação mais adequada é:"
            ),
            "alternativas": {
                "a": "O alumínio apresenta menor resistividade que o cobre, logo tende a produzir menor queda de tensão",
                "b": "O cobre apresenta menor resistividade que o alumínio, logo tende a oferecer menor resistência elétrica ao circuito",
                "c": "Cobre e alumínio apresentam exatamente a mesma resistividade em temperatura ambiente",
                "d": "A escolha entre cobre e alumínio não influencia a resistência elétrica do condutor",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_D_002,
            "pergunta": (
                "A resistência elétrica de um condutor homogêneo pode ser modelada por "
                "**R = \\rho L / A**. Nessa expressão, o significado físico da grandeza "
                "**\\rho** é:"
            ),
            "alternativas": {
                "a": "A potência dissipada por unidade de volume do material",
                "b": "A corrente máxima admissível do cabo",
                "c": "A propriedade intrínseca do material que expressa sua oposição à condução de corrente elétrica",
                "d": "A tensão nominal de operação do circuito",
            },
            "alternativa_correta": "c",
        },
    ]


def _blocos_sucesso_diagnostico() -> list[dict]:
    return [
        {
            "tipo": "alerta",
            "nivel": "success",
            "texto": (
                "Você demonstrou domínio inicial sobre material do condutor, resistividade elétrica "
                "e sua influência na resistência do circuito. Este conteúdo pode ser considerado "
                "concluído nesta etapa."
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
                    "Na questão 1, a resposta correta é **b**. O cobre apresenta, em temperatura ambiente, "
                    "resistividade elétrica menor que a do alumínio. Como a resistência de um condutor "
                    "uniforme é dada por **R = \\rho L / A**, para mesmo comprimento **L** e mesma seção "
                    "transversal **A**, o material com menor **\\rho** resulta em menor resistência elétrica. "
                    "Em circuitos de alimentação, isso tende a reduzir perdas por efeito Joule e a queda de "
                    "tensão ao longo do percurso."
                ),
            }
        )

    if not resultado.get("q2_correta", False):
        blocos.append(
            {
                "tipo": "texto",
                "texto": (
                    "Na questão 2, a resposta correta é **c**. A resistividade elétrica **\\rho** é uma "
                    "propriedade intrínseca do material e quantifica sua oposição à passagem de corrente. "
                    "Ela não depende diretamente do comprimento do cabo, mas o comprimento influencia a "
                    "resistência total pelo modelo **R = \\rho L / A**. Assim, a resistividade conecta a "
                    "natureza física do material ao comportamento elétrico macroscópico do circuito."
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
                "Em circuitos de alimentação elétrica, os condutores não são elementos ideais. "
                "Eles apresentam resistência elétrica e, por isso, influenciam diretamente a "
                "corrente, as perdas de potência e a queda de tensão no sistema. Para analisar "
                "tecnicamente um circuito de alimentação de motor, é necessário compreender como "
                "as propriedades físicas do material do cabo afetam o comportamento elétrico da instalação."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Os materiais mais usuais em condutores de potência são **cobre** e **alumínio**. "
                "Ambos podem ser empregados em instalações elétricas, mas possuem propriedades distintas. "
                "O cobre apresenta menor resistividade elétrica e, portanto, para uma mesma geometria de "
                "cabo, tende a oferecer menor resistência ao escoamento de corrente. O alumínio, por sua vez, "
                "possui maior resistividade, exigindo em geral seções maiores para desempenho elétrico equivalente."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A resistência elétrica de um condutor uniforme pode ser modelada por:\n\n"
                "$$ R = \\frac{\\rho L}{A} $$\n\n"
                "em que **R** é a resistência elétrica do condutor, **\\rho** é a resistividade elétrica do "
                "material, **L** é o comprimento do trecho analisado e **A** é a área da seção transversal. "
                "Essa equação mostra que a resistência cresce com o comprimento e com a resistividade, "
                "e diminui com o aumento da seção do cabo."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Do ponto de vista microscópico, a resistividade expressa a dificuldade encontrada pelos "
                "portadores de carga ao atravessar o material. Em termos macroscópicos, isso significa que "
                "materiais com maior **\\rho** dissipam mais energia para uma mesma corrente e geometria de "
                "condutor. Em engenharia, essa relação é crucial porque o aumento da resistência provoca "
                "elevação das perdas por efeito Joule, dadas por:\n\n"
                "$$ P_J = I^2 R $$\n\n"
                "onde **I** é a corrente elétrica no circuito."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "A influência do material do condutor também aparece na queda de tensão ao longo da linha. "
                "Em uma modelagem simplificada, a queda de tensão em um trecho pode ser escrita como:\n\n"
                "$$ \\Delta V = I R $$\n\n"
                "Substituindo a expressão da resistência, obtém-se:\n\n"
                "$$ \\Delta V = I \\frac{\\rho L}{A} $$\n\n"
                "Portanto, para uma mesma corrente e um mesmo comprimento, a escolha do material e da seção "
                "transversal do cabo interfere diretamente na tensão efetivamente disponível nos terminais do motor."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Na formação em engenharia ambiental e civil, essa análise é relevante porque sistemas de "
                "bombeamento, tratamento de água, recalque, drenagem e edificações dependem de circuitos "
                "elétricos confiáveis. O projetista precisa compreender que o condutor é parte ativa do "
                "desempenho do sistema: ele não apenas transporta energia, mas condiciona perdas, aquecimento "
                "e qualidade da alimentação elétrica."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=ok4O4VwbnKQ",
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=-zCx4Y3I99o",
        },
        {
            "tipo": "texto",
            "texto": (
                "No sistema estudado, o motor da bomba impõe uma corrente ao circuito de alimentação. "
                "Os cabos devem conduzir essa corrente com segurança, limitando o aquecimento e preservando "
                "a tensão nos terminais do equipamento. Se o material do condutor possuir resistividade mais "
                "elevada, ou se a seção for insuficiente, a resistência do circuito aumenta."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Esse aumento de resistência pode produzir dois efeitos técnicos relevantes: maior dissipação "
                "de potência por efeito Joule e maior queda de tensão ao longo do circuito. Em instalações de "
                "bombeamento, esses efeitos podem comprometer o desempenho do motor, reduzir eficiência e "
                "elevar o estresse térmico sobre a isolação dos cabos."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Assim, a análise de material do condutor e resistividade não é apenas teórica. Ela sustenta "
                "decisões de projeto sobre seleção entre cobre e alumínio, escolha de seção transversal e "
                "avaliação da adequação elétrica do circuito de alimentação do motor."
            ),
        },
        {
            "tipo": "lista",
            "itens": [
                "Cobre e alumínio possuem resistividades elétricas diferentes.",
                "A resistência do cabo depende de material, comprimento e seção transversal.",
                "A relação fundamental é R = ρL/A.",
                "Perdas por aquecimento crescem com a resistência e com o quadrado da corrente.",
                "Queda de tensão aumenta quando a resistividade é maior ou a seção do cabo é menor.",
                "Esses conceitos são essenciais no dimensionamento do circuito de alimentação do motor.",
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
                "Dois condutores possuem o mesmo comprimento e conduzem a mesma corrente. "
                "Se um deles for substituído por outro de maior seção transversal, conclui-se que:"
            ),
            "alternativas": {
                "a": "A resistência elétrica aumenta e a queda de tensão também aumenta",
                "b": "A resistência elétrica diminui e a queda de tensão tende a diminuir",
                "c": "A resistividade do material aumenta automaticamente",
                "d": "A corrente no circuito necessariamente zera",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": Q_F_002,
            "pergunta": (
                "Na comparação entre cobre e alumínio, para mesma geometria e mesma temperatura, "
                "o material com menor resistividade tende a apresentar:"
            ),
            "alternativas": {
                "a": "Maior resistência elétrica",
                "b": "Maior queda de tensão para a mesma corrente",
                "c": "Menor resistência elétrica e menores perdas por efeito Joule",
                "d": "Menor tensão de alimentação da concessionária",
            },
            "alternativa_correta": "c",
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