from datetime import datetime, date
from Berles import Berles
from Auto import Auto


class Autokolcsonzo:

    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    def get_nev(self):
        return self._nev

    def hozzaad_auto(self, auto: Auto):
        self._autok.append(auto)

    def autoberles(self, autoid: int, datum: date):
        for berles in self._berlesek:
            if berles.get_auto() == self._autok[autoid] and berles.get_datum() == datum:
                return "Bérlés sikertelen. Autó arra a napra bérelve van!"
        berles = Berles(self._autok[autoid], datum)
        self._berlesek.append(berles)
        return "Bérlés sikeres! Bérleti díj: " + str(berles.get_auto().get_dij()) + "Ft"

    def get_aktualis_berlesek(self):
        akt_berles = []
        for berles in self._berlesek:
            if berles.get_datum() >= datetime.now().date():
                akt_berles.append(berles)
        return akt_berles

    def aktualis_berles_lista(self):
        s = ""
        for berles in self.get_aktualis_berlesek():
            s = s + str(berles) + "\n"
        s = s[:-1]
        if len(s) == 0:
            return "Nincs bérlés"
        else:
            return s

    def get_autok(self):
        return self._autok

    def berles_lemondas(self, akt_index: int):
        ber = self.get_aktualis_berlesek()[akt_index]
        for berles in self._berlesek:
            if berles == ber:
                self._berlesek.remove(ber)
                return "Lemondás sikeres!"
        return "Lemondás sikertelen!"


