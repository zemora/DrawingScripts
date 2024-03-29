"""
This script draws illustrating figures for the CFTP algorithm.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch


def dir(deg):
    """
    Convert an angle in degrees to a unit complex number.
    """
    theta = np.radians(deg)
    return np.cos(theta) + np.sin(theta) * 1j


def plotline(ax, z1, z2, *args, **kwargs):
    """
    Plot a line between two complex numbers.
    """
    return ax.plot((z1.real, z2.real), (z1.imag, z2.imag), *args, **kwargs)


def draw_bounding_hexagon(ax, vertices):
    """
    Draw the bounding hexagon (in black) on a matplotlib `ax` instance and
    return the path patch.
    """
    coords = [(z.real, z.imag) for z in vertices]
    xlist, ylist = zip(*coords)
    ax.plot(xlist, ylist, "k-", lw=1)
    codes = [Path.MOVETO] + 5 * [Path.LINETO] + [Path.CLOSEPOLY]
    patch = PathPatch(Path(coords, codes), facecolor="none", ec="k")
    ax.add_patch(patch)
    return patch


def draw_background_triangle_lattice(ax, ULR, n):
    """
    Draw the background triangle lattice in a hexagon (dashed gray lines).
    """
    U, L, R = ULR
    lines = []
    for i in range(-n, n):
        # three families of grid lines
        for P, Q in [[U, L], [U, R], [L, U]]:
            v1 = i * P + n * Q
            v2 = i * P - n * Q
            lines.extend(
                plotline(ax, v1, v2, '--', color=(0.5, 0.5, 0.5), lw=1)
            )
    return lines


def draw_background_square_lattice(ax, ULR, n):
    """
    Draw the background triangle lattice in a hexagon (dashed gray lines).
    """
    U, L, R = ULR
    k = np.sqrt(2)
    lines = []
    for i in range(-n, n):
        # two families of grid lines
        for P, Q in [[U, L], [U, R]]:
            v1 = i * P * k + n * Q
            v2 = i * P * k - n * Q
            lines.extend(
                plotline(ax, v1, v2, '--', color=(0.5, 0.5, 0.5), lw=1)
            )
    return lines


def draw_triangle_paths_on_hexagon(ax, size, ULR, paths):
    """
    Draw a set of nonintersecting paths on a matplotlib `ax` instance (bold red).
    """
    a, b, c = size
    U, L, R = ULR
    for i, path in enumerate(paths[1:-1]):
        v1 = b * L + (i + 0.5) * U
        for ht1, ht2 in zip(path[:-1], path[1:]):
            if ht1 < ht2:  # move right-up
                v2 = v1 - L
            else:  # move right-down
                v2 = v1 + R
            plotline(ax, v1, v2, 'r-', lw=2)
            v1 = v2


def draw_square_paths_on_hexagon(ax, size, ULR, paths):
    """
    Draw a set of nonintersecting paths on a matplotlib `ax` instance (bold red).
    """
    a, b, c = size
    U, L, R = ULR
    k = np.sqrt(2)
    for i, path in enumerate(paths[1:-1]):
        v1 = b * L + i * U * k
        for ht1, ht2 in zip(path[:-1], path[1:]):
            if ht1 < ht2:  # move right-up
                v2 = v1 - L
            else:  # move right-down
                v2 = v1 + R
            plotline(ax, v1, v2, 'r-', lw=2)
            v1 = v2


def draw_hexagon_on_triangle_lattice(size, paths=None):
    """
    Set up the figure and combine all the stuff.
    :param size: side lengths of the hexagon, a tuple of three integers.
    :param paths: a set of nonintersecting paths.
    """
    U = dir(90)
    L = dir(210)
    R = dir(-30)

    a, b, c = size
    k = np.sqrt(3) / 2
    A = c * U
    B = b * L
    C = a * R

    fig = plt.figure(figsize=(6, 6), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis([-b * k - 1, a * k + 1, -(a + b) / 2 - 1, c + 1])
    ax.axis("off")

    verts = [A, A + B, B, B + C, C, A + C, A]
    n = 2 * (a + b + c)
    patch = draw_bounding_hexagon(ax, verts)
    lines = draw_background_triangle_lattice(ax, (U, L, R), n)
    for line in lines:
        line.set_clip_path(patch)

    if paths:
        draw_triangle_paths_on_hexagon(ax, size, (U, L, R), paths)

    # add text annotations
    size = 18
    z = A + C / 2
    ax.text(z.real + 0.2, z.imag + 0.2, "$a$", fontsize=size)
    z = A + B / 2
    ax.text(z.real - 0.6, z.imag + 0.2, "$b$", fontsize=size)
    z = A / 2 + B
    ax.text(z.real - 0.8, z.imag, "$c$", fontsize=size)
    fig.savefig("hexagon.png")


def draw_hexagon_on_square_lattice(size, paths=None):
    """
    Set up the figure and combine all the stuff.
    :param size: side lengths of the hexagon, a tuple of three integers.
    :param paths: a set of nonintersecting paths.
    """
    U = dir(90)
    L = dir(225)
    R = dir(-45)

    a, b, c = size
    k = np.sqrt(2)
    A = (c - 1) * U * k
    B = b * L
    C = a * R

    fig = plt.figure(figsize=(6, 6), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis([-b / k - 1, a / k + 1, -(a + b) / k - 1, (c - 1) * k + 1])
    ax.axis("off")

    verts = [A, A + B, B, B + C, C, A + C, A]
    n = 2 * (a + b + c)
    patch = draw_bounding_hexagon(ax, verts)
    lines = draw_background_square_lattice(ax, (U, L, R), n)
    for line in lines:
        line.set_clip_path(patch)

    if paths:
        draw_square_paths_on_hexagon(ax, size, (U, L, R), paths)

    fig.savefig("square.png")


size = (12, 10, 6)
draw_hexagon_on_triangle_lattice(size)
draw_hexagon_on_square_lattice(size)
