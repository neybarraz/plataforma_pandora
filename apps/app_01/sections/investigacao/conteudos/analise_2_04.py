from __future__ import annotations


CONTEUDO_ID = "em_construcao"


def get_blocos() -> list[dict]:
    return [
        {
            "tipo": "texto",
            "texto": (
                "#### Ambiente em desenvolvimento\n"
                "Este ambiente ainda está em construção. "
                "Estamos trabalhando para disponibilizar os conteúdos e ferramentas "
                "de investigação científica em breve."
            ),
        },
        {
            "tipo": "texto",
            "texto": (
                "Nosso objetivo é oferecer um espaço interativo para análise, "
                "experimentação e construção de conhecimento científico. "
                "Novas funcionalidades e conteúdos serão adicionados gradualmente."
            ),
        },
        {
            "tipo": "alerta",
            "nivel": "info",
            "texto": (
                "Em breve este ambiente estará disponível para uso completo. "
                "Agradecemos sua paciência enquanto finalizamos a estrutura do sistema."
            ),
        },
    ]