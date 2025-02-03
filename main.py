from classes.square import Square
from classes.cube import Cube

def main():
    print('*'*40)
    square = Square(10)
    print(square)
    print(f'Area:{square.area()}')
    print(f'Perimeter:{square.perimeter()}')
    print(f'Volume:{square.volume()}')
    print(f'Surface Area:{square.surface_area()}')
    print(f'Density:{square.density()}')
    print(f'Mass:{square.mass()}')

    print('*'*40)
    cube = Cube(10, 1000)
    print(cube)
    print(f'Area:{cube.area()}')
    print(f'Perimeter:{cube.perimeter()}')
    print(f'Volume:{cube.volume()}')
    print(f'Surface Area:{cube.surface_area()}')
    print(f'Density:{cube.density()}')
    print(f'Mass:{cube.mass()}')

if __name__ == "__main__":
    main()


