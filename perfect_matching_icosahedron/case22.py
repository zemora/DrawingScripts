from piscript.PiModule import *
from math import *

init(700, 250)
center()
scale(100)

setlinewidth(2.5)

L = 0.6
ca = cos(pi/3)
sa = sin(pi/3)


x1 = -2.5
x2 = 1
gsave()
translate(x1, 0)

newpath()
moveto(0, 0)
lineto(1, 0)
stroke(1, 0, 0)

gsave()
setlinewidth(1)
setdash([4, 4], 0)
newpath()
moveto(0, 0)
lineto(-ca, sa)
stroke(0.5)

newpath()
moveto(0, 0)
lineto(-ca, -sa)
stroke(0.5)
grestore()

gsave()
setlinewidth(1)
newpath()
circle(0, 0, 0.05)
fill(1)
stroke(0, 0, 1)
grestore()

grestore()

gsave()
translate(x1+1, 0)

gsave()
setlinewidth(1)
setdash([4, 4], 0)
newpath()
moveto(0, 0)
lineto(ca, sa)
stroke(0.5)

newpath()
moveto(0, 0)
lineto(ca, -sa)
stroke(0.5)
grestore()

newpath()
circle(0, 0, 0.05)
fill(1)
setlinewidth(1)
stroke(0, 0, 1)
grestore()


setarrowdims(0.04, 0.2)
newpath()
arrow((-0.8, 0), (0.2, 0))
stroke()

gsave()
translate(x2, 0)

P1 = Vector(-ca, sa) * 0.5
P2 = Vector(-ca, -sa) * 0.5
P3 = Vector(1, 0) * 0.5

newpath()
moveto(P3)
lineto(2*P3)
stroke(1, 0, 0)


gsave()
setlinewidth(1)
setdash([4, 4], 0)
newpath()
moveto(P2)
lineto(2*P2)
stroke(0.5)

newpath()
moveto(P1)
lineto(2*P1)
stroke(0.5)
grestore()

newpath()
moveto(P1)
lineto(P2)
stroke(1, 0, 0)

gsave()
setlinewidth(1)
setdash([4, 4], 0)

newpath()
moveto(P1)
lineto(P3)
stroke(0.5)

newpath()
moveto(P2)
lineto(P3)
stroke(0.5)
grestore()


gsave()
setlinewidth(1)
newpath()
circle(P1, 0.03)
fill(1)
stroke(0, 0, 1)

newpath()
circle(P2, 0.03)
fill(1)
stroke(0, 0, 1)

newpath()
circle(P3, 0.03)
fill(1)
stroke(0, 0, 1)
grestore()
grestore()

Q1 = Vector(-1, 0) * 0.5
Q2 = Vector(ca, sa) * 0.5
Q3 = Vector(ca, -sa) * 0.5
gsave()
translate(x2+1.5, 0)
newpath()
moveto(Q3)
lineto(Q2)
stroke(1, 0, 0)

gsave()
setlinewidth(1)
setdash([4, 4], 0)
newpath()
moveto(Q1)
lineto(Q2)
stroke(0.5)
moveto(Q1)
lineto(Q3)
stroke(0.5)

newpath()
moveto(Q2)
lineto(Q2*2)
stroke(0.5)

newpath()
moveto(Q2)
lineto(Q2*2)
stroke(0.5)

newpath()
moveto(Q3)
lineto(Q3*2)
stroke(0.5)

grestore()


gsave()
setlinewidth(1)
newpath()
circle(Q1, 0.03)
fill(1)
stroke(0, 0, 1)

newpath()
circle(Q2, 0.03)
fill(1)
stroke(0, 0, 1)

newpath()
circle(Q3, 0.03)
fill(1)
stroke(0, 0, 1)
grestore()

grestore()
finish()
