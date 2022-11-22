
def inputOptional(label, default):
    if default.strip() != "":
        label += f"({default}) "
    line = input(label)
    if line.strip() == "":
        return default
    else:
        return line


class Person:
    def __init__(self, first_name="", last_name="", tel="", street="", city="", plz="", number=""):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.street = street
        self.city = city
        self.plz = plz
        self.tel = tel

    def getAttrList(self):
        return [
            self.first_name,
            self.last_name,
            self.number,
            self.street,
            self.city,
            self.plz,
            self.tel
        ]

    def print(self):
        print(" __________________________________")
        print(f"| Name:     {self.first_name} {self.last_name}")
        print(f"| Tel.:     {self.tel}")
        print(f"| Straße:   {self.street}")
        print(f"| Haus-Nr.: {self.number}")
        print(f"| PLZ:      {self.plz}")
        print(f"| Stadt:    {self.city}")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    def readFromInput(self):
        self.last_name = inputOptional("Wie lautet der Nachname des neuen Kontakts? ", self.last_name)
        self.first_name = inputOptional("Wie lautet der Vorname? ", self.first_name)
        self.street = inputOptional("In welcher Straße wohnt die Person? ", self.street)
        if self.street[-3:].lower() == "str":
            self.street += "aße"
        elif self.street[-4:].lower() == "str.":
            punkt = self.street.replace(".", "a")
            self.street = punkt + "ße"
        self.number = inputOptional ("Und die Hausnummer: ", self.number)
        self.plz = inputOptional ("Postleitzahl? ", self.plz)
        self.city = inputOptional ("In welcher Stadt lebt die Person? ", self.city)
        self.tel = inputOptional("Welche Telefonnummer hat der Kontakt? ", self.tel)
