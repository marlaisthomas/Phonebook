from person import Person
from Phonebook import Phonebook
import os


def elim(phonebook):
    print("Wen suchen Sie?")
    search = input("Suche: ")
    treffer = phonebook.query(search)
    print(f"Zu löschende Einträge ({len(treffer)}):")
    for person in treffer:
        person.print()
    answer = input("Möchten Sie die ausgesuchten Einträge löschen? (j/n) ")
    if answer.lower() == "j":
        for person in treffer:
            phonebook.remove(person)
        print("Einträge wurden erfolgreich entfernt")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    phonebook = Phonebook()
    phonebook.readFromFile()
    #phonebook.injectTestData()
    #phonebook.writeToFile()
    #heinz = Person("heinz", "djkfj")
    #print(heinz.getAttrList())
    run = True
    while run:
        clear()
        print(" ")
        print(" ")
        print("Wählen Sie den passenden Buchstaben für die gewünschte Option:")
        print("    a: List all")
        print("    b: Telefonnummer suchen")
        print("    c: Kontakt hinzufügen")
        print("    d: Kontakt entfernen")
        print("    e: Bearbeiten")
        print("    f: Programm beenden")

        choice = (input("    ")).lower()

        clear()

        if choice == "a":
            phonebook.printAll()
            input("Press ENTER to continue ...")

        elif choice == "b":
            print("Wen suchen Sie?")
            search = input("Suche: ")
            treffer = phonebook.query(search)
            print(f"Gefundene {len(treffer)} Einträge:")
            for person in treffer:
                person.print()
            input("Press ENTER to continue ...")

        elif choice == "c":
            #test = input("Möchten Sie erst prüfen, ob der Kontakt schon angelegt ist? (j/n)")
            #if test.lower() == "j":
            #    input("press enter")
            newPerson = phonebook.add()
            if newPerson != None:
                print("Eintrag wurde dem Telefonbuch hinzugefügt als:")
                newPerson.print()
            input("Press ENTER to continue ...")

        elif choice == "d":
            elim(phonebook)
            input("Press ENTER to continue ...")

        elif choice == "e":
            print("Wen suchen Sie?")
            search = input("Suche: ")
            treffer = phonebook.query(search)
            for person in treffer:
                print("-----------------------------------------------")
                person.print()
                person.readFromInput()
            input("Press ENTER to continue ...")

        elif choice == "f":
            run = False

        phonebook.writeToFile()


if __name__ == "__main__":
    main()
