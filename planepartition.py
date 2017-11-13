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
        
        ax.text(-0.8, self.c + 0.2, "(0, c)")
        ax.text(self.b - 0.5, -0.5, "(b, 0)")
        fig.savefig("gauss_path.png")
        
    
    def nonintersect_path_system(self):
        fig = plt.figure(figsize=(6, 6), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-1, self.b + self.a + 1, -1, self.c + self.a + 1])
        ax.axis("off")
        
        frames = 61
        
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
            ax.text(-0.8, self.c + 0.2, "(0, c)")
            ax.text(self.b - 0.5, -0.5, "(b, 0)")
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
            for i, path in enumerate(self.paths):
                xs, ys = zip(*path)
                xx = [z + t * (self.a - i) for z in xs]
                yy = [z + t * (self.a - i) for z in ys]
                lines[i].set_data(xx, yy)
            
            fig.canvas.draw()
            return lines

        anim = FuncAnimation(fig, animate, init_func=init, interval=20,
                             frames=frames, blit=True)
        anim.save('nonintersecting_paths.gif', writer='imagemagick', fps=60, dpi=100)
        
        
    def draw_planepartition(self, show_path=False):
        fig = plt.figure(figsize=(4, 4), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([-self.a, self.b, -self.b - 1, self.c + 2])
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
           
        fig.savefig("planepartion.png")
        
        
pp = PlanePartition([[6, 5, 4, 3, 2],
                     [5, 4, 3, 3],
                     [3, 2, 1],
                     [2, 1],
                     [1]],
                    6, 6, 6)

#pp.draw_paths()
#pp.nonintersect_path_system()
pp.draw_planepartition(show_path=False)
