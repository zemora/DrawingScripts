from piscript.PiModule import *
import numpy as np


def hyperbolic2d():
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

    init("hyperbolic2d.eps", 500, 300)
    center()
    scale(100)
    translate(0, -1.45)

    newpath()
    moveto(0, 0)
    lineto(4, 4)
    lineto(0, 4)
    closepath()
    fill(1, 1, 0)
    stroke()

    newpath()
    moveto(-4, 0)
    lineto(4, 0)
    stroke()

    N = 3
    points = []
    for k in range(N):
        r = np.array([1, 1]) * 8
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
        r = np.array([1, 1]) * 8
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
        r = np.array([0, 1]) * 8
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
        r = np.array([0, 1]) * 8
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

    ht = .8

    sc = 1.5
    TEX = r"\mathcal{{D}}"
    t = texinsert(r"${}$".format(TEX))
    t.scale(sc)
    t.translate(0, t.height/2)
    place(t, ht/2, ht)

    #t = texinsert(r"$tC$")
    t = texinsert(r"$t{}$".format(TEX))
    t.scale(sc)
    t.translate(0, t.height/2)
    place(t, ht*(1.5), ht)

    #t = texinsert(r"$tsC$")
    t = texinsert(r"$ts{}$".format(TEX))
    t.scale(sc)
    t.translate(0, t.height/2)
    place(t, ht*(2.5), ht)

    #t = texinsert(r"$sC$")
    t = texinsert(r"$s{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width, t.height/2)
    place(t, -ht/2, ht)

    #t = texinsert(r"$stC$")
    t = texinsert(r"$st{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width, t.height/2)
    place(t, -ht*1.5, ht)

    #t = texinsert(r"$stsC$")
    t = texinsert(r"$sts{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width, t.height/2)
    place(t, -ht*2.5, ht)

    col = (0, 0, 0)
    newpath()
    moveto(-4*ht, ht)
    lineto(4*ht, ht)
    stroke(*col)


    dx = 0.03
    for k in range(-8, 8):
        newpath()
        moveto(k*ht, ht-dx)
        lineto(k*ht, ht+dx)
        stroke(*col)

    sc = 4
    P = np.array([0.4, 1.2])
    t = texinsert("$R$")
    t.scale(sc)
    place(t, *P)

    t = texinsert("$sR$")
    t.scale(sc)
    t.atransform([f1[0], f1[1], f2[0], f2[1], 0, 0])
    Q = ref(P)
    place(t, *Q)

    t = texinsert("$tR$")
    t.scale(sc)
    t.atransform([g1[0], g1[1], g2[0], g2[1], 0, 0])
    Q = ref2(P)
    place(t, *Q)

    t = texinsert("$stR$")
    t.scale(sc)
    t.atransform([g1[0], g1[1], g2[0], g2[1], 0, 0])
    t.atransform([f1[0], f1[1], f2[0], f2[1], 0, 0])
    Q = ref2(P)
    Q = ref(Q)
    place(t, *Q)

    flush()

#reflection()
hyperbolic2d()
