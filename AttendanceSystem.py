class AttendanceSystem:
    def __init__(self):
        self.attendance = {}
    
    def mark_present(self, student_name):
        self.attendance[student_name] = "Present"

    def mark_absence(self, student_name):
        self.attendance[student_name] = "Absent"

attendance_system = AttendanceSystem()
attendance_system.mark_present("RJK")
attendance_system.mark_absence("TOM")
attendance_system.mark_present("SAM")
print(attendance_system.attendance)