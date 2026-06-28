import finnhub
import os

client = finnhub.Client(api_key=os.getenv("FINNHUB_KEY"))


def get_penny_universe():
    symbols = client.stock_symbols("US")

    filtered = []

    for s in symbols:
        sym = s["symbol"]

        # فلترة أولية فقط لتخفيف الضغط
        if sym.isalpha() and 1 <= len(sym) <= 5:
            filtered.append(sym)

    return filtered
