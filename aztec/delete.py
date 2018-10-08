from piscript.PiModule import *


N = Vector(0, 1)
S = Vector(0, -1)
W = Vector(-1, 0)
E = Vector(1, 0)
Dirs = [E, N, W, S]
blue = (0, 0, 1)



def line(p, q, color=None):
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()

def dashline(p, q, color=None):
    gsave()
    setdash([4, 4], 0)
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()
    grestore()

def dots(pts, rad):
    for p in pts:
        newpath()
        circle(p, rad)
        fill(1, 0, 0)
        stroke()

def text(string, pos, sc):
    newpath()
    t = texinsert(string)
    t.scale(sc)
    place(t, pos)

def fork(p, n, L):
    p = Vector(p)
    n = Vector(n)
    q1 = p + n * L
    q2 = p + n.rotated(pi/4) * L
    q3 = p + n.rotated(-pi/4) * L
    for q in [q1, q2, q3]:
        newpath()
        moveto(p)
        lineto(q)
        stroke()

def fork_all(pts, L):
    for p, n in zip(pts, [E, N, W, S]):
        fork(p, n, L)

def delete():
    init("delete.eps", 640, 200)
    center()
    scale(50)
    #scalelinewidth(1.5)
    gsave()
    translate(-5, 0)
    
    line(N, W, color=blue)
    line(S, E, color=blue)
    dashline(E, N)
    dashline(S, W)
    fork_all([E, N, W, S], 0.3)
    dots([N,E,S,W], 0.07)
    grestore()

    gsave()
    translate(-0.5, 0)
    L = 0.4
    out = [p + L * q for p, q in zip(Dirs, Dirs)]
    inner = [p - L * q for  p, q in zip(Dirs, Dirs)]
    line(inner[1], inner[2], color=blue)
    line(inner[3], inner[0], color=blue)
    dashline(inner[0], inner[1])
    dashline(inner[2], inner[3])
    fork_all(out, 0.3)

    for p, q in zip(inner, Dirs):
        dashline(p, q)

    for p, q in zip(out, Dirs):
        line(p, q, blue)

    dots(out + inner + Dirs, 0.07)
    grestore()
    gsave()
    translate(4.5, 0)
    inner = Dirs
    dashline(inner[1], inner[2])
    dashline(inner[3], inner[0])
    dashline(inner[0], inner[1])
    dashline(inner[2], inner[3])
    fork_all(out, 0.3)

    for p, q in zip(out, Dirs):
        line(p, q, blue)

    dots(out + inner, 0.07)
    grestore()

    setarrowdims(0.04, 0.2)
    newpath()
    arrow((-3.5, 0), (-2.5, 0))
    stroke()

    newpath()
    arrow((1.5, 0), (2.5, 0))
    stroke()
    finish()


delete()
