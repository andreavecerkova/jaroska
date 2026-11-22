# Napište funkci ‹no_two_ones›, která vrátí seznam všech řetězců
# délky ‹n› složených ze znaků ‹"0"› a ‹"1"›, v nichž nejsou dvě
# jedničky bezprostředně za sebou (tedy žádný řetězec neobsahuje
# podřetězec ‹"11"›). Řetězce vraťte seřazené abecedně.
# Pro ‹n› = 0 existuje jediný řetězec: prázdný.

def no_two_ones(n):
    pass


def main():
    assert no_two_ones(0) == [""]
    assert no_two_ones(1) == ["0", "1"]
    assert no_two_ones(2) == ["00", "01", "10"]
    assert no_two_ones(3) == ["000", "001", "010", "100", "101"]
    assert len(no_two_ones(10)) == 144
    assert len(no_two_ones(15)) == 1597
    assert no_two_ones(15)[-1] == "101010101010101"


if __name__ == "__main__":
    main()
