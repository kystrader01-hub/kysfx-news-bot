import feedparser
from deep_translator import GoogleTranslator

RSS_URL = "https://www.forexfactory.com/ffcal_week_this.xml"

HIGH_IMPACT = [
    "Non-Farm Payroll",
    "CPI",
    "Core CPI",
    "FOMC",
    "Interest Rate",
    "PPI",
    "PCE",
    "GDP",
    "Retail Sales",
    "Powell"
]


def get_calendar():

    feed = feedparser.parse(RSS_URL)

    kalender = []

    for item in feed.entries:

        title = item.title

        if any(x.lower() in title.lower() for x in HIGH_IMPACT):

            try:
                title = GoogleTranslator(
                    source="auto",
                    target="id"
                ).translate(title)
            except:
                pass

            kalender.append({
                "title": title,
                "date": item.get("published", ""),
                "impact": "⭐⭐⭐⭐⭐"
            })

    return kalender
