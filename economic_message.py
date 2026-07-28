from datetime import datetime


def buat_pesan_event(event):

    title = event.get("title", "Unknown Event")
    country = event.get("country", "")
    impact = event.get("impact", "High")
    previous = event.get("previous", "-")
    forecast = event.get("forecast", "-")
    actual = event.get("actual", "-")
    waktu = event.get("time", "-")

    nama = title.lower()

    bullish = "Lihat hasil rilis"
    bearish = "Lihat hasil rilis"

    if "non-farm" in nama or "nfp" in nama:
        bullish = f"Actual < {forecast}"
        bearish = f"Actual > {forecast}"

    elif "cpi" in nama:
        bullish = f"Actual < {forecast}"
        bearish = f"Actual > {forecast}"

    elif "ppi" in nama:
        bullish = f"Actual < {forecast}"
        bearish = f"Actual > {forecast}"

    elif "interest rate" in nama or "fomc" in nama:
        bullish = "Suku bunga turun / dovish"
        bearish = "Suku bunga naik / hawkish"

    pesan = f"""🚨 HIGH IMPACT NEWS

🇺🇸 {title}

━━━━━━━━━━━━━━━━━━

⏰ Jadwal
{waktu} WITA

📊 Previous : {previous}
📈 Forecast : {forecast}
❓ Actual : {actual}

━━━━━━━━━━━━━━━━━━

🎯 Dampak Gold

🟢 Bullish Gold
{bullish}

🔴 Bearish Gold
{bearish}

━━━━━━━━━━━━━━━━━━

🔥 Impact
{impact}

━━━━━━━━━━━━━━━━━━

⚠️ Tips Trading

• Hindari entry 5-10 menit sebelum berita
• Waspadai spread melebar
• Tunggu candle konfirmasi
• Gunakan manajemen risiko

━━━━━━━━━━━━━━━━━━

🤖 KysFx News Bot
"""

    return pesan
