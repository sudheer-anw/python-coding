from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.speed(10)
tim.pensize(10)

colors = ["Red", "Blue", "Green", "Purple", "Orange", "Pink", "Brown", "Gray", "Black", "Cyan", "Magenta", "Lime", "Maroon", "Navy", "Olive", "Teal", "Silver", "Gold"]

directions = [0,90, 180, 270,360]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(25)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()





