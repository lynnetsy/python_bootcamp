import turtle as t
import random
import Turtle as t


# 3 classes: snake, food, scoreboard
def screen():
    my_screen = t.Screen()
    my_screen.screensize(canvwidth=500, canvheight=500)
    my_screen.colormode(255)
    return my_screen


class Snake:

    def __init__(self):
        self.body = []
        self.xcord = -42
        self.pos_x = None
        self.point = None
        self.move_head()
        self.new_point()

    def draw_snake(self, size=3):
        snake = []
        for _ in range(1, size + 1):
            pos_x = self.xcord - (_ * 21)
            point = self.new_point(pos_x)
            snake.append(point)
        return self.body

    def new_point(self, pos_x, pos_y=0):
        point = t.Turtle()
        point.shape("square")
        point.setx(pos_x)
        point.sety(pos_y)
        return point

    def move(self, last_cmd):
        cmd = input("Introduce\n a)move backward \n d)move forward \n w)move up\n s)move down\n").lower()
        directions = {
            'a': 'd',
            'd': 'a',
            'w': 's',
            's': 'w'
        }
        last_pos = self.body[0].pos()

        if cmd != directions[last_cmd]:
            self.move_head(self.body, cmd)
            for _ in range(1, len(self.body)):
                x = last_pos[0]
                y = last_pos[1]
                last_pos = self.body[_].pos()
                self.body[_].setposition(x, y)

        return cmd, last_pos

    def move_head(self, cmd):
        head = self.body[0]
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

    def eat(self, food, body):
        head = body[0]
        return food.pos() == head.pos()

    def grow_up(self, body, last_pos):
        new_square = self.new_point(last_pos[0], last_pos[1])
        self.body.append(new_square)

    def bited(self):
        head = self.body[0]
        for _ in range(1, len(self.body)):
            flag = self.body[_]
            if head.pos() == flag.pos():
                return True
        return False


class Food:
    def __init__(self):
        self.square = None
        self.get_axis()
        self.set_food_pos()
        self.get_axis()

    def draw_food(self):
        self.square = t.Turtle()
        self.square.shape("square")
        self.square.color("pink")
        self.set_food_pos(self.square)
        return self.square

    def set_food_pos(self):
        axis_x, axis_y = self.get_axis()
        self.square.setposition(axis_x, axis_y)

    def get_axis(self):
        x = random.randint(-3, 3) * 21
        y = random.randint(-3, 3) * 21
        return x, y


def game():
    screen()
    food = Food
    snake = Snake
    cmd = "d"

    while not snake.bited():
        cmd, last_pos = snake.move(cmd)
        if snake.eat(food):
            snake.set_food_pos(food)
            snake.grow_up(snake, last_pos)