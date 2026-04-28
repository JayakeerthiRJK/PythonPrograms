def greatest_number(a,b):
    if a>b:
        return a
    elif a==b:
        return "Both are equal!"
    else:
        return b


num1 = int(input("Enter a value for num1: "))
num2 = int(input("Enter a value for num2: "))

greatest_num = greatest_number(num1,num2)

print(f"The greatest number is {greatest_num}")
