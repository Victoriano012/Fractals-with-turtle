import turtle as t
import random

############################################################################################################
# un parell de funcions auxiliars

def dist(punt): # distancia d'un punt a la posició de la tortuga
    return (t.xcor()-punt[0])**2 + (t.ycor()-punt[1])**2
def color_random():
    return list([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])


############################################################################################################
# Funció recursiva:

def espiral(ite, graus, radi):
    if(ite == 0): # cas base
        t.pd()
        t.color(color_random())

    pos = [t.xcor(), t.ycor(), t.heading()]
    prev = [0, 0]

    for i in range(radi):
        t.circle(i, graus) # fa les espirals com molts sectors de cerle molt petits, que creixen lentament
        if(ite != 0 and dist(prev) > (radi/7)**2*1.6): # només fa la recursió prou lluny de l'anterior vegada
            espiral(ite-1, 7*graus, radi//11) # pas recursiu
            prev = [t.xcor(), t.ycor()]

    if(ite == 0): t.pu()
    t.goto(pos[0], pos[1]) # torna a la posició d'abans de fer l'espiral, per poder seguir amb la més gran
    t.setheading(pos[2])


############################################################################################################
# setup

w = 1500
h = 1500

t.setup(width=w, height=h)
t.setworldcoordinates(0, 0, w, h)

t.penup()
t.goto(w/2, h/2)
t.pensize(2)

t.speed(0)
t.shape("turtle")

random.seed()

###########################################################################################################

espiral(2, 2, 700) # fer el dibuix


canvas = t.getcanvas()
canvas.postscript(file="resultat_turtle.ps", colormode='color')
t.done()
