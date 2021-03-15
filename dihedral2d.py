from piscript.PiModule import *
from math import *
import numpy as np

init("finite.eps", 400, 400)
center()
scale(180)

N = 5
a = pi / N

nA = np.array((1, 0))
nB = np.array((-cos(a), sin(a)))

pA = (0, 1)
pB = (cos(pi/2 - a), sin(pi/2-a))

def ref(v, n):
    
    return v - 2 * np.dot(v, n) * n


G = []
for k in range(N // 2 + 1):
    G.append("st"*k)
    G.append("t" + "st"*k)

for k in range(1, N // 2 + 1):
    G.append("ts"*k)

for k in range(N // 2):
    G.append("s" + "ts"*k)


newpath()
moveto(0, 0)
lineto(*pA)
lineto(*pB)
closepath()
fill(1, 1 ,0)

v0 = (0.2, 0.6)
for g in G:
    v = v0
    if len(g) > 0:
        for s in g[::-1]:
            if s == "s":
                v = ref(v, nA)
            else:
                v = ref(v, nB)

        t = texinsert(r"${}\mathcal{{D}}$".format(g))
        t.translate(-t.width/2, -t.height/2)
        place(t, v[0], v[1])
    else:
        t = texinsert(r"$\mathcal{{D}}$")
        t.translate(-t.width/2, -t.height/2)
        place(t, v0[0], v0[1])

for k in range(10):
    newpath()
    moveto(0, 0)
    lineto(cos(a*k+pi/2-a), sin(a*k+pi/2-a))
    if k % 2 == 0:
        stroke(0)
    else:
        stroke(1, 0.5, 0)

flush()
