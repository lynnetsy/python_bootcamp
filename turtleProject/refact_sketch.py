import turtle as t


def game():
    drawer = t.Turtle()
    my_screen = t.Screen()
    drawer.pensize(5)
    drawer.color("midnight blue")
    my_screen.colormode(cmode=255)
    flag = True
    while flag:
        choice, action = user_choice(drawer)
        if choice == "e":
            flag = False
        else:
            handler_action(choice, action)


def user_choice(drawer):
    moves = {
        'w': {
            "action": drawer.forward,
            "label": "move forward"
        },
        's': {
            "action": drawer.backward,
            "label": "move backward"
        },
        'a': {
            "action": drawer.setheading,
            "label": "move counter-clockwise"
        },
        'd': {
            "action": drawer.setheading,
            "label": "move clockwise"
        },
        'c': {
            "action": drawer.clear,
            "label": "Clear sketch"
        },
        'e': {
            "action": None,
            "label": "Exit"
        }
    }

    msg = 'Select a choice\n'
    for key, item in moves.items():
        msg += f"{key} = {item['label']}\n"

    opt = input(msg).lower()
    move = moves[opt]

    return opt, move["action"]


def handler_action(choice, action):
    if choice == 'w' or choice == 's':
        distance = int(input('INTRODUCE DISTANCE:'))
        action(distance)
    if choice == 'a':
        angle = int(input('INTRODUCE ANGLE:'))
        action(-angle)
    if choice == 'd':
        angle = int(input('INTRODUCE ANGLE:'))
        action(angle)
    if choice == 'c':
        action()


game()



