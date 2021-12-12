from random import randrange

def tah(cislo_policka, symbol):
    pole = 20*"-"   
    zacatek_pole = pole[:cislo_policka]
    konec_pole = pole[1+cislo_policka:]
    ukazka_pole = (zacatek_pole+ symbol + konec_pole)
    pole = ukazka_pole
    return ukazka_pole


def tah_hrace():
    while():
        hrac = int(input("kam chces hrat?"))
        if hrac <= 0:
            print("nelze zadat zaporne cislo")
        elif hrac >= 0:
            break
        else:
            print("nerozumim zkus to znova")
    return (hrac, "X")

def Id_piskvorky():
    print()
    return

Id_piskvorky()
tah_hrace()
