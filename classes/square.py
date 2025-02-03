from shape_abstract import Shape

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def volume(self):
        return 0

    def density(self):
        return 0

    def mass(self):
        return 0

    def surface_area(self):
        return 0

    def __str__(self):
        return f'Square(side={self.side})'
