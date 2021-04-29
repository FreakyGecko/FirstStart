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
