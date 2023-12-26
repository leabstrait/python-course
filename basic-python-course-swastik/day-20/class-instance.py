# OOP
# Encapsulate properties and behaviours
# Abstraction
# Allow code reuse - Inheritance

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        print(f"{self.first} {self.last}")

    def applyraise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        Employee.raise_amount = amount

    @staticmethod
    def is_workday(day):
        return not (day.weekday() == 5 or day.weekday() == 6)


emp_3 = Employee('Badri', 'Aran', 300000)

import datetime

today = datetime.datetime.now()

print(Employee.is_workday(today + datetime.timedelta(days=1)))
print(emp_3.is_workday(today))