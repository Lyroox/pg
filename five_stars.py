#funkce demonstrující užití cyklusu while
def stars_while():
    print ("Zacatek")

    i=0

    while i<5:
        print("*")
        i+=1

    print ("Konec")

#stars_while()


#funkce demonstrující užití cyklusu for
def stars_for():
    print ("Zacatek")

    i=0

    for i in range(5):
        print("*", i)

    print ("Konec")

#stars_for()


#program rozdělující či number naleží mezi min_number a max_number
def in_range(min_number, max_number, number):
    if number >= min_number and number <= max_number:
        print("Is in range")
    else:
        print("Is not in range")

#in_range(100, 1000, 1001)


#program vypíše "Ahoj 'jmeno'!"
def zobraz_pozdrav(jmeno):
    print("Ahoj",jmeno+"!")
    
jm=input("Zadej jmeno: ")
#zobraz_pozdrav(jm)