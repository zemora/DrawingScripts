from piscript.PiModule import *
import numpy as np

alpha = np.array([1, 0])
alpha_vee = np.array([2, 1])

P = np.array([0.6, 1]) * 0.4

def ref(v):
    return v - np.dot(alpha, v) * alpha_vee

e1 = np.array([1, 0])
e2 = np.array([0, 1])

f1 = ref(e1)
f2 = ref(e2)

Q = ref(P)

P1 = np.array([0.7, -1.4]) * 0.4
Q1 = ref(P1)

init("test.eps", 400, 400)
center()
scale(120)
setfont("CMR10", 12)
newpath()
moveto(0, -1.5)
lineto(0, 1.5)
stroke()

newpath()
moveto(1.6, .8)
lineto(-1.6, -.8)
stroke()


T = [1, 0.5, 0, 1, 0, 0]
t = texinsert(r"R")
#t.translate(-t.width/2, t.height/2)
t.scale(5)
t.atransform(T)
place(t, *P)

t = texinsert(r"R")
#t.translate(-t.width/2, t.height/2)
t.scale(5)
t.atransform(T)
t.atransform([f1[0], f1[1], f2[0], f2[1], 0, 0])
place(t, *Q)

t = texinsert(r"S")
t.scale(5)
t.atransform(T)
place(t, *P1)

t = texinsert(r"S")
#t.translate(-t.width/2, t.height/2)
t.scale(5)
t.atransform(T)
t.atransform([f1[0], f1[1], f2[0], f2[1], 0, 0])
place(t, *Q1)

t = texinsert(r"$\alpha=0$")
t.scale(2)
place(t, 0.1, 1.5)


setarrowdims(0.04, 0.1)
newpath()
arrow((0, 0), alpha_vee*0.6)
fill(1, 0.5, 0)
stroke()

newpath()
arrow((0, 0), -alpha_vee*0.6)
fill(1, 0.5, 0)
stroke()

t = texinsert(r"$\alpha^\vee$")
t.scale(2)
place(t, 1.2, 0.4)


flush()
