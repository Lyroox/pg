def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    slovnik_jednotky = {0:"nula", 1:"jedna", 2:"dva", 3:"tři", 4:"čtyři", 5:"pět", 6:"šest", 7:"sedm", 8:"osm", 9:"devět"}
    slovnik_nact = {11:"jedenáct", 12:"dvanáct", 13:"třináct", 14:"čtrnáct", 15:"patnáct", 16:"šestnáct", 17:"sedmnáct", 18:"osmnáct", 19:"devatenáct"}
    slovnik_desitky = {10:"deset", 20:"dvacet", 30:"třicet", 40:"čtyřicet", 50:"padesát", 60:"šedesát", 70:"sedmdesát", 80:"osmdesát", 90:"devadesát", 100:"sto"}
    
    try:
        cislo=int(cislo)
        
        if cislo >= 0 and cislo <= 100:

            if cislo in slovnik_jednotky:
                return  f"{slovnik_jednotky[cislo]}"
        
            elif cislo in slovnik_nact:
                return  f"{slovnik_nact [cislo]}"
        
            elif cislo in slovnik_desitky:
                return  f"{slovnik_desitky [cislo]}"
        
            else:
                desitky = (cislo // 10) * 10
                jednotky = cislo % 10
                return  f"{slovnik_desitky[desitky]} {slovnik_jednotky[jednotky]}"
            
        # pokud číslo nesplňuje podmínky, vypíše upozornění
        else:
            return f"Číslo {cislo} má špatnou hodnotu!"
        
    # pokud uživatel zadá cokoliv jiného než číslo    
    except ValueError:
        return "Zadaný znak není platný!"
    

if __name__ == "__main__":
    cislo = int(input("Zdravím, zadejte číslo: "))
    text = cislo_text(cislo)
    print(text)