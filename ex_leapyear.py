#calculo si el año es bisiesto o no 
#BISIESTO : AÑO/4=SI  PERO AÑO/100=NO
#BISIESTO : AÑO/4 SI, AÑO/100=SI Y AÑO/400=SI

print("Bienvenido al calculador de años bisiestos\n")
year = int(input("Selecciona el año que deseas calcular:\n"))

if year % 4 == 0:
    if year % 100 != 0:
        print("Es año bisiesto")
    elif year % 400 == 0:
        print("Es año bisiesto")
    else:
        print("No es bisiesto")
else:
    print("No es bisiesto")

