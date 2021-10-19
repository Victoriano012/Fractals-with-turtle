import turtle as t
import math

colors = ["navy", "dodgerblue", "mediumturquoise", "powderblue", "white"]

def rodona(size, times):
    t.fillcolor(colors[times])
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    if(times == 0):
        return
    for i in range(4):
        t.circle(size, 90)
        rodona(size//2.5, times-1)



w = 1000
h = 1000

t.setup(width=w, height=h)
t.setworldcoordinates(0, 0, w, 2*h//3)

t.speed(0)

t.bgcolor("aquamarine")

t.pu()
t.goto(w//2, 50)
t.pd()

rodona(300, 4)
