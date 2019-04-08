class Pet():
    def __init__(self, name, hunger = 0, tiredness = 0):
        self.__name = name
        self.hunger = hunger
        self.tiredness = tiredness
        self.__mood = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        while len(name) < 3 and str.isalpha(name):
            name = input("Podaj 3 literowe imie zwierzaka(wyłącznie litery")
        self.__name = name

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        return self.__mood

    @mood.setter
    def mood(self, x = 1):
        print("x")
        if (self.hunger + self.tiredness < 5):
            self.__mood = "szczęśliwy"
        if (5 < self.hunger + self.tiredness < 10):
            self.__mood = "zadowolony"
        if (11 < self.hunger + self.tiredness < 15):
            self.__mood = "podenerwowany"
        if (self.hunger + self.tiredness > 15):
            self.__mood = "wściekły"

    def eat(self, food = 4):
        self._passage_of_time()
        self.hunger -= food

    @property
    def talk(self):
        self._passage_of_time()
        return f"{self.name} jest {self.__mood}"

    def play(self, fun = 4):
        self._passage_of_time()
        self.tiredness -= fun

    def __str__(self):
        return f"Imie: {self.name}, Głód: {self.hunger}, Zmęczenie: {self.tiredness}, Humor: {self.mood}"


kot = Pet("Grażyna")
kot.mood
print(kot.talk)
kot.play(5)
kot.eat(5)
print(kot)

kot = Pet("Głodny", 15)

print(kot.talk)
kot.play(5)
kot.eat(5)
print(kot)



