#TYPES OF OPERATORS PYTHON
#** , * , /, + -
#** = float number


#BMI CALCULATOR
#BMI = WEIGHT(KG) / HEIGHT ** 2 (M*2)

height = float(input("Enter your height\n"))
weight = float(input("Enter your weight\n"))

bmi = weight / (height ** 2)
bmi_as_int = int(bmi)

print(bmi)
print(bmi_as_int)


#Operations with python

sum = 2 + 2
substraction = 10 - 5
multiplication = 2 * 2
power = 2 ** 2
division = 10 / 2

#Jerarquía de operaciones, fijarse en el resultado 
#Se sabe que primero se resuelven las multiplicaciones
#luego la división y después las sumas y restas

order_operations = 3 * 3 + 3 / 3 - 3
print(order_operations)

#Vamos a ver la forma en la que podemos imprimir el tipo de dato que devuelve
#nuestra operacion (dependiendo de esta) y la podemos mandar a llamar creando otra
#variable o usando F-string poniendo una f al principio del print y usando {nombre_variable}
#en estas f-strings pueden mandarse a llamar funciones {type(nombre_variable)}

type_sum = str(type(sum))
type_substraction = str(type(substraction))

print(sum, "sum type is " + type_sum)
print(substraction, "substaction type is " + type_substraction)
print(multiplication)
print(power)
print(division)
print(f"result of multiplication {multiplication}")
print(f"type of multiplication {type(multiplication)}")

#Redondear decimales o usar solo enteros en las divisiones
#para redondear un numero utilizaremos nuestra función 
#round( division , numero de decimales mostrados en pantalla)

print(8 / 3)
print(round(8 / 3, 3))

#O si solo necesitamos que nos den el entero de una división
#utilizaremos //

print( 8 // 3)

#CONTADORES EN PYTHON
# Se usan para manipular un valor con el anterior (se sobreescriben)

score = 1
print(score)
score += 1
print(f"aqui se va a ir sumando el nuevo valor de score con el anterior, por lo que es {score}")

score_substraction = 5
print(f"el primer valor sera {score_substraction}")
score_substraction -= 2
print(f"ahora se resto el valor anterior sobreescribiendo el resultado siendo {score_substraction}")



