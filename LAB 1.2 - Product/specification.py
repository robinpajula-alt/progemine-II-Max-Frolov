class ColorSpecification:
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, product):
        return self.color == product.color

    def __and__(self, other):
        return AndSpecification(self, other)
    
class SizeSpecification:
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product):
        return self.size == product.size
    
    def __and__(self, other):
        return AndSpecification(self, other)
    
class AndSpecification:
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, product):
        for spec in self.args:
            if not spec.is_satisfied(product):
                return False
        return True