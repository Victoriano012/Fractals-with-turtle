import turtle as t
from jutge import read

def main():
    w = 1000
    h = 500
    t.setup(width=w, height=h)
    t.setworldcoordinates(0, 0, w, h)
    mick = t.Turtle()
    mick.speed(0)
    # mick.hideturtle()
    mick.pu()
    mick.goto(25, 100)
    mick.begin_fill()
    joan = mick.clone()
    joan.fillcolor("green")
    joan.goto(25, 400)
    joan.pd()
    mick.pd()
    mick.pencolor("red")
    joan.pencolor("blue")
    r = 1
    for j in range(30):
        mick.circle(r*150, 3)
        joan.circle(-150*r, 3)
    for i in range(2):
        r *= -1
        for j in range(60):
            mick.circle(r*150, 3)
            joan.circle(-150*r, 3)
    r *= -1
    for j in range(30):
        mick.circle(r*150, 3)
        joan.circle(-150*r, 3)
    mick.end_fill()
    joan.end_fill()



main()
a = read(int)
