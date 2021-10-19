import turtle as t
from math import cos, pi
from jutge import read

def calc_l(n):
    r = n//4
    Ans = -0.5
    for i in range(r+1):
        Ans += cos(i*2*pi/n)
    Ans = int(Ans)+1
    return 240//Ans

def main():
    w = 500
    h = 500
    t.setup(width=w, height=h)
    t.setworldcoordinates(0, 0, w, h)
    t.speed(0)

    angle = 5

    n = read(int)
    t.pu()
    l = calc_l(n)
    t.goto(250 - l//2, 10)
    t.color("blue")
    t.fillcolor("red")

    for x in range(l//4):
        for i in range(n):
            t.begin_fill()
            t.fd(l-4*x)
            pos = [t.xcor(), t.ycor()]
            t.bk(l-4*x)
            t.lt(angle)
            t.fd(l-4*x-2)
            t.goto(pos[0], pos[1])
            t.right(angle)
            t.lt(360/n)
            t.end_fill()
        t.lt(360/n + 2*angle)
        t.fd(l-4*x-2)



main()
a = read(int)
