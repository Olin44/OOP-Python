import math
class Figure:
    def __init__(self, colour = "Red", is_filled = False):
        self.is_filled = is_filled
        self.colour = colour
    def __str__(self):
        if self.is_filled:
            return f"Kolor: {self.colour}, Wypełniony\n"
        if self.is_filled == False:
            return f"Kolor: {self.colour}\n"
    def __repr__(self):
        pom = ""
        for k, v in self.__dict__.items():
            pom += "".join("{} = {}".format(k.lstrip("_"), v)) + " "
        text = f"{type(self).__name__}({pom})"
        return text


class Circle(Figure):
    def __init__(self, radius, colour = "Red", is_filled = False):
        super().__init__(colour, is_filled)
        self.radius = radius
    @property
    def radius(self):
        return float(self._radius)

    @radius.setter
    def radius(self, value):
        while True:
            try:
                float(value)
            except ValueError:
                value = input("Podaj poprawne dane(liczba nieujemna)")
            else:
                if 0 >= float(value):
                    value = input("Podaj poprawne dane(liczba nieujemna)")
                else:
                    self._radius = value
                    break

    def area(self):
        return math.pi * float(self._radius) ** 2
    def perimeter(self):
        return 2 * math.pi * float(self._radius)
    def diameter(self):
        return float(self._radius) * 2
    def __str__(self):
        return f"{Figure.__str__(self)}Promień { self._radius}, Pole: {self.area()}, Obwód: {self.perimeter()}, Średnica: {self.diameter()}"

class Rectangle(Figure):
    def __init__(self, width, height, colour = "Red", is_filled = False):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    @property
    def height(self):
        return float(self._width)

    @height.setter
    def height(self, value):
        while True:
            try:
                float(value)
            except ValueError:
                value = input("Podaj poprawne dane(liczba nieujemna)")
            else:
                if 0 >= float(value):
                    value = input("Podaj poprawne dane(liczba nieujemna)")
                else:
                    self._height = value
                    break

    @property
    def width(self):
        return float(self._width)

    @width.setter
    def width(self, value):
        while True:
            try:
                float(value)
            except ValueError:
                value = input("Podaj poprawne dane(liczba nieujemna)")
            else:
                if 0 >= float(value):
                    value = input("Podaj poprawne dane(liczba nieujemna)")
                else:
                    self._width = value
                    break

    def perimeter(self):
        return  self.width * self.height

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height **2)

    def area(self):
        return  (self.width * 2) + (2 * self.height)

    def __str__(self):
        return f"{Figure.__str__(self)}Wysokość: {self.height}, Długość: {self.width}, Przekątna: {self.diagonal()} Pole: {self.perimeter()} Obwód: {self.area()}"


f1 = Figure("Żółty", 1)
print(repr(f1))



f2 = Rectangle(12, 12, "Zielony", 0)
print(repr(f2))

f3 = Circle(-1, "Black", 1)
print(repr(f3))
