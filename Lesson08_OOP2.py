# Object oriented programming
class Player():  # Parent Model (wird bei den Kinder-Modellen in der Klammer übergeben)
    def __init__(self, Vorname, Nachname, Groesse, Gewicht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Groesse = Groesse
        self.Gewicht = Gewicht

    def kg2pound(self):  # Eine Funktion innerhalb einer Klasse wird als Methode bezeichnet
        pounds = self.Gewicht * 2.20462
        return pounds


class GolfPlayer(Player):  # Definiert das Objekt, holt sich die Elemente aus dem Parent-Modell
    def __init__(self, Vorname, Nachname, Groesse, Gewicht, Punkte, Handicap, Turniere):  # Beim ersten Aufruf wird der Prozess ausgeführt
        super().__init__(Vorname=Vorname, Nachname=Nachname, Groesse=Groesse, Gewicht=Gewicht)
        self.points = Punkte
        self.handicap = Handicap
        self.tournaments = Turniere


class FootballPlayer(Player):
    def __init__(self, Vorname, Nachname, Groesse, Gewicht, Tore, RoteKarten, GelbeKarten):
        super().__init__(Vorname=Vorname, Nachname=Nachname, Groesse=Groesse, Gewicht=Gewicht)
        self.Tore = Tore
        self.RoteKarten = RoteKarten
        self.GelbeKarten = GelbeKarten


player01_object = GolfPlayer(Vorname="Tiger", Nachname="Woods", Groesse=180, Gewicht=80, Handicap=2, Punkte=20000, Turniere=300)  # Hier wird ein neues Objekt basierend auf dem Modell GolfPlayer erstellt.
player02_object = GolfPlayer(Vorname="Noob", Nachname="Best", Groesse=165, Gewicht= 55, Handicap=55, Punkte=0, Turniere=0)

print(player02_object.Gewicht)

listGolfPlayers = [player01_object, player02_object]

for player in listGolfPlayers:
    print(str(player.points) + " Punkte in " + str(player.tournaments) + " Turnieren")

print(player02_object.kg2pound())

FBSpieler01 = FootballPlayer(Vorname="Cristiano", Nachname="Ronaldo", Groesse="170", Gewicht="70", Tore="500", RoteKarten="30", GelbeKarten="250")

listGolfPlayers.sort(key=lambda x: x.Vorname, reverse=False)  # Durch die Lamda funktion werden die kompletten Datensätze sortiert (nicht nur die Spalte)

for player in listGolfPlayers:
    print("Name: " + player.Vorname)

