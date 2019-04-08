import Smartphone

def add_phone():
    phone = Smartphone.Smartphone("", "", 0)
    phone.set_attribute()
    return phone

def made_list():
    phone_list = []
    i = 0
    while True:
        print("Podaje dane telefonu")
        phone_list.append(add_phone())
        x = input("Kliknij x, by zakończyć, kliknij dowolny inny klawisz, by kontynuować. ")
        if x == "x":
            return phone_list

def print_list(phone_list):
    for i in range(len(phone_list)):
        print(f"\nTelefon numer {i+1}:")
        print(phone_list[i].print_attribute())
    return "Koniec listy"

print(print_list(made_list()))