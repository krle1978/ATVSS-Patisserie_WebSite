from sastojci import Kolac, Sastojak
def meni():
    print("\n--- Meni ---")
    print("1. Kreiraj kolač")
    print("2. Prikaz porudžbine")
    print("3. Obračun ukupne cene")
    print("4. Obračun ukupnih kalorija")
    print("5. Izlaz")

def kreiraj_kolac():
    ime = input("Unesite ime kolača: ")
    osnovne_kalorije = int(input("Unesite osnovne kalorije kolača: "))
    osnovna_cena = float(input("Unesite osnovnu cenu kolača: "))
    kolac = Kolac(ime, osnovne_kalorije, osnovna_cena)
    
    while True:
        print("\n--- Dodavanje sastojaka ---")
        naziv = input("Unesite naziv sastojka (ili 'kraj' za završetak): ")
        if naziv.lower() == "kraj":
            break
        kalorije = int(input(f"Unesite kalorije za {naziv}: "))
        cena = float(input(f"Unesite cenu za {naziv}: "))
        sastojak = Sastojak(naziv, kalorije, cena)
        kolac.dodaj_sastojak(sastojak)
    
    return kolac

def prikazi_porudzbinu(porudzbina):
    if not porudzbina:
        print("\nPorudžbina je prazna.")
    else:
        for i, kolac in enumerate(porudzbina, start=1):
            print(f"\n{i}. {kolac}")

def ukupna_cena_porudzbine(porudzbina):
    return sum(k.ukupna_cena() for k in porudzbina)

def ukupne_kalorije_porudzbine(porudzbina):
    return sum(k.ukupne_kalorije() for k in porudzbina)

# Glavni program
porudzbina = []
while True:
    meni()
    izbor = input("Izaberite opciju: ")
    if izbor == "1":
        kolac = kreiraj_kolac()
        porudzbina.append(kolac)
    elif izbor == "2":
        prikazi_porudzbinu(porudzbina)
    elif izbor == "3":
        print(f"\nUkupna cena porudžbine: {ukupna_cena_porudzbine(porudzbina)} RSD")
    elif izbor == "4":
        print(f"\nUkupne kalorije porudžbine: {ukupne_kalorije_porudzbine(porudzbina)}")
    elif izbor == "5":
        print("Hvala što ste koristili naš sistem!")
        break
    else:
        print("Nepoznata opcija, pokušajte ponovo.")
