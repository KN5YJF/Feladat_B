import time
from Jarat import Jarat

# --------------------------------------------------------------------------------
# - JegyFoglalas: egy utas szempontjából a foglalás adatait tárolja
#   (utas neve, a választott Jarat, foglalás időpontja és az ár)
# --------------------------------------------------------------------------------
class JegyFoglalas:
    def __init__(self, utas_nev: str, jarat: Jarat, foglalas_ido=None):
        # - utas_nev: utas neve
        # - jarat: Jarat objektum
        # - foglalas_ido: időpont, ha nincs megadva, a jelenlegi idő
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.foglalas_ido = foglalas_ido or time.localtime()
        # - ar: a járat aktuális jegyára
        self.ar = jarat.jegyar

    def __str__(self) -> str:
        # - formázott string: utas neve, járatszám, időpont, ár
        t = self.foglalas_ido
        ido_str = f"{t[0]:04d}-{t[1]:02d}-{t[2]:02d} {t[3]:02d}:{t[4]:02d}"
        return f"Foglalás {self.utas_nev}, járat: {self.jarat.jaratszam}, idő: {ido_str}, ár: {self.ar} Ft"