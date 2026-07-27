import requests

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


def get_calendar():

    try:
        data = requests.get(URL, timeout=10).json()

        hasil = []

        for item in data:

            impact = str(item.get("impact", "")).lower()

            if "high" not in impact:
                continue

            hasil.append({
                "title": item.get("title", ""),
                "country": item.get("country", ""),
                "date": item.get("date", ""),
                "impact": item.get("impact", "")
            })

        return hasil

    except Exception as e:
        print("Calendar Error:", e)
        return []
