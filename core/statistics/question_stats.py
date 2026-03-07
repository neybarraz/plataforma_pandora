# core/statistics/question_stats.py

def question_accuracy(total, correct):
    if total == 0:
        return 0
    return round((correct/total)*100,2)