import enum
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


