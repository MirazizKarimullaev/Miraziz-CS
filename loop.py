import turtle
from turtle import *
t = Turtle()
def square():
    for i in range(72):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.right(5)
square()