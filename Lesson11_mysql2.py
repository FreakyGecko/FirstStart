# Vor Programmierung unten im Terminal Befehl "pip install mysql-connector-python" eingeben
# => Wird heruntergeladen und installiert

import mysql.connector

# Verbindung braucht (1) Link (2) Benutzername und (3) Passwort
MeineDB = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n",
    database="sql11404167"  # Alle Befehle sollen in der angeführten Datenbank erfolgen (user name)
)

DBAktion = MeineDB.cursor()  # Sogenannte Cursor-Methode um SQL-Befehle an die Datenbank zu schicken.
# Der Befehl kann auch als Variable vorher angelegt werden?
sql = "DROP TABLE IF EXISTS cpl"
DBAktion.execute(sql)
DBAktion.execute("CREATE TABLE cpl (name VARCHAR(255), address VARCHAR(255))")  #Datenbank kann nur einmal angelegt werden
DBAktion.execute("SHOW TABLES")

for Tabellen in DBAktion:
    print(Tabellen)

DBAktion.execute("ALTER TABLE cpl ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# fügt der Tabelle eine Spalte "id" hinzu mit einer fortlaufenden Nummer
sql = "INSERT INTO cpl (name, address) VALUES (%s, %s)"
# values = ("Christoph", "Bald wo anders")
values = [("Person 1", "Straße 1"), ("Person 2", "Gasse 2"), ("Person 3", "Platz 3")]
DBAktion.executemany(sql, values)  # für eine Liste braucht SQL den Befehl excecuteMANY

MeineDB.commit()  # Speichern der Daten

print(DBAktion.rowcount, "Datensätze in der Tabelle")
print("ID: ", DBAktion.lastrowid)

sql = "SELECT * FROM cpl"
DBAktion.execute(sql)
MeineDaten = DBAktion.fetchall()  # Hier werden alle Ergebnisse aus dem ausgeführten Befehl in die Variable gelesen.
for data in MeineDaten:
    print(data)



MeineDB.close()  # Datenbank sollte aus Sicherheitsgründen immer geschlossen werden, sonst bleibt die Datenbank im Hintergrund offen.

