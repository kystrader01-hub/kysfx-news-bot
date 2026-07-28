def hitung_volatilitas(berita):

    skor = 0

    for item in berita:

        impact = item.get("impact", "").lower()

        if "⭐⭐⭐⭐⭐" in impact:
            skor += 5

        elif "⭐⭐⭐⭐" in impact:
            skor += 4

        elif "⭐⭐⭐" in impact:
            skor += 3

        elif "⭐⭐" in impact:
            skor += 2

        elif "⭐" in impact:
            skor += 1

    if skor >= 30:
        return "⭐⭐⭐⭐⭐", "SANGAT TINGGI"

    elif skor >= 20:
        return "⭐⭐⭐⭐☆", "TINGGI"

    elif skor >= 10:
        return "⭐⭐⭐☆☆", "SEDANG"

    else:
        return "⭐⭐☆☆☆", "RENDAH"
