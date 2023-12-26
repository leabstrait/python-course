from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # @staticmethod LIMITATION:1 Doesn't preserve cls name while creating instances from subclasses
    @staticmethod
    def from_fathers_birthyear(name, fatherbirthyear, fatherpersonsagediff):
        return Person(name, date.today().year - fatherbirthyear - fatherpersonsagediff)
    

    # @classmethod USAGE:1 Create factory method as an alternative constructor
    # @classmethod USAGE:2 Preserves cls name while creating instances from subclasses
    @classmethod
    def from_birth_year(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person_1 = Person('Aman', 21)
person_1.display()

person_2 = Person.from_birth_year('Gopal', 1999)
person_2.display()


class Man(Person):
    sex = 'Male'

man_1 = Man.from_birth_year('Darshan', 1998)
print(isinstance(man_1, Man))

man_2 = Man.from_fathers_birthyear('Labin', 1960, 20)
man_2.display()
print(isinstance(man_2, Man))
print(isinstance(man_2, Person))
