import turtle
from turtle import *
t = Turtle()


def square(x,y):
    for i in range(4):
        t.forward(x)
        t.right(y)

def squareshell (iRange):
    length = 5
    for i in range(iRange):
        square(length,90)
        t.right(5)
        length= length+5

squareshell(60)
