
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return (n1 / n2)

def ask_numbers():
    number1 = int(input("Introduce el primer numero con el que deseas realizar una operacion\n"))
    number2 = int(input("Ahora el 2do numero\n"))
    return (number1, number2)

def flujo():
    choice = input("Bienvenido a la calculadora\n Escribe el tipo de operación que deseas realizar\n").lower()
    numbers = ask_numbers()
    n1 = numbers[0]
    n2 = numbers[1]
    result = 0
    if choice == 'suma':
        result = add(n1, n2)
    elif choice == 'resta':
        result = substract(n1, n2)
    elif choice == 'multiplicacion':
        result = multiply(n1,n2)
    else:
        result = divide(n1,n2)
    print(f"El resultado de tu {choice} es {result} ")

primer = flujo()

