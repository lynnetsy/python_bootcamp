#Vamos a crear un programa que genere contraseñas utilizando listas y loops con el for, también utilizaremos la
#funcion random para generar aleatoriamente estas contraseñas

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','#','$','%','&','(',')','*','+']
number_letters = int(input("Cuantas letras quieres en tu contraseña:\n"))
number_digits = int(input("Cuantos digitos quieres para tu contraseña:\n"))
number_symbols = int(input("Cuantos simbolos quieres que tenga tu contraseña:\n"))
total_elements = number_letters + number_digits + number_symbols
password = []

for letter in range(0, number_letters):
    random_letter = random.randint (0, len(letters))
    y = letters[random_lett er]
    password.append(y)

for number in range(0, number_digits):
    random_digit = random.randint(0, 9)
    password.append(str(random_digit))
  
for symbol in range(0, number_symbols):
    random_symbol = random.randint(0, number_symbols)
    z = symbols[random_symbol]
    password.append(z)

new = random.sample(password, total_elements)

password_as_str =''.join(new)

print(f"Tu contraseña se generara con {total_elements} de caracteres")
print(f"{password_as_str}")
        