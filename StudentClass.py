class student:
    name = ""
    marks = []

    def calculate_grade(self):
        total = 0
        for i in range(len(self.marks)):
            total += self.marks[i]
        if total >= 450:
            grade = "A+"
        elif total >= 400:
            grade = "A"
        elif total >= 350:
            grade = "B+"
        elif total >= 300:
            grade = "B"
        elif total >= 250:
            grade = "C+"
        elif total >= 200:
            grade = "c"
        else:
            grade = "f"

        return f"Hi {self.name}, your grade is {grade}"


student_1 = student()

student_1.name = input("Enter the name for student 1: ")

for i in range(5):
    mark = int(input(f"Enter the mark for subject {i+1}: "))
    student_1.marks.append(mark)
print(student_1.marks)
print(student_1.calculate_grade())

        
