from piscript.PiModule import *
from math import *

init(800, 800)
center()
scale(200, 200)
scalelinewidth(3)

L = 1.7
sc = 0.8
v1 = Vector(cos(pi/3), sin(pi/3))
v2 = Vector(cos(2*pi/3), sin(2*pi/3))
v3 = Vector(cos(5*pi/6), sin(5*pi/6))
sw = 0.03
hw = 4 * sw
setarrowdims(sw, hw)

#  --- fill region C ---
newpath()
moveto(0, 0)
lineto(L*v1)
lineto(0, L)
closepath()
fill(1, 1, 0)

# ---  two mirrors ------
newpath()
moveto(0, -L)
lineto(0, L)
stroke()

newpath()
moveto(-L*v1)
lineto(L*v1)
stroke()

# ---- -x axis -----

newpath()
moveto(-L, 0)
lineto(0, 0)
stroke()

# ---- alpha_t -----

newpath()
arrow((0, 0), L*sc*v3)
stroke()

# ----- alpha_s -----

newpath()
arrow((0, 0), (L*sc, 0))
stroke()

# ----- t(alpha_s) ------

newpath()
arrow((0, 0), L*sc*v2)
stroke()

# ----- arcarrow shows rotation st -----

newpath()
arcarrow(0, 0, L*0.76, pi/12, pi/10+pi/6)
fill(1, 0, 0)
stroke()

# ----- add tex labels -----

fontscale = 4

t = texinsert(r"$\alpha_s$")
t.scale(fontscale)
t.translate(-t.width/2, -t.height)
place(t, L*(sc+0.1), 0)

t = texinsert(r"$\alpha_t$")
t.scale(fontscale)
t.translate(-t.width/2, -t.height)
place(t, L*(sc+0.15)*v3)

t = texinsert(r"$t(\alpha_s)$")
t.scale(fontscale)
t.translate(-t.width, -t.height)
place(t, L*(sc+0.15)*v2)


t = texinsert("${\cal C}$")
t.scale(fontscale)
t.translate(-t.width, -t.height)
place(t, L*(sc-0.1)*((v1+Vector(0, 1))/2))

t = texinsert(r"$s=0$")
t.scale(fontscale)
t.translate(-t.width, -t.height)
place(t, 0, L+0.15)

t = texinsert(r"$t=0$")
t.scale(fontscale)
t.translate(-t.width, -t.height)
place(t, (L+0.25)*v1)

t = texinsert(r"$st$")
t.scale(fontscale)
place(t, L*sc*cos(pi/6.5), L*sc*sin(pi/6.5))

# ---- angle arcs -----

newpath()
setdash([2, 2], 0)
arc(0, 0, 0.4, 2*pi/3, pi)
stroke()

t = texinsert(r"$\frac{\pi}{m}$")
t.scale(fontscale/1.5)
t.translate(-t.width/2, t.height)
place(t, 0.6 * (v2+v3) / 2)

t = texinsert(r"$\frac{\pi}{m}$")
t.scale(fontscale/1.5)
t.translate(-t.width/2, t.height)
place(t, 0.6 * (v3+(-1, 0)) / 2)

# --------------------------------
finish()
