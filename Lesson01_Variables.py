print("Hallo Welt")

# Datentyp Integer
x = 100
x = x + 1
print(x, end="MW")

# Datentyp String
string_Grußwort = "Hallo"
string_Name = "Christoph"
print(string_Name + " " + string_Grußwort, ".")

# Datentyp Dezimalzahl (float)
float_Dezimalzahl1 = 19.75
float_Dezimalzahl2 = 1.25
print("Ergebnis = ",float_Dezimalzahl1 / float_Dezimalzahl2)

# Datentyp Boolean
bool_01 = True
bool_02 = False

# Datentyp nicht bestimmt
Nichts = None

# Interaktion Eingabe vom Ausführenden
UserName = input("Bitte hier den Namen eingeben: ")
UInput_Zahl1 = float(input("Nenner eingeben: ")) # Der Befehl input gibt immer zuerst einen String aus, daher muss die Eingabe in einen anderen Datentyp umgewandelt werden
UInput_Zahl2 = float(input("Teiler eingeben: "))
DecErg01 = UInput_Zahl1 / UInput_Zahl2
print("Hallo",UserName, "Dein Ergebnis ist ", DecErg01)

# If-Operationen
Tag = "Wednesday"
if Tag  == "Monday":
    print("Montag")
elif Tag == "Tuesday": # Die Elseif müssen auf der selben Ebene sein, wie das If
    print("Dienstag")
elif Tag == "Wednesday":
    print("Mittwoch")
else:
    print("Wochenende")

# Beispiel var_a, var_b = 1, 5.0
