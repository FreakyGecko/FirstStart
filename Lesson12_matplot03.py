import matplotlib.pyplot as plt
import numpy as np

xWerte = np.array([0, 15, 16, 20])
yWerte = np.array([12, 27, 50, 10])

plt.subplot(2, 2, 1)  # Erstellt im Plot einen Raster (Zeilen, Spalen, Zeile, Spalte)
plt.plot(xWerte, yWerte)
plt.xlabel('Tag')
plt.ylabel('Wert')

xWerte = np.array([0, 2, 3, 6])
yWerte = np.array([12, 27, 50, 10])

plt.subplot(2, 2, 2)
plt.plot(xWerte, yWerte, 'o')
plt.xlabel('Tag')
plt.ylabel('Wert')

xWerte = np.array(["A", "B", "C", "D"])
yWerte = np.array([12, 27, 50, 10])

plt.subplot(2, 2, 3)
plt.barh(xWerte, yWerte, height=0.9, color='#4ACF50')  # bar ist vertikal, barh ist horizontal
plt.xlabel('Tag')
plt.ylabel('Wert')

yWerte = np.array([12, 27, 50, 10])
labels = ["A", "B", "C", "D"]
special = [0.3, 0, 0, 0]
customer_color = ["c","black", "#4ACF50", "lime"]

plt.subplot(2, 2, 4)
plt.pie(yWerte, labels=labels, explode=special, shadow=True, colors=customer_color)  # Tortendiagramm


plt.show()
