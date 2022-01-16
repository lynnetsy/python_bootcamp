#Hacer un piedra, papel o tijera donde Tu introduzcas una de estas opciones mediante un input
#Y un numero dependiendo de esta opcion, mientras que la computadora aleatoriamente va a generar otra
#opcion y con eso vamos a ver quien gana.
import random

option = int(input("Selecciona una de las opciones: \n 1.Tijera\n2.Piedra\n3.Papel\n"))
list =["tijera", "piedra", "papel"]
x = list[option - 1]
y = random.randint(1,3)
compu_option = list[y - 1]  
print(f"El rival ha escogido {compu_option}")

if x == compu_option :
    print("Es un empate")
elif x == "tijera" and compu_option == "piedra":
    print(f"Escogiste {x}. Pierdes contra piedra")
elif x == "tijera" and compu_option == "papel":
    print(f"Escogiste {x}. Ganas contra papel")
elif x == compu_option :
    print("Es un empate")
elif x == "piedra" and compu_option == "papel":
    print(f"Escogiste {x}. Pierdes contra papel")
elif x == "piedra" and compu_option == "tijera":
    print(f"Escogiste {x}. Ganas contra tijera")
elif x == compu_option: 
    print("Es un empate")
elif x == "papel" and compu_option == "piedra":
    print(f"Escogiste {x}.Ganas contra {compu_option}")
elif x == "papel" and compu_option == "tijera":
    print(f"Escogiste {x}. Perdiste contra {compu_option}")

