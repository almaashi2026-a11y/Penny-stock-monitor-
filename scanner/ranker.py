def rank_stocks(stocks):
    return sorted(stocks, key=lambda x: x["score"], reverse=True)[:5]
