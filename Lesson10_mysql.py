# Vor Programmierung unten im Terminal Befehl "pip install mysql-connector-python" eingeben
# => Wird heruntergeladen und installiert

import mysql.connector

# Verbindung braucht (1) Link (2) Benutzername und (3) Passwort
MeineDB = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n"
)

print(MeineDB)

MeinZeiger = MeineDB.cursor()  # Sogenannte Cursor-Methode um SQL-Befehle an die Datenbank zu schicken.
MeinZeiger.execute("SHOW DATABASES")  # "SHOW DATABASES" ist ein SQL-Befehl
# Mit *.execute("CREATE DATABASE dbnamen") kann eine neue Datenbank angelegt werden.

for x in MeinZeiger:
    print(x)

MeineDB.close()  # Datenbank sollte aus Sicherheitsgründen immer geschlossen werden, sonst bleibt die Datenbank im Hintergrund offen.

# danach kann normal Python weitergeschrieben werden
