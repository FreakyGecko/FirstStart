import matplotlib.pyplot as plt
import numpy as np

y1Werte = np.array([0, 15, 16, 20])
y2Werte = np.array([50, 100, 50, 100])

cdesign = {'color' : 'green', 'linewidth' : 1.25, 'linestyle' : '--'}
plt.plot(y1Werte, **cdesign)  # mit ** werden die Argumente aus einem Dictionary übergeben
plt.plot(y2Werte)

font1 = {'family': 'serif', 'color': 'blue', 'size': 16}
font2 = {'family': 'calibri', 'color': 'forestgreen', 'size': 12}

plt.title('Titel der Grafik', fontdict=font1)
plt.xlabel('Tag', fontdict=font2)
plt.ylabel('Wert', fontdict=font2)



plt.grid(axis='y', linewidth=0.5, color='red', linestyle='--')

plt.show()
