from abc import ABC


class Auto(ABC):
    def __init__(self, rendszam, tipus, dij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._dij = dij

    def __str__(self):
        pass

    def get_dij(self):
        return self._dij
