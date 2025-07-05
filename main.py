import random
import turtle
from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.speed("fastest")
import colorgram

def colors_list():
    rgb_colors = []
    image_colors = colorgram.extract("image.jpg", 30)
    for color in image_colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        rgb_colors.append((r , g, b))
    return rgb_colors
def color_line():
    colors = colors_list()
    for i in range(10):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.color(random.choice(colors))
        timmy.dot(size=20)
def hirst_painting():
    timmy.penup()
    timmy.setheading(220)
    timmy.forward(340)
    timmy.pendown()
    timmy.setheading(0)
    for i in range(10):
        color_line()
        timmy.setheading(90)
        timmy.penup()
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

hirst_painting()


screen.exitonclick()
