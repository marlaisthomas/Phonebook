from person import Person


class Phonebook:
    def __init__(self):
        self.persons = []


def writeInFile(self):
             with open("phonebook.txt", "w" ) as textFile:
                textFile.write(self.persons)



phonebook = Phonebook()
phonebook.writeInFile()
