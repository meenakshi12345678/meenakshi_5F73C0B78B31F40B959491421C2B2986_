def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Define a student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with sample student objects
student1 = Student("Alice", "S001", 3.8)
student2 = Student("Bob", "S002", 3.9)
student3 = Student("Charlie", "S003", 3.7)