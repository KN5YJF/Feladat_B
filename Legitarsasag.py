from Jarat import Jarat                  # → a fájl neve Jarat.py (nagy J)
from Jegy_foglalas import JegyFoglalas  # → fájlnév: Jegy_foglalas.py

# - LegiTarsasag: járatok és foglalások kezelése
class LegiTarsasag:
    def __init__(self, nev: str):
        # - nev: légitársaság neve
        self.nev = nev
        # - jaratok: elérhető járatok listája
        self.jaratok = []
        # - foglalasok: aktuális foglalások listája
        self.foglalasok = []

    def add_jarat(self, jarat: Jarat):
        # - járat hozzáadása
        self.jaratok.append(jarat)

    def list_jaratok(self) -> None:
        # - járatok listázása 1-től
        if not self.jaratok:
            print("Nincsenek elérhető járatok.")
            return
        for idx, jarat in enumerate(self.jaratok, start=1):
            print(f"{idx}: {jarat.get_info()}")

    def foglal(self, utas_nev: str, jaratszam: str) -> float:
        # - járat keresése
        jarat = next((j for j in self.jaratok if j.jaratszam == jaratszam), None)
        if jarat is None:
            # - hiba: nem található
            raise ValueError(f"Nincs '{jaratszam}' járatszám!")
        # - új foglalás létrehozása
        fog = JegyFoglalas(utas_nev, jarat)
        # - foglalás mentése
        self.foglalasok.append(fog)
        # - visszatérési érték: ár
        return fog.ar

    def lemond(self, foglalas_index: int) -> bool:
        # - index ellenőrzés
        if foglalas_index < 0 or foglalas_index >= len(self.foglalasok):
            raise IndexError("Hibás sorszámot adott meg.")
        # - foglalás törlése
        del self.foglalasok[foglalas_index]
        return True

    def listaz(self) -> None:
        # - foglalások listázása 1-től
        if not self.foglalasok:
            print("Nincs foglalás.")
            return
        for idx, fog in enumerate(self.foglalasok, start=1):
            print(f"{idx}: {fog}")