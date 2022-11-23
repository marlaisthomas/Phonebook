from person import Person


class Phonebook:
    def __init__(self):
        self.persons = []

    def injectTestData(self):
        self.persons.append(Person("Heinz",   "Grünwald", "911", "Gotenstr.",      "Bonn",       "53111", "13" ))
        self.persons.append(Person("Nele",    "Amiri",    "112", "Schubertstr.",   "Köln",       "50676", "38" ))
        self.persons.append(Person("Claudia", "Weckmann", "123", "Dornierstr.",    "Leverkusen", "51381", "112"))
        self.persons.append(Person("Bertolt", "Heising",  "007", "Breslauer Str.", "Hamburg",    "22297", "3"  ))


    def add(self):
        neu = Person()
        neu.readFromInput()
        self.persons.append(neu)
        return neu

    def query(self, search):
        treffer = []
        for person in self.persons:
            for i in person.getAttrList():
                if i.strip() != '' and search.lower() in i.lower():
                    if not person in treffer:
                        treffer.append(person)
        return treffer

    def remove(self, person):
        if person in self.persons:
            self.persons.remove(person)

    def printAll(self):
        for person in self.persons:
            person.print()

    def writeInFile(self):
            with open("phonebook.txt" ) as textFile:
                textFile.write(self.persons)

            self.persons
