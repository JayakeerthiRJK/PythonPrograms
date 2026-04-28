print("PYTHON")
num1 = int(input("Enter a number for num1: "))
num2 = int(input("Enter a number for num2: "))
print("Enter the number of the following function to do the calculation.")
print("1.ADDITION 2.SUBTRACTION 3.DIVISION 4.MULTIPLICATION")
calc = int(input(""))
add = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
if calc == 1:
    print("Addition:",add)
elif calc == 2:
    print("Subtraction:",sub)
elif calc == 3:
    print("Division:",div)
elif calc == 4:
    print("Mutiplication:",mul)
else:
    print("Enter a valiable number!")
