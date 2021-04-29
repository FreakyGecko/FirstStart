a = 22
b = "Warum"
c = [1, 4, 6]

a = 0
b = a
b += 20
print(a, b)
print(id(a), id(b))
# Einfache Datentypen (bol, int, str) werden über den Value ausgegeben (und im Ram abgespeichert)

a = [1, 2, 4]
b = a
b += [55]
print(a, b)
print(id(a), id(b))
# Erweiterte Datentypen (array, dict, etc.) werden als Referenzen (zum Speicherplatz) übergeben.


a = [2, 12, 5]
b = a
b = [2, 12, 5]
b[0] = 42
print(a, b)


# kopieren:
def make_value_42(x):
    x[0] = 42


a = [1, 2, 3]
make_value_42(a)
print(a)

a = [1, 2, 3]
b = list(a)  # Im Gegenteil zu "b = a" werden die Werte und nicht die Referenz weitergegeben.
b[0] = 42
print(a, b)

# ACHTUNG ! Bei verschachtelten Listen funktioniert "list" nur in der obersten Ebene
a = [22, 33, [44]]
b = list(a)
b[2] += [55]
print(a, b)

from copy import deepcopy  # Diese Funktion kopiert alle Unterebenen auf neue Speicherplätze

a = [12, 23, [34]]
b = deepcopy(a)
b[2] += [45]
print(a, b)


class Ding(object):
    Test = []


a = Ding()
b = Ding()
b.Test.append(15)
print(a.Test, b.Test)

# Richtige Lösung für Objekte: Self bedeutet neuer Speicherplatz für ein neues Objekt
class Ding2(object):
    def __init__(self):
        self.test = []


a = Ding2()
b = Ding2()
b.test.append(15)
print(a.test, b.test)
