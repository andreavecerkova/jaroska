# Napište funkci ‹partitions›, která spočte, kolika způsoby lze
# kladné číslo ‹n› zapsat jako součet kladných celých čísel, přičemž
# na pořadí sčítanců nezáleží. Například číslo 4 lze zapsat pěti
# způsoby: 4, 3+1, 2+2, 2+1+1, 1+1+1+1 (zápisy 3+1 a 1+3 se
# považují za stejný). Pro ‹n› = 0 existuje jeden způsob: prázdný součet.

def partitions(n):
    pass


def main():
    assert partitions(0) == 1
    assert partitions(1) == 1
    assert partitions(2) == 2
    assert partitions(4) == 5
    assert partitions(5) == 7
    assert partitions(10) == 42
    assert partitions(30) == 5604
    assert partitions(50) == 204226


if __name__ == "__main__":
    main()
