from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def density(self):
        pass

    @abstractmethod
    def mass(self):
        pass
