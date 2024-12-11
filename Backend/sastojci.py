class Sastojak:
    def __init__(self, naziv, kalorije, cena):
        self.naziv = naziv
        self.kalorije = kalorije
        self.cena = cena

    def __str__(self):
        return f"Sastojak: {self.naziv}, Kalorije: {self.kalorije}, Cena: {self.cena}"

class Kolac:
    def __init__(self, ime, osnovne_kalorije, osnovna_cena):
        self.ime = ime
        self.osnovne_kalorije = osnovne_kalorije
        self.osnovna_cena = osnovna_cena
        self.sastojci = []

    def dodaj_sastojak(self, sastojak):
        self.sastojci.append(sastojak)

    def ukupne_kalorije(self):
        return self.osnovne_kalorije + sum(s.kalorije for s in self.sastojci)

    def ukupna_cena(self):
        return self.osnovna_cena + sum(s.cena for s in self.sastojci)

    def __str__(self):
        sastojci_opis = ", ".join(s.naziv for s in self.sastojci) or "Nema dodatih sastojaka"
        return (
            f"{self.ime} (Osnovne kalorije: {self.osnovne_kalorije}, Osnovna cena: {self.osnovna_cena} RSD)\n"
            f"Sastojci: {sastojci_opis}\n"
            f"Ukupne kalorije: {self.ukupne_kalorije()} | Ukupna cena: {self.ukupna_cena()} RSD"
        )
