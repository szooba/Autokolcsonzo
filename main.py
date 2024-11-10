from datetime import datetime
from TeherAuto import Teherauto
from SzemelyAuto import Szemelyauto
from Autokolcsonzo import Autokolcsonzo

def bemenet(szoveg: str, minimum: int, maximum: int):
    while True:
        szam = input(szoveg)
        if not szam.isnumeric() or int(szam) > maximum or int(szam) < minimum:
            print("Próbálja újra!" + " (" + str(minimum) + "-" + str(maximum) + ")")
        else:
            return int(szam)

def mai_datum():
    datum = datetime.now().date()
    return datum

def datum_bemenet(szoveg: str):
    hiba = "Próbálja újra!"
    while True:
        datum = input(szoveg)
        s = datum.split("-")
        if not len(s) == 3 or not s[0].isnumeric() or not s[1].isnumeric() or not s[2].isnumeric() or int(s[1]) > 12 or int(s[1]) < 1 or int(s[2]) > 31 or int(s[2]) < 1:
            print(hiba)
        else:
            datumki = datetime(int(s[0]), int(s[1]), int(s[2])).date()
            if datumki < mai_datum():
                print(hiba)
            else:
                return datumki

def menu(kolcsonzo: Autokolcsonzo):
    while True:
        print("\n" + kolcsonzo.get_nev())
        print("(1) Autó bérlése")
        print("(2) Bérlés lemondása")
        print("(3) Bérlések listázása")
        print("(4) Kilépés")

        valaszt = bemenet("Válasz a fenti menüpontok közül: ", 1,4)

        if valaszt == 1:
            i = -1
            for auto in kolcsonzo.get_autok():
                i = i + 1
                print("(" + str(i + 1) + ") " + str(auto))
            if i == -1:
                print("Nincs bérlés")
            else:
                autoid = bemenet("Válasz a fenti autók közül: ", 1, i + 1) - 1
                datum = datum_bemenet("Adja meg, hogy melyik napra akarja kibérelni az autót (pl. " + str(mai_datum()) + "): ")
                print(kolcsonzo.autoberles(autoid, datum))
        elif valaszt == 2:
            i = -1
            berlesek = kolcsonzo.get_aktualis_berlesek()
            for berles in berlesek:
                i = i + 1
                print("(" + str(i+1) + ") " + str(berles))
            if i == -1:
                print("Nincs bérlés")
            else:
                valasz = bemenet("Válasz a fenti bérlések közül: ", 1, i + 1)-1
                print(kolcsonzo.berles_lemondas(valasz))
        elif valaszt == 3:
            print(kolcsonzo.aktualis_berles_lista())
        elif valaszt == 4:
            return

kolcsonzo = Autokolcsonzo("Autókölcsönző")
kolcsonzo.hozzaad_auto(Szemelyauto("ABC-123", "Opel Astra", 8000, 5))
kolcsonzo.hozzaad_auto(Teherauto("CBA-321", "Volvo FH", 10000, 1000))
kolcsonzo.hozzaad_auto(Teherauto("AB-CD-123", "Ford Transit", 13000, 2000))
kolcsonzo.autoberles(0, datetime(2025, 10, 14).date())
kolcsonzo.autoberles(0, mai_datum())
kolcsonzo.autoberles(1, datetime(2024, 11, 7).date())
kolcsonzo.autoberles(1, datetime(2024, 12, 10).date())
menu(kolcsonzo)