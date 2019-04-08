from Rectangle import Rectangle, Cuboid

class InvalidData(Exception):
    def searcher(numbers):
        for number in numbers:
            try:
                float(number)
            except ValueError:
                return 0
            else:
                if float(number) <= 0:
                    return 0
        return list(map(float, numbers))

file = open("dane.txt", "r").read()
lines = file.split('\n')
for line in lines:
    numbers = line.split(' ')
    data = InvalidData.searcher(numbers)
    if data:
        if data[0] == 1.0 and len(data) == 3:
            print(Rectangle(data[1], data[2]))
        if data[0] == 2.0 and len(data) == 4:
            print(Cuboid(data[1], data[2], data[3]))













