#Calcular numeros pares e impares usando condicionantes

number = int(input("Introduce el número para calcular:\n"))
even_number = number % 2

if even_number == 0:
    print("El número es par")
else:
    print("El número es impar")


#Vamos a actualizar nuestro ejercicio de BMI usando if, elif, else
#Para dar 5 mensajes distintos dependiendo del resultado del bmi 
#desde que este bajo de peso hasta clinicamente obeso

#BMI CALCULATOR
#BMI = WEIGHT(KG) / HEIGHT ** 2 (M*2)

height = float(input("Enter your height\n"))
weight = float(input("Enter your weight\n"))

bmi = weight / (height ** 2)

if bmi <= 18.5 :
    print("You are underweight")
elif 18.5 < bmi <= 25 :
    print("You have a normal weight")
elif 25 < bmi <= 30 :
    print("You are overweight")
elif 30 < bmi <= 35 :
    print("You are obese")
else:
    print("You are clinically obese")
