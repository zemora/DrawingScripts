from piscript.PiModule import *
from math import *

init(300, 300)
center()
scale(75)
translate(0, -0.2)
R = 1.8
r = 0.15

scalelinewidth(2.5)

A = Vector(0, R)
B = Vector(R*cos(pi*7/6), R*sin(pi*7/6))
C = Vector(R*cos(pi*11/6), R*sin(pi*11/6))


newpath()
moveto(A)
lineto(B)
lineto(C)
closepath()
stroke()

# -------------
def draw_dot(v):
    newpath()
    circle(v, r)
    fill(1, 1, 0)
    stroke()

draw_dot(A)
draw_dot(B)
draw_dot(C)

t = texinsert(r"{\bf 4}")
t.scale(3.6)
place(t, -0.1, -1.5)
finish()
