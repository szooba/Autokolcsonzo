from Auto import Auto


class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, dij, ferohely):
        super().__init__(rendszam, tipus, dij)
        self._ferohely = ferohely

    def __str__(self):
        return "Személyautó: " + self._tipus + " Rendszám: " + self._rendszam + " Bérleti díj: " + str(self._dij) + "Ft Férőhely: " + str(self._ferohely)