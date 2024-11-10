class Berles:

    def __init__(self, auto, datum):
        self._auto = auto
        self._datum = datum

    def __str__(self):
        return "Bérelve: " + str(self._datum) + " " + str(self._auto)

    def get_auto(self):
        return self._auto

    def get_datum(self):
        return self._datum
