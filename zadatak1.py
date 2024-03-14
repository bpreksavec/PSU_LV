#Unos radnih sai od strane korisnika:
print ("Unesite broj radnih sati: ")
br_h = float(input())

#Unos satnice
print ("Unesite Vasu satnicu: ")
eurph = float(input())

#Izračun plaće bez funkcije
plata = br_h * eurph
print("Zaradili ste ", plata)

#Izračun sa funkcijom
def total_euro(br_h, eurph):
    placa = br_h * eurph
    return placa

placa = total_euro(br_h, eurph)
print("Zaradili ste ", placa)
