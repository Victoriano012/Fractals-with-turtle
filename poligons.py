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


    angle = 5

    n = read(int)
    t.pu()
    l = calc_l(n)
    t.goto(250 - l//2, 10)
    t.color("blue")
    t.fillcolor("red")

    for x in range(2): #l//10
        for i in range(n):
            t.begin_fill()
            t.fd(l-50*x)
            pos = [t.xcor(), t.ycor()]
            t.bk(l-50*x)
            t.lt(angle)
            t.fd(l-50*x-25)
            t.goto(pos[0], pos[1])
            t.right(angle)
            t.lt(360/n)
            t.end_fill()
        t.lt(2*angle)
        t.fd(l-50*x)
        t.lt(360/n - angle)



main()
a = read(int)
