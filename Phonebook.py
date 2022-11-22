

class Phonebook:
    def __init__(self, name="", tel="", street="", city="", plz="", number=""):
        self.name = name
        self.number = number
        self.street = street
        self.city = city
        self.plz = plz
        self.tel = tel

    def getAttrList(self):
        return [
            self.name,
            self.number,
            self.street,
            self.city,
            self.plz,
            self.tel
        ]

    def print(self):
        print(" __________________________________")
        print(f"| Name:     {self.name}")
        print(f"| Tel.:     {self.tel}")
        print(f"| Straße:   {self.street}")
        print(f"| Haus-Nr.: {self.number}")
        print(f"| PLZ:      {self.plz}")
        print(f"| Stadt:    {self.city}")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    def readFromInput(self):
        lastName = input("Wie lautet der Nachname des neuen Kontakts? ")
        firstName = input("Wie lautet der Vorname? ")
        self.name = f"{firstName} {lastName}"
        self.street = input("In welcher Straße wohnt die Person? ")
        if self.street[-3:].lower() == "str":
            self.street += "aße"
        elif self.street[-4:].lower() == "str.":
            punkt = self.street.replace(".", "a")
            self.street = punkt + "ße"
        self.number = input ("Und die Hausnummer: ")
        self.plz = input ("Postleitzahl? ")
        self.city = input ("In welcher Stadt lebt die Person? ")
        self.tel = input("Welche Telefonnummer hat der Kontakt? ")




#print("test")
#pers4.print()
#myNew = Phonebook()
#myNew.readFromInput()
#myNew.print()


global listP
listP = [
    Phonebook("Heinz Grünwald", "Gotenstr. 13", "53111 Bonn", "028839116"),
    Phonebook("Nele Amiri", "Schubertstr. 38", "50676 Köln", "02217632002"),
    Phonebook("Claudia Weckmann", "Dornierstr. 112", "51381 Leverkusen", "022315717"),
    Phonebook("Bertolt Heising", "Breslauer Str. 3", "22297 Hamburg", "040219613")
]

# listP = [["Grünwald", "Heinz", "Gotenstraße", "13", "53111", "Bonn", "028839116"]]
# listP.append(["Amiri", "Nele", "Schubertstraße", "38", "50676", "Köln", "02217632002"])
# listP.append(["Weckmann", "Claudia", "Dornierstraße", "112", "51381", "Leverkusen", "022315717"])
# listP.append(["Heising", "Bertolt", "Breslauer Straße", "3", "22297", "Hamburg", "040219613"])
# listP.append(["Gause", "Gundula", "Bonner Wall", "47", "50117", "Köln", "0221219613"])
# listP.append(["Wischnewski", "Robert", "Mozartstraße", "11", "30161", "Hannover", "05717113042"])
# listP.append(["Franziska", "Mahler", "Uhlandstraße", "41", "53315", "Bonn", "0228482993" ])
# listP.append(["Traunstein", "Helge", "Mühlenstraße", "8", "31237", "Hildesheim", "052191736"])
# listP.append(["Ucar", "Cem", "Herbertstraße", "24", "36381", "Gießen", "0471116265"])
# listP.append(["Jork", "Maria", "Am Gesundbrunnen", "29", "10443", "Berlin", "030518271"])




def add():
    global listP
    neu = Phonebook()
    neu.readFromInput()
    listP.append(neu)
    print("Eintrag wurde dem Telefonbuch hinzugefügt als:")
    neu.print()



def query():
    global listP
    print("Geben Sie möglichst viele Informationen über den gesuchten Eintrag ein. Falls Sie die jeweilige Info nicht wissen, drücken Sie Enter: ")
    search = input("Suche: ")
    # lastName = input("Nachname: ")
    # firstName = input("Vorname: ")
    # street = input("Straße: ")
    # houseNum = input("Hausnummer: ")
    # plz = input("Postleitzahl: ")
    # city = input("Stadt: ")
    # telNum = input("Telefonnummer: ")
    # inputs = [lastName.lower(), firstName.lower(), street.lower(), houseNum.lower(), plz.lower(), city.lower(), telNum.lower()]
    treffer = []
    for person in listP:
        for i in person.getAttrList():
            if i.strip() != '' and search.lower() in i.lower():
                if not person in treffer:
                    treffer.append(person)
    print(f"Found {len(treffer)} entries:")
    for person in treffer:
        person.print()
    return treffer





def elim():
    treffer = query()
    answer = input("Möchten Sie die ausgesuchten Einträge löschen? (j/n) ")
    if answer.lower() == "j":
        for person in treffer:
            listP.remove(person)
        print("Einträge wurden erfolgreich entfernt")




def quit():
    global y
    y = False




def main():

    # global listP
    # listP = [["Grünwald", "Heinz", "Gotenstraße", "13", "53111", "Bonn", "028839116"]]
    # listP.append(["Amiri", "Nele", "Schubertstraße", "38", "50676", "Köln", "02217632002"])
    # listP.append(["Weckmann", "Claudia", "Dornierstraße", "112", "51381", "Leverkusen", "022315717"])
    # listP.append(["Heising", "Bertolt", "Breslauer Straße", "3", "22297", "Hamburg", "040219613"])
    # listP.append(["Gause", "Gundula", "Bonner Wall", "47", "50117", "Köln", "0221219613"])
    # listP.append(["Wischnewski", "Robert", "Mozartstraße", "11", "30161", "Hannover", "05717113042"])
    # listP.append(["Franziska", "Mahler", "Uhlandstraße", "41", "53315", "Bonn", "0228482993" ])
    # listP.append(["Traunstein", "Helge", "Mühlenstraße", "8", "31237", "Hildesheim", "052191736"])
    # listP.append(["Ucar", "Cem", "Herbertstraße", "24", "36381", "Gießen", "0471116265"])
    # listP.append(["Jork", "Maria", "Am Gesundbrunnen", "29", "10443", "Berlin", "030518271"])
    # directory_file = open("Phonebook1.txt", "w")




    global y
    y = True
    while y == True:
        print(" ")
        print(" ")
        print("Wählen Sie den passenden Buchstaben für die gewünschte Option:")
        print("    0: List all")
        print("    a: Telefonnummer suchen")
        print("    b: Kontakt hinzufügen")
        print("    c: Kontakt entfernen")
        print("    d: Programm beeenden")
        print()
        choice = input("    ")

        if choice == "a":
            query()
        elif choice == "b":
            add()
        elif choice == "c":
            elim()
        elif choice == "d":
            quit()
        elif choice == "0":
            global listP
            for p in listP:
                p.print()





if __name__ == "__main__":
    main()
