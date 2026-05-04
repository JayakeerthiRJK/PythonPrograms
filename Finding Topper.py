#List of student names
students = ["Vijay","Ajith","Sam","Tom","Jerry","Jack"]

#List of student marks
marks = [78, 92, 85, 99, 67, 88]

#Assigning first mark as the topper
topper_mark = marks[0]
topper_name = students[0]

#Compare each mark with largest mark
for i in range(len(marks)):
    if marks[i] > topper_mark:
        topper_mark = marks[i]
        topper_name = students[i]

#Print the topper
print("Topper ", topper_name)
print("Mark: ", topper_mark)
