class Unternehmen():  # Parent model für Unternehmen
    def __init__(self, FBN, Name_Unt, PLZ, Ort, Land):
        self.FBN = FBN
        self.Name_Unt = Name_Unt
        self.PLZ = PLZ
        self.Ort = Ort
        self.Land = Land


class Person():
    def __init__(self, Vorname, Nachname, Geschlecht):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Geschlecht = Geschlecht


class Mitarbeiter(Unternehmen, Person):
    def __init__(self, FBN, Name_Unt, PLZ, Ort, Land, Vorname, Nachname, Diensteintritt, Vollzeit):
        super().__init__(FBN=FBN, Name_Unt=Name_Unt, PLZ=PLZ, Ort=Ort, Land=Land), \
        super().__init__(Vorname=Vorname, Nachname=Nachname)
        self.Diensteintritt = Diensteintritt
        self.Vollzeit = Vollzeit


Obj_MA_1 = Mitarbeiter(FBN="123456f", Name_Unt="Scheinfirma ohne Haft", PLZ=2335, Ort="Testdort", Land="Österreich",
                       Vorname="Max", Nachname="Muster", Diensteintritt=2010, Vollzeit=True)
Obj_MA_2 = Mitarbeiter(FBN="123456f", Name_Unt="Scheinfirma ohne Haft", PLZ=2335, Ort="Testdort", Land="Österreich",
                       Vorname="Miriam", Nachname="Maxer", Diensteintritt=2015, Vollzeit=False)
