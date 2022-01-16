from resources import machine_resources, drinks


def order():
    answer = input("What would you like\nEspresso\nLatte\nCappuccino\n").lower()
    return answer


def print_report(machine_resources):
    msg = f"""------------------------------------
Resources of Coffee Machine Lynnis:
    * Water: {machine_resources['water']}
    * Milk: {machine_resources['milk']}
    * Coffee: {machine_resources['coffee']}
    * Money available: {machine_resources['cash']}
------------------------------------"""
    print(msg)
    return msg


def get_drink(user_choice, drinks):
    try:
        return drinks[user_choice]
    except KeyError:
        return None


def check_resources(resources, drink):
    return resources['water'] >= drink['water'] \
            and resources['milk'] >= drink['milk'] \
            and resources['coffee'] >= drink['coffee']


def rest_resources(resources, drink):
    resources['water'] -= drink['water']
    resources['milk'] -= drink['milk']
    resources['coffee'] -= drink['coffee']

    return resources


def transaction(value, resources):
    total = 0
    print(f'Total: ${value}')
    while total <= value:
        coins = float(input(f'Insert coin (${total}):\n'))
        resources['cash'] += coins
        total += coins

    if total > value:
        change = total - value
        resources['cash'] -= change
        print(f'Take your {change}')

    return resources


def machine(resources):
    print_report(resources)

    user_choice = order()
    if user_choice == 'off':
        return

    drink = get_drink(user_choice, drinks)
    if drink is None or not check_resources(resources, drink):
        print('xxxxxx La maquina no puede procesar tu bebida xxxxxx')
        return machine(resources)

    value = drink['value']
    resources = transaction(value, resources)
    resources = rest_resources(resources, drink)
    if drink is None:
        print('xxxxxx Esa bebida no existe xxxxxx')
    else:
        print(f'!!! Tu bebida esta lista, {drink} !!!')

    machine(resources)


machine(machine_resources)
