#Vamos a crear un programa utilizando ciclo for para calcular el numero de elementos en una lista de alturas
#que introduzcamos y vamos obtener el promedio de estas alturas

student_height = input("Introduce las alturas de los estudiantes: (usando una coma y un espacio para separar estas) ").split(", ")
suma = 0
i = 0
for student in student_height:
    i += 1
    suma += float(student_height[i - 1])
    print(f"{i} veces me estoy sumando {student_height[i - 1]}")
    #1.50, 1.60, 1.70, 1.80, 1.90

print(f"El total de las alturas de los estudiantes es: {suma}")
promedio = suma / i
print(f"Por lo que si dividimos: {suma} / {i} (numero de estudiantes) = {promedio}")
