print("Find your grade")

#inputs
mark = int(input("Enter your mark: "))

#using if condition to find grade
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("You are Fail!!")
