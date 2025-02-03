from classes.shape_abstract import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def volume(self):
        return 0

    def surface_area(self):
        return self.area()

    def density(self):
        return 0

    def mass(self):
        return 0