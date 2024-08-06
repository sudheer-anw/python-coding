from turtle import Turtle,Screen
import random
tim = Turtle()

color = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

def draw_shape (num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(color))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
