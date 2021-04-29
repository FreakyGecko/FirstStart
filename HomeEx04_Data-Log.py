import json
import HomeEx02_UnitConverter

with open("HomeEx04_UnitConverterLog.txt", "r") as fileLog:
    strContent = json.loads(fileLog.read())

with open("HomeEx04_UnitConverterLog.txt", "w") as fileLog:
    strContent.append(HomeEx02_UnitConverter.strErgebnis)
    fileLog.write(json.dumps(strContent))
