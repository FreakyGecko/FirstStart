import json
from urllib.request import urlopen  # Bibliothek und Funktion zur ansteuerung von Online-Daten

api_key = "2410ffa9-4d79-4873-b1af-aab3f07e1796"
URL = "https://transparency.entsoe.eu/api?" + "securityToken=" + api_key + "&documentType=" + "A73" + "&processType=" + "A16" + "&in_Domain=" + "10YAT-APG------L" + "&periodStart=" + "202101010100&periodEnd=202101020100 "
print(URL)

response = urlopen(URL)
data = json.load(response)

print(data)
#print(data["weather"][0]["description"])  # Weil nach weather "[" steht muss man auf den ersten wert mit [0] zugreifen
