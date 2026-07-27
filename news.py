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
    "trump"
]

def get_news():
    feed = feedparser.parse(RSS_URL)
    news = []

    for item in feed.entries[:10]:
        title = item.title

        if any(keyword.lower() in title.lower() for keyword in KEYWORDS):

            try:
                judul_id = GoogleTranslator(
                    source="auto",
                    target="id"
                ).translate(title)
            except:
                judul_id = title

            news.append({
                "title": judul_id,
                "link": item.link
            })

    return news
