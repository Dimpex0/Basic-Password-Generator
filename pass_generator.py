import random


person = input("Whose password is this:")
website = input('Where is this password for:')
length = int(input('Length of password:'))
symb = input('With or without special symbols:')

chars_small = 'abcdefghljklmnopqrstuvwxyz'
chars_big = 'ABCDEFGHLJKLMNOPQRSTUVWXYZ'
symbols = './!@#$%^&*()_+,'

all = chars_big + chars_small + symbols
password = '1!A'

if symb == 'with':
    all = chars_big + chars_small + symbols
else:
    all = chars_big + chars_small

for _ in range(length):
    sym = random.choice(all)
    password += sym


print(f"{person}'s password for {website} is: {password}")

file = open("password.txt", "a")
L = f"{person}'s password for {website} is: {password}\n"
print(file.writelines(L))
file.close()