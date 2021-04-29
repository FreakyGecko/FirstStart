import json
from urllib.request import urlopen  # Bibliothek und Funktion zur ansteuerung von Online-Daten

api_key = "c879fcd01314ad8339878a42751e751f"

response = urlopen("http://api.openweathermap.org/data/2.5/weather?q=Vienna&appid=" + api_key)
data = json.load(response)

print(data)
print(data["weather"][0]["description"])  # Weil nach weather "[" steht muss man auf den ersten wert mit [0] zugreifen

# Weitere api Daten für Österreich https://www.data.gv.at/

