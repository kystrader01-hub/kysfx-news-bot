import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/getMe"

r = requests.get(url)

print("Status:", r.status_code)
print("Response:", r.text)
