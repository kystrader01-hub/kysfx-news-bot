import os
import time
import requests
from news import get_news

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

sent = set()

while True:
    try:
        news = get_news()

        for item in news:
            if item["link"] not in sent:

                text = f"""🚨 BREAKING NEWS

📰 {item['title']}

🔗 {item['link']}
"""

                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": text
                    }
                )

                sent.add(item["link"])

        time.sleep(300)

    except Exception as e:
        print(e)
        time.sleep(60)
