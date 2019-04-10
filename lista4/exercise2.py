from abc import ABC, abstractmethod


class Temperature(ABC):

    @abstractmethod
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{self.convert_to_Celsius().temperature} degree in Celsius scale"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.temperature})"

    def above_freezing(self):
        return True if self.convert_to_Celsius().temperature > 0 else False

    @abstractmethod
    def convert_to_Fahrenheit(self):
        pass

    @abstractmethod
    def convert_to_Celsius(self):
        pass

    @abstractmethod
    def convert_to_Kelvin(self):
        pass

    @property
    @abstractmethod
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        pass

    @abstractmethod
    def get_temperature(self):
        return self.temperature

    
class Fahrenheit(Temperature):

    def __init__(self, temperature):
        super().__init__(temperature)

    def convert_to_Fahrenheit(self):
        return Fahrenheit(self.temperature)

    def convert_to_Celsius(self):
        return Celsius(0.556 * (self.temperature - 32.0))

    def convert_to_Kelvin(self):
        return Kelvin(self.convert_to_Celsius().temperature + 273.16)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < 0:
            self._temperature = 0
        else:
            self._temperature = value

    def get_temperature(self):
        return self.temperature


class Celsius(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def convert_to_Celsius(self):
        return Celsius(self.temperature)

    def convert_to_Fahrenheit(self):
        return Fahrenheit(self.temperature / 0.556 + 32)

    def convert_to_Kelvin(self):
        return Kelvin(self.temperature + 273.16)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.17:
            self.temperature = -273.17
        else:
            self._temperature = value

    def get_temperature(self):
        return self.temperature


class Kelvin(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def convert_to_Celsius(self):
        return Celsius(self.temperature - 273.17)

    def convert_to_Fahrenheit(self):
        return Fahrenheit(self.convert_to_Celsius().temperature / 0.556 + 32)

    def convert_to_Kelvin(self):
        return Kelvin(self.temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -459.67:
            self.temperature = -459.67
        else:
            self._temperature = value

    def get_temperature(self):
        return self.temperature

c1 = Celsius(12)
c2 = Celsius(-290)
c3 = Celsius(250)
c4 = Celsius(20)
f1 = Fahrenheit(273)
f2 = Fahrenheit(500)
f3 = Fahrenheit(0)
f4 = Fahrenheit(300)
k1 = Kelvin(-470.67)
k2 = Kelvin(500)
k3 = Kelvin(0)
k4 = Kelvin(300)

list = [c1, c2, c3, c4, f1, f2, f3, f4, k1, k2, k3, k4]

print("\nPrint if temperature is above 0")
for i in list:
    if i.above_freezing():
        print(repr(i), i.__str__(), "is above 0 degree")
    else:
        print(repr(i), i.__str__())


print("\n Convert to Fahrenheit")
list1 = [i.convert_to_Fahrenheit() for i in list]
print(list1)
for i in list1:
    if i.above_freezing():
        print(i)

print("\nConvert to Kelvin")
list2 = [i.convert_to_Kelvin() for i in list]
print(list2)
for i in list2:
    if i.above_freezing():
        print(i)







