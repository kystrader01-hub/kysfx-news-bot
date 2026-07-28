def ai_summary(sentimen, volatilitas):

    bias = sentimen["bias"]
    skor = sentimen["skor"]

    if "Bullish" in bias:

        if volatilitas["level"] in ["TINGGI", "SANGAT TINGGI"]:

            return (
                "Mayoritas berita mendukung penguatan harga emas. "
                "Sentimen safe haven masih dominan dan volatilitas tinggi "
                "berpotensi memicu pergerakan harga yang lebih besar. "
                "Tetap tunggu konfirmasi sebelum entry."
            )

        return (
            "Sentimen pasar masih cenderung mendukung kenaikan emas. "
            "Namun volatilitas belum terlalu tinggi sehingga disiplin "
            "menunggu konfirmasi tetap penting."
        )

    elif "Bearish" in bias:

        return (
            "Berita hari ini lebih banyak mendukung penguatan USD "
            "sehingga berpotensi menekan harga emas. "
            "Perhatikan data ekonomi AS sebelum membuka posisi."
        )

    else:

        if skor == 0:

            return (
                "Sentimen pasar masih berimbang. "
                "Belum ada katalis yang cukup kuat untuk menentukan arah. "
                "Fokus pada konfirmasi dari price action."
            )

        return (
            "Sentimen pasar masih bercampur sehingga arah emas "
            "belum sepenuhnya jelas. "
            "Gunakan manajemen risiko dengan disiplin."
                                    )
