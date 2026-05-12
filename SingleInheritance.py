class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


employee1 = Employee("RJK", 20, 10000)
employee2 = Employee("SAM", 19, 120000)

print(f"{employee1.name} is {employee1.age} years old and has a salary of {employee1.salary}.")
print(f"{employee2.name} is {employee2.age} years old and has a salary of {employee2.salary}.")