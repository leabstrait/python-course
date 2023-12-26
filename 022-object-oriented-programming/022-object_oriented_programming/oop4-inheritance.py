class Employee():

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
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        return not (day.weekday() == 5 or day.weekday() == 6)


class Developer(Employee):
    # Overriding the parent class properties
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print('--->', emp.fullname())

dev_1 = Developer("Labin", "Ojha", 300000, "Python")
dev_2 = Developer("Test", "User", 100000, "Java")

print(dev_1.prog_lang)
print(dev_2.email)

# Method Resolution Order, even if Developer is not defined, it searched the superclasses to find the specific methods
print(help(dev_1))

# Continuing
print(dev_1.pay)
dev_1.applyraise()
print(dev_1.pay)

# # Managers
mgr_1 = Manager('Swastik', 'Thapa', 200000, [dev_1])

print(mgr_1.email)

mgr_1.print_employees()
mgr_1.add_employee(dev_2)
mgr_1.print_employees()

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))