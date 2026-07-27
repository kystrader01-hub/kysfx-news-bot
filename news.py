import feedparser
from deep_translator import GoogleTranslator

RSS_URL = "https://www.forexlive.com/feed/"

KEYWORDS = [
    "gold",
    "xau",
    "fed",
    "fomc",
    "powell",
    "cpi",
    "core cpi",
    "nfp",
    "non-farm",
    "ppi",
    "pce",
    "gdp",
    "interest rate",
    "rate decision",
    "inflation",
    "usd",
    "dollar",
    "treasury",
    "yield",
    "iran",
    "israel",
    "russia",
    "ukraine",
    "china",
    "taiwan",
    "middle east",
    "oil",
    "opec",
    "trump"
]


def dampak(title):
    t = title.lower()

    if any(x in t for x in [
        "iran",
        "israel",
        "war",
        "missile",
        "attack",
        "conflict",
        "middle east",
        "nuclear",
        "sanction"
    ]):
        return "🟢 Dampak : Bullish Gold ⭐⭐⭐⭐⭐"

    if any(x in t for x in [
        "rate hike",
        "hawkish",
        "strong dollar",
        "higher inflation",
        "treasury yield"
    ]):
        return "🔴 Dampak : Bearish Gold ⭐⭐⭐⭐"

    return "🟡 Dampak : Netral ⭐⭐⭐"


def kategori(title):
    t = title.lower()

    if any(x in t for x in [
        "iran",
        "israel",
        "war",
        "missile",
        "middle east",
        "conflict"
    ]):
        return "🌍 Geopolitik"

    if any(x in t for x in [
        "fed",
        "fomc",
        "powell",
        "interest rate",
        "rate decision"
    ]):
        return "🏦 Federal Reserve"

    if any(x in t for x in [
        "cpi",
        "core cpi",
        "ppi",
        "pce",
        "inflation"
    ]):
        return "📈 Inflasi"

    if any(x in t for x in [
        "nfp",
        "employment",
        "payroll",
        "job"
    ]):
        return "💼 Tenaga Kerja"

    if any(x in t for x in [
        "oil",
        "opec"
    ]):
        return "🛢️ Energi"

    return "📰 Berita Pasar"


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
            except Exception:
                title_id = title

            berita.append({
                "title": title_id,
                "impact": dampak(title),
                "category": kategori(title),
                "link": item.link
            })

    return berita
