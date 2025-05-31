import time
from abc import ABC, abstractmethod

# --------------------------------------------------------------------------------
# - Jarat: absztrakt alap osztály a járatokhoz
#   A járatszámot, célállomást és jegyárat tárolja, a jegyárat a setter validálja.
# --------------------------------------------------------------------------------
class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        # - _jaratszam: privát járatszám
        # - _celallomas: privát célállomás
        # - _jegyar: privát jegyár (setterrel validáljuk)
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = None
        self.jegyar = jegyar  # setter hívás validációra

    @property
    def jaratszam(self) -> str:
        # - getter: járatszám lekérése
        return self._jaratszam

    @property
    def celallomas(self) -> str:
        # - getter: célállomás lekérése
        return self._celallomas

    @property
    def jegyar(self) -> float:
        # - getter: jegyár lekérése
        return self._jegyar

    @jegyar.setter
    def jegyar(self, ertek: float):
        # - setter: jegyár beállítása (érvényesítés: nem lehet negatív)
        if ertek < 0:
            raise ValueError("A jegyár nem lehet negatív!")
        self._jegyar = ertek

    @abstractmethod
    def get_info(self) -> str:
        # - absztrakt metódus, a leszármazottaknak kell implementálniuk
        pass


# --------------------------------------------------------------------------------
# - BelfoldiJarat: belföldi járat, extra attribútum: távolság km-ben
# --------------------------------------------------------------------------------
class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float, tavolsag_km: float):
        super().__init__(jaratszam, celallomas, jegyar)
        # - _tavolsag_km: privát távolság
        self._tavolsag_km = None
        self.tavolsag_km = tavolsag_km  # setterrel validáljuk

    @property
    def tavolsag_km(self) -> float:
        # - getter: távolság lekérése
        return self._tavolsag_km

    @tavolsag_km.setter
    def tavolsag_km(self, ertek: float):
        # - setter: távolság beállítása (nem lehet negatív)
        if ertek < 0:
            raise ValueError("A távolság nem lehet negatív!")
        self._tavolsag_km = ertek

    def get_info(self) -> str:
        # - a belföldi járat részletes leírása
        return (
            f"Belföldi járat {self.jaratszam}  |  "
            f"Cél: {self.celallomas}, Távolság: {self.tavolsag_km} km, Ár: {self.jegyar} Ft"
        )


# --------------------------------------------------------------------------------
# - NemzetkoziJarat: nemzetközi járat, extra attribútum: ország
# --------------------------------------------------------------------------------
class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float, orszag: str):
        super().__init__(jaratszam, celallomas, jegyar)
        # - _orszag: privát célország
        self._orszag = None
        self.orszag = orszag  # setterrel validáljuk

    @property
    def orszag(self) -> str:
        # - getter: ország lekérése
        return self._orszag

    @orszag.setter
    def orszag(self, ertek: str):
        # - setter: ország beállítása (nem lehet üres)
        if not ertek:
            raise ValueError("Az ország nem lehet üres!")
        self._orszag = ertek

    def get_info(self) -> str:
        # - a nemzetközi járat részletes leírása
        return (
            f"Nemzetközi járat {self.jaratszam}  |  "
            f"Cél: {self.celallomas} ({self.orszag}), Ár: {self.jegyar} Ft"
        )
