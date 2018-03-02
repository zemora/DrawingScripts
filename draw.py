# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# directions of the three axis.
X = np.exp(1j * np.pi * 7 / 6)
Y = np.exp(1j * np.pi * 11 / 6)
Z = np.exp(1j * np.pi / 2)

# colors of the faces.
TOP_COLOR = (1, 0, 0)
LEFT_COLOR = (0, 1, 1)
RIGHT_COLOR = (0.75, 0.5, 0.25)
PATH_COLOR = (1, 1, 0.2)

# three faces of the unit cube at (0, 0).
TOP = np.array([(0, 0), (np.sqrt(3) * 0.5, 0.5), (0, 1), (-np.sqrt(3) * 0.5, 0.5), (0, 0)])
LEFT = np.array([(0, 0), (-np.sqrt(3) * 0.5, 0.5), (-np.sqrt(3) * 0.5, -0.5), (0, -1), (0, 0)])
RIGHT = np.array([(0, 0), (np.sqrt(3) * 0.5, 0.5), (np.sqrt(3) * 0.5, -0.5), (0, -1), (0, 0)])

def topface(ax):
    face = plt.Polygon(TOP, fc=TOP_COLOR, ec='k', lw=1)
    return ax.add_patch(face)

def leftface(ax):
    face = plt.Polygon(LEFT, fc=LEFT_COLOR, ec='k', lw=1)
    return ax.add_patch(face)

def rightface(ax):
    face = plt.Polygon(RIGHT, fc=RIGHT_COLOR, ec='k', lw=1)
    return ax.add_patch(face)


def draw_tiling(T):
    """
    Draw the lozenge tiling `T` with matplotlib.
    """
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    a, b, c = T.size
    ax.axis([-b-0.5, a+0.5, -a-0.5, c+2])
    ax.axis("off")
    
    # floor
    for i in range(a):
        for j in range(b):
            floor = topface(ax)
            shift = i * Y + j * X
            floor.set_xy(TOP + (shift.real, shift.imag))
    
    # left wall
    for i in range(b):
        for j in range(c):
            left_wall = rightface(ax)
            shift = i * X + j * Z - Y + Z
            left_wall.set_xy(RIGHT + (shift.real, shift.imag))
    
    # right wall
    for i in range(a):
        for j in range(c):
            right_wall = leftface(ax)
            shift = i * Y + j * Z - X + Z 
            right_wall.set_xy(LEFT + (shift.real, shift.imag))

    # cubes
    pp = T.to_plane_partition()
    print(pp)
    for i, x in enumerate(pp):
        for j, val in enumerate(x):
            for k in range(val):
                shift = i * Z + j * X + k * Y + Z
                floor = topface(ax)
                floor.set_xy(TOP + (shift.real, shift.imag))
                left_wall = rightface(ax)
                left_wall.set_xy(RIGHT + (shift.real, shift.imag))
                right_wall = leftface(ax)
                right_wall.set_xy(LEFT + (shift.real, shift.imag))

    for i, path in enumerate(T.paths[-2:0:-1], start=1):
        gauss = [path[t+1] - path[t] for t in range(len(path) - 1)]
        z = (i + 0.5)*Z + a * Y
        newpath = [(z.real, z.imag)]
        xx, yy = zip(*newpath)
        ax.plot(xx, yy, 'o', color=PATH_COLOR, lw=1.5)
        for step in gauss:
            if step == 0:
                z -= Y
            else:
                z += X
            newpath.append((z.real, z.imag))
        xx, yy = zip(*newpath)
        ax.plot(xx, yy, '--', color=PATH_COLOR, lw=1.5)
        xxx, yyy = newpath[-1]
        ax.plot(xxx, yyy, 'o', color=PATH_COLOR, lw=1.5)

    fig.savefig("lozenge_tiling.png")
    return T


def path_system(T):
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    a, b, c = T.size
    ax.axis([-(c+2), a+1,  -1, b+c+2])
    ax.axis("off")

    colors = plt.cm.jet(np.linspace(0, 1, c+2))
    frames = 121

    dots = []
    for i in range(b+c+2):
        dots.extend(ax.plot([a, -(c+1)], [i, i], 'k:'))

    for i in range(-(c+1), a+1):
        dots.extend(ax.plot([i, i], [0, b+c+1], 'k:'))

    lines = []
    for i in range(c+2):
        lines.extend(ax.plot([], [], '-', lw=2, color=colors[i]))

    def init():
        ax.text(-0.5, -0.8, "$(0, 0)$")
        #ax.plot(0, 0, 'bo', markersize=5)
        ax.text(a+0.2, b, "$(a, b)$")
        #ax.plot(a, b, 'bo', markersize=5)
        for i in range(0, c + 2):
            ax.plot(-i, i, 'ko', markersize=5)
            ax.plot(a-i, b+i, 'ko', markersize=5)
            #ax.text(-0.5 + i, 0.2 + self.c + i, "$A_{0}$".format(i))
            #ax.text(self.b + i, -0.5 + i, "$B_{0}$".format(i))
        for l in lines:
            l.set_data([], [])
        return dots + lines

    def animate(t):
        t = t / (frames - 1.0)
        t *= 3
        for i, path in enumerate(T.paths):
            xs = []
            ys = []
            for ind, ht in enumerate(path):
                xs.append(ind-ht+i) 
                ys.append(ht-i) 
            xx = [z + max(0, t-2) * (- i)  for z in xs]
            yy = [z + max(0, t-2) * ( i)  for z in ys]
            lines[i].set_data(xx, yy)
            
        fig.canvas.draw()
        return lines

    anim = FuncAnimation(fig, animate, init_func=init, interval=20,
                         frames=frames, blit=True)
    anim.save('nonintersecting_paths.gif', writer='imagemagick', fps=60, dpi=100)
        

    fig.savefig("test.png")
