import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🤖 KysFx Bot berhasil online!\n\nSelanjutnya saya akan mulai mengirim berita XAU/USD."
}

requests.post(url, data=data)

print("Pesan berhasil dikirim.")
