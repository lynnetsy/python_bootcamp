#Exercise
#Se tiene un consumo introducido por el usuario de algún restaurante y nos dan la opción de 
#dejar el 10, 12 o 15% de propina del total del consumo, luego introducimos entre cuantas personas
#se dividirá la cuenta, todo esto con un formato de 2 decimales
print("Welcome to the tip calculator!")
account = float(input("Introduce the total bill:\n"))
tip = int(input("Introduce your percentage of tip you wish to left:\n"))
number_split = int(input("How many friends will split the tip?\n"))
#Aqui en money left vamos a calcular el total de la cuenta mas la propina siendo
money_left = (1 + (tip/100)) * account 
#Aqui vamos a dividir el total de la cuenta que es money left entre el numero de personas que pagaran
#que es number_split, usando la función round para que no nos salgan muchos decimales 
personal_tip = round((money_left / number_split), 2)
message = f"Each one of you have to left ${personal_tip} \n"
print(message)


