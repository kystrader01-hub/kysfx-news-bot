import os
import time
import requests
from news import get_news

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

sent = set()

def analisa(judul):
    j = judul.lower()

    bullish = [
        "iran",
        "israel",
        "war",
        "missile",
        "attack",
        "middle east",
        "conflict",
        "tension"
    ]

    bearish = [
        "rate hike",
        "hawkish",
        "strong dollar",
        "higher inflation"
    ]

    if any(x in j for x in bullish):
        return "🟢 Bullish Gold\n💡 Ketegangan geopolitik meningkatkan permintaan emas sebagai safe haven."

    if any(x in j for x in bearish):
        return "🔴 Bearish Gold\n💡 Dolar AS berpotensi menguat sehingga emas bisa tertekan."

    return "🟡 Netral\n💡 Tunggu konfirmasi pergerakan harga."

while True:
    try:
        berita = get_news()

        for item in berita:

            if item["link"] not in sent:

                pesan = f"""
🚨 BREAKING NEWS

📰 {item['title']}

📊 Analisis
{analisa(item['title'])}

🔗 {item['link']}
"""

                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": pesan
                    }
                )

                sent.add(item["link"])

        time.sleep(300)

    except Exception as e:
        print(e)
        time.sleep(60)
