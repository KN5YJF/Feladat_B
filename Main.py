from Jarat          import BelfoldiJarat, NemzetkoziJarat   # → fájl: Jarat.py
from Legitarsasag   import LegiTarsasag                     # → fájl: Legitarsasag.py

# - run_tests: egységtesztek futtatása
def run_tests():
    lt = LegiTarsasag("TesztLégitársaság")
    # - belföldi járat létrehozása és ár validáció
    f1 = BelfoldiJarat("B123", "Budapest", 20000, 250)
    lt.add_jarat(f1)
    assert lt.foglal("TesztUtas", "B123") == 20000
    assert len(lt.foglalasok) == 1
    assert lt.lemond(0)
    assert len(lt.foglalasok) == 0
    # - nemzetközi járat létrehozása és ország validáció
    f2 = NemzetkoziJarat("N456", "Berlin", 60000, "Németország")
    lt.add_jarat(f2)
    print("Minden teszt sikeres.")

# - main: konzolos felület
def main():
    lt = LegiTarsasag("Magyar Légitársaság")
    lt.add_jarat(BelfoldiJarat("BUD123", "Debrecen", 15000, 200))
    lt.add_jarat(BelfoldiJarat("BUD456", "Szeged", 12000, 180))
    lt.add_jarat(NemzetkoziJarat("INT789", "London", 80000, "Egyesült Királyság"))
    for nev, js in zip([f"Utas{i}" for i in range(1,7)], ["BUD123","BUD456","INT789"]*2):
        lt.foglal(nev, js)

    while True:
        print("\n1: Foglalás  2: Lemondás  3: Foglalás lista  4: Járatok lista  9: Kilépés")
        choice = input("Választás: ")
        if choice == "1":
            nev = input("Utas neve: ")
            try:
                ar = lt.foglal(nev, input("Járatszám: "))
                print(f"Foglalás sikeres, ár: {ar} Ft")
            except Exception as e:
                print(e)
        elif choice == "2":
            lt.listaz()
            try:
                if lt.lemond(int(input("Sorszám: ")) - 1):
                    print("Lemondás sikeres.")
            except Exception as e:
                print(e)
        elif choice == "3":
            lt.listaz()
        elif choice == "4":
            lt.list_jaratok()
        elif choice == "9":
            print("Viszontlátástra! Köszönöjük hogy, minket választott!")
            break
        else:
            print("Hibás opció.")

if __name__ == "__main__":
    run_tests()
    main()