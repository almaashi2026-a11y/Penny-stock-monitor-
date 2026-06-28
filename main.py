import time
from scanner.universe import get_penny_universe
from scanner.engine import scan_symbol
from scanner.ranker import rank_stocks
from services.telegram import send_alert


def scan_market(symbols):
    results = []

    for s in symbols:
        try:
            res = scan_symbol(s)
            if res:
                results.append(res)
        except:
            continue

    return results


while True:
    print("🚀 Scanning market...")

    # 1) جلب كل الأسهم
    symbols = get_penny_universe()

    # 2) فحص الأسهم
    results = scan_market(symbols[:200])  # حماية من الضغط

    # 3) ترتيب أفضل الفرص
    top_stocks = rank_stocks(results)

    # 4) إرسال أفضل 5 فقط
    for stock in top_stocks:
        send_alert(stock)

    print(f"✅ Sent {len(top_stocks)} alerts")

    # 5) انتظار
    time.sleep(300)
