#Creating Dictionary

employee_salary = {
    "Sam":10000,
    "Jayakeerthi":10000000,
    "Mekala":1000000,
    "Mothesh":50000,
    }


highest_salary = list(employee_salary.values())[0]
print(highest_salary)
#Using for loop and if statement
for x,y in employee_salary.items():
    if y > highest_salary:
        highest_salary = y
        employee = x

print("Highest_salary:" , employee, "=", highest_salary)
