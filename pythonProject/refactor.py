import turtle as t
import random
import time


def screen():
    my_screen = t.Screen()
    my_screen.screensize(canvwidth=500, canvheight=500)
    my_screen.colormode(255)
    return my_screen


def draw_snake():
    snake = []
    position = 10
    for _ in range(0, 3):
        point = t.Turtle()
        point.shape("square")
        point.setx(position)
        point.pos()
        position += 10
        snake.append(point)

    return snake


def game():
    snake = draw_snake()
    for element in snake:
        print(element.pos())

    time.sleep(3)

game()