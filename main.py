import os
import time
import requests
from news import get_news
from calendar import get_calendar

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

sent_news = set()
sent_calendar = set()


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
            "💡 Ketegangan geopolitik meningkatkan permintaan emas sebagai safe haven."
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

        # ==========================
        # BERITA
        # ==========================
        berita = get_news()

        for item in berita:

            if item["link"] not in sent_news:

                pesan = f"""🚨 BREAKING NEWS

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

                sent_news.add(item["link"])

        # ==========================
        # KALENDER EKONOMI
        # ==========================
        kalender = get_calendar()

        for item in kalender:

            key = f"{item['title']}_{item['date']}_{item['time']}"

            if key not in sent_calendar:

                pesan = f"""📅 KALENDER EKONOMI

🌍 Negara : {item['country']}

📌 Berita :
{item['title']}

🕒 Jadwal :
{item['date']} {item['time']}

⚠️ Dampak:
Berpotensi menyebabkan volatilitas tinggi pada XAU/USD.
"""

                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": pesan
                    }
                )

                sent_calendar.add(key)

        if len(sent_news) > 1000:
            sent_news.clear()

        if len(sent_calendar) > 500:
            sent_calendar.clear()

        # Tunggu 5 menit
        time.sleep(300)

    
    except Exception as e:

        print("ERROR:", e)

        try:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": f"⚠️ Error Bot\n\n{str(e)}"
                }
            )
        except Exception:
            pass

        time.sleep(60)
