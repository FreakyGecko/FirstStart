# Loops

secret = 29

# #Übungsbeispiel für Schleife
# guess = int(input("Rate eine Zahl zwischen 1 und 30: "))
# if guess == secret:
#     print("Hurra, diesmal keine Niete")
# else:
#     print("Try again, not " + str(guess))

# while: Schleife solange etwas erfüllt ist
secret = 14
guess = 0 # Variablendefinition wird gebraucht, weil er in der Schleifendefinition noch keine Variable hat
while guess != secret: # != bedeutet <>
    guess = int(input("Rate eine Zahl zwischen 1 und 30: "))
    if guess == secret:
        print("Hurra, diesmal keine Niete")
    else:
        print("Try again, not " + str(guess))



