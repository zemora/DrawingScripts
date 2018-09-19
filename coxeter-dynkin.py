from piscript.PiModule import *
from math import *

init(400, 100)
center()
scale(100)

ex = 1.6
r = 0.08
setlinewidth(2.5)


newpath()
circle(0, 0, r)
fill(1, 1, 0)
stroke()

newpath()
circle(-ex, 0, r)
fill(1, 1, 0)
stroke()

newpath()
circle(ex, 0, r)
fill(1, 1, 0)
stroke()

newpath()
circle(-ex, 0, 2*r)
stroke()

t = texinsert(r"${\bf 4}$")
t.scale(3)
t.translate(-t.width, -t.height/2)
place(t, -ex/2, 0.2)

"""
newpath()
circle(0, 0, 2*r)
stroke()

newpath()
circle(ex, 0, 2*r)
stroke()


newpath()
moveto(-ex+2*r, 0)
lineto(-2*r, 0)
stroke()

newpath()
moveto(2*r, 0)
lineto(ex-2*r, 0)
stroke()
"""
newpath()
moveto(-ex+2*r, 0)
lineto(-r, 0)
stroke()

newpath()
moveto(r, 0)
lineto(ex-r, 0)
stroke()

finish()
