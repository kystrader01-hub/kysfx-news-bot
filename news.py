import feedparser

RSS_URL = "https://www.forexlive.com/feed/"

KEYWORDS = [
    "gold", "xau", "fed", "fomc", "cpi", "nfp",
    "iran", "israel", "usa", "united states",
    "china", "russia", "middle east"
]

def get_news():
    feed = feedparser.parse(RSS_URL)
    news = []

    for item in feed.entries[:10]:
        title = item.title

        if any(k.lower() in title.lower() for k in KEYWORDS):
            news.append({
                "title": title,
                "link": item.link
            })

    return news
