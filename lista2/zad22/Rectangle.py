class Rectangle:
    def __init__(self, length, height ):
        self.length = length
        self.height = height
    def area(self):
        return self.length * self.height

    def __str__(self):
        return f"Wysokość: {self.height}, Długość: {self.length}, Pole: {self.area()}"

    def __repr__(self):
        return f"Obiekt klasy Rectangle. "

class Cuboid(Rectangle):
    def __init__(self, length, height, width ):
        super().__init__(length, height)
        self.width = width
    def __str__(self):
        return f"{super().__str__()}  Wysokość prostopadłościanu: {self.width}, Pole: {self.area()}, Objętość: {self.volume()}"
    def area(self):
        return (2 * self.length * self.height) + (2 * self.length * self.width) + (2 * self.length * self.width)
    def volume(self):
        return super().area() * self.width
    def __repr__(self):
        return f"{super().__repr__()} \nObiekt klasy Cuboid"
