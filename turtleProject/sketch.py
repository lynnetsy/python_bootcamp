import turtle as t


def turtle_commands(obj, opt):
    moves = [
        {
            'w': obj.forward,
            's': obj.backward,
            'a': obj.setheading,
            'c': obj.clear,
        }
    ]
    return moves[0][opt]


def game(turtle_commands):
    opt = (input(
        'SELECT A CHOICE \nw = sketch.forward\ns = sketch.backward\na = sketch.clockwise\nc = sketch.clear\n'
    )).lower()
    drawer = t.Turtle()
    my_screen = t.Screen()
    drawer.pensize(15)
    my_screen.colormode(cmode=255)
    actions = turtle_commands(drawer, opt)
    if opt == 'w' or opt == 's':
        distance = int(input('INTRODUCE DISTANCE:'))
        actions(distance)
    elif opt == ''

    print(actions)





game(turtle_commands)








