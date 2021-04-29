import random # importiert die Programm-Funktionen-Bibiothek "Random"; solange kein Befehl verwendet wird ist diese Zeile ausgegraut
import json # Importiert Elemente aus der json-Bibliothek
import datetime

currentTime = datetime.datetime.now()
print(currentTime)

secret = random.randint(1, 30)
intAttempts = 0

with open("Lesson05_GameScoreDict.txt", "r") as fileScore:
    listScore = json.loads(fileScore.read())
    print("Top scores" + str(listScore[:3])) # :3 gibt vom 0ten bis exkl. 3ten Element aus. "3:" gibt die letzten drei Elemente aus

    for listDict in listScore:
        print(str(listDict["attempts"]) + " Versuche, am" + str(listDict["timestamp"]))

while True: # Endlos-Schleife; nur durch "break" beenden
    guess = int(input("Rate eine Zahl: "))
    intAttempts += 1 # Kurze Schreibweise von x = x + 1

    if guess == secret:
        print("You got it!")
        print("Verbrauchte Versuche:" + str(intAttempts))
        listScore.append({"attempts": intAttempts, "timestamp": str(datetime.datetime.now())}) # Zusammenstellung eines Datensatzes mit Zahl und Datum

        with open("Lesson05_GameScoreDict.txt", "w") as fileScore:
            fileScore.write(json.dumps(listScore)) # Hier wird die neue Liste erzeugt
        break  # Beenden der Schleife, wenn diese Zeile erreicht wird

    elif guess > secret:
        print("Die gesuchte Zahl ist kleiner als", guess)

    else:
        print("Die gesuchte Zahl ist größer als", guess)
