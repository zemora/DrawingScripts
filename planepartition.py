import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


TOP_COLOR = (1, 0, 0)
LEFT_COLOR = (0, 1, 1)
RIGHT_COLOR = (0.75, 0.5, 0.25)

X = np.exp(1j * np.pi * 7 / 6)
Z = np.exp(1j * np.pi / 2)
Y = np.exp(np.pi * 11 / 6 * 1j)

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
