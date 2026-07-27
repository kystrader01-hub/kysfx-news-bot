from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")

if TOKEN:
    print("Bot siap dijalankan")
else:
    print("BOT_TOKEN belum diatur")
