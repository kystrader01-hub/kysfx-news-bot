def hitung_sentimen(berita):

    bullish = 0
    bearish = 0
    netral = 0

    kata_bullish = [
        "iran",
        "israel",
        "war",
        "attack",
        "missile",
        "conflict",
        "sanction",
        "nuclear"
    ]

    kata_bearish = [
        "rate hike",
        "hawkish",
        "strong dollar",
        "higher inflation",
        "treasury yield"
    ]

    for item in berita:

        judul = item["title"].lower()

        if any(x in judul for x in kata_bullish):
            bullish += 1

        elif any(x in judul for x in kata_bearish):
            bearish += 1

        else:
            netral += 1

    skor = bullish - bearish

    if skor >= 2:
        bias = "🟢 Bullish Gold"

    elif skor <= -2:
        bias = "🔴 Bearish Gold"

    else:
        bias = "🟡 Netral"

    return {
        "bullish": bullish,
        "bearish": bearish,
        "netral": netral,
        "skor": skor,
        "bias": bias
          }
