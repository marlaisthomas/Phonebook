import time
import datetime

class Phonebook:
    def __init__(self, name, street, city, number):
        self.name = ' '
        self.street = ' '
        self.city = ' '
        self.number = ' '

pers1 = Phonebook("Heinz Grünwald", "Gotenstr. 13", "53111 Bonn", "028839116")
pers2 = Phonebook("Nele Amiri", "Schubertstr. 38", "50676 Köln", "02217632002")
pers3 = Phonebook("Claudia Weckmann", "Dornierstr. 112", "51381 Leverkusen", "022315717")
pers4 = Phonebook("Bertolt Heising", "Breslauer Str. 3", "22297 Hamburg", "040219613")


global listP
listP = [["Grünwald", "Heinz", "Gotenstraße", "13", "53111", "Bonn", "028839116"]]
listP.append(["Amiri", "Nele", "Schubertstraße", "38", "50676", "Köln", "02217632002"])
listP.append(["Weckmann", "Claudia", "Dornierstraße", "112", "51381", "Leverkusen", "022315717"])
listP.append(["Heising", "Bertolt", "Breslauer Straße", "3", "22297", "Hamburg", "040219613"])
listP.append(["Gause", "Gundula", "Bonner Wall", "47", "50117", "Köln", "0228219613"])

def add():
    lastName = input("Wie lautet der Nachname des neuen Kontakts? ")
    firstName = input("Wie lautet der Vorname? ")
    street = input("In welcher Straße wohnt die Person? ")
    if street[-3:].lower() == "str":
        street = street + "aße" 
    elif street[-4:].lower() == "str.":
        punkt = street.replace(".", "a")
    street = punkt + "ße"
    houseNum = input ("Und die Hausnummer: ")
    plz = input ("Postleitzahl? ")
    city = input ("In welcher Stadt lebt die Person? ") 
    telNum = input("Welche Telefonnummer hat der Kontakt? ")
    listP.append([lastName + ', ' + firstName, street + ' ' + houseNum, plz + ' ' + city, telNum])    


def query():
    print("Geben Sie möglichst viele Informationen über den gesuchten Eintrag ein. Falls Sie die jeweilige Info nicht wissen, drücken Sie Enter: ")
    lastName = input("Nachname: ")
    firstName = input("Vorname: ")
    street = input("Straße: ")
    houseNum = input("Hausnummer: ")
    plz = input("Postleitzahl: ")
    city = input("Stadt: ")
    telNum = input("Telefonnummer: ")
    treffer = []
    count = -1
    for attr in listP:
        count += 1
        for i in attr:
            if i != '' and i.lower() in [lastName.lower(), firstName.lower(), street.lower(), houseNum.lower(), plz.lower(), city.lower(), telNum.lower()]:
                print(listP[count])
        #print(treffer)

