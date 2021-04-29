# Durch Suche json Sample findet man direkt einfache Programme
# https://support.oneskyapp.com/hc/en-us/articles/208047697-JSON-sample-files

import json

with open("Lesson09_Download_example_2.json") as file:
    data = json.load(file)

print(data["quiz"]["sport"]["q1"]["answer"])

# Endpoint = Link (Schnittstelle) : API Application Programming Interface
