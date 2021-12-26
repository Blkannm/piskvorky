from random import randrange

def tah(pole, cislo_policka, symbol): 
    zacatek_pole = pole[:cislo_policka]
    konec_pole = pole[1+cislo_policka:]
    pole = (zacatek_pole+ symbol + konec_pole)
    return pole

def tah_hrace():
    pozice = input("kam chces hrat? ")
    return pozice

def Id_piskvorky():
    pole = 20*"-"
    while(pole.find("-") >= 0 ):
        cislo_pole = tah_hrace()
        if pole[cislo_pole] == "-":
            pole = tah(pole,cislo_pole,"x")
            print(pole)
        elif pole[cislo_pole] != "-":
            print("zabrane pole!")
    
    #pole = tah(pole, 8,"x")
    #tah_pocitace = randrange(0, 19)
    #print(tah_pocitace)
    #pole = tah(pole, tah_pocitace, "o")
    
    return print(pole)

Id_piskvorky()

