import numpy as np
import matplotlib.pyplot as plt
files = ['A', 'B', 'C', 'D']
for file in files:
    input = np.loadtxt(file + '.txt', delimiter='	', skiprows=1)
    print(input)
    sorted_array = sorted(input, key=lambda x: x[0])
    x = [pair[0] for pair in sorted_array]
    y = [pair[1] for pair in sorted_array]
    plt.plot(x, y, '-o')
    plt.grid(color='gray', linestyle='-')
    plt.xlabel('$\mathrm{U}$ [V]')
    plt.ylabel('$\mathrm{I}$ [A]')
    plt.show()
    plt.savefig('images/' + file + '.png')
    plt.cla()