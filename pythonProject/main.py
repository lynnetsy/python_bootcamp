import turtle as t
import random


def screen():
    my_screen = t.Screen()
    my_screen.screensize(canvwidth=500, canvheight=500)
    my_screen.colormode(255)
    return my_screen


def draw_snake(xcord, size=3):
    snake = []
    for _ in range(1, size + 1):
        pos_x = xcord - (_*21)
        point = new_point(pos_x)
        snake.append(point)
    return snake


def new_point(pos_x, pos_y=0):
    point = t.Turtle()
    point.shape("square")
    point.setx(pos_x)
    point.sety(pos_y)
    return point


def draw_food():
    square = t.Turtle()
    square.shape("square")
    square.color("pink")
    set_food_pos(square)
    return square


def set_food_pos(food):
    axis_x, axis_y = get_axis()
    food.setposition(axis_x, axis_y)


def get_axis():
    x = random.randint(-3, 3) * 21
    y = random.randint(-3, 3) * 21
    return x, y


def move(snake, last_cmd):
    cmd = input("Introduce\n a)move backward \n d)move forward \n w)move up\n s)move down\n").lower()
    directions = {
        'a': 'd',
        'd': 'a',
        'w': 's',
        's': 'w'
    }
    last_pos = snake[0].pos()

    if cmd != directions[last_cmd]:
        move_head(snake, cmd)
        for _ in range(1, len(snake)):
            x = last_pos[0]
            y = last_pos[1]
            last_pos = snake[_].pos()
            snake[_].setposition(x, y)

    return cmd, last_pos


def move_head(snake, cmd):
    head = snake[0]
    last_pos = head.pos()
    x = last_pos[0]
    y = last_pos[1]
    if cmd == "a":
        x = last_pos[0] - 21
        y = last_pos[1]
    elif cmd == "s":
        x = last_pos[0]
        y = last_pos[1] - 21
    elif cmd == "d":
        x = last_pos[0] + 21
        y = last_pos[1]
    elif cmd == "w":
        x = last_pos[0]
        y = last_pos[1] + 21

    head.setposition(x, y)


def eat(food, snake):
    head = snake[0]
    return food.pos() == head.pos()


def grow_up(snake, last_pos):
    new_square = new_point(last_pos[0], last_pos[1])
    snake.append(new_square)


def bited(snake):
    head = snake[0]
    for _ in range(1, len(snake)):
        body = snake[_]
        if head.pos() == body.pos():
            return True
    return False


def game():
    screen()
    food = draw_food()
    snake = draw_snake(-42)
    cmd = "d"

    while not bited(snake):
        cmd, last_pos = move(snake, cmd)
        if eat(food, snake):
            set_food_pos(food)
            grow_up(snake, last_pos)


game()
