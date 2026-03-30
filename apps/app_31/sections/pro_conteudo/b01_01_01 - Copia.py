from __future__ import annotations


def get_blocos() -> list[dict]:
    return [

        {
            "tipo": "titulo",
            "texto": "Situação de campo: coleta de dados para dimensionamento do bombeamento",
        },

        {
            "tipo": "texto",
            "texto": (
                "Você está realizando uma visita técnica em um sistema de bombeamento de água. "
                "O motor está instalado e conectado ao quadro elétrico, porém ainda não foi verificado "
                "se os cabos de alimentação estão corretamente dimensionados. "
                "Antes de qualquer cálculo, é necessário transformar a situação real em dados confiáveis. "
                "O objetivo desta etapa é coletar as grandezas físicas que descrevem o sistema. "
                "Sem dados corretos, qualquer dimensionamento se torna inválido."
            ),
        },

        {
            "tipo": "titulo",
            "texto": "Objetivo da coleta de dados",
        },

        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, você deve levantar todos os parâmetros necessários para o dimensionamento dos cabos.\n\n"
                "Esses dados serão usados para:\n\n"
                "- determinar a corrente do motor\n"
                "- calcular a queda de tensão\n"
                "- verificar o aquecimento dos cabos\n\n"
                "A precisão dessa coleta define a qualidade de todo o projeto."
            ),
        },
        {
            "tipo": "video",
            "titulo": "Como ler a placa do motor",
            "descricao": (
                "Assista ao vídeo e identifique onde estão os dados de potência, tensão, "
                "fator de potência e rendimento. "
                "Essas informações serão usadas no dimensionamento."
            ),
            "url": "https://www.youtube.com/watch?v=ZLV_MHFdmWk",
            "caption": "Fonte: YouTube",
        },

        {
            "tipo": "titulo",
            "texto": "Dados do motor",
        },

        {
            "tipo": "texto",
            "texto": (
                "Registre os dados da placa do motor. "
                "Essas informações definem a exigência elétrica do sistema."
            ),
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0001",
            "rotulo": "Potência do motor",
            "unidade": "kW",
            "placeholder": "Ex: 3.7"
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0002",
            "rotulo": "Tensão nominal",
            "unidade": "V",
            "placeholder": "Ex: 380"
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0003",
            "rotulo": "Fator de potência",
            "unidade": "--",
            "placeholder": "Ex: 0.86"
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0004",
            "rotulo": "Rendimento",
            "unidade": "--",
            "placeholder": "Ex: 0.88"
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.001.0005",
            "pergunta": (
                "Qual dessas grandezas está diretamente ligada à corrente elétrica exigida pelo motor?"
            ),
            "alternativas": {
                "a": "Comprimento do cabo",
                "b": "Potência do motor",
                "c": "Temperatura ambiente",
                "d": "Tipo de eletroduto",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # DADOS DO CIRCUITO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Dados do circuito elétrico",
        },

        {
            "tipo": "texto",
            "texto": (
                "Agora registre as características físicas do percurso entre o quadro e o motor. "
                "Esses dados determinam a resistência do circuito e a queda de tensão."
            ),
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0006",
            "rotulo": "Distância entre quadro e motor",
            "unidade": "m",
            "placeholder": "Ex: 150"
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.001.0007",
            "pergunta": (
                "Se a distância do cabo aumenta, o que acontece com a resistência elétrica?"
            ),
            "alternativas": {
                "a": "Diminui",
                "b": "Permanece constante",
                "c": "Aumenta",
                "d": "Zera",
            },
            "alternativa_correta": "c",
        },

        # -------------------------------------------------
        # DADOS DE INSTALAÇÃO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Condições de instalação",
        },

        {
            "tipo": "video",
            "titulo": "Tipos de instalação de cabos elétricos",
            "descricao": (
                "Observe no vídeo os diferentes métodos de instalação de cabos, como eletroduto embutido, "
                "aparente, bandeja e enterrado. "
                "Essas formas de instalação influenciam diretamente a dissipação de calor do cabo e, "
                "consequentemente, sua capacidade de condução de corrente. "
                "Durante a visita técnica, identifique qual método está sendo utilizado no sistema analisado."
            ),
            "url": "https://www.youtube.com/watch?v=yV9_Rt-ML4g",
            "caption": "Fonte: YouTube",
        },

        {
            "tipo": "texto",
            "texto": (
                "As condições do ambiente influenciam diretamente a capacidade de condução do cabo. "
                "Temperatura e forma de instalação alteram o aquecimento do condutor."
            ),
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0008",
            "rotulo": "Temperatura ambiente",
            "unidade": "°C",
            "placeholder": "Ex: 40"
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.001.0009",
            "pergunta": (
                "Temperaturas mais altas no ambiente causam qual efeito nos cabos?"
            ),
            "alternativas": {
                "a": "Aumentam a capacidade de corrente",
                "b": "Reduzem o aquecimento",
                "c": "Diminuem a capacidade de condução",
                "d": "Não causam efeito",
            },
            "alternativa_correta": "c",
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.001.0010",
            "pergunta": (
                "Qual é o método de instalação do cabo?"
            ),
            "alternativas": {
                "a": "Eletroduto embutido",
                "b": "Eletroduto aparente",
                "c": "Bandeja",
                "d": "Enterrado",
            },
            "alternativa_correta": "a",
        },

        # -------------------------------------------------
        # OBSERVAÇÃO REAL
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Observação do comportamento do sistema",
        },

        {
            "tipo": "texto",
            "texto": (
                "Além dos dados de placa, observe o comportamento real do sistema. "
                "Essas informações ajudam a identificar indícios de problemas elétricos."
            ),
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0011",
            "rotulo": "Tensão medida no motor",
            "unidade": "V",
            "placeholder": "Ex: 365"
        },

        {
            "tipo": "entrada_numerica_inline",
            "id": "problema.01.001.0012",
            "rotulo": "Corrente medida",
            "unidade": "A",
            "placeholder": "Ex: 8.5"
        },

        {
            "tipo": "questao_multipla_escolha",
            "id": "problema.01.001.0013",
            "pergunta": (
                "Se a tensão medida no motor for menor que a nominal, qual é a causa mais provável?"
            ),
            "alternativas": {
                "a": "Excesso de potência do motor",
                "b": "Queda de tensão no cabo",
                "c": "Cabo muito grosso",
                "d": "Alta eficiência do sistema",
            },
            "alternativa_correta": "b",
        },

        # -------------------------------------------------
        # FECHAMENTO
        # -------------------------------------------------

        {
            "tipo": "titulo",
            "texto": "Síntese da coleta de dados",
        },

        {
            "tipo": "texto",
            "texto": (
                "Agora você possui todos os dados necessários para o dimensionamento. "
                "Resumo do que foi coletado:\n\n"
                "- Dados elétricos do motor\n"
                "- Distância do circuito\n"
                "- Condições de instalação\n"
                "- Medições reais de tensão e corrente\n\n"
                "Na próxima etapa, esses dados serão usados para construir o modelo matemático "
                "e verificar se o cabo está corretamente dimensionado."
            ),
        },

    ]