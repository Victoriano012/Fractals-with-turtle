import turtle as t
import math

colors = ["deepskyblue", "mediumblue", "mediumturquoise", "white"]

def rodona(size, times):
    t.fillcolor(colors[times])
    t.begin_fill()
    t.circle(-size)
    t.end_fill()
    if(times == 0):
        return
    for i in range(4):
        t.circle(-size, 90)
        rodona(size//2.5, times-1)

def koch(times, size):
    if times == -1:
        t.forward(size)
    else:
        koch(times-1, size/3)
        t.fillcolor(colors[times])

        t.pu()
        t.begin_fill()
        t.forward(size/3)
        t.right(120)
        t.forward(size/3)
        t.right(120)
        t.forward(size/3)
        t.right(120)
        t.end_fill()
        t.pd()

        t.right(60)
        koch(times-1, size/3)
        t.left(120)
        koch(times-1, size/3)
        t.right(60)
        koch(times-1, size/3)

def p(size):
    t.fillcolor("lightblue")
    t.begin_fill()
    koch(3, size)
    t.end_fill()

    t.fillcolor("mediumpurple")
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.right(90)
    t.end_fill()

    t.fd(size//2)
    rodona(size//2, 3)
    t.bk(size//2)

    t.left(90)

w = 1000
h = 1000

t.setup(width=w, height=h)
t.setworldcoordinates(0, 0, w, h)

t.speed(0)
# t.hideturtle()

t.pu()
t.goto(w//2, h//2)
t.pd()

s = 10
for i in range(20):
    p(s)
    s *= 1.4

canvas = t.getcanvas()
canvas.postscript(file="resultat_turtle.ps", colormode='color')

print("Ja s'ha acabat")
t.done()
