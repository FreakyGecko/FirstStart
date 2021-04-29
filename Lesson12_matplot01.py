# pip install matplotlib
# https://matplotlib.org/

import matplotlib.pyplot as plt
import numpy as np
# plt & np ist eine Verküzung des Bibliothek-Namens zur schnelleren Schreibweise

xWerte = np.array([0, 15, 16, 20])
yWerte = np.array([50, 100, 50, 100])

# Plot legt einen x-y-Kombination als Linie an.
plt.plot(xWerte, yWerte)  # wenn auf einer "Achse" keine Werte angegeben werden, dann legt er automatisch 0, 1, 2 ... an
plt.plot(xWerte, yWerte, 'o:g')  # Kurzschreibweise: 'o' bedeutet, dass nur die Punkte geplottet werden, 'g' in grün.
# Beispiele Formatkombinationen: '*-y' gelbe Linie, 'o:m' Punkte:Magenta, 'o-.g' Strichpunktlinie mit Endpunkten in grün
plt.plot(xWerte, yWerte, 'D', ms=20, mec='forestgreen', mfc='#4CAF50')  # Langschreibweise, geht auch mit Hexadezimal
# Farben für Plot: https://matplotlib.org/stable/gallery/color/named_colors.html

plt.show()

