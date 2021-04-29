import tkinter

wndCalc = tkinter.Tk(className="Test")

lblTitle01 = tkinter.Label(wndCalc, text="Wert").grid(row=0, column=0)
lblTitle02 = tkinter.Label(wndCalc, text="Einheit").grid(row=0, column=1)
lblTitle03 = tkinter.Label(wndCalc, text="Ergebnis").grid(row=0, column=2)
lblTitle04 = tkinter.Label(wndCalc, text="Einheit").grid(row=0, column=3)

fltInput01 = tkinter.Entry(wndCalc).grid(row=1, column=0)
strInput02 = tkinter.Entry(wndCalc).grid(row=1, column=1)
strResult01 = tkinter.Label(wndCalc, text="x").grid(row=1, column=2)
strInput03 = tkinter.Entry(wndCalc).grid(row=1, column=3)

wndCalc.mainloop()
