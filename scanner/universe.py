import finnhub
import os

client = finnhub.Client(api_key=os.getenv("FINNHUB_KEY"))


def get_symbols():
    # قائمة مبدئية (لاحقًا نكبرها تلقائي)
    symbols = client.stock_symbols("US")

    return [s["symbol"] for s in symbols if s["symbol"]]
