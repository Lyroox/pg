def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5

    
    if isinstance(binarni_cislo, str):
        binary = int(binarni_cislo)
    else:
        binary = binarni_cislo
    
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    
    return decimal


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

test_funkce()
print (bin_to_dec("0"))
print (bin_to_dec(1))
print (bin_to_dec("100"))
print (bin_to_dec(101))
print (bin_to_dec("010101"))
print (bin_to_dec(10000000))
print("Všechna čísla byla úspěšně převedena.")
