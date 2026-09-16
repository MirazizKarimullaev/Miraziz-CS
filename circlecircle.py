import turtle
from turtle import *
t = Turtle()
def circle():
    for i in range(180):
        t.forward(2)
        t.left(2)

def doubleCircles(iRange):
    for i in range(iRange):
        circle()
        t.right(10)
doubleCircles(36)