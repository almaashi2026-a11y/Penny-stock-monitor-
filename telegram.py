import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_alert(stock):
    msg = f"""
🚀 PENNY STOCK ALERT

📊 {stock['symbol']}
💰 Price: {stock['price']}$  
📈 Change: {stock['change']}%
📊 RVOL: {stock['rvol']}
🔥 Score: {stock['score']}/100

⚡ Early explosion signal
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
