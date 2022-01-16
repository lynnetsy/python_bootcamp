import turtle as t
import random
import time
from main import random_color



def turtl(y):
    player = t.Turtle()
    color = random_color()
    player.color(color)
    player.setx(-250)
    player.sety(y)
    player.shape("turtle")
    player.shapesize(1.5)
    player.pencolor("white")
    return player


def screen():
    my_screen = t.Screen()
    my_screen.screensize(canvwidth=500, canvheight=500)
    my_screen.colormode(255)
    return my_screen

def counter():
    msg = t.Turtle()
    limit = 3
    for i in range(0, limit):
        msg.write(limit - i, align="center", font=("arial", 60, "bold"))
        time.sleep(1)
        msg.clear()


def move(turtle):
    speed = ['fastest', 'fast', 'normal', 'slow', 'slowest']
    s = random.choice(speed)
    dist = random.randint(2, 10)
    turtle.forward(dist)
    turtle.speed(s)


def winner_msg(turtle):
    winner = t.Turtle()

    color = turtle.color()
    bg_color = []
    for c in color[1]:
        bg_color.append(int(c))

    winner.color(bg_color)
    winner.write("Champion", align="center", font=("arial", 50, "bold"))


def finish_line():
    rect = t.Turtle()
    rect.shape("square")
    rect.setx(250)
    rect.sety(250)


def game():
    num_turtles = int(input("INTRODUCE NUMBER OF TURTLES\n"))
    screen()
    finish_line()
    players = []
    for _ in range(1, num_turtles + 1):
        player = turtl(_*35)
        players.append(player)

    counter()

    flag = True
    while flag:
        for turtle in players:
            move(turtle)

            if turtle.xcor() >= 250:
                winner_msg(turtle)

                flag = False
                break

    input("PRESS ENTER TO FINISH")


game()
