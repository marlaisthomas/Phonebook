from person import Person
from phonebook import Phonebook


def elim(phonebook):
    print("Geben Sie möglichst viele Informationen über den gesuchten Eintrag ein. Falls Sie die jeweilige Info nicht wissen, drücken Sie Enter: ")
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


def main():
    phonebook = Phonebook()
    phonebook.injectTestData()
    run = True
    while run:
        print(" ")
        print(" ")
        print("Wählen Sie den passenden Buchstaben für die gewünschte Option:")
        print("    0: List all")
        print("    a: Telefonnummer suchen")
        print("    b: Kontakt hinzufügen")
        print("    c: Kontakt entfernen")
        print("    d: Programm beeenden")
        print("    e: Bearbeiten")
        print()
        choice = input("    ")

        if choice == "a":
            print("Geben Sie möglichst viele Informationen über den gesuchten Eintrag ein. Falls Sie die jeweilige Info nicht wissen, drücken Sie Enter: ")
            search = input("Suche: ")
            treffer = phonebook.query(search)
            print(f"Found {len(treffer)} entries:")
            for person in treffer:
                person.print()

        elif choice == "b":
            newPerson = phonebook.add()
            if newPerson != None:
                print("Eintrag wurde dem Telefonbuch hinzugefügt als:")
                newPerson.print()

        elif choice == "c":
            elim(phonebook)

        elif choice == "d":
            run = False

        elif choice == "0":
            phonebook.printAll()

        elif choice == "e":
            print("Geben Sie möglichst viele Informationen über den gesuchten Eintrag ein. Falls Sie die jeweilige Info nicht wissen, drücken Sie Enter: ")
            search = input("Suche: ")
            treffer = phonebook.query(search)
            for person in treffer:
                print("-----------------------------------------------")
                person.print()
                person.readFromInput()


if __name__ == "__main__":
    main()
