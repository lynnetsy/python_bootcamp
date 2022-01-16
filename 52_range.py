#Vamos a escribir una suma del 1 al 100 incluyendo a este ultimo, utilizando la función range 
#solo se debe de imprimir el resultado final de esta sumatoria

sumatoria = 0
for number in range(2, 101, 2):
    sumatoria += number

print(sumatoria)