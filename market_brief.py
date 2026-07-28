from datetime import datetime
from news import get_news


def get_market_brief():

    berita = get_news()

    top_news = berita[:3]

    daftar = ""

    if len(top_news) == 0:
        daftar = "• Belum ada berita penting.\n"
    else:
        for item in top_news:
            daftar += f"• {item['title']}\n"

    jam = datetime.now().hour

    if 8 <= jam < 15:
        sesi = "🌏 ASIA MARKET OPEN"
    elif 15 <= jam < 20:
        sesi = "🇬🇧 LONDON MARKET OPEN"
    else:
        sesi = "🇺🇸 NEW YORK MARKET OPEN"

    pesan = f"""📈 {sesi}

━━━━━━━━━━━━━━━━━━

📊 Bias Hari Ini
🟡 Menunggu Konfirmasi

━━━━━━━━━━━━━━━━━━

📰 3 Berita Teratas

{daftar}

━━━━━━━━━━━━━━━━━━

⚠️ Yang Perlu Diperhatikan

• Perhatikan kekuatan USD
• Pantau berita berdampak tinggi
• Tunggu konfirmasi sebelum entry

━━━━━━━━━━━━━━━━━━

🎯 Rencana Trading

✓ Ikuti trend utama
✓ Jangan FOMO
✓ Gunakan manajemen risiko
✓ Risk maksimal sesuai trading plan

━━━━━━━━━━━━━━━━━━

🤖 KysFx News Bot
"""

    return pesan
