import time
from scanner.universe import get_penny_universe
from scanner.engine import scan_symbol
from services.telegram import send_alert

while True:
    symbols = get_penny_universe()

    print(f"Scanning {len(symbols)} symbols...")

    for s in symbols[:200]:  # حماية من الضغط
        result = scan_symbol(s)

        if result:
            send_alert(result)

    time.sleep(300)
