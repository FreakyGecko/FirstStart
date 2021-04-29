import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(100, 15, 200)  # Generierung von zufälligen Zahlen in einer gaußschen Verteilung (Mittelwert, Bereich, Anzahl Werte)

print(x)
print(x)

plt.hist(x)
plt.show()
