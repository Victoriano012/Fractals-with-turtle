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
    w = 700
    h = 700
    t.setup(width=w, height=h)
    t.setworldcoordinates(0, 0, w, h)
    t.speed(0)

    angle = 5

    n = read(int)
    t.pu()
    l = calc_l(n)
    t.goto(250 - l//2, 200)
    t.color('#FF0000')
    t.pd()

    for x in range(l//3):
        for i in range(n):
            t.fd(l-3*x)
            t.lt(360/n)
        t.lt(2*angle)
        t.fd(l-3*x-2)
        t.lt(360/n)



main()
a = read(int)
