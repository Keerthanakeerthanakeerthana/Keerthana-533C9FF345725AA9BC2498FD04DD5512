class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
if __name__ == "__main__":
    students = [
        Student("Nisha", "A101", 4.1),
        Student("Keerthana", "B102", 4.0),
        Student("Jeeva", "C103", 4.0),
        Student("Kokila", "D104", 4.2),
    ]

    sorted_students = sort_students(students)

    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
      
