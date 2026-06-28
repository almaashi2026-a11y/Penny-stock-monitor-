def calculate_score(change, rvol):
    score = 0

    # 🔥 volume = أهم عامل
    if rvol > 5:
        score += 50
    elif rvol > 3:
        score += 35
    elif rvol > 2:
        score += 20

    # 📈 momentum
    if change > 8:
        score += 40
    elif change > 4:
        score += 25
    elif change > 2:
        score += 10

    return min(score, 100)
