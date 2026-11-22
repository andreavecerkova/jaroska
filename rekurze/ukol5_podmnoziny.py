# Napište funkci ‹subset_sum›, která zjistí, zda z čísel v seznamu
# ‹numbers› (kladná celá čísla) lze vybrat některá (každé číslo
# nejvýše jednou) tak, aby jejich součet byl přesně ‹target›.
# Prázdný výběr má součet 0.
#
# Funkce vrátí ‹True›, nebo ‹False›. Původní seznam nesmíte měnit.

def subset_sum(numbers, target):
    pass


def main():
    assert subset_sum([], 0) is True
    assert subset_sum([], 5) is False
    assert subset_sum([5], 5) is True
    assert subset_sum([5], 3) is False
    assert subset_sum([3, 34, 4, 12, 5, 2], 9) is True
    assert subset_sum([3, 34, 4, 12, 5, 2], 30) is False
    assert subset_sum([2, 4, 6, 8], 15) is False
    assert subset_sum([7, 11, 13, 17, 19], 50) is True
    assert subset_sum([7, 11, 13, 17, 19], 67) is True
    assert subset_sum([7, 11, 13, 17, 19], 68) is False
    nums = [1, 2, 3]
    subset_sum(nums, 4)
    assert nums == [1, 2, 3]


if __name__ == "__main__":
    main()
