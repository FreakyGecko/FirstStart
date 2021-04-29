with open("Lesson03_TextFileExample.txt", "r") as fileSample: # "r" ist für Read, "w" für Write
    strContent = fileSample.read()
    print(strContent)

with open("Lesson03_TextFileExample.txt", "r") as fileSample02:
    strContent02 =fileSample02.read().splitlines() # Befehl Splitlines teilt die Zeilen

    print(strContent02[2]) # "[]" liest eine beliebige Zeile aus

    for intline in strContent02:
        print(intline)

with open("Lesson03_TextFileExample02.txt", "w") as fileSample03:
    fileSample03.write("Digitale Signatur")
    