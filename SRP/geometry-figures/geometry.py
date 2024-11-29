from abc import ABC, abstractmethod
import math


# Інтерфейс стратегії
class Figure(ABC):
    def __init__(self, side_length):
        self.side_length = side_length

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


# Реалізація фігур
class Circle(Figure):
    def perimeter(self):
        result = 2 * math.pi * self.side_length
        return int(result) if float(result).is_integer() else round(result, 2)

    def area(self):
        result = math.pi * (self.side_length ** 2)
        return int(result) if float(result).is_integer() else round(result, 2)

    def volume(self):
        return 0


class Triangle(Figure):
    def perimeter(self):
        result = 3 * self.side_length
        return int(result) if float(result).is_integer() else round(result, 2)

    def area(self):
        result = (math.sqrt(3) / 4) * (self.side_length ** 2)
        return int(result) if float(result).is_integer() else round(result, 2)

    def volume(self):
        return 0


class Square(Figure):
    def perimeter(self):
        result = 4 * self.side_length
        return int(result) if float(result).is_integer() else round(result, 2)

    def area(self):
        result = self.side_length ** 2
        return int(result) if float(result).is_integer() else round(result, 2)

    def volume(self):
        return 0


class Pentagon(Figure):
    def perimeter(self):
        result = 5 * self.side_length
        return int(result) if float(result).is_integer() else round(result, 2)

    def area(self):
        result = (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.side_length ** 2)
        return int(result) if float(result).is_integer() else round(result, 2)

    def volume(self):
        return 0


class Hexagon(Figure):
    def perimeter(self):
        result = 6 * self.side_length
        return int(result) if float(result).is_integer() else round(result, 2)

    def area(self):
        result = ((3 * math.sqrt(3)) / 2) * (self.side_length ** 2)
        return int(result) if float(result).is_integer() else round(result, 2)

    def volume(self):
        return 0


class Cube(Figure):
    def perimeter(self):
        result = 12 * self.side_length
        return int(result) if float(result).is_integer() else round(result, 2)

    def area(self):
        result = 6 * (self.side_length ** 2)
        return int(result) if float(result).is_integer() else round(result, 2)

    def volume(self):
        result = self.side_length ** 3
        return int(result) if float(result).is_integer() else round(result, 2)


# Контекст
class Parameters:
    def __init__(self, side_length):
        self.side_length = side_length
        self.figure = None

    def choose_figure(self, figure):
        self.figure = figure

    def perimeter(self):
        return self.figure.perimeter()

    def area(self):
        return self.figure.area()

    def volume(self):
        return self.figure.volume()


# Основна програма
def main():
    figure = Parameters(10)

    # Circle
    figure.choose_figure(Circle(10))
    print("Circle perimeter:", figure.perimeter())
    print("Circle area:", figure.area())
    print("Circle volume:", figure.volume())

    # Triangle
    figure.choose_figure(Triangle(10))
    print("Triangle perimeter:", figure.perimeter())
    print("Triangle area:", figure.area())
    print("Triangle volume:", figure.volume())

    # Square
    figure.choose_figure(Square(10))
    print("Square perimeter:", figure.perimeter())
    print("Square area:", figure.area())
    print("Square volume:", figure.volume())

    # Pentagon
    figure.choose_figure(Pentagon(10))
    print("Pentagon perimeter:", figure.perimeter())
    print("Pentagon area:", figure.area())
    print("Pentagon volume:", figure.volume())

    # Hexagon
    figure.choose_figure(Hexagon(10))
    print("Hexagon perimeter:", figure.perimeter())
    print("Hexagon area:", figure.area())
    print("Hexagon volume:", figure.volume())

    # Cube
    figure.choose_figure(Cube(10))
    print("Cube perimeter:", figure.perimeter())
    print("Cube area:", figure.area())
    print("Cube volume:", figure.volume())


if __name__ == "__main__":
    main()
