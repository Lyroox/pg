def dec_to_bin(cislo):
    # Funkce převede číslo na binární reprezentaci (cislo může být str i int)
    # 7 -> "111"
    # 5 -> "101"

    if isinstance(cislo, str):
        cislo = int(cislo)

    if cislo == 0:
        return "0"

    binarni_cislo = ""
    while cislo > 0:
        binarni_cislo = str(cislo % 2) + binarni_cislo
        cislo = cislo // 2

    return binarni_cislo


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

    print(dec_to_bin("0"))
    print(dec_to_bin(1))
    print(dec_to_bin("100"))
    print(dec_to_bin(101))
    print(dec_to_bin(127))
    print(dec_to_bin("128"))
    print("Všechna čísla byla úspěšně převedena.")


test_bin_to_dec()
