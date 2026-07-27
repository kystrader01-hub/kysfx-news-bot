from datetime import datetime, timedelta, timezone
import requests

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


def get_calendar():
def convert_to_wita(utc_time):
    try:
        dt = datetime.fromisoformat(utc_time.replace("Z", "+00:00"))
        wita = timezone(timedelta(hours=8))
        return dt.astimezone(wita)
    except Exception:
        return None
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
