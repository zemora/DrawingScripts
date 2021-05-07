from piscript.PiModule import *


init("macdonald-bijection.eps", 400, 340, "noclip")
scale(40)
translate(1, 1)
setarrowdims(0.08, 0.15)

ts = 1



gsave()
setdash([6, 6], 0)
N = 8
M = 6
for k in range(0, N+1):
    moveto(k, 0)
    lineto(k, M)
    stroke(0.8)
for k in range(0, M+1):
    moveto(0, k)
    lineto(N, k)
    stroke(0.8)
grestore()

newpath()
arrow([8, 0], [8.5, 0])
stroke()

newpath()
arrow([0, 6], [0, 6.5])
stroke()

scalelinewidth(1.5)
newpath()
moveto(0, 0)
lineto(1, 0)
lineto(1, 1)
lineto(3, 1)
lineto(3, 2)
lineto(6, 2)
lineto(6, 4)
lineto(7, 4)
lineto(7, 5)
lineto(7, 6)
lineto(8, 6)
stroke()



t = texinsert("$x$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 8.5, -0.5)

t = texinsert("$y$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.4, 6.5)

t = texinsert("$O$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.5, -0.5)

t = texinsert("$(m,n)$")
t.translate(-t.width/2, 0)
t.scale(1)
place(t, 8+0.2, 6+0.2)

t = texinsert("$\lambda=(\lambda_1,\lambda_2,\ldots,\lambda_6)=(7, 7, 6, 6, 3, 1)$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 4, 7)


t = texinsert(r"$\{\lambda_i+n-i\ |\ 1\leq i\leq 6\}=\{12, 11, 9, 8, 4, 1\}$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 4, 6+0.5)


t = texinsert("$m=8$")
t.translate(-t.width/2, 0)
t.scale(1)
place(t, 4, -0.5)

t = texinsert("$n=6$")
t.translate(-t.width/2, -t.height/2)
t.scale(1)
place(t, -0.5, 3)

ts = 1
k = -0.3
setcolor(0.8, 0, 0)
t = texinsert("0")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 0.5, k)

t = texinsert("2")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 1.5, k+1)

t = texinsert("3")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 2.5, k+1)

t = texinsert("5")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 3.5, k+2)

t = texinsert("6")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 4.5, k+2)

t = texinsert("7")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 5.5, k+2)

t = texinsert("10")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 6.5, k+4)

t = texinsert("13")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 7.5, k+6)


setcolor(0, 0.8, 0)
j = 0.2
t = texinsert("1")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+1, 0.5)

t = texinsert("4")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+3, 1.5)

t = texinsert("8")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+6, 2.5)

t = texinsert("9")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+6, 3.5)

t = texinsert("11")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+7, 4.5)

t = texinsert("12")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+7, 5.5)

finish()
