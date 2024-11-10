from Auto import Auto


class Teherauto(Auto):

    def __init__(self, rendszam, tipus, dij, teherbiras):
        super().__init__(rendszam, tipus, dij)
        self._teherbiras = teherbiras

    def __str__(self):
        return "Teherautó: " + self._tipus + " Rendszám: " + self._rendszam + " Bérleti díj: " + str(self._dij) + "Ft Teherbírás: " + str(self._teherbiras) + " kg"