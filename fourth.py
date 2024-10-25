def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    # Ověří, zda je cílová pozice na šachovnici
    radek, sloupec = cilova_pozice
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

    # Ověří, zda je cílová pozice volná
    if cilova_pozice in obsazene_pozice:
        return False
    
    # Ověří, zda se figurka může přesunout na danou pozici.
    typ_figurky = figurka["typ"]
    vychozi_radek, vychozi_sloupec = figurka["pozice"]

    # Pravidla pro pohyb figurek

    # Pěšec
    if typ_figurky == "pěšec":
        # Pěšec se může posunout o 1 pole vpřed
        if radek == vychozi_radek + 1 and sloupec == vychozi_sloupec:
            return True  
        # Pěšec se může posunout o 2 pole vpřed pouze z 1. řady
        if vychozi_radek == 1 and radek == vychozi_radek + 1 and sloupec == vychozi_sloupec:
            if (vychozi_radek + 1, sloupec) not in obsazene_pozice:  # Kontrola, zda je pole před volné
                return True  

    # Jezdec
    elif typ_figurky == "jezdec":
        if (abs(radek - vychozi_radek), abs(sloupec - vychozi_sloupec)) in [(2, 1), (1, 2)]:
            return True  # Jezdec se může pohnout
    
    # Věž
    elif typ_figurky == "věž":
        if radek == vychozi_radek or sloupec == vychozi_sloupec:
            radek_dir = 1 if radek > vychozi_radek else -1 if radek < vychozi_radek else 0
            sloupec_dir = 1 if sloupec > vychozi_sloupec else -1 if sloupec < vychozi_sloupec else 0
            
            current_radek = vychozi_radek + radek_dir
            current_sloupec = vychozi_sloupec + sloupec_dir
            
            while (current_radek, current_sloupec) != (radek, sloupec):
                if (current_radek, current_sloupec) in obsazene_pozice:
                    return False  # Na cestě je obsazená pozice
                current_radek += radek_dir
                current_sloupec += sloupec_dir
            
            return True  # Věž se může posunout na cílovou pozici

    # Střelec
    elif typ_figurky == "střelec":
        if abs(radek - vychozi_radek) == abs(sloupec - vychozi_sloupec):
            radek_dir = 1 if radek > vychozi_radek else -1
            sloupec_dir = 1 if sloupec > vychozi_sloupec else -1
            
            current_radek = vychozi_radek + radek_dir
            current_sloupec = vychozi_sloupec + sloupec_dir
            
            while (current_radek, current_sloupec) != (radek, sloupec):
                if (current_radek, current_sloupec) in obsazene_pozice:
                    return False  # Na cestě je obsazená pozice
                current_radek += radek_dir
                current_sloupec += sloupec_dir
            
            return True  # Střelec se může posunout na cílovou pozici

    # Dáma
    elif typ_figurky == "dáma":
        if radek == vychozi_radek or sloupec == vychozi_sloupec or abs(radek - vychozi_radek) == abs(sloupec - vychozi_sloupec):
            radek_dir = 1 if radek > vychozi_radek else -1 if radek < vychozi_radek else 0
            sloupec_dir = 1 if sloupec > vychozi_sloupec else -1 if sloupec < vychozi_sloupec else 0
            current_radek = vychozi_radek + radek_dir
            current_sloupec = vychozi_sloupec + sloupec_dir
            while (current_radek, current_sloupec) != (radek, sloupec):
                if (current_radek, current_sloupec) in obsazene_pozice:
                    return False  # Na cestě je obsazená pozice
                current_radek += radek_dir
                current_sloupec += sloupec_dir
            return True  # Dáma se může posunout na cílovou pozici

    # Král
    elif typ_figurky == "král":
        if max(abs(radek - vychozi_radek), abs(sloupec - vychozi_sloupec)) == 1:
            return True  # Král se může posunout na cílovou pozici

    return False  # Pokud žádná z podmínek neplatí


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
