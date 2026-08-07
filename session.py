from datetime import datetime
from zoneinfo import ZoneInfo


def get_market_sessions():
    """
    Jadwal Market Open (WITA)
    Menggunakan timezone asli sehingga DST dihitung otomatis.
    """

    london = datetime.now(ZoneInfo("Europe/London"))
    newyork = datetime.now(ZoneInfo("America/New_York"))

    # Cek DST
    london_dst = london.dst().total_seconds() != 0
    newyork_dst = newyork.dst().total_seconds() != 0

    # Asia tidak memakai DST
    asia = "07:50"

    # Frankfurt mengikuti DST Eropa
    frankfurt = "12:50" if london_dst else "13:50"

    # London
    london = "13:50" if london_dst else "14:50"

    # New York
    newyork = "18:50" if newyork_dst else "19:50"

    return {
        "asia": asia,
        "frankfurt": frankfurt,
        "london": london,
        "newyork": newyork
    }
