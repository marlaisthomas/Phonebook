from person import Person


class Phonebook:
    def __init__(self):
        self.persons = []

    def injectTestData(self):
        self.persons.append(Person("Heinz",   "Grünwald", "911", "Gotenstr.",      "13",  "53111", "Bonn"       ))
        self.persons.append(Person("Nele",    "Amiri",    "112", "Schubertstr.",   "38",  "50676", "Köln"       ))
        self.persons.append(Person("Claudia", "Weckmann", "123", "Dornierstr.",    "112", "51381", "Leverkusen" ))
        self.persons.append(Person("Bertolt", "Heising",  "007", "Breslauer Str.", "3",   "22297", "Hamburg"    ))

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
        print(f"Currently {len(self.persons)} persons loaded:")
        for person in self.persons:
            person.print()

    def writeToFile(self):
        with open("phonebook.txt", 'w+') as textFile:
            for person in self.persons:
                person.writeToFile(textFile)

    def readFromFile(self):
        self.persons = []
        with open("phonebook.txt", 'r') as textFile:
            while True:
                readPerson = Person.readFromFile(textFile)
                if not readPerson is None:
                    self.persons.append(readPerson)
                else:
                    break




# phonebook = Phonebook()
# phonebook.writeToFile()

# #print(type(person))
