#было - стало
class shape(): - class geometric_shape():
class tab(QTabWidget): - class tasks_table(QTabWidget):
class baseView(QGraphicsView): - class map_view(QGraphicsView):
class newestDescription(QDialog): - class input_description(QDialog):
class newAerialAttr(QDialog): - class input_attribute(QDialog):

def coloredshape_frompoints(self, points, color): - def __init__(self, points), def _encolor(self, color)
def change_point(self, index, newpoint): - def adjust_point(self, index, coordinates)
def point_at_pos(self, point2): - def is_occupied(self, point):
def closest_to(self, point2): - def find_occupation(self, point):
def index_of(self, point): - def occupation_index(self, point):
class newProject(QDialog): - class input_project(QDialog):
class basedProject(newProject): - class adjust_project(input_project)