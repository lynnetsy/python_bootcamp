#Hacer una funcion que reciba la altura y el ancho para pintar una pared, 
#si un bote de pintura puede pintar 5 square de la pared, para calcular cuantos botes
#de pintura tiene que comprar una persona.
#Se calcula así no.cubetas = (altura x ancho) / 5

alt_pared = int(input("Introduce la altura de la pared\n"))
ancho_pared = int(input("Introduce ahora el ancho de la pared\n"))

def calculo_area(altura = alt_pared, ancho = alt_pared):
    numero_cubetas = (altura * ancho ) / 5
    return f"{numero_cubetas}"

calculo_area(alt_pared, ancho_pared)