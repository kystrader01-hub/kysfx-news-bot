import os
import time
import requests
from datetime import datetime

from news import get_news
from market_brief import get_market_brief
from session import get_market_sessions
from economic_calendar import get_calendar


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
            "🟢 Bullish Gold ⭐⭐⭐⭐⭐\n"
            "💡 Ketegangan geopolitik meningkatkan permintaan emas "
            "sebagai aset safe haven."
        )

    if any(x in j for x in bearish):
        return (
            "🔴 Bearish Gold ⭐⭐⭐⭐\n"
            "💡 Penguatan USD dan kenaikan suku bunga "
            "dapat menekan harga emas."
        )

    return (
        "🟡 Netral ⭐⭐⭐\n"
        "💡 Tunggu konfirmasi arah pasar."
    )


def kirim_telegram(text):

    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": text
            }
        )

        return response.status_code

    except Exception as e:
        print("Telegram Error:", e)
        return None



while True:

    try:

        now = datetime.now()
        waktu = now.strftime("%H:%M")


        # ==========================
        # MARKET OPEN BRIEF
        # ==========================

        jadwal = get_market_sessions()

        if waktu in jadwal.values():

            if last_brief != waktu:

                pesan = get_market_brief()

                status = kirim_telegram(pesan)

                print("Market Brief:", status)

                last_brief = waktu



        # ==========================
        # RESET HARIAN
        # ==========================

        if waktu == "00:00":

            last_brief = ""
            sent_news.clear()



        # ==========================
        # BREAKING NEWS
        # ==========================

        news_list = get_news()


        for news in news_list:

            judul = news["title"]


            if judul not in sent_news:


                analisa_news = analisa(judul)


                pesan = (
                    "🚨 BREAKING NEWS\n\n"
                    f"📂 {news.get('category','📰 Berita Pasar')}\n\n"
                    f"📰 {judul}\n\n"
                    f"{analisa_news}\n\n"
                    f"🔗 {news.get('url','')}"
                )


                status = kirim_telegram(pesan)


                print("News:", status)


                sent_news.add(judul)



        # ==========================
        # BATAS MEMORY
        # ==========================

        if len(sent_news) > 200:

            sent_news.clear()



    except Exception as e:

        print("ERROR:", e)



    time.sleep(60)
