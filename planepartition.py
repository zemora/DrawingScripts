import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from palettable.colorbrewer.qualitative import Set1_7 as Set


#colors = Set.mpl_colors[2: 6]
TOP_COLOR, LEFT_COLOR, RIGHT_COLOR, PATH_COLOR = [(1, 0, 0),
                                                  (0, 1, 1),
                                                  (0.75, 0.5, 0.25),
                                                  (1, 1, 0.2)]

X = np.exp(1j * np.pi * 7 / 6)
Y = np.exp(1j * np.pi * 11 / 6)
Z = np.exp(1j * np.pi / 2)


TOP = np.array([(0, 0),
                (np.sqrt(3) * 0.5, 0.5),
                (0, 1),
                (-np.sqrt(3) * 0.5, 0.5),
                (0, 0)])

LEFT = np.array([(0, 0),
                 (-np.sqrt(3) * 0.5, 0.5),
                 (-np.sqrt(3) * 0.5, -0.5),
                 (0, -1),
                 (0, 0)])

RIGHT = np.array([(0, 0),
                 (np.sqrt(3) * 0.5, 0.5),
                 (np.sqrt(3) * 0.5, -0.5),
                 (0, -1),
                 (0, 0)])


def topface(ax):
    TOPFACE = plt.Polygon(TOP, fc=TOP_COLOR, ec='k', lw=1)
    return ax.add_patch(TOPFACE)

def leftface(ax):
    LEFTFACE = plt.Polygon(LEFT, fc=LEFT_COLOR, ec='k', lw=1)
    return ax.add_patch(LEFTFACE)

def rightface(ax):
    RIGHTFACE = plt.Polygon(RIGHT, fc=RIGHT_COLOR, ec='k', lw=1)
    return ax.add_patch(RIGHTFACE)


class PlanePartition(object):

    def __init__(self, array, a, b, c):
        self.a = a
        self.b = b
        self.c = c
  
        self.heightmap = np.zeros((a, b), dtype=np.int)
        for i, row in enumerate(array):
            self.heightmap[i][0: len(row)] = row
            
        self.colors = plt.cm.jet(np.linspace(0, 1, a))
        self.paths = [self.gauss_path(row) for row in self.heightmap]

        
    def gauss_path(self, path):
        result = [(0, self.c)]
        for i, val in enumerate(path):
            result += [(i, val), (i+1, val)]
        result.append((self.b, 0))
        return result
        
        
    def draw_paths(self):
        fig = plt.figure(figsize=(4, 4), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-1, self.b + 1, -1, self.c + 1])
        ax.axis("off")
        
        # draw the grid with dotted lines
        for i in range(self.c + 1):
            ax.plot([0, self.b], [i, i], 'k:')
        for i in range(self.b + 1):
            ax.plot([i, i], [0, self.b], 'k:')
        
        # draw the paths
        for path, color, arr in zip(self.paths, self.colors, self.heightmap):
            xs, ys = zip(*path)
            ax.plot(xs, ys, lw=2, color=color)
            # add labels
            for i, x in enumerate(arr):
                if x > 0:
                    ax.text(i + 0.4, x + 0.1, str(x))
        
        ax.text(-0.8, self.c + 0.2, "$(0, c)$", fontsize=16)
        ax.text(self.b - 0.5, -0.5, "$(b, 0)$", fontsize=16)
        fig.savefig("gauss_path.png")
        
    
    def nonintersect_path_system(self):
        fig = plt.figure(figsize=(6, 6), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-1, self.b + self.a + 1, -1, self.c + self.a + 1])
        ax.axis("off")
        
        frames = 121
        
        # dotted lines
        dots = []
        for i in range(self.c + self.a + 1):
            dots.extend(ax.plot([0, self.b + self.a], [i, i], 'k:'))

        for i in range(self.b + self.a + 1):
            dots.extend(ax.plot([i, i], [0, self.b + self.a], 'k:'))
        
        # the paths
        lines = []
        for i in range(self.a):
            lines.extend(ax.plot([], [], '-', lw=2, color=self.colors[i]))

        # the two trajectories
        trajects = []
        trajects.extend(ax.plot([0, self.a], [self.c, self.a + self.c], 'k--', lw=1))
        trajects.extend(ax.plot([self.b, self.b + self.a], [0, self.a], 'k--', lw=1))
        
        def init():
            ax.text(-0.8, self.c + 0.2, "$(0, c)$")
            ax.text(self.b - 0.5, -0.5, "$(b, 0)$")
            for i in range(1, self.a + 1):
                ax.plot(i, self.c + i, 'ko', markersize=5)
                ax.plot(self.b + i, i, 'ko', markersize=5)
                ax.text(-0.5 + i, 0.2 + self.c + i, "$A_{0}$".format(i))
                ax.text(self.b + i, -0.5 + i, "$B_{0}$".format(i))
            for l in lines:
                l.set_data([], [])
            return dots + lines + trajects
        
        def animate(t):
            t = t / (frames - 1.0)
            t *= 3
            for i, path in enumerate(self.paths):
                xs, ys = zip(*path)
                xx = [z + max(0, t-2) * (self.a - i) for z in xs]
                yy = [z + max(0, t-2) * (self.a - i) for z in ys]
                lines[i].set_data(xx, yy)
            
            fig.canvas.draw()
            return lines

        anim = FuncAnimation(fig, animate, init_func=init, interval=20,
                             frames=frames, blit=True)
        anim.save('nonintersecting_paths.gif', writer='imagemagick', fps=60, dpi=100)
        
        
    def draw_planepartition(self, show_path=False):
        fig = plt.figure(figsize=(4, 4), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-self.a + 0.5, self.b - 0.5, -self.b, self.c + 1.5])
        ax.axis("off")
        
        for i in range(self.a):
            for j in range(self.b):
                floor = topface(ax)
                shift = i * X + j * Y
                floor.set_xy(TOP + (shift.real, shift.imag))
        for i in range(self.a):
            for j in range(self.c):
                left_wall = rightface(ax)
                shift = i * X + j * Z - Y + Z
                left_wall.set_xy(RIGHT + (shift.real, shift.imag))
                
        for i in range(self.b):
            for j in range(self.c):
                right_wall = leftface(ax)
                shift = i * Y + j * Z - X + Z
                right_wall.set_xy(LEFT + (shift.real, shift.imag))
             
        # cubes
        for i, x in enumerate(self.heightmap):
            for j, val in enumerate(x):
                if val > 0:
                    for k in range(1, val + 1):
                        shift = i * X + j * Y + k * Z
                        floor = topface(ax)
                        floor.set_xy(TOP + (shift.real, shift.imag))
                        left_wall = rightface(ax)
                        left_wall.set_xy(RIGHT + (shift.real, shift.imag))
                        right_wall = leftface(ax)
                        right_wall.set_xy(LEFT + (shift.real, shift.imag))

        if show_path:
            for i, path in enumerate(self.paths):
                newpath = []
                for x, y in path:
                    z = x * Y + y * Z + X * (i + 0.5) + Z
                    newpath.append((z.real, z.imag))
                xx, yy = zip(*newpath)
                ax.plot(xx, yy, '--', color=PATH_COLOR, lw=1.5)
           
        fig.savefig("planepartition.png")


    def draw_hexagon(self):
        M = max(self.a, self.b, self.c)
        fig = plt.figure(figsize=(4, 4), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-self.a, self.b+0.6, -self.b - 1, self.c + 0.5])
        ax.axis("off")
        verts_complex = [self.c * Z,
                         self.c * Z + self.a * X,
                         self.a * X,
                         self.a * X + self.b * Y,
                         self.b * Y,
                         self.b * Y + self.c * Z,
                         self.c * Z]
        verts = [(z.real, z.imag) for z in verts_complex]
        xx, yy = zip(*verts)
        ax.plot(xx, yy, 'k-', lw=1)

        lines = []
        for i in range(-M, M):
            start = i * Z + M * X
            end = i * Z  - M * X
            lines.extend(ax.plot([start.real, end.real], [start.imag, end.imag], '--', color=(0.5, 0.5, 0.5), lw=.5))

        for i in range(-M, M):
            start = M * Z + i * X
            end = -M * Z  + i * X
            lines.extend(ax.plot([start.real, end.real], [start.imag, end.imag], '--', color=(0.5, 0.5, 0.5), lw=.5))

        for i in range(-M, M):
            start = i * Z + M * Y
            end = i * Z  - M * Y
            lines.extend(ax.plot([start.real, end.real], [start.imag, end.imag], '--', color=(0.5, 0.5, 0.5), lw=.5))

        from matplotlib.path import Path
        from matplotlib.patches import PathPatch
        codes = [Path.MOVETO] + 5 * [Path.LINETO] + [Path.CLOSEPOLY]
        path = Path(verts, codes)
        patch = PathPatch(path, facecolor='none', ec='k')
        ax.add_patch(patch)
        for l in lines:
            l.set_clip_path(patch)

        size = 18
        za = self.c * Z + self.a * X / 2
        ax.text(za.real-0.5, za.imag+0.3, "$a$", fontsize=size)

        zb = self.c * Z + self.b * Y / 2
        ax.text(zb.real+0.2, zb.imag+0.2, "$b$", fontsize=size)

        zc = self.c * Z / 2 + self.b * Y
        ax.text(zc.real+0.3, zc.imag, "$c$", fontsize=size)

        
        fig.savefig("hexagon.png")


    def gessel_viennot(self):
        fig = plt.figure(figsize=(6, 6), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-1, self.b + self.a + 1, -1, self.c + self.a + 1])
        ax.axis("off")
        
        # dotted lines
        dots = []
        for i in range(self.c + self.a + 1):
            dots.extend(ax.plot([0, self.b + self.a], [i, i], 'k:'))

        for i in range(self.b + self.a + 1):
            dots.extend(ax.plot([i, i], [0, self.b + self.a], 'k:'))
        
        # the paths
        lines = []
        for i in range(self.a):
            lines.extend(ax.plot([], [], '-', lw=2, color=self.colors[i]))

        # the two trajectories
        trajects = []
        trajects.extend(ax.plot([0, self.a], [self.c, self.a + self.c], 'k--', lw=1))
        trajects.extend(ax.plot([self.b, self.b + self.a], [0, self.a], 'k--', lw=1))
        
        ax.text(-0.8, self.c + 0.2, "$(0, c)$")
        ax.text(self.b - 0.5, -0.5, "$(b, 0)$")
        for i in range(1, self.a + 1):
            ax.plot(i, self.c + i, 'ko', markersize=5)
            ax.plot(self.b + i, i, 'ko', markersize=5)
            ax.text(-0.5 + i, 0.2 + self.c + i, "$A_{0}$".format(i))
            ax.text(self.b + i, -0.5 + i, "$B_{0}$".format(i))
            
        for i, path in enumerate(self.paths):
            xs, ys = zip(*path)
            xx = [z +  (self.a - i) for z in xs]
            yy = [z +  (self.a - i) for z in ys]
            lines[i].set_data(xx, yy)

        ax.plot(9, 8, 'ro', markersize=10)
        ax.plot(9, 8, 'ko', markersize=4)
        ax.plot(8, 9, 'ro', markersize=6)
        ax.plot(9, 5, 'ro', markersize=6)
        ax.plot(8, 5, 'ro', markersize=6)
        ax.plot(7, 6, 'ro', markersize=6)
        ax.plot(3, 5, 'ro', markersize=6)
        ax.plot(3, 7, 'ro', markersize=6)
        ax.text(9.2, 8.2, "$C$", fontsize=15)
        fig.savefig("gessel_viennot.png")
        
        
pp = PlanePartition([[5, 4, 2, 2, 1],
                     [4, 4, 4, 4],
                     [4, 4, 3, 1, 1],
                     [4, 4, 3, 3, 3],
                     [5, 3, 3, 3],
                     [5, 4, 3, 2]],
                     6, 5, 5)

#pp.draw_paths()
#pp.nonintersect_path_system()
#pp.draw_planepartition(show_path=False)
#pp.draw_hexagon()
pp.gessel_viennot()
