import turtle
from turtle import *
t = Turtle()
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)
t.backward(300)
def addsquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length + 25
addsquares(5)