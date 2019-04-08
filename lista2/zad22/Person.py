import re
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def age(self):
        return int(self._age)

    @age.setter
    def age(self, value):
        while True:
            try:
                int(value)
            except ValueError:
                value = input("Podaj poprawne dane(liczba całkowita z zakresu 0 do 130)")
            else:
                if 0 > int(value) or int(value) > 130:
                    value = input("Podaj poprawne dane(liczba całkowita z zakresu 0 do 130)")
                else:
                    self._age = value
                    break


    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        while True:
            if isinstance(value, str):
                if len(value) >= 3 and (re.match("^[a-zA-Z]+$", value)):
                    self._surname = value
                    break
                else:
                    value = input("Podaj minimum 3 literowe nazwisko")
            else:
                value = input("Podaj minimum 3 literowe nazwisko")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        while True:
            if isinstance(value, str):
                if len(value) >= 3 and (re.match("^[a-zA-Z]+$", value)):
                    self._name = value
                    break
                else:
                    value = input("Podaj minimum 3 literowe nazwisko")
            else:
                value = input("Podaj minimum 3 literowe nazwisko")

    def __str__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}, Wiek: {self.age}"

class Student(Person):
    def __init__(self, name, surname, age, field_of_study, student_book):
        super().__init__(name, surname, age)
        self.field_of_study = field_of_study
        self.student_book = student_book

    @property
    def field_of_study(self):
        return self._field_of_study

    @field_of_study.setter
    def field_of_study(self, value):
        while True:
            if isinstance(value, str):
                if len(value) >= 2 and (re.match("^[a-zA-Z]+$", value)):
                    self._field_of_study = value
                    break
                else:
                    value = input("Podaj minimum 2 literową nazwę uczelni")
            else:
                value = input("Podaj minimum 2 literową nazwę uczelni")

    @property
    def student_book(self):
        return self._student_book

    @student_book.setter
    def student_book(self, value):
        if type(value) == type({}):
            for i, j in value.items():
                while True:
                    if re.match("[0-6]", str(j)):
                        j = input("Podaj poprawną ocenę(liczba od 1-6): ")
                        value[i] = j
                        print(value)
                    else:
                        break
                while True:
                    if not re.match("^[1-6A-Za-z]+$", i):
                        new = input("Podaj poprawną nazwę przedmiotu: ")
                        value[new] = value.pop(i)
                        i = new
                        print(value)
                    else:
                        break

        self._student_book = value

    def __str__(self):
        return f"{super().__str__()} Uczelnia: {self.field_of_study} Oceny: {self.student_book}"


person1 = Person("jjj", "chuj", 15)
Student1 = Student("jjj", "chuj", 45, "UP", {"%" : "x", "#" : 232})
print(Student1)
print(person1)