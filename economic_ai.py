def analisa_event(event):

    nama = event.get("title", "").lower()

    if "non-farm" in nama or "nfp" in nama:
        return {
            "emoji": "💼",
            "pengaruh": "⭐⭐⭐⭐⭐",
            "bullish": "Actual lebih rendah dari Forecast",
            "bearish": "Actual lebih tinggi dari Forecast"
        }

    elif "cpi" in nama:
        return {
            "emoji": "📈",
            "pengaruh": "⭐⭐⭐⭐⭐",
            "bullish": "Inflasi lebih rendah dari Forecast",
            "bearish": "Inflasi lebih tinggi dari Forecast"
        }

    elif "ppi" in nama:
        return {
            "emoji": "🏭",
            "pengaruh": "⭐⭐⭐⭐",
            "bullish": "PPI lebih rendah dari Forecast",
            "bearish": "PPI lebih tinggi dari Forecast"
        }

    elif "fomc" in nama or "interest rate" in nama:
        return {
            "emoji": "🏦",
            "pengaruh": "⭐⭐⭐⭐⭐",
            "bullish": "Nada dovish / suku bunga turun",
            "bearish": "Nada hawkish / suku bunga naik"
        }

    elif "powell" in nama:
        return {
            "emoji": "🎤",
            "pengaruh": "⭐⭐⭐⭐",
            "bullish": "Komentar dovish",
            "bearish": "Komentar hawkish"
        }

    return {
        "emoji": "📅",
        "pengaruh": "⭐⭐⭐",
        "bullish": "Potensi mendukung Gold",
        "bearish": "Potensi menekan Gold"
  }
