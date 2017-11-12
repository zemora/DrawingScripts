import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


TOP_COLOR = (1, 0, 0)
LEFT_COLOR = (0, 1, 1)
RIGHT_COLOR = (0.75, 0.5, 0.25)

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
                 (-0.5, -np.sqrt(3) * 0.5),
                 (0, -1),
                 (0, 0)])

RIGHT = np.array([(0, 0),
                 (np.sqrt(3) * 0.5, 0.5),
                 (np.sqrt(3) * 0.5, -0.5),
                 (0, -1),
                 (0, 0)])


TOPFACE = plt.Polygon(TOP, fc=TOP_COLOR, ec='k', lw=1)
LEFTFACE = plt.Polygon(LEFT, fc=LEFT_COLOR, ec='k', lw=1)
TOPFACE = plt.Polygon(RIGHT, fc=RIGHT_COLOR, ec='k', lw=1)


class PlanePartition(object):

    def __init__(self, array, a, b, c):
        self.heightmap = np.zeros((a, b), dtype=np.int)
        for i, row in enumerate(array):
            self.heightmap[i][0: len(row)] = row
            
        self.colors = plt.cm.jet(np.linspace(0, 1, a))
        self.paths = [self.gauss_path(row) for row in self.heightmap]
        self.a = a
        self.b = b
        self.c = c
  
        
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
        
        # draw the paths and put texts over them.
        for path, color, arr in zip(self.paths, self.colors, self.heightmap):
            xs, ys = zip(*path)
            ax.plot(xs, ys, lw=2, color=color)
            
            for i, x in enumerate(arr):
                if x > 0:
                    ax.text(i+0.4, x+0.1, str(x))
        
        ax.text(-0.8, self.c + 0.2, "(0, c)")
        ax.text(self.b - 0.5, -0.5, "(b, 0)")
        fig.savefig("gauss_path.png")
        
        
