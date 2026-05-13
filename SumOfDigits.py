#variable for storing sum value
sum = 0

#using input function to get a number
num = int(input("Enter a  number(more than 1 digits): "))

#using while loop to find the sum of digits
while num > 0:
    digit = num % 10
    sum += digit
    num = num//10

print("Sum of the digits: "sum)
