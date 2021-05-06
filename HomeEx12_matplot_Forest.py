import matplotlib.pyplot as plt
import numpy as np

Trees = 20
# Generierung von zufälligen Zahlen in gaußscher Verteilung (Mitte, Abweichung, Anzahl Werte)
TreeHeights = np.random.normal(8, 3, Trees)
TreeWidths = np.random.normal(4, 1, Trees)

TreeColor = {'color': 'green', 'linewidth': 1}

TreeStandardXValues = ([1.0, 1.0, 1.5, 2.0, 2.0, 1.5, 0.5, 0.0, 0.0, 0.5, 1.0, 1.0])
TreeStandardYValues = ([0.0, 1.0, 1.0, 1.5, 3.0, 3.5, 3.5, 3.0, 1.5, 1.0, 1.0, 0.0])

TreeIndividualXValue = []
TreeIndividualYValue = []
n = 0
TreeDistance = 0

while n != Trees:
    for x in TreeStandardXValues:
        TreeIndividualXValue.append(x / max(TreeStandardXValues) * TreeWidths[n] + TreeDistance)

    TreeDistance = max(TreeIndividualXValue)

    for y in TreeStandardYValues:
        TreeIndividualYValue.append(y / max(TreeStandardYValues) * TreeHeights[n])

    n += 1
    plt.plot(TreeIndividualXValue, TreeIndividualYValue, **TreeColor)

plt.show()
