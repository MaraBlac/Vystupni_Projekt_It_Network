class Person:
    def __init__(self, name, surname, phone_number, age):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.age = age

people = []

def add_person():
    name = input("Vložte křestní jméno: ")
    surname = input("Vložte příjmení : ")
    phone_number = input("Vložte telefoní čísllo: ")
    age = input("Vložte věk: ")
    person = Person(name, surname, phone_number, age)
    people.append(person)

def print_people():
    for person in people:
        print(f"{person.name} {person.surname} - Telefon: {person.phone_number}, Věk: {person.age}")

def find_person():
    name = input("Vložte jméno hledaného: ")
    surname = input("Vložte příjmení hledaného: ")
    for person in people:
        if person.name == name and person.surname == surname:
            print(f"{person.name} {person.surname} - Telefon: {person.phone_number}, Věk: {person.age}")
            return
    print("Pojištěnec nenalezen.")
