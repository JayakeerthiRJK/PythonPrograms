#Variable for getting number from user
num = int(input("Enter the number: "))

#Finding number of digits
num_of_digits = 0

while num > 0:
    num = num//10
    num_of_digits += 1 

print(num_of_digits)
