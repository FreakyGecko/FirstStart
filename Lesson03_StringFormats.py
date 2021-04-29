str_one = "Hallo"
str_two = "Echo"

print(str_one + " " + str_two)
print("{0} {1}".format(str_one, str_two))
print("{0} {1}, Hallo Otto".format(str_one, str_two)) # nummerierte Elemente aus format ausgeben
print("%s %s" % (str_one, str_two)) # %s ist ein String-Ausgabe die einfach über die Anzahl der Elemente läuft, erkennt Zahlen als fehler
# %d wäre für Dezimalzahlen
print(f"{str_one} {str_two}")
# https://realpython.com/python-string-formatting/ String-Format-Anwendungsbeispiele

print(str_one.lower()) # Stellt alle Letter eines Strings auf LowCase um.

# https://www.python.org/dev/peps/pep-0008/ Empfehlungen in Python

