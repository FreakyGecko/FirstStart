secret = 13

for Versuche in range(3):
    guess = int(input("Noch " + str(3 - Versuche) + " Versuche! Rate eine Zahl: "))
    if guess == secret:
        print("You got it!")
        break # Beenden der Schleife, wenn diese Zeile erreicht wird
        # exit = Beendet das gesamte Programm, wenn die Zeile erreicht wird
    else:
        print("Die Zahl " + str(guess) + " war falsch")
        if Versuche == 2:
            print("Vielleicht beim nächsten mal")
