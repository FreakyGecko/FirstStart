# Bibliotheken- und Funktionen-Import
from HomeEx08_Functions import DecPrefix  # Funktion Erkennung und Umwandlung der Dezimalpräfixe in Multiplikatoren
from HomeEx08_Functions import RawUnit  # Funktion Entfernung des Dezimalpräfix
from HomeEx08_Functions import Convert2SIUnit  # Funktion Einheit in Multiplikator umwandeln
import tkinter
from tkinter import messagebox


def Switch():
    fltInput01 = float(Input01.get())
    strInput02 = str(Input02.get())
    strInput03 = str(Input03.get())

    # Identifikation der Präfix-Multiplikatoren
    fltDecPrefix = DecPrefix(strInput02), DecPrefix(strInput03)

    # Umwandlung in Einheiten ohne Präfixe
    strRohEinheit = RawUnit(strInput02, fltDecPrefix[0]), RawUnit(strInput03, fltDecPrefix[1])

    # Einheitenumwandlung in Faktoren
    bolUnitFactor = Convert2SIUnit(strRohEinheit[0])[0], Convert2SIUnit(strRohEinheit[1])[0]
    fltUnitFactor = Convert2SIUnit(strRohEinheit[0])[1], Convert2SIUnit(strRohEinheit[1])[1]

    if bolUnitFactor[0] is True or fltUnitFactor[1] is True:
        messagebox.showinfo(title="Einheit nicht gefunden", message="Die angegebene Einheit konnte nicht identifiziert werden! Bitte versuche es nochmal.")
    else:
        fltErgebnis = float(fltInput01) * fltDecPrefix[0] / fltDecPrefix[1] / fltUnitFactor[0] * fltUnitFactor[1]
        shwErgebnis.config(text=str(fltErgebnis))


wndMain = tkinter.Tk(className=" Einheiten-Umrechner")  # Erstellt Hauptfenster

# messagebox.showinfo("Willkommen beim Einheiten-Umrechner! (Version 0.3)")
# messagebox.showinfo("Zwischen den folgenden Einheiten kann umgerechnet werden: J | Wh | toe | cal | gSKE | BTU")
tkinter.Label(wndMain, text="Wert").grid(row=0, column=1)
tkinter.Label(wndMain, text="Einheit").grid(row=0, column=2)
tkinter.Label(wndMain, text="Eingabe").grid(row=1, column=0)
tkinter.Label(wndMain, text="Ergebnis").grid(row=2, column=0)
shwErgebnis = tkinter.Label(wndMain, text="")
shwErgebnis.grid(row=2, column=1)

# Eingabe durch BenutzerInnen
Input01 = tkinter.Entry(wndMain)
Input01.grid(row=1, column=1)
Input02 = tkinter.Entry(wndMain)
Input02.grid(row=1, column=2)
Input03 = tkinter.Entry(wndMain)
Input03.grid(row=2, column=2)

Schalter = tkinter.Button(wndMain, text="Berechnen", command=Switch).grid(row=3, column=1)
wndMain.mainloop()  # Konstantes öffnen des Fensters


