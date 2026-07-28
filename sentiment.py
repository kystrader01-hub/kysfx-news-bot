def hitung_sentimen(berita):

    bullish = 0
    bearish = 0
    netral = 0

    kata_bullish = [
        "iran", "israel", "war", "attack", "missile",
        "conflict", "sanction", "nuclear",
        "safe haven", "gold demand"
    ]

    kata_bearish = [
        "rate hike", "hawkish", "higher inflation",
        "strong dollar", "treasury yield",
        "fed tightening"
    ]

    for item in berita:

        judul = item["title"].lower()

        if any(k in judul for k in kata_bullish):
            bullish += 1

        elif any(k in judul for k in kata_bearish):
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

    total = bullish + bearish + netral

    if total == 0:
        confidence = 0
    else:
        confidence = round(max(bullish, bearish) / total * 100)

    return {
        "bullish": bullish,
        "bearish": bearish,
        "netral": netral,
        "skor": skor,
        "bias": bias,
        "confidence": confidence
            }
