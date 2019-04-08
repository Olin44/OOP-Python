class Smartphone:
    def __init__(self, price, manufacturer, model,):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price
        return
    def set_attribute(self):
        self.__manufacturer = input("Podaj nazwę producenta: ")
        self.__model = input("Podaj nazwę modelu: ")
        self.__price = input("Podaj cene: ")
        while True:
            try:
                self.__price = float(self.__price)
            except ValueError:
                print("To nie jest liczba")
                self.__price = input("Podaj cene: ")
            else:
                print("Podałeś wszystkie parametry!")
        return

    def print_attribute(self):
        return (f"Nazwa producenta: {self.__manufacturer}\nNazwa modelu: {self.__model}\nCena: {self.__price}")




