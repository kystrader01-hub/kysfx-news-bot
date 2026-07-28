from datetime import datetime


def is_dst():
    """
    Perkiraan DST:
    Maret - Oktober = DST aktif
    November - Februari = DST tidak aktif
    """

    bulan = datetime.utcnow().month

    return 3 <= bulan <= 10


def get_market_sessions():

    if is_dst():

        return {
            "asia": "07:50",
            "frankfurt": "12:50",
            "london": "13:50",
            "newyork": "18:50"
        }

    else:

        return {
            "asia": "07:50",
            "frankfurt": "13:50",
            "london": "14:50",
            "newyork": "19:50"
        }
