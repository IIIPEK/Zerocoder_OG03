from classes.shape_abstract import Shape

class Cube(Shape):
    def __init__(self, side,weight=0 ):
        self.side = side
        self.weight = weight

    def volume(self):
        return self.side ** 3

    def __str__(self):
        return f'Cube(side={self.side})'

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 12 * self.side

    def surface_area(self):
        return 6 * self.area()

    def mass(self):
        return self.weight

    def density(self):
        if self.volume() == 0:
            return 0
        return self.mass() / self.volume()

