# apps/app_02/sections/problema/conteudos/conteudo_01.py

from __future__ import annotations


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "titulo",
            "texto": "Placa de identificação do motor",
        },
        {
            "tipo": "texto",
            "texto": (
                "Nesta etapa, observe a placa de identificação do motor e "
                "relacione as informações disponíveis com o funcionamento "
                "do sistema de bombeamento."
            ),
        },
        {
            "tipo": "questao_multipla_escolha",
            "id": "q_001",
            "pergunta": "Qual informação da placa indica a potência nominal do motor?",
            "alternativas": {
                "a": "Tensão nominal",
                "b": "Potência nominal",
                "c": "Frequência",
                "d": "Grau de proteção",
            },
            "alternativa_correta": "b",
        },
        {
            "tipo": "texto",
            "texto": (
                "A leitura correta da placa é importante porque ela fornece "
                "dados essenciais para análise técnica e escolha adequada "
                "das condições de operação."
            ),
        },
        {
            "tipo": "video",
            "url": "https://www.youtube.com/watch?v=PSuVujxAcOg",
            "caption": "Vídeo complementar sobre leitura de placa de motor",
        },
        {
            "tipo": "questao_texto",
            "id": "q_002",
            "pergunta": (
                "Explique, com suas palavras, por que a placa de identificação "
                "do motor é importante para a análise do sistema de bombeamento."
            ),
            "placeholder": "Digite sua resposta aqui...",
            "altura": 180,
        },
    ]