# apps/app_01/sections/visao_geral/avaliacao.py
import pandas as pd
import streamlit as st


# -----------------------------
# UTILIDADES
# -----------------------------

def _titulo_destaque(texto: str, nivel: int = 2) -> None:
    tamanhos = {1: "2.2rem", 2: "1.8rem", 3: "1.35rem", 4: "1.15rem"}
    tamanho = tamanhos.get(nivel, "1.2rem")

    st.markdown(
        f"""
        <div style="
        font-size:{tamanho};
        font-weight:700;
        color:#14B8A6;
        margin-top:0.6rem;
        margin-bottom:0.8rem;">
        {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _texto_justificado(texto: str) -> None:
    st.markdown(
        f"""
        <div style="text-align:justify;">
        {texto}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _lista_justificada(itens: list[str]) -> None:
    html_itens = "".join(f"<li>{i}</li>" for i in itens)

    st.markdown(
        f"""
        <div style="text-align:justify;">
        <ul>{html_itens}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# BARRA DE PROGRESSO
# -----------------------------

def progresso(etapa: int) -> None:
    cores = []

    for i in range(3):
        if i < etapa:
            cores.append("#22c55e")
        elif i == etapa:
            cores.append("#f59e0b")
        else:
            cores.append("#e5e7eb")

    st.markdown(
        f"""
        <div style="display:flex; gap:8px; margin-bottom:10px;">
            <div style="flex:1;height:10px;background:{cores[0]};border-radius:5px"></div>
            <div style="flex:1;height:10px;background:{cores[1]};border-radius:5px"></div>
            <div style="flex:1;height:10px;background:{cores[2]};border-radius:5px"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# DADOS EXEMPLO
# -----------------------------

def _dados_unidade_1() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Nome": "Capitão Gradiente Térmico",
                "B1": 10.0,
                "B2": 10.0,
                "B3": 10.0,
                "MP": (10.0 + 10.0 + 10.0) / 3,
                "Penalidade": 0.0,
                "Unid. 1": (10.0 + 10.0 + 10.0) / 3,
                "Obs.": "Entregou tudo no prazo.",
            },
            {
                "Nome": "Dona Convecção Natural",
                "B1": 9.0,
                "B2": 8.5,
                "B3": 9.2,
                "MP": (9.0 + 8.5 + 9.2) / 3,
                "Penalidade": 1.0,
                "Unid. 1": ((9.0 + 8.5 + 9.2) / 3) - 1.0,
                "Obs.": "Atrasou a entrega e recebeu penalidade.",
            },
            {
                "Nome": "Mestre da Radiação Solar",
                "B1": 6.5,
                "B2": 5.8,
                "B3": 0.0,
                "MP": (6.5 + 5.8 + 0.0) / 3,
                "Penalidade": 0.0,
                "Unid. 1": (6.5 + 5.8 + 0.0) / 3,
                "Obs.": "Não entregou o Bloco 3.",
            },
            {
                "Nome": "Barão da Superfície Quente",
                "B1": 7.8,
                "B2": 6.0,
                "B3": 5.4,
                "MP": (7.8 + 6.0 + 5.4) / 3,
                "Penalidade": 0.8,
                "Unid. 1": ((7.8 + 6.0 + 5.4) / 3) - 0.8,
                "Obs.": "Desempenho irregular com atraso na entrega.",
            },
        ]
    )


def _dados_unidade_2() -> pd.DataFrame:
    w_prova = 0.7
    w_memorial = 0.3

    rows = [
        {
            "Nome": "Capitão Gradiente Térmico",
            "Prova B1": 10.0,
            "Memorial B1": 9.5,
            "Prova B2": 10.0,
            "Memorial B2": 10.0,
            "Prova B3": 10.0,
            "Memorial B3": 9.8,
            "Obs.": "Excelente desempenho individual.",
        },
        {
            "Nome": "Dona Convecção Natural",
            "Prova B1": 8.0,
            "Memorial B1": 8.5,
            "Prova B2": 8.5,
            "Memorial B2": 8.0,
            "Prova B3": 7.8,
            "Memorial B3": 8.2,
            "Obs.": "Bom equilíbrio entre prova e memorial.",
        },
        {
            "Nome": "Mestre da Radiação Solar",
            "Prova B1": 4.0,
            "Memorial B1": 5.5,
            "Prova B2": 3.5,
            "Memorial B2": 4.0,
            "Prova B3": 3.0,
            "Memorial B3": 0.0,
            "Obs.": "Provas fracas e memorial incompleto.",
        },
        {
            "Nome": "Barão da Superfície Quente",
            "Prova B1": 6.2,
            "Memorial B1": 6.8,
            "Prova B2": 5.7,
            "Memorial B2": 6.0,
            "Prova B3": 5.0,
            "Memorial B3": 5.5,
            "Obs.": "Memorial melhora parcialmente a nota.",
        },
    ]

    df = pd.DataFrame(rows)

    df["B1"] = w_prova * df["Prova B1"] + w_memorial * df["Memorial B1"]
    df["B2"] = w_prova * df["Prova B2"] + w_memorial * df["Memorial B2"]
    df["B3"] = w_prova * df["Prova B3"] + w_memorial * df["Memorial B3"]
    df["MP"] = (df["B1"] + df["B2"] + df["B3"]) / 3
    df["Unid. 2"] = df["MP"]

    return df[
        [
            "Nome",
            "Prova B1",
            "Memorial B1",
            "B1",
            "Prova B2",
            "Memorial B2",
            "B2",
            "Prova B3",
            "Memorial B3",
            "B3",
            "MP",
            "Unid. 2",
            "Obs.",
        ]
    ]


def _dados_resultado_final(df_a: pd.DataFrame, df_b: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Nome": "Capitão Gradiente Térmico",
                "Unid. 1": float(df_a.loc[df_a["Nome"] == "Capitão Gradiente Térmico", "Unid. 1"].iloc[0]),
                "Unid. 2": float(df_b.loc[df_b["Nome"] == "Capitão Gradiente Térmico", "Unid. 2"].iloc[0]),
                "Reposição": "-",
                "Nota final": 10.0,
                "Situação": "Aprovado",
            },
            {
                "Nome": "Dona Convecção Natural",
                "Unid. 1": float(df_a.loc[df_a["Nome"] == "Dona Convecção Natural", "Unid. 1"].iloc[0]),
                "Unid. 2": float(df_b.loc[df_b["Nome"] == "Dona Convecção Natural", "Unid. 2"].iloc[0]),
                "Reposição": "-",
                "Nota final": float(df_a.loc[df_a["Nome"] == "Dona Convecção Natural", "Unid. 1"].iloc[0]),
                "Situação": "Aprovado",
            },
            {
                "Nome": "Mestre da Radiação Solar",
                "Unid. 1": float(df_a.loc[df_a["Nome"] == "Mestre da Radiação Solar", "Unid. 1"].iloc[0]),
                "Unid. 2": float(df_b.loc[df_b["Nome"] == "Mestre da Radiação Solar", "Unid. 2"].iloc[0]),
                "Reposição": 6.0,
                "Nota final": 6.0,
                "Situação": "Aprovado na recuperação (teto 6,0)",
            },
            {
                "Nome": "Barão da Superfície Quente",
                "Unid. 1": float(df_a.loc[df_a["Nome"] == "Barão da Superfície Quente", "Unid. 1"].iloc[0]),
                "Unid. 2": float(df_b.loc[df_b["Nome"] == "Barão da Superfície Quente", "Unid. 2"].iloc[0]),
                "Reposição": "-",
                "Nota final": float(df_a.loc[df_a["Nome"] == "Barão da Superfície Quente", "Unid. 1"].iloc[0]),
                "Situação": "Reprovado (abaixo de 6,0)",
            },
        ]
    )


# -----------------------------
# CONTEÚDO DAS ETAPAS
# -----------------------------

def pagina_1() -> None:
    _titulo_destaque("Sistema de Avaliação", nivel=1)

    _texto_justificado(
        """
        A avaliação da disciplina será realizada por meio da metodologia de Problem-Based Learning (PBL), na qual a
        aprendizagem ocorre a partir da análise e resolução de problemas. Nesse modelo, os estudantes desenvolvem
        investigação, elaboram soluções e registram tecnicamente o processo de construção do conhecimento.

        O processo de aprendizagem seguirá a seguinte sequência: apresentação do problema, investigação e estudo dos
        conceitos necessários, desenvolvimento da solução e elaboração de um memorial técnico. Após essa etapa, será
        realizada uma avaliação individual para verificação da aprendizagem conceitual.

        Nesta disciplina, o problema central está relacionado à análise do conforto térmico em uma sala de aula,
        considerando os fundamentos de termodinâmica, os mecanismos de transferência de calor e a interpretação do
        campo térmico do ambiente.

        A nota da disciplina será composta por duas unidades avaliativas.
        """
    )

    _titulo_destaque("Unidade Avaliativa 1 – Memorial Técnico (0 a 10 pontos)", nivel=3)

    _texto_justificado(
        """
        Cada estudante deverá elaborar e entregar individualmente um memorial técnico
        descrevendo o processo de análise do conforto térmico do ambiente e a construção
        da solução técnica fundamentada. Embora a investigação e a discussão possam ocorrer
        de forma colaborativa em sala de aula, o documento entregue deverá ser produzido
        individualmente.

        O memorial técnico será avaliado considerando os seguintes critérios:
        """
    )

    _lista_justificada(
        [
            "Compreensão do problema proposto (2 pontos)",
            "Investigação e levantamento de informações necessárias (2 pontos)",
            "Descrição da solução desenvolvida (3 pontos)",
            "Fundamentação técnica utilizada na solução (2 pontos)",
            "Reflexão sobre o processo e possíveis melhorias (1 ponto)",
        ]
    )

    _titulo_destaque("Unidade Avaliativa 2 – Prova Individual (0 a 10 pontos)", nivel=3)

    _texto_justificado(
        """
        Após a conclusão do projeto e entrega do memorial técnico, será aplicada uma prova
        individual em sala de aula. Essa avaliação tem como objetivo verificar a compreensão
        dos conceitos estudados durante o desenvolvimento do problema, especialmente os
        fundamentos de termodinâmica, os mecanismos de transferência de calor e a análise
        do campo térmico do ambiente, bem como a capacidade do estudante de aplicar esses
        conhecimentos em situações similares.

        A nota final será calculada pela média aritmética das duas unidades avaliativas.

        Caso a média final seja inferior a 6,0 pontos, o estudante terá direito a realizar
        uma atividade de recuperação, conforme orientações fornecidas pelo professor.
        """
    )


def pagina_2() -> None:
    _titulo_destaque("Política de Entrega e Recuperação de Avaliações", nivel=2)

    _texto_justificado(
        """
        As atividades avaliativas da disciplina devem ser entregues dentro dos prazos
        estabelecidos pelo professor. O cumprimento desses prazos faz parte do processo
        de organização acadêmica e será considerado na avaliação das atividades.
        """
    )

    _titulo_destaque("Política de entrega do memorial técnico", nivel=4)

    _texto_justificado(
        """
        O memorial técnico deverá ser entregue na data indicada no cronograma da atividade.
        Em caso de atraso, a pontuação obtida será ajustada de acordo com os critérios abaixo:
        """
    )

    _lista_justificada(
        [
            "Entrega no prazo: nota integral.",
            "Até 3 dias de atraso: desconto de 5% da nota por dia de atraso.",
            "Do 4º ao 7º dia de atraso: desconto de 10% da nota por dia de atraso.",
            "Após 7 dias de atraso: a nota máxima possível será limitada a 6,0 pontos.",
            "Não entrega da atividade: nota 0,0.",
        ]
    )

    _texto_justificado(
        """
        O período de atraso será contabilizado em dias corridos, a partir da data
        originalmente definida para a entrega da atividade.
        """
    )

    _titulo_destaque("Política de recuperação", nivel=4)

    _texto_justificado(
        """
        A nota final da disciplina será calculada pela média das duas unidades avaliativas:
        """
    )

    _lista_justificada(
        [
            "Unidade 1: memorial técnico.",
            "Unidade 2: prova individual.",
        ]
    )

    _texto_justificado(
        """
        Caso a média final seja inferior a 6,0 pontos, o estudante terá direito a realizar
        uma atividade de recuperação. O formato da recuperação será definido de acordo
        com a avaliação em que o estudante obteve menor desempenho.
        """
    )

    _lista_justificada(
        [
            "Se a menor nota tiver sido obtida na prova, o estudante realizará uma nova prova individual.",
            "Se a menor nota tiver sido obtida no memorial técnico, o estudante deverá refazer o memorial técnico.",
        ]
    )

    _texto_justificado(
        """
        A atividade de recuperação será realizada presencialmente em sala de aula,
        em data definida pelo professor, e deverá ser desenvolvida individualmente.

        A nota obtida na recuperação substituirá a nota da avaliação correspondente
        realizada anteriormente.
        """
    )


def pagina_3() -> None:
    _titulo_destaque("Exemplos de Cálculo", nivel=2)

    _texto_justificado(
        """
        Os exemplos a seguir simulam situações comuns de desempenho ao longo do semestre
        na análise do problema de conforto térmico. O objetivo é demonstrar como são
        aplicadas a nota do memorial técnico, a nota da prova individual, os descontos
        por atraso na entrega e a regra de recuperação quando a média final for inferior
        a 6,0 pontos.
        """
    )

    df_exemplos = _dados_exemplos_avaliacao()

    _titulo_destaque("Tabela — Simulações de notas e recuperação", nivel=4)
    st.caption(
        "Unidade 1 = memorial técnico. Unidade 2 = prova individual. "
        "Se a média for menor que 6,0, a recuperação ocorre na menor nota."
    )

    df_exibicao = df_exemplos.copy()

    colunas_numericas = [
        "Memorial bruto",
        "Penalidade (%)",
        "Unid. 1",
        "Unid. 2",
        "Média antes da rec.",
        "Média final",
    ]

    for col in colunas_numericas:
        df_exibicao[col] = df_exibicao[col].map(
            lambda x: f"{x:.1f}" if isinstance(x, (int, float)) else x
        )

    df_exibicao["Recuperação"] = df_exibicao["Recuperação"].map(
        lambda x: f"{x:.1f}" if isinstance(x, (int, float)) else x
    )

    html_tabela = df_exibicao.to_html(index=False, escape=False)

    st.markdown(
        """
        <style>
        .tabela-simulacao {
            max-width: 980px;
        }

        .tabela-simulacao table {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
            font-size: 0.7rem;
        }

        .tabela-simulacao th,
        .tabela-simulacao td {
            border: 1px solid #ddd;
            padding: 8px;
            vertical-align: top;
            text-align: left;
            white-space: normal !important;
            word-break: break-word;
            overflow-wrap: anywhere;
        }

        .tabela-simulacao th:nth-child(1),
        .tabela-simulacao td:nth-child(1) {
            width: 100px;
        }

        .tabela-simulacao th:nth-child(2),
        .tabela-simulacao td:nth-child(2) {
            width: 200px;
            max-width: 220px;
            white-space: normal !important;
            word-break: break-word;
            overflow-wrap: anywhere;
        }

        .tabela-simulacao th:nth-child(3),
        .tabela-simulacao td:nth-child(3),
        .tabela-simulacao th:nth-child(4),
        .tabela-simulacao td:nth-child(4),
        .tabela-simulacao th:nth-child(5),
        .tabela-simulacao td:nth-child(5),
        .tabela-simulacao th:nth-child(6),
        .tabela-simulacao td:nth-child(6),
        .tabela-simulacao th:nth-child(7),
        .tabela-simulacao td:nth-child(7),
        .tabela-simulacao th:nth-child(8),
        .tabela-simulacao td:nth-child(8),
        .tabela-simulacao th:nth-child(10),
        .tabela-simulacao td:nth-child(10) {
            width: 60px;
            text-align: center;
        }

        .tabela-simulacao th:nth-child(9),
        .tabela-simulacao td:nth-child(9) {
            width: 60px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f'<div class="tabela-simulacao">{html_tabela}</div>', unsafe_allow_html=True)

    _texto_justificado(
        """
        Nos casos em que houver recuperação, a nova nota substitui a nota original da
        avaliação correspondente. Se a menor nota tiver sido a da prova, a recuperação
        ocorrerá por meio de nova prova individual. Se a menor nota tiver sido a do
        memorial técnico, o estudante deverá refazer o memorial técnico de forma
        individual, presencialmente em sala de aula.
        """
    )

    st.info(
        "Os exemplos apresentados são ilustrativos e servem apenas para demonstrar "
        "como as regras de avaliação são aplicadas."
    )


def _dados_exemplos_avaliacao() -> pd.DataFrame:
    dados = [
        {
            "Aluno": "Capitão Gradiente Térmico",
            "Situação": "Entregou o memorial técnico no prazo e apresentou bom desempenho na prova individual.",
            "Memorial bruto": 8.5,
            "Penalidade (%)": 0.0,
            "Unid. 1": 8.5,
            "Unid. 2": 7.5,
            "Média antes da rec.": 8.0,
            "Recuperação de": "Não se aplica",
            "Recuperação": "-",
            "Média final": 8.0,
        },
        {
            "Aluno": "Dona Convecção Natural",
            "Situação": "Entregou o memorial com 2 dias de atraso, sofrendo desconto na nota, mas manteve bom resultado final.",
            "Memorial bruto": 9.0,
            "Penalidade (%)": 10.0,
            "Unid. 1": 8.1,
            "Unid. 2": 7.0,
            "Média antes da rec.": 7.6,
            "Recuperação de": "Não se aplica",
            "Recuperação": "-",
            "Média final": 7.6,
        },
        {
            "Aluno": "Mestre da Radiação Solar",
            "Situação": "Apresentou desempenho baixo na prova e precisou realizar recuperação nessa avaliação.",
            "Memorial bruto": 7.5,
            "Penalidade (%)": 0.0,
            "Unid. 1": 7.5,
            "Unid. 2": 4.0,
            "Média antes da rec.": 5.8,
            "Recuperação de": "Prova",
            "Recuperação": 6.5,
            "Média final": 7.0,
        },
        {
            "Aluno": "Barão da Superfície Quente",
            "Situação": "Teve dificuldade na elaboração do memorial técnico e precisou refazer essa avaliação em sala de aula.",
            "Memorial bruto": 3.5,
            "Penalidade (%)": 0.0,
            "Unid. 1": 3.5,
            "Unid. 2": 7.0,
            "Média antes da rec.": 5.2,
            "Recuperação de": "Memorial técnico",
            "Recuperação": 6.0,
            "Média final": 6.5,
        },
        {
            "Aluno": "Professor Equilíbrio Térmico",
            "Situação": "Entregou o memorial com mais de 7 dias de atraso e, por regra, sua nota ficou limitada ao máximo de 6,0 pontos.",
            "Memorial bruto": 8.5,
            "Penalidade (%)": 0.0,
            "Unid. 1": 6.0,
            "Unid. 2": 5.5,
            "Média antes da rec.": 5.8,
            "Recuperação de": "Prova",
            "Recuperação": 6.0,
            "Média final": 6.0,
        },
        {
            "Aluno": "Senhor Zona de Desconforto",
            "Situação": "Não entregou o memorial técnico e não alcançou média suficiente mesmo após a recuperação.",
            "Memorial bruto": 0.0,
            "Penalidade (%)": 0.0,
            "Unid. 1": 0.0,
            "Unid. 2": 5.0,
            "Média antes da rec.": 2.5,
            "Recuperação de": "Memorial técnico",
            "Recuperação": 4.5,
            "Média final": 4.8,
        },
    ]

    return pd.DataFrame(dados)


# -----------------------------
# RENDER PRINCIPAL
# -----------------------------

def render_avaliacao(ctx=None) -> None:
    if "etapa_avaliacao" not in st.session_state:
        st.session_state.etapa_avaliacao = 0

    etapa = st.session_state.etapa_avaliacao

    progresso(etapa)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if etapa > 0:
            if st.button("⬅ Voltar", key="voltar_avaliacao"):
                st.session_state.etapa_avaliacao -= 1
                st.rerun()

    with col2:
        st.markdown(
            f"<div style='text-align:center;font-weight:600;'>Etapa {etapa + 1}/3</div>",
            unsafe_allow_html=True,
        )

    with col3:
        if etapa < 2:
            if st.button("Próximo ➜", key="proximo_avaliacao"):
                st.session_state.etapa_avaliacao += 1
                st.rerun()

    if etapa == 0:
        pagina_1()
    elif etapa == 1:
        pagina_2()
    elif etapa == 2:
        pagina_3()


def render(ctx=None) -> None:
    render_avaliacao(ctx)