import time
import datetime

import time
import datetime

class Phonebook:
    def __init__(self, name, street, city, number):
        self.name = ' '
        self.street = ' '
        self.city = ' '
        self.number = ' '

    def print(self):
        print(f"{self.name}")

pers1 = Phonebook("Heinz Grünwald", "Gotenstr. 13", "53111 Bonn", "028839116")
pers2 = Phonebook("Nele Amiri", "Schubertstr. 38", "50676 Köln", "02217632002")
pers3 = Phonebook("Claudia Weckmann", "Dornierstr. 112", "51381 Leverkusen", "022315717")
pers4 = Phonebook("Bertolt Heising", "Breslauer Str. 3", "22297 Hamburg", "040219613")

#pers4.print()

global listP
listP = [["Grünwald", "Heinz", "Gotenstraße", "13", "53111", "Bonn", "028839116"]]
listP.append(["Amiri", "Nele", "Schubertstraße", "38", "50676", "Köln", "02217632002"])
listP.append(["Weckmann", "Claudia", "Dornierstraße", "112", "51381", "Leverkusen", "022315717"])
listP.append(["Heising", "Bertolt", "Breslauer Straße", "3", "22297", "Hamburg", "040219613"])
listP.append(["Gause", "Gundula", "Bonner Wall", "47", "50117", "Köln", "0221219613"])
listP.append(["Wischnewski", "Robert", "Mozartstraße", "11", "30161", "Hannover", "05717113042"])
listP.append(["Franziska", "Mahler", "Uhlandstraße", "41", "53315", "Bonn", "0228482993" ])
listP.append(["Traunstein", "Helge", "Mühlenstraße", "8", "31237", "Hildesheim", "052191736"])
listP.append(["Ucar", "Cem", "Herbertstraße", "24", "36381", "Gießen", "0471116265"])
listP.append(["Jork", "Maria", "Am Gesundbrunnen", "29", "10443", "Berlin", "030518271"])




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
    neu = [lastName, firstName, street, houseNum, plz, city, telNum]
    listP.append(neu)
    print("Eintrag wurde dem Telefonbuch hinzugefügt als:\n" + ", ".join(neu))



def query():
    print("Geben Sie möglichst viele Informationen über den gesuchten Eintrag ein. Falls Sie die jeweilige Info nicht wissen, drücken Sie Enter: ")
    lastName = input("Nachname: ")
    firstName = input("Vorname: ")
    street = input("Straße: ")
    houseNum = input("Hausnummer: ")
    plz = input("Postleitzahl: ")
    city = input("Stadt: ")
    telNum = input("Telefonnummer: ")
    global treffer
    treffer = []
    global count
    count = -1
    for attr in listP:
        count += 1
        for i in attr:
            if i != '' and i.lower() in [lastName.lower(), firstName.lower(), street.lower(), houseNum.lower(), plz.lower(), city.lower(), telNum.lower()]:
                treffer.append(listP[count])
                global zaehlung
                zaehlung = []
                zaehlung.append(count)
                global x
                x = listP[count]
                if len(treffer) == 1:
                    print()
                print(str(x[1]) + ' ' + str(x[0]) + ', ' + str(x[2]) + ' ' + str(x[3])+ '/ ' + str(x[4]) + ' ' + str(x[5]) + ',' + ' Tel. ' +  str(x[6]))
                print(' ')





def elim():
    query()
    answer = input("Möchten Sie die ausgesuchten Einträge löschen? (j/n) ")
    if answer.lower() == "j":
        for lauf_v in zaehlung:
            del listP[lauf_v]
        print("Einträge wurden erfolgreich entfernt")
    treffer.clear()




def exit():
    y == False




def main():

    global listP
    listP = [["Grünwald", "Heinz", "Gotenstraße", "13", "53111", "Bonn", "028839116"]]
    listP.append(["Amiri", "Nele", "Schubertstraße", "38", "50676", "Köln", "02217632002"])
    listP.append(["Weckmann", "Claudia", "Dornierstraße", "112", "51381", "Leverkusen", "022315717"])
    listP.append(["Heising", "Bertolt", "Breslauer Straße", "3", "22297", "Hamburg", "040219613"])
    listP.append(["Gause", "Gundula", "Bonner Wall", "47", "50117", "Köln", "0221219613"])
    listP.append(["Wischnewski", "Robert", "Mozartstraße", "11", "30161", "Hannover", "05717113042"])
    listP.append(["Franziska", "Mahler", "Uhlandstraße", "41", "53315", "Bonn", "0228482993" ])
    listP.append(["Traunstein", "Helge", "Mühlenstraße", "8", "31237", "Hildesheim", "052191736"])
    listP.append(["Ucar", "Cem", "Herbertstraße", "24", "36381", "Gießen", "0471116265"])
    listP.append(["Jork", "Maria", "Am Gesundbrunnen", "29", "10443", "Berlin", "030518271"])
    directory_file = open("Phonebook1.txt", "w")




    global y
    y = True
    while y == True:
        print(" ")
        print(" ")
        print("Wählen Sie den passenden Buchstaben für die gewünschte Option:")
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
            exit()





if __name__ == "__main__":
    main()
