import turtle as t
import random

###########################################################################################################
# un parell de funcions auxiliars

def color_random():
    return list([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])


###########################################################################################################
# Funció recursiva:

def tree(ite, len):
    if(ite == 0):
        return

    t.pensize(ite)

    t.color(color_random())
    t.fd(len)

    pos = [t.xcor(), t.ycor(), t.heading()]

    times = random.randint(2, 4)
    for i in range(times):
        t.right(random.randint(150*i//times - 75, 150*(i+1)//times-75))
        tree(ite-1, len*random.uniform(0.4, 0.75))
        t.goto(pos[0], pos[1])
        t.setheading(pos[2])

# (si, només són 14 linies)
###########################################################################################################
# setup

w = 1400
h = 1400

t.setup(width=w, height=h)
t.setworldcoordinates(0, 0, w, h)

t.pu()
t.goto(w/2, 0)
t.left(90)
t.pd()

t.speed(0)
t.hideturtle()

random.seed()

###########################################################################################################

tree(7, 500) # fer el dibuix


canvas = t.getcanvas()
canvas.postscript(file="resultat_turtle.ps", colormode='color')

print("Ja s'ha acabat")
t.done()
