
import sys
""""
# funkce vrati treti prvek ze seznamu, pokud ma mene nez 3 prvky, vrati None
def vrat_treti(seznam):
    if len(seznam)<3:
        return None
    else:
        return seznam[2]

# funkce spocita prumer z hodnot v seznamu, pouzijte sum(), len()
def udelej_prumer(seznam):
    return sum(seznam) / len(seznam)
"""""

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    jmeno = slovnik["jmeno"]
    prijmeni = slovnik["prijmeni"]
    vek = slovnik["vek"]
    znamky = slovnik["znamky"]
    return f"Jméno: {jmeno}, Přijmení: {prijmeni}, Věk: {vek}, Průměrná známka: {round(sum(znamky) / len(znamky), 2)}"


if __name__ == "__main__":
    #print(vrat_treti([9,8,7,6,5]))      #vrati 7
    #print(udelej_prumer([9,8,7,6,5]))   #vrati "c"
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))

    #obalka = [9, 8, 7, 6, 5]
    #vysledek = udelej_prumer(obalka)
    #print(vysledek)