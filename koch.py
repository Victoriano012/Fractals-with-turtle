import turtle as t
import math


def koch(level, size):
    if level == 0:
        t.forward(size)
    else:
        koch(level-1, size/3)
        t.left(60)
        koch(level-1, size/3)
        t.right(120)
        koch(level-1, size/3)
        t.left(60)
        koch(level-1, size/3)


def main():
    n = 3
    w = 1000
    h = 1000
    t.setup(width=w, height=h)
    t.setworldcoordinates(0, 0, w, h)
    t.pu()
    t.goto(50, 250)
    t.pd()
    t.setheading(30)
    for i in range(3):
        koch(n, h/2)
        t.right(120)


main()
