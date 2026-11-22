# Hanojské věže: na tyči ‹source› leží ‹n› disků (nahoře nejmenší).
# Disky je třeba přemístit na tyč ‹target›, přičemž smíte přesouvat
# vždy jen jeden disk a nikdy nesmíte položit větší disk na menší.
# K dispozici je ještě pomocná tyč ‹spare›.
#
# Napište funkci ‹hanoi›, která vrátí seznam tahů (dvojic
# ‹(odkud, kam)›) v pořadí, v jakém je máte provést, a to
# s nejmenším možným počtem tahů. Pro ‹n› = 0 vrátí prázdný seznam.

def hanoi(n, source, target, spare):
    pass


def main():
    assert hanoi(0, "A", "C", "B") == []
    assert hanoi(1, "A", "C", "B") == [("A", "C")]
    assert hanoi(2, "A", "C", "B") == [("A", "B"), ("A", "C"), ("B", "C")]
    assert hanoi(3, "A", "C", "B") == [
        ("A", "C"), ("A", "B"), ("C", "B"), ("A", "C"),
        ("B", "A"), ("B", "C"), ("A", "C"),
    ]
    assert hanoi(2, "X", "Y", "Z") == [("X", "Z"), ("X", "Y"), ("Z", "Y")]
    assert len(hanoi(10, "A", "C", "B")) == 1023
    assert len(hanoi(16, "A", "C", "B")) == 65535


if __name__ == "__main__":
    main()
