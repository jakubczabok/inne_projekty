import sys
import random
import string
import os
os.system("cls")
password = []
characters_left = -1
password_lenght = int(input("Liczba znaków hasła: "))
if password_lenght < 5:
    print("Hasło musi mieć co najmniej 5 znaków")
    sys.exit(0)
else:
    characters_left = password_lenght
lowercase_letters = int(input("Liczba małych liter: "))
characters_left = characters_left - lowercase_letters
if characters_left == 0:
    print("Wyczerpano limit znaków")
if characters_left < 0 or lowercase_letters < 0:
    print("Nieodpowiednia liczba znaków")
    sys.exit(0)
print ("Pozostało znaków:", characters_left)
uppercase_letters = int(input("Liczba dużych liter: "))
characters_left = characters_left - uppercase_letters
if characters_left == 0:
    print("Wyczerpano limit znaków")
if characters_left < 0 or uppercase_letters < 0:
    print("Nieodpowiednia liczba znaków")
    sys.exit(0)
print ("Pozostało znaków:", characters_left)
digits = int(input("Liczba cyfr: "))
characters_left = characters_left - digits
if characters_left > 0:
    print("Wykorzystano za mało znaków")
    sys.exit(0)
if characters_left < 0 or digits < 0:
    print("Nieodpowiednia liczba znaków")
    sys.exit(0)
for i in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
random.shuffle(password)
print("Hasło:", "".join(password))
sys.exit(0)