from ..storage import save_question_response

def save_answer(username, node_id, question_id, value):
    section = "engine"  # 🔥 agora válido

    full_question_id = f"{node_id}.{question_id}"

    return save_question_response(
        username=username,
        section=section,
        question_id=full_question_id,
        question_type="texto",
        pergunta="Pergunta teste",
        resposta=value,
    )