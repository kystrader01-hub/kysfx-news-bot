from datetime import datetime, timedelta, timezone
import requests

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


def convert_to_wita(utc_time):
    try:
        dt = datetime.fromisoformat(utc_time.replace("Z", "+00:00"))
        wita = timezone(timedelta(hours=8))
        return dt.astimezone(wita)
    except Exception:
        return None


def get_calendar():

    try:

        data = requests.get(URL, timeout=10).json()

        hasil = []

        for item in data:

            impact = str(item.get("impact", "")).lower()

            if "high" not in impact:
                continue

            # Debug sementara
            print(
                item.get("title"),
                "| Previous:", item.get("previous"),
                "| Forecast:", item.get("forecast"),
                "| Actual:", item.get("actual")
            )

            hasil.append({
                "title": item.get("title", ""),
                "country": item.get("country", ""),
                "date": item.get("date", ""),
                "impact": item.get("impact", ""),
                "previous": item.get("previous", ""),
                "forecast": item.get("forecast", ""),
                "actual": item.get("actual", "")
            })

        return hasil

    except Exception as e:

        print("Calendar Error:", e)

        return []
