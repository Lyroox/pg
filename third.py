import math

def je_prvocislo(cislo):
    #funkce zkontroluje, jestli je číslo prvočíslo, a podle toho vrací True nebo False
    
    if cislo <= 1:
        return False  #číslo 1 a menší nejsou prvočísla
    
    delitel_limit = int(math.sqrt(cislo))
    for delitel in range(2, delitel_limit + 1):
        if cislo % delitel == 0:
            return False  #nalezen dělitel čísla, tedy číslo není prvočíslo
    
    return True  #číslo je prvočíslo

def vrat_prvocisla(maximum):
    #funkce spočítá všechna prvočísla v rozsahu 1 až maximum a vrátí je jako seznam
    
    prvocisla = []
    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla


if __name__ == "__main__":
    uzivatel_cislo = int(input("Zadej maximální číslo pole: "))
    prvocisla = vrat_prvocisla(uzivatel_cislo)

    print(f"Prvočísla od 1 do {uzivatel_cislo}: {prvocisla}")