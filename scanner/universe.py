import finnhub
import os

client = finnhub.Client(api_key=os.getenv("FINNHUB_KEY"))


def get_penny_universe():
    symbols = client.stock_symbols("US")

    filtered = []

    for s in symbols:
        sym = s["symbol"]

        # 🔥 فلترة نظيفة للأسهم فقط
        if (
            sym.isalpha() and
            1 <= len(sym) <= 5 and
            not sym.endswith("W") and
            not sym.endswith("R")
        ):
            filtered.append(sym)

    # 🔥 تقليل الضغط على النظام
    return filtered[:2000]
