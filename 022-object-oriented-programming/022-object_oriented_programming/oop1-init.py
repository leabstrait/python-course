class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Labin", "Ojha", 300000)
emp_2 = Employee("Test", "User", 100000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1))   # This runs in the background for above statement


