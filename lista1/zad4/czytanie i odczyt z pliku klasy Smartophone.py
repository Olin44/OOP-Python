import Smartphone
import random
import pickle

def write_binary(len_list):
    tel = []
    for i in range(len_list):
        tel.append(Smartphone.Smartphone(random.choice(["Samsung", "Sony", "Nokia"]), random.choice(["X", "Y", "Z"]), random.randint(1000,1500)))
    return tel

output = open('phones.dat', 'wb')
pickle.dump(write_binary(5), output)
output.close()

output = open('phones.dat', 'rb')
data1 = pickle.load(output )
output.close()

for i in range(len(data1)):
    print(data1[i].print_attribute())



