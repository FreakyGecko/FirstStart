# Beispiel: Eingabe Zahl zwischen 1 und 100, wenn die Ausgabe durch 3 teilbar ist, dann soll Wort "fizz", bei 5 "buzz"
# wenn beides zutrifft, dann "fizzbuzz"

end_zahl = int(input("Zahl zwischen 1 und 100: "))

for number in range(1, end_zahl + 1):
    if number % 3 == 0 and number % 5 == 0: # "%" = modulo = Restwert bei Division
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
