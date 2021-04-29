# Programmierung einer grafischen Oberfläche
import tkinter  # Zwischen Python 2 und 3 gab es einige Umbenennungen, "Tkinter" ist ein Indikator für eine alte Version
import random
from tkinter import messagebox  # wird nicht mit der Bibliothek importiert

secret = random.randint(1, 20)

window = tkinter.Tk()  # Es wird immer zuerst ein Element erstellt, in diesem Fall ein Fenster


LabelHello = tkinter.Label(window, text="Hallo Fenster")
LabelHello.pack()

Name = tkinter.Entry(window)
Name.pack()


def Schalter():
    if int(Name.get()) == secret:
        Ergebnis = "Gewonnen"
    elif int(Name.get()) > secret:
        Ergebnis = "Zu hoch"
    else:
        Ergebnis = "Zu niedrig"

    messagebox.showinfo("Ergebnis:", Ergebnis)

submit = tkinter.Button(window, text="Senden", command=Schalter)


submit.pack()

window.mainloop()  # Sorgt dafür, dass das Fenster konstant offen bleibt
