from economic_calendar import get_calendar, convert_to_wita

for item in get_calendar():
    waktu = convert_to_wita(item["date"])

    print("-----------------------")
    print(item["title"])
    print(item["country"])
    print(waktu.strftime("%d-%m-%Y %H:%M WITA"))
