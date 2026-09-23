import turtle
from turtle import *
t = Turtle()
sidelength = 100
rotate = 90
def square(length, rotate):
     for i in range(4):
            t.forward(length)
            t.left(rotate)
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)
