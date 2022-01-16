import os


datos = []


def save_user(name_user, bid_user):
    new_user = {
        "name": name_user,
        "bid": bid_user,
    }
    datos.append(new_user)


def request_data():
    name = input('Introduce tu nombre con el que deseas registrarte:\n').lower()
    bid = int(input('Introduce bid:\n'))
    return (name, bid)


def question():
    response = input('Deseas jugar?\n').lower()
    if response == 'yes':
        return True
    else:
        return False


def calculo():
    max = 0
    name = None
    for user in datos:
        bid = user["bid"]
        if bid > max :
            max = bid
            name = user["name"]

    print(f"la maxima suma fue ${max} de {name}")


def ciclo():
    play = question()
    if play == True: 
        data = request_data()
        # data = ("lynnete", 100)
        name = data[0]
        bid = data[1]
        save_user(name, bid)
        os.system('cls')
        ciclo()
    else:
        calculo()


ciclo()




