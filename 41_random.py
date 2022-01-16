#USAR EL MODULO RANDOM PARA GENERAR NUMEROS ALEATORIOS

import random

#random_integer = random.randint(1,10)
#print(random_integer)

#random_float = random.random()
#print(random_float)

#GENERAR un numero decimal entre 0 y 5

#random_num = random.uniform(0,5)
#print(random_num)
#print(f"este es el decimal entre 0 y 5 {random_decimal}")

#CREAR UN JUEGO QUE USE RANDOM Y DEPENDIENDO DE LO QUE TE SALGA
#PONER TAIL OR HEAD

random_choice = random.randint(0,1)
print(random_choice)

if random_choice == 1:
    print("\nHEADS\n")
else:
    print("\nTAILS\n")