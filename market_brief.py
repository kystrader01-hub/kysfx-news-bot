from datetime import datetime

def get_market_brief():

    now = datetime.now()

    jam = now.hour

    if 8 <= jam < 15:
        sesi = "🌏 ASIA"

    elif 15 <= jam < 20:
        sesi = "🇬🇧 LONDON"

    else:
        sesi = "🇺🇸 NEW YORK"

    return f"""📈 MARKET OPEN BRIEF

{sesi}

━━━━━━━━━━━━━━

📊 Bias
🟡 Menunggu konfirmasi

⚠️ Fokus

• Perhatikan kekuatan USD
• Pantau berita berdampak tinggi
• Tunggu konfirmasi sebelum entry

🎯 Disiplin trading lebih penting daripada banyak entry.
"""
