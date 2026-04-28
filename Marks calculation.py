no_of_subject = 5

student_name = input("Enter the student name: ")

marks = []

total = 0
fullmark = no_of_subject * 100

for i in range(no_of_subject):
    mark = int(input(f"Enter the mark for subject{i+1}: "))
    marks.append(mark)

for i in range(no_of_subject):
    total += marks[i]
    
average = total/no_of_subject
percentage = (total/fullmark)*100

print(f"TotalMark= {total}")
print(f"AverageMark= {average}")
print(f"percentage= {percentage}%")
