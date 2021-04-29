# pip install matplotlib
# https://matplotlib.org/

import matplotlib.pyplot as plt
import numpy as np
# plt & np ist eine Verküzung des Bibliothek-Namens zur schnelleren Schreibweise

xWerte = np.array([0, 15])
yWerte = np.array([50, 100])

plt.plot(xWerte, yWerte)
plt.show()

