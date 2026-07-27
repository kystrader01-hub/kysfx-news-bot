import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🤖 Test KysFx Bot"
}

r = requests.post(url, data=data)

print("Status:", r.status_code)
print("Response:", r.text)
