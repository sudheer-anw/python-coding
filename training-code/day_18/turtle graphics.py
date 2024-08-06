#retangula and dash lines

from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.fd(100)
timmy_the_turtle.right(90)
timmy_the_turtle.fd(100)
timmy_the_turtle.right(90)
timmy_the_turtle.fd(100)
timmy_the_turtle.right(90)
timmy_the_turtle.fd(100)
timmy_the_turtle.left(90)

for _ in range(15):
    timmy_the_turtle.fd(5)
    timmy_the_turtle.penup()
    timmy_the_turtle.fd(5)
    timmy_the_turtle.pendown()

timmy_the_turtle




screen =Screen()
# screen.exitonclick()

#idfferent kind of shapes
from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")
#pentagon
num_side = 5

for _ in range(num_side):
    angle = 360/num_side
    tim.fd(100)
    tim.right(angle)
    
num_side = 6
tim.color("black")
for _ in range(num_side):
    angle = 360/num_side
    tim.fd(100)
    tim.right(angle)

num_side = 7
tim.color("tan")
for _ in range(num_side):
    angle = 360/num_side
    tim.fd(100)
    tim.right(angle)

screen = Screen()
screen.exitonclick()




















