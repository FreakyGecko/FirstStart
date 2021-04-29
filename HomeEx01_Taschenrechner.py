fltZahl1 = float(input("Bitte geben Sie hier die erste Zahl ein: "))
strOperator = input("Bitte geben Sie hier den Operator ein: ")
fltZahl2 = float(input("Bitte geben Sie hier die zweite Zahl ein: "))

fltErgebnis = None

if strOperator == "+":
    fltErgebnis = fltZahl1 + fltZahl2
elif strOperator == "-":
    fltErgebnis = fltZahl1 - fltZahl2
elif strOperator == "*":
    fltErgebnis = fltZahl1 * fltZahl2
elif strOperator == "/":
    fltErgebnis = fltZahl1 / fltZahl2
else:
    fltErgebnis = "Konnte den Operator nicht identifizieren!"

print(fltErgebnis)
