'''Zadanie2(1pkt)
Utwórzklase˛ Coin
.Bezparametrowy konstruktortejklasypowinien tworzyć atrybut (side) utrzymuja˛cy aktualna˛
strone˛ monety.
Zdeﬁniuj dwie metody: throw() - losowo "zmienia" strone˛ monety,
show_side() - zwraca wartość atrybutu side.
a) Utwórzkilkaobiektówklasy Coin iwywołajichmetody.
b) Utwórzmodułzawieraja˛cydeﬁnicje˛klasy
Coiniosobnyplikzprogramemktóry goimportujeiwykonajsymulacje˛pie˛tnasturzutówmoneta˛. '''

class Coin1:
    def __init__(self):
        self.throw();

    def throw(self):
        import random
        self.side = random.choice(["orzeł", "reszka"]) #losuje z listy

    def show_side(self):
        return self.side
    def __str__(self):
        return f"sdss {self.argument}"

coin2 = Coin1()
coin2.throw()
coin2.show_side()
print(coin2.show_side())

class Coin2:
    def __init__(self):
        pass

    def throw(self):
        import random
        self.side = random.randint(0,1)  #losowanie z zakresu

    def show_side(self):
        return self.side

