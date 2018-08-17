import matplotlib.pyplot as plt

def coxeter_dynkin(diagram, active):
    nodes = len(diagram) + 1
    intervals = len(diagram)
    fig = plt.figure(figsize=(intervals + 0.4, 0.6), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([0.8, nodes + 0.2, -0.2, 0.4])
    ax.plot([1, nodes], [0, 0], "k-")
    ax.plot(list(range(1, nodes+1)), [0]*nodes, "ko", markersize=6)
    for i, x in enumerate(active, start=1):
        if x:
            ax.plot([i], [0], "ko", markersize=12, markerfacecolor='none')
    for i, x in enumerate(diagram):
        if x > 3:
            ax.text(i + 1.4, 0.1, str(x), fontsize=16)
    fig.savefig("".join(str(x) for x in diagram) + ".png")

coxeter_dynkin((5, 3, 3), (0, 1, 0,1))
