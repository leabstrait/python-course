# OOP
# Encapsulate properties and behaviour
# Allow code reuse

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = "Labin"
emp_1.last = "Ojha"
emp_1.email = "leabstrait@gmail.com"
emp_1.pay = 300000

emp_2.first = "Test"
emp_2.last = "user"
emp_2.email = "testu@gmail.com"
emp_2.pay = 100000

print(emp_1.email)
print(emp_2.email)


