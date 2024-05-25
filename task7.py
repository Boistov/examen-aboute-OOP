import datetime

class Person:
    def __init__(self, name, country, birth):
        self.name = name
        self.country = country
        self.birth = birth
    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
        return age

person1 = Person("Saidakbar", "Tajikistan", datetime.date(2004, 2, 10))
print(person1.calculate_age())