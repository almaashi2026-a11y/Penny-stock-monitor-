import finnhub
import os

client = finnhub.Client(api_key=os.getenv("FINNHUB_KEY"))


def get_penny_universe():
    symbols = client.stock_symbols("US")

    filtered = []

    for s in symbols:
        sym = s["symbol"]

        # 🔥 فلترة ذكية وخفيفة
        if (
            sym.isalpha() and
            1 <= len(sym) <= 5 and
            not sym.endswith("W") and
            not sym.endswith("R") and
            not "." in sym
        ):
            filtered.append(sym)

    # 🔥 تقليل الضغط (مهم جداً)
    return filtered[:1500]
