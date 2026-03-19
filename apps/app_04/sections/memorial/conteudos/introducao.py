from __future__ import annotations


def get_pagina() -> dict:
    return {
        "id": "memorial_01",
        "titulo": "Introdução",
        "titulo_menu": "Introdução",
        "conteudos": [
            {
                "id": "memorial_01_001",
                "titulo": "1. CONTEXTO E DEFINIÇÃO DO PROBLEMA",
                "titulo_menu": "Contexto e problema",
                "blocos": [
                    {
                        "tipo": "texto",
                        "texto": (
                            "Esta primeira parte do memorial técnico deve situar o leitor e apresentar com clareza "
                            "o problema investigado. O objetivo é mostrar **onde o estudo ocorre**, **qual é o sistema "
                            "analisado**, **qual efeito foi observado** e **qual pergunta técnica guiou o trabalho**."
                        ),
                    },
                    {
                        "tipo": "alerta",
                        "nivel": "info",
                        "texto": (
                            "Evite opiniões soltas. Descreva a situação de forma técnica, concreta e objetiva."
                        ),
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "1.1 Situação do sistema",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_01_001_q_0001",
                        "pergunta": "Descreva o ambiente ou sistema analisado.",
                        "placeholder": (
                            "Onde ocorre o estudo? Qual é a função do sistema? Quem é afetado pelo problema observado?"
                        ),
                        "altura": 180,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "1.2 Problema identificado",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_01_001_q_0002",
                        "pergunta": "Explique qual problema técnico motivou a investigação.",
                        "placeholder": (
                            "O que está inadequado? Qual efeito foi observado? Por que essa situação merece análise?"
                        ),
                        "altura": 180,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "1.3 Recorte da análise",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_01_001_q_0003",
                        "pergunta": "Delimite o recorte adotado no estudo.",
                        "placeholder": (
                            "O que foi analisado? O que ficou fora? Qual foi a fronteira técnica da investigação?"
                        ),
                        "altura": 170,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "1.4 Pergunta técnica",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_01_001_q_0004",
                        "pergunta": "Formule a pergunta central do trabalho.",
                        "placeholder": (
                            "Ex.: Existe diferença significativa de temperatura entre regiões da sala?"
                        ),
                        "altura": 120,
                    },
                    {
                        "tipo": "subtitulo",
                        "texto": "1.5 Objetivo do trabalho",
                    },
                    {
                        "tipo": "questao_texto",
                        "id": "memorial_01_001_q_0005",
                        "pergunta": "Declare o objetivo técnico do trabalho.",
                        "placeholder": (
                            "O que o trabalho pretende demonstrar, avaliar, comparar ou explicar?"
                        ),
                        "altura": 140,
                    },
                ],
            }
        ],
    }