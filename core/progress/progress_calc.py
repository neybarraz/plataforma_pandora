# core/progress/progress_calc.py

def calculate_progress(answered, total):
    if total == 0:
        return 0
    return round((answered/total)*100,2)