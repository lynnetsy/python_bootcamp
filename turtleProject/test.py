import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

screen.colormode(255)
tim.pensize(15)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    mixcolor = (r, g, b)

    return mixcolor

def random_walk():
    for _ in range(1000):
        #colors = screen.colormode(random_color)
        direction = random.choice(tim.back(50))
        tim.setheading(direction)

