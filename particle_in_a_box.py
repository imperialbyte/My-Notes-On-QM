# INFINITE POTENTIAL WELL

import matplotlib.pyplot as plt
import numpy as np

# Reduced Planck's Constant h bar
h = 1
# Mass
m = 1

# Boundary End
a = 1

# Potential Energy
V = 0

# Wave Function
psi = 0

dpsi = 1

x = 0
dx = a * 0.001

xlist = []
psilist = []

E = 16

while x <= a:
    ddpsi = 2 * m/h**2 * (V - E) * psi
    dpsi = dpsi + ddpsi * dx
    psi = psi + dpsi * dx
    x = x + dx
    xlist.append(x)
    psilist.append(psi)
    plt.plot(xlist, psilist)

plt.show()