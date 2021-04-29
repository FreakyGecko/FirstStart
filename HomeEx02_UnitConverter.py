boolEnde, strErgebnis = "y", ""
while boolEnde == "y":
    print("Willkommen beim Einheitenrechner!")
    fltBasis: float = float(input("Geben Sie hier die umzuwandelnde Zahl ein: "))
    strBasis = input("Geben Sie hier die Energieeinheit (Wh / kcal) dieser Zahl ein: ")
    strZiel = input("Geben Sie hier die gewünschte Einheit (Wh / kcal) an: ")
    if strBasis == "Wh":
        fltZiel = fltBasis * 3600
    elif strBasis == "kcal":
        fltZiel = fltBasis * 4184
    else:
        break
    if strZiel == "Wh":
        fltZiel = fltZiel / 3600
    elif strZiel == "kcal":
        fltZiel = fltZiel / 4184
    else:
        break
    strErgebnis = strErgebnis + str(fltBasis) + strBasis + " = " + str(fltZiel) + strZiel + " ! "
    boolEnde = input("Möchten Sie weitermachen (y/n): ")
print(strErgebnis)
