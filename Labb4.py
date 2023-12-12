import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import fy
files = ['A', 'B', 'C', 'D']
def find_max(x, y):
    return y[x + 1] < y[x]

# U: V
def find_width_double_barrier(U):
    a = 2 * 0.067 * fy.m_e / (fy.h_**2)
    V_0 = fy.Joule(0.2)
    E = -(V_0 - 0.15 * fy.Joule(U))
    eq1 = math.sqrt(-E/(E+V_0))
    ateq1 = math.atan(eq1)
    eq2 = math.sqrt(a*(E+V_0))
    half_barrier = ateq1/eq2
    barrier = half_barrier * 2
    return barrier

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
        print(str(find_width_double_barrier(x[maxima])))
    plt.plot(x, y, '-b+')
    plt.grid(color='gray', linestyle='-')
    plt.xlabel('$\mathrm{U}$ [V]')
    plt.ylabel('$\mathrm{I}$ [A]')
    #plt.show()
    plt.savefig('images/' + file + '.png')
    plt.cla()