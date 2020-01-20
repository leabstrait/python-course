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


emp_1 = Employee("Labin", "Ojha", 300000)
emp_2 = Employee("Test", "User", 100000)


# classmethods demo
print(emp_1.pay)
emp_1.applyraise()
print(emp_1.pay)

Employee.set_raise_amount(1.05)
emp_1.set_raise_amount(1.06)        # but doesn't make much sense

emp_1.applyraise()
print(emp_1.pay)


# staticmethods demo

import datetime
my_date = datetime.date(2020, 1, 18)

print(Employee.is_workday(my_date))
print(emp_1.is_workday(my_date))    # only difference from classmethods and regular method is that staticmethods don't bind the instance or the class via their arguments