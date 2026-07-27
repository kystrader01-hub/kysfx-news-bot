import feedparser
from deep_translator import GoogleTranslator

RSS_URL = "https://www.forexlive.com/feed/"

KEYWORDS = [
    "gold",
    "xau",
    "fed",
    "fomc",
    "cpi",
    "nfp",
    "iran",
    "israel",
    "usa",
    "united states",
    "china",
    "russia",
    "middle east",
    "usd",
    "powell",
    "trump",
    "tariff",
    "oil",
    "opec"
]


def dampak(title):
    t = title.lower()

    bullish = [
        "iran",
        "israel",
        "war",
        "missile",
        "attack",
        "conflict",
        "middle east",
        "nuclear",
        "sanction"
    ]

    bearish = [
        "rate hike",
        "hawkish",
        "strong dollar",
        "higher inflation",
        "treasury yield"
    ]

    if any(x in t for x in bullish):
        return "🟢 Dampak : Bullish Gold ⭐⭐⭐⭐⭐"

    if any(x in t for x in bearish):
        return "🔴 Dampak : Bearish Gold ⭐⭐⭐⭐"

    return "🟡 Dampak : Netral ⭐⭐⭐"


def get_news():

    feed = feedparser.parse(RSS_URL)

    berita = []

    for item in feed.entries[:20]:

        title = item.title

        if any(k.lower() in title.lower() for k in KEYWORDS):

            try:
                title_id = GoogleTranslator(
                    source="auto",
                    target="id"
                ).translate(title)
            except:
                title_id = title

            berita.append({
                "title": title_id,
                "impact": dampak(title),
                "link": item.link
            })

    return berita
