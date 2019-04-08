class Account:
    def __init__(self, balance):
        self.__balance = balance
    def pay(self, payment):
        self.__balance += payment
    def take(self, withdrawal):
        if self.__balance - withdrawal >= 0:
            self.__balance -= withdrawal
        else:
            print("Brak środków")
    def show_balance(self):
        return self.__balance
    def __str__(self):
        return f"Saldo konta wynosi {self.__balance}"

def test():
    MaciekAccount = Account(500)
    print(MaciekAccount)
    MaciekAccount.pay(400)
    MaciekAccount.take(900)
    MaciekAccount.pay(900)
    print(f"Teraz stan konta wynosi: {MaciekAccount.show_balance()}")
    print(MaciekAccount)

test()


