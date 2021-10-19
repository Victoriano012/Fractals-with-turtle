import turtle as t
import math

colors = ["darkgreen", "forestgreen", "mediumseagreen", "mediumspringgreen"]

def triangle(color, l):
    t.fillcolor(color)
    t.pd()
    t.begin_fill()
    t.left(60)
    t.fd(l)
    t.right(120)
    t.fd(l)
    t.end_fill()
    t.right(30)
    t.pu()

def dibuix(l, i):
    triangle(verds[i%4], l)
    for j in range(2):
        t.fd(l)
        t.right(90)
    t.fd(l/10)
    t.left(60)
    t.backward(l/10)
    t.right(90)

w = 1000
h = 1000

t.setup(width=w, height=h)
t.setworldcoordinates(0, 0, w, h)

t.speed(0)

t.pu()
t.goto(50, 600)

t.hideturtle()
t.bgcolor("aquamarine")

for i in range(39):
    l = 1500/3 - i*1500/120
    dibuix(l, i)
    t.fd(l//5)
    t.right(10)

t.done()
