#Vamos a pedir una lista de nombres para que aleatoriamente el nombre que salga será
#la persona que pagará la cuenta, vamos a convertir los nombres que introduzcamos en una lista
#esta será con el método .split(" ,") y después vamos a utilizar la función len() que nos dará el
#numero de nombres que escribimos, esto para que lo utilicemos con las funciones del modulo RANDOM
#Y este sea el rango de la función randint(0, # de nombres) con este número generado de forma aleatoria
#lo utilizaremos para acceder a la lista que creamos y será el que imprimamos en nuestro mensaje final

import random

names = input("Dame los nombres separados por una coma y un espacio: \n")
list_names = names.split(", ")
print(list_names)
random_choice = random.randint (0, len(list_names - 1))
print(f"GOOD LUCK? {list_names[random_choice]} YOU HAVE TO PAY THE BILL!!!")
