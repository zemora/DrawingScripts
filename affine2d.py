from piscript.PiModule import *
import numpy as np


def reflection():
    alpha = np.array([1, 0])
    alpha_vee = np.array([2, 1])

    P = np.array([0.4, 1]) * 0.4

    def ref(v):
        return v - np.dot(alpha, v) * alpha_vee

    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    f1 = ref(e1)
    f2 = ref(e2)

    Q = ref(P)

    P1 = np.array([0.7, -1.4]) * 0.4
    Q1 = ref(P1)

    init("reflection.eps", 400, 400)
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
    t.scale(5)
    t.atransform(T)
    place(t, *P)

    t = texinsert(r"R")
    t.scale(5)
    t.atransform(T)
    t.atransform([f1[0], f1[1], f2[0], f2[1], 0, 0])
    place(t, *Q)

    t = texinsert(r"S")
    t.scale(5)
    t.atransform(T)
    place(t, *P1)

    t = texinsert(r"S")
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


def affine2d():
    alpha = np.array([2, 0])
    alpha_vee = np.array([1, 0])

    beta_vee = np.array([-1, 0])
    beta = np.array([-2, 2])

    def ref(v):
        return v - np.dot(alpha, v) * alpha_vee

    def ref2(v):
        return v - np.dot(beta, v) * beta_vee

    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    f1 = ref(e1)
    f2 = ref(e2)

    g1 = ref2(e1)
    g2 = ref2(e2)

    init("affine2d.eps", 360, 160)
    center()
    scale(100)
    translate(0, -0.7)

    newpath()
    moveto(0, 0)
    lineto(2, 2)
    lineto(0, 2)
    closepath()
    fill(1, 1, 0)
    stroke()

    newpath()
    moveto(-2, 0)
    lineto(2, 0)
    stroke()

    N = 3
    points = []
    for k in range(N):
        r = np.array([1, 1]) *2
        word = "s" + "ts" * k
        for w in reversed(word):
            if w == "s":
                r = ref(r)
            else:
                r = ref2(r)

        newpath()
        moveto(0, 0)
        lineto(*r)
        stroke()
        points.append(r)

    for k in range(N):
        r = np.array([1, 1]) * 2
        word = "ts" * k
        for w in reversed(word):
            if w == "s":
                r = ref(r)
            else:
                r = ref2(r)

        newpath()
        moveto(0, 0)
        lineto(*r)
        stroke()
        points.append(r)

    for k in range(N):
        r = np.array([0, 1]) *2
        word = "t" + "st" * k
        for w in reversed(word):
            if w == "s":
                r = ref(r)
            else:
                r = ref2(r)

        newpath()
        moveto(0, 0)
        lineto(*r)
        stroke()
        points.append(r)

    for k in range(N):
        r = np.array([0, 1]) * 2
        word = "st" * k
        for w in reversed(word):
            if w == "s":
                r = ref(r)
            else:
                r = ref2(r)

        newpath()
        moveto(0, 0)
        lineto(*r)
        stroke()
        points.append(r)

    setarrowdims(0.03, 0.075)
    newpath()
    arrow((0, 0), alpha_vee*0.6)
    fill(1, 0.5, 0)
    stroke()

    newpath()
    arrow((0, 0), -alpha_vee*0.6)
    fill(1, 0.5, 0)
    stroke()

    ht = .5

    t = texinsert(r"$C$")
    t.translate(0, t.height/2)
    place(t, ht/2, ht)

    t = texinsert(r"$tC$")
    t.translate(0, t.height/2)
    place(t, ht*(1.5), ht)

    t = texinsert(r"$tsC$")
    t.translate(0, t.height/2)
    place(t, ht*(2.5), ht)

    t = texinsert(r"$sC$")
    t.translate(-t.width, t.height/2)
    place(t, -ht/2, ht)

    t = texinsert(r"$stC$")
    t.translate(-t.width, t.height/2)
    place(t, -ht*1.5, ht)

    t = texinsert(r"$stsC$")
    t.translate(-t.width, t.height/2)
    place(t, -ht*2.5, ht)

    col = (0, 0, 1)
    scalelinewidth(2)
    newpath()
    moveto(-4*ht, ht)
    lineto(0, ht)
    stroke(*col)

    newpath()
    moveto(ht, ht)
    lineto(4*ht, ht)
    stroke(*col)

    newpath()
    moveto(0, ht)
    lineto(ht, ht)
    stroke(0.5)

    dx = 0.03
    for k in range(-4, 5):
        newpath()
        moveto(k*ht, ht-dx)
        lineto(k*ht, ht+dx)
        stroke(*col)

    flush()

#reflection()
affine2d()
