from ..storage import save_question_response


def save_answer(
    username,
    node_id,
    question_id,
    value,
    *,
    tipo="texto",
    pergunta="",
    alternativas=None,
):
    return save_question_response(
        username=username,
        section="engine",
        question_id=f"{node_id}.{question_id}",
        question_type=tipo,
        pergunta=pergunta,
        resposta=value,
        alternativas=alternativas,
    )
