import turtle as t

import random

tim = t.Turtle()
screen = t.Screen()

directions = [0, 45, 90, 135, 180, 215, 270]
actions = [tim.backward, tim.forward]
tim.pensize(15)
screen.colormode(cmode=255)


colours_dict = \
    ["royal blue", "midnight blue", "gold", "orange", "orange red", "salmon", "hot pink",
     "deep pink", "medium violet red", "purple", "violet"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

#for shape_side_n in range(3,11):
    #tim.color(random.choice(colours))
    #draw_shape(shape_side_n)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def random_walk():
    for _ in range(1000):
        tim.color(random_color())
        my_method = random.choice(actions)
        my_method(50)
        direction = random.choice(directions)
        tim.setheading(direction)


def make_spyro(colors):
    spyro = t.Turtle()
    screen_spy = t.Screen()
    screen_spy.colormode(255)
    spyro.pensize(5)

    for _ in range(500):
        spyro.circle(50)
        spyro.right(10)


if __name__ == '__main__':
    make_spyro()

def turtle_config():
    spyro = t.Turtle()
    screen_spy = t.Screen()
    screen_spy.colormode(255)
    spyro.pensize(5)

    return spyro, screen_spy
