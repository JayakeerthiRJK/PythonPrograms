# MiniCalc class with basic arithmetic operations
class MiniCalc:
    # Method to add two numbers
    def add(self, a, b):
        return a + b
    
    # Method to subtract two numbers
    def subtract(self, a, b):
        return a - b
    
    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b
    
    # Method to divide two numbers
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
        
# Object creation and method calls
calc = MiniCalc()
print(calc.add(10, 5))        # Output: 15
print(calc.subtract(10, 5))   # Output: 5
print(calc.multiply(10, 5))   # Output: 50
print(calc.divide(10, 5))     # Output: 2.0
