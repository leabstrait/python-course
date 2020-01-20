class Employee:
    
    # Class Variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def applyraise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        return not (day.weekday() == 5 or day.weekday() == 6)

    def __repr__(self):
        # Developer Representation, fallback for str
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        # End User Representation
        return f"{self.fullname()} - {self.email}"

emp_1 = Employee("Labin", "Ojha", 300000)
emp_2 = Employee("Test", "User", 100000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1)) 

print(emp_1.__repr__())
print(emp_1.__str__())
