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


    high_impact = [
        "fomc",
        "fed",
        "federal reserve",
        "interest rate",
        "rate decision",
        "central bank",
        "powell",
        "cpi",
        "core cpi",
        "nfp",
        "non farm",
        "payroll",
        "inflation",
        "boj",
        "ecb"
    ]


    geopolitik = [
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


    usd_yield = [
        "strong dollar",
        "hawkish",
        "treasury yield",
        "higher yield",
        "rate hike"
    ]


    oil = [
        "oil",
        "opec",
        "crude",
        "brent",
        "wti"
    ]


    if any(x in j for x in high_impact):

        return (
            "⚠️ High Impact News ⭐⭐⭐⭐⭐\n\n"
            "🟡 Gold:\n"
            "Potensi volatilitas tinggi. Tunggu reaksi harga.\n\n"
            "💵 USD:\n"
            "Perhatikan arah dolar setelah rilis data/kebijakan.\n\n"
            "📈 Yield:\n"
            "Kenaikan yield dapat menekan Gold.\n\n"
            "🛢️ Oil:\n"
            "Perubahan minyak dapat mempengaruhi ekspektasi inflasi."
        )


    if any(x in j for x in geopolitik):

        return (
            "🟢 Bullish Gold ⭐⭐⭐⭐⭐\n\n"
            "🟡 Gold:\n"
            "Safe haven meningkat akibat risiko geopolitik.\n\n"
            "💵 USD:\n"
            "Permintaan aset aman dapat meningkat.\n\n"
            "📈 Yield:\n"
            "Yield menjadi perhatian pasar.\n\n"
            "🛢️ Oil:\n"
            "Risiko konflik dapat mendorong harga minyak."
        )


    if any(x in j for x in usd_yield):

        return (
            "🔴 Bearish Gold ⭐⭐⭐⭐\n\n"
            "🟡 Gold:\n"
            "Tekanan dari USD dan yield tinggi.\n\n"
            "💵 USD:\n"
            "USD menguat dapat membebani emas.\n\n"
            "📈 Yield:\n"
            "Yield tinggi biasanya negatif untuk Gold."
        )


    if any(x in j for x in oil):

        return (
            "🟡 Oil Impact ⭐⭐⭐\n\n"
            "🛢️ Oil:\n"
            "Perubahan minyak dapat mempengaruhi inflasi.\n\n"
            "🟡 Gold:\n"
            "Perhatikan respon pasar terhadap inflasi."
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
        print("Sekarang :", waktu)
print("Jadwal :", jadwal)

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
