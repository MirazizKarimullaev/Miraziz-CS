import turtle
from turtle import *
t = Turtle()
def square():
     for i in range(4):
            t.forward(100)
            t.left(90)
t.backward(300)
def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)
triangle()
t.forward(300)
def coolloop():
    for i in range(60):
       square()
       t.right(5)
coolloop()