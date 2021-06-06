from math import pi, sqrt


class Shape:
    def __init__(self, a):
        self.a = a


class Square(Shape):
    def __init__(self, a):
        super().__init__(a)

    def area(self):
        return self.a * self.a

    def circuit(self):
        return 4 * self.a


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def area(self):
        return self.a * self.b

    def circuit(self):
        return (2 * self.a) + (2 * self.b)


class Triangle(Shape):
    def __init__(self, a):
        super().__init__(a)

    def __get_hight(self):
        return (self.a * sqrt(3)) / 2

    def area(self):
        return 0.5 * self.a * self.__get_hight()

    def circuit(self):
        return self.a * 3


class Circle(Shape):
    def __init__(self, a):
        super().__init__(a)

    def area(self):
        return pi * (self.a * self.a)

    def circuit(self):
        return 2 * pi * self.a


class Rhombus(Square):
    def __init__(self, a, h):
        super().__init__(a)
        self.h = h

    def area(self):
        return self.a * self.h


class Trepezoid(Rectangle):
    def __init__(self, a, b, c, d, h):
        super().__init__(a, b)
        self.c = c
        self.d = d
        self.h = h

    def area(self):
        return 0.5 * (self.a + self.b) * self.h

    def circuit(self):
        return self.a + self.b + self.c + self.d


if __name__ == "__main__":

    r = Rectangle(2, 4)
    print(r.circuit())
    ro = Rhombus(5, 6)
    print(ro.area())
    print(ro.circuit())
