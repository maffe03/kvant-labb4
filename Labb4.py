import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
files = ['A', 'B', 'C', 'D']
def find_max(x, y):
    return y[x + 1] < y[x]
for file in files:
    input = np.loadtxt(file + '.txt', delimiter='	', skiprows=1)
    #print(input)
    sorted_array = sorted(input, key=lambda x: x[0])
    x = [pair[0] for pair in sorted_array]
    y = [pair[1] for pair in sorted_array]
    maxima = list(sp.signal.argrelmax(np.array(y)))
    for maxima in maxima[0]:
        plt.annotate(str(y[maxima]), (x[maxima], y[maxima]*1.05))
        plt.plot(x[maxima], y[maxima], 'o', markerfacecolor='red', markeredgecolor='red', markersize=8, zorder=10)
        print(y[maxima])
    plt.plot(x, y, '-b+')
    plt.grid(color='gray', linestyle='-')
    plt.xlabel('$\mathrm{U}$ [V]')
    plt.ylabel('$\mathrm{I}$ [A]')
    #plt.show()
    plt.savefig('images/' + file + '.png')
    plt.cla()