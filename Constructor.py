class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("RJK", 20)
person2 = Person("SAM", 19)

print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")