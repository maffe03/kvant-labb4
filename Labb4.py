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
    maxima = maxima[0]
    if len(maxima) > 0:
        maxima = maxima[0]
        plt.annotate("{:.2g}".format(y[maxima]*1000) + 'mA\n' + "{:.2g}".format(x[maxima]) + 'V', (x[maxima], y[maxima]*1.15), bbox=dict(facecolor='white', alpha=0.8))
        plt.plot(x[maxima], y[maxima], 'o', markerfacecolor='red', markeredgecolor='black', markersize=8, zorder=10)
        print(y[maxima])
    plt.plot(x, y, '-b+')
    plt.grid(color='gray', linestyle='-')
    plt.xlabel('$\mathrm{U}$ [V]')
    plt.ylabel('$\mathrm{I}$ [A]')
    #plt.show()
    plt.savefig('images/' + file + '.png')
    plt.cla()