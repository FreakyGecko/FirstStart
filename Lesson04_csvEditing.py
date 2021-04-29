with open("Lesson04.csv","r") as csvFile:
    csvData = csvFile.read().splitlines() # Hier wird die Textdatei in Zeilen gesplittet

    for csvRow in csvData:
        csvRowData = csvRow.split(",") # Hier wird die Zeile in Elemente gesplittet
        print(f"{csvRowData[0]}, in {csvRowData[1]}") # [] ist das x-Element pro Zeile

