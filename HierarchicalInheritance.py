class Animal:
    def sound(self):
        return "Animals make sounds."
    
class Dog(Animal):
    def sound(self):
        return "Dogs bark."
    
class Cat(Animal):
    def sound(self):
        return "Cats meow."
    
dog1 = Dog()
cat1 = Cat()

print(dog1.sound())
print(cat1.sound()) 
    
