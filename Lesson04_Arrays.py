# Einfache Datentypen int, String, Float, ...
intBeispiel = 5

# arrays / Listen:
intListBeispiel = [3, 77, 43, 12, 3, 8] # Liste mit Ganzzahlen
print(intListBeispiel[3])

strListBeispiel = ["Badminton", "Bergsteigen", "Fitness", "Tennis"]
print(strListBeispiel)

# Gemischte Liste mit unterschiedlichen Datentypen
varListBeispiel = [55, "Identifikator", True, "Ja, Natürlich", 3.14159]

intListBeispiel.sort() # Listen gleichen Datentyps werden aufsteigend sortiert
print(intListBeispiel)

# varListBeispiel.sort() # eine gemischte Liste kann nicht sortiert werden

for item in varListBeispiel:
    print(item)

