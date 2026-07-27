import os
import time
import requests
from news import get_news

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

sent_news = set()


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
        "tension",
        "sanction",
        "nuclear"
    ]

    bearish = [
        "rate hike",
        "hawkish",
        "higher inflation",
        "strong dollar",
        "treasury yield"
    ]

    if any(x in j for x in bullish):
        return (
            "🟢 Bullish Gold\n"
            "💡 Ketegangan geopolitik meningkatkan permintaan emas sebagai aset safe haven."
        )

    if any(x in j for x in bearish):
        return (
            "🔴 Bearish Gold\n"
            "💡 Penguatan USD dan kenaikan suku bunga dapat menekan harga emas."
        )

    return (
        "🟡 Netral\n"
        "💡 Tunggu konfirmasi arah pasar."
    )


while True:
    try:

        berita = get_news()

        for item in berita:

            if item["link"] not in sent_news:

                pesan = f"""🚨 BREAKING NEWS

📰 {item['title']}

📊 Analisis
{analisa(item['title'])}

🔗 {item['link']}
"""

                response = requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": pesan
                    }
                )

                print(response.status_code)
                print(response.text)

                sent_news.add(item["link"])

        if len(sent_news) > 1000:
            sent_news.clear()

        time.sleep(300)

    except Exception as e:

        print("ERROR:", e)

        time.sleep(60)
