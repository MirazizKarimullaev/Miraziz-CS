import turtle
from turtle import *
t = Turtle()
def star(x,y):
    for i in range(5):
        t.forward(x)
        t.right(y)
def starshell(z):
    length=5
    rotate=144
    for i in range(z):
        star(length,rotate)
        length +=5
        t.right(5)
starshell(60)
