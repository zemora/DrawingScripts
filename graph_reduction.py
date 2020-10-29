from piscript.PiModule import *
import math


init(320, 125)
center()
scale(40)

translate(-1.7, 0)
ts = 1.5
r = 0.08
sw = 0.03
hw = sw
dt = 0.12
for x, y in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
    newpath()
    circle(x, y, r)
    if x == -1:
        fill(1, 0.5, 0)
        stroke()
    else:
        fill(0, 1, 0.5)
        stroke()

setarrowdims(sw, hw)
newpath()
arcarrow([0, 0], 1.414, math.pi/4 + dt, math.pi/4*3-dt)
fill(0)
stroke()

newpath()
arcarrow([0, 0], 1.414, math.pi/4*3 + dt, math.pi/4*5-dt)
fill(1, 0.5, 0)
stroke()

newpath()
arcarrow([0, 0], 1.414, math.pi/4*5 + dt, math.pi/4*7-dt)
fill(0)
stroke()

newpath()
arcarrow([0, 0], 1.414, math.pi/4*7 + dt, math.pi/4-dt)
fill(1, 0.5, 0)
stroke()

t = texinsert(r"$f_1$")
t.scale(ts)
t.translate(-t.width/2, 0)
place(t, -1.8, 0)


t = texinsert(r"$f_2$")
t.scale(ts)
t.translate(-t.width/2, 0)
place(t, 1.7, 0)

# ------------------------

translate(2.2, 0)
setarrowdims(0.08, 0.2)
arrow([0.8, 0])
stroke()


translate(2.2, 0)
setarrowdims(sw, hw)
newpath()
circle(-1, 0, r)
fill(1, 0.5, 0)
stroke()

newpath()
circle(1, 0, r)
fill(0, 1, 0.5)
stroke()

newpath()
arcarrow([0, -1], 1.414, math.pi/4+0.1, math.pi/4*3-0.1)
fill(0)
stroke()


newpath()
arcarrow([0, 1], 1.414, math.pi/4*5+0.1, math.pi/4*7-0.1)
fill(0)
stroke()


finish()
