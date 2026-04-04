from shape import Shape

class Square(Shape):
    def __init__(self, length):
        self._length = length
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        self._length = value
        
    @property
    def area(self):
        return self._length * self._length
    
    def __str__(self):
        return f"Length: {self._length}"