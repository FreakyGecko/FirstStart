import random # importiert die Programm-Funktionen-Bibiothek "Random"; solange kein Befehl verwendet wird ist diese Zeile ausgegraut

secret = random.randint(1, 30)

while True: # Endlos-Schleife; nur durch "break" beenden
    guess = int(input("Rate eine Zahl: "))
    if guess == secret:
        print("You got it!")
        break  # Beenden der Schleife, wenn diese Zeile erreicht wird
        # exit = Beendet das gesamte Programm, wenn die Zeile erreicht wird
    elif guess > secret:
        print("Die gesuchte Zahl ist kleiner als", guess)
    else:
        print("Die gesuchte Zahl ist größer als", guess)

