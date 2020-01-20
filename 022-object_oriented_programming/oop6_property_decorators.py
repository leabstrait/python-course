# To add getter, setter, deleter functionalities

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee("Labin", "Ojha", 300000)

print(emp_1.first)
print(emp_1.email)
# print(emp_1.fullname()) # After setting property, () will give error

emp_1.first = "Kushal"

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# Still can't do this
# emp_1.fullname = "Labin Ojha"

# after @fullname.setter, we can
emp_1.fullname = "Labin Ojha"

print(emp_1.fullname)

# Deletion
del emp_1.fullname

print(emp_1.fullname)