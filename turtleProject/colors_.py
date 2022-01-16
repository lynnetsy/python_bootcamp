import colorgram
from PIL import Image
import turtle as t
import random

filename = "sakura_japan.jpg"
img = Image.open(filename)

draws = t.Turtle()
my_screen = t.Screen()
my_screen.colormode(255)
my_screen.setup(800, 800)

my_palette = colorgram.extract(filename, 20)


def palette_colors(my_palette, n):
    first_color = my_palette[n]
    rgb = first_color.rgb
    return rgb


i = 0
x = 0
for i in range(10000):
    draws.dot(25, palette_colors(my_palette, i))
    draws.forward(10 + 22 + 10 * i)
    draws.sety(x + 10)
   # draws.dot(25, palette_colors(my_palette, i))
    #draws.left(90)
    #draws.dot(25, palette_colors(my_palette, i))



    #if draws.ycor() >= my_screen.setup(800, 800):
        #draws.left(-45)
        #draws.backward(40)



