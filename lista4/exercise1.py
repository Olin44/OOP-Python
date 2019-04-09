class Pupil:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        while len(value) < 3 or not str.isalpha(value):
            value = input("Enter a 3 letter name (letters only): ")
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        while len(value) < 3 or not str.isalpha(value):
            value = input("Enter a 3 letter surname (letters only): ")
        self._surname = value


    def complete_marks(self):
        marks = {"1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5", "5.5", "6"}
        while True:
            course = input("Enter the correct course name: ")
            while len(course) < 3 or not str.isalpha(course) or course in self.marks:
                course = input("Enter the correct course name: ")
            grade = input("Enter correct grade: ")
            while grade not in marks:
                grade = input("Enter correct grade: ")
            self.marks[course] = float(grade)
            course = ""
            grade = ""
            x = input("Click x to end or any key to continue. ")
            if x == "x":
                break

    def print_marks(self):
        print(self.marks)

    def mean(self):
        grades = 0.0
        for mark, values in self.marks.items():
            grades += float(values)
        return grades/len(self.marks)

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Mean: {str(self.mean())}"


class Student(Pupil):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.weights = {}

    def complete_weights(self):
        for k, v in self.marks.items():
            print(f"Set weight for the course: {k}.")
            scales = float(input("Set correct weight for the course: "))
            while scales < 0 or scales > 1:
                scales = float(input("Set correct weight for the course: "))

            self.weights[k] = scales
            scales = ""

    def mean(self):
        mean = 0.0
        weights = 0.0
        for k, v in self.marks.items():
            mean += v * self.weights[k]
            weights += self.weights[k]
        return mean / weights

    def __str__(self):
        return super().__str__() + f" weighted average: {self.mean()}"
