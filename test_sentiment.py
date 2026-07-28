from news import get_news
from sentiment import hitung_sentimen

hasil = hitung_sentimen(get_news())

print(hasil)
