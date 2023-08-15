class Qpolygon():
    def __init__(self):
        self.points = [3, 5]

class geometric_shape():
    def __init__(self, source):
        if isinstance(source, list):
            self._from_coordinates(source)
        if isinstance(source, Qpolygon):
            self._from_qpolygon(source)
        if isinstance(source, geometric_shape):
            self._from_geometric_shape(source)

    def _from_coordinates(self, coordinates: list):
        self.coordinates = coordinates

    def _from_qpolygon(self, polygon: Qpolygon):
        self.coordinates = polygon.points

    def _from_geometric_shape(self, geometric_shape):
        self.coordinates = geometric_shape.coordinates

    def get_coordinates(self):
        return self.coordinates

a = Qpolygon()
b = geometric_shape(a)
a = [2, 4]
b = geometric_shape(a)
c = geometric_shape(b)