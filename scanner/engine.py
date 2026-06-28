import finnhub
import os
from scanner.scoring import score_stock

client = finnhub.Client(api_key=os.getenv("FINNHUB_KEY"))


def scan_symbol(symbol):
    q = client.quote(symbol)

    price = q["c"]
    prev = q["pc"]

    if price == 0 or prev == 0:
        return None

    change = ((price - prev) / prev) * 100

    # ❗ فلتر البيني
    if not (0.2 <= price <= 10):
        return None

    # ❗ فلتر أولي للحركة
    if change < 1:
        return None

    # 📊 نحاكي volume (Finnhub محدود في الخطة المجانية)
    rvol = 2 if change > 3 else 1.5

    score = score_stock(change, rvol)

    if score < 60:
        return None

    return {
        "symbol": symbol,
        "price": price,
        "change": round(change, 2),
        "rvol": rvol,
        "score": score
    }
