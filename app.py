import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def rectangle():
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
rectangle()

t.left(180)
t.forward(300)
t.left(180)

def triangle():
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
triangle()