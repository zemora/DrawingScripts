import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


TOP_COLOR = (1, 0, 0)
LEFT_COLOR = (0, 1, 1)
RIGHT_COLOR = (0.75, 0.5, 0.25)

LEFT = np.exp(1j * np.pi * 7 / 6)
TOP = np.exp(1j * np.pi / 2)
RIGHT = np.exp(np.pi * 11 / 6 * 1j)
