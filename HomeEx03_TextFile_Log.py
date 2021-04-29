import HomeEx02_UnitConverter

strContentNew = HomeEx02_UnitConverter.strErgebnis

with open("HomeEx03_TextFile_Log.txt", "r") as fileSample:
    strContent = fileSample.read()
strContent = strContent + strContentNew
with open("HomeEx03_TextFile_Log.txt", "w") as fileSample:
    fileSample.write(strContent)
