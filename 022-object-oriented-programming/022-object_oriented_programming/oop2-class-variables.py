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


print(Employee.num_of_emps)

emp_1 = Employee("Labin", "Ojha", 300000)
emp_2 = Employee("Test", "User", 100000)

print(Employee.num_of_emps)

print(emp_1.pay)
emp_1.applyraise()
print(emp_1.pay)
