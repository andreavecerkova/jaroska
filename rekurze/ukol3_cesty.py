# Máme mřížku s ‹rows› řádky a ‹cols› sloupci. Začínáme v levém horním
# rohu (políčko ‹(0, 0)›) a chceme se dostat do pravého dolního rohu
# (políčko ‹(rows - 1, cols - 1)›). Z každého políčka se smíme posunout
# buď o jedno políčko doprava, nebo o jedno políčko dolů.
#
# Některá políčka jsou zablokovaná: množina ‹blocked› obsahuje jejich
# souřadnice ‹(řádek, sloupec)›. Na zablokované políčko nesmíme vstoupit.
#
# Napište funkci ‹count_paths›, která spočte, kolika různými cestami
# se z levého horního rohu do pravého dolního dostaneme.
#
# Pozor: poslední dva testy jsou záludné. Zvládne váš program i velkou
# mřížku v rozumném čase?

def count_paths(rows, cols, blocked):
    pass


def main():
    assert count_paths(1, 1, set()) == 1
    assert count_paths(2, 2, set()) == 2
    assert count_paths(3, 3, set()) == 6
    assert count_paths(3, 3, {(1, 1)}) == 2
    assert count_paths(3, 3, {(0, 1), (1, 0)}) == 0
    assert count_paths(3, 4, {(1, 2)}) == 4
    assert count_paths(10, 10, set()) == 48620
    assert count_paths(18, 18, set()) == 2333606220
    assert count_paths(18, 18, {(9, 9)}) == 1707866820


if __name__ == "__main__":
    main()
