import random



def ask_number():
    ask = input("Escribe un número\n")
    return int(ask)

def random_number():
    random_number = random.randint(0, 100)
    return random_number

def get_message(diferencia,rand_number, user_number):
    if diferencia == 0:
        message = "Acertaste"
    elif diferencia <= 10 and rand_number < user_number:
        message = "Estas cerca, estas por debajo del numero"
    elif diferencia <= 10 and rand_number > user_number:
        message = "Estas cerca!, estas por arriba del numero"
    elif diferencia > 10 and rand_number < user_number:
        message = "Estas lejos :( muy por abajo del numero"
    elif diferencia > 10 and rand_number > user_number:
        message = "Estas lejos :( muy por arriba del numero"
    return message

def difficult(dif_choice):
    if dif_choice == 'facil':
        oportunity = 10
    elif dif_choice == 'medio':
        oportunity = 5
    else:
        oportunity = 1
    return oportunity

def program():
    
    dif_choice = input("Escoge la dificultad en la que quieres jugar:\n").lower()
    number_op = difficult(dif_choice)
    rand_number = random_number()
    print(f"{rand_number}")

    c = 0
    while c < number_op:
        user_number = ask_number()
        diferencia = abs(rand_number - user_number)
        message = get_message(diferencia, user_number, rand_number)
        print(message)
        if diferencia == 0:
            return
        
        c+=1



inicio = program()

