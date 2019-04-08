import Coin


coin1 = Coin.Coin1()
coin1.throw()
print(coin1.side)

coin2 = Coin.Coin1()
coin1.throw()
print(coin1.side)

coin1 = Coin.Coin2()
coin1.throw()
print(coin1.side)

coin = Coin.Coin1()
for i in range(15):
    coin.throw()
    print(f"Rzut nr {i+1} dał wynik: {coin.side}")