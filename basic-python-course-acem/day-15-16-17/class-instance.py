
class Employee():
    
    total_employees = 0
    increase_percent = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.__email = first + '.' + last + '@acem.com'
        self._salary = salary
        Employee.total_employees += 1

    def fullname(this):
        return this.first + ' ' + this.last

    @classmethod
    def change_increase_percent(empsdfs, new_percent):
        empsdfs.increase_percent = new_percent


    @staticmethod
    def is_weekend():
        pass

    def promote(self):
        print("You're promoted")
        self._salary = int(self._salary * Employee.increase_percent)

    def __str__(self):
        return (f"{self.first} {self.last} with email add: {self.__email} earns Rs.{self._salary}")

emp_1 = Employee("Labin","Ojha",300000)


print(emp_1)
