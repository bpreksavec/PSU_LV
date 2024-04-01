#Zadatak 1 prvo rjesenje
workh = float(input("Unesite broj radnih sati: "))
payph = float(input("Unesite satnicu u €: "))

placa = workh * payph

print("Vaša plaća iznosi: ", placa, " €")

#Zadatak 1 drugo rjesenje
def total_euro(radnisati, pph):
    return radnisati * pph

def main():
    radnisati = float(input("Unesite broj radnih sati: "))
    pph = float(input("Unesite satnicu u €: "))

    zarada = total_euro(radnisati, pph)
    print("Vaša plaća iznosi: ", zarada, " €")

if __name__ == "__main__":
    main()