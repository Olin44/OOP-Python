class RocketEngine:

    count = 0
    __all_power = 0
    def __init__(self,  name, power, working = False ):
        self.working = working
        self.name = name
        self.power = power
        type(self).count += 1

    def start(self):
        if self.working == False:
            self.working = True
            RocketEngine.__all_power += self.power
    def stop(self):
        if self.working == True:
            self.working = False
            RocketEngine.__all_power -=  self.power
    def __str__(self):
        return f"Nazwa silnika: {self.name}\nMoc silnika: {self.power}\n"
    def __del__(self):
        if self.count > 0:
            type(self).count -= 1
    @staticmethod
    def status():
        print(f"Liczba silników: {RocketEngine.count}\nŁączna moc: {RocketEngine.__all_power}\n")

print("Początek lotu: \nStworzenie silników.\n")
engine = RocketEngine("Manewrowy 1", 50)
engine1 = RocketEngine("Manewrowy 2", 50)
print(engine)
print(engine1)
print("Stan statku: ")
RocketEngine.status()
print("Start silników manewrowych!")

engine.start()
engine1.start()
RocketEngine.status()

print("Włączenie silników głównych!")
engine2 = RocketEngine("Główny 1", 500)
engine3 = RocketEngine("Główny 2", 500)
print(engine2)
print(engine3)
engine2.start()
engine3.start()

print("Włączenie silnika nadprzestrzennego!")
engine4 = RocketEngine("Główny 1", 400000)
engine4.start()
RocketEngine.status()

print("Wyjście z nadprzestrzeni!")
engine4.stop()
del engine4
RocketEngine.status()

print("Zwalniamy!")
engine2.stop()
engine3.stop()
del engine2, engine3
RocketEngine.status()


print("Lądujemy!")
engine1.stop()
engine.stop()
RocketEngine.status()

del engine, engine1
print("Dezaktywacja silników!")
RocketEngine.status()


