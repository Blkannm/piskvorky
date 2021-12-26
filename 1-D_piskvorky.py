from random import randrange

def tah(pole, cislo_policka, symbol): 
    zacatek_pole = pole[:cislo_policka]
    konec_pole = pole[1+cislo_policka:]
    pole = (zacatek_pole+ symbol + konec_pole)
    return pole


def tah_hrace():
    while():
        pozice = int(input("kam chces hrat?"))
        if pozice < 0:
            print("nelze zadat zaporne cislo")
        elif pozice >= 0:
            break
        else:
            print("nerozumim zkus to znova")
    return (pozice)

def Id_piskvorky():
    
    print()
    return

Id_piskvorky()


# zmnena
# zmena 2 t
