class Iterator1():
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        self.start += 2
        return self.start


def Generator():
    i = 0
    while True:
        i += 1
        yield i



def SquareNumberGenerator():
    for n in Generator():
        yield n ** 2


def select(generator_name, n):
    list = []
    iterator = iter(generator_name)
    for number in range(n):
        list.append(next(iterator))
        if number >= n:
            break
    print(list)

select(SquareNumberGenerator(), 20)

trojki = ((a*a, b*b, c*c) for c in Generator() for b in range(1, c) for a in range(1, b) if a ** 2 + b ** 2 == c ** 2)
print(select(trojki, 15))

#Zdeﬁniuj generator produkuja˛cy trójelementowe krotki zawieraja˛ce tzw.
# trójki pitagorejskie tzn. krotki postaci (a,b,c) gdzie a2 + b2 == c2 -
# wykorzystaj wyrażenie generatora (załóż, że a < b < c). Wyświetl 15 pierwszychtrójekkorzystaja˛czfunkcji select().


#for item in select(SquareNumberGenerator(),)