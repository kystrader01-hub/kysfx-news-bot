import os
import time
import requests
from datetime import datetime

from news import get_news
from market_brief import get_market_brief
from session import get_market_sessions

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

sent_news = set()
last_brief = ""


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

        now = datetime.now()
        waktu = now.strftime("%H:%M")

        jadwal = get_market_sessions()

        # ==========================
        # MARKET OPEN BRIEF
        # ==========================
        if waktu in jadwal.values():

            if last_brief != waktu:

                response = requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": get_market_brief()
                    }
                )

                print("Market Brief:", response.status_code)

                last_brief = waktu

        # Reset setiap hari
        if waktu == "00:00":
            last_brief = ""

        # ==========================
        # BERITA
        # ==========================
        berita = get_news()

        for item in berita:

            if item["link"] not in sent_news:

                pesan = f"""🚨 BREAKING NEWS

📂 {item['category']}

📰 {item['title']}

{item['impact']}

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

        # Cek setiap 1 menit
        time.sleep(60)

    except Exception as e:

        print("ERROR:", e)

        time.sleep(60)
