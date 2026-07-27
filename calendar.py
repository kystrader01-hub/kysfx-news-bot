import requests
from datetime import datetime

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

HIGH = [
    "Non-Farm Employment Change",
    "CPI",
    "Core CPI",
    "Federal Funds Rate",
    "FOMC Statement",
    "FOMC Press Conference",
    "Fed Chair Powell Speaks",
    "GDP",
    "Core PCE Price Index",
    "PPI"
]

def get_calendar():
    try:
        data = requests.get(URL, timeout=10).json()

        hasil = []

        for item in data:

            title = item.get("title", "")

            if any(x.lower() in title.lower() for x in HIGH):

                hasil.append({
                    "title": title,
                    "country": item.get("country", ""),
                    "date": item.get("date", ""),
                    "time": item.get("time", "")
                })

        return hasil

    except:
        return []
