#Vamos a crear un programa donde vamos a crear una matriz, la forma en la que la vamos a crear es
#haciendo 3 listas de 3 elementos vacíos que contengan un espacio, luego vamos a crear una lista que
#contenga estas 3 listas y la vamos a imprimir con cierto formato, luegp tenemos que preguntar mediante
#un input donde vamos a poner la X de dicha matriz, se empieza por columna y luego por hilera

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

treasure_choice = input("Where do you want to put the treasure?\n please first write the column and then the row (please use a space between them):\n")
location = treasure_choice.split(" ")
x = int(location[0])
y = int(location[1])

map[x - 1][y - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

