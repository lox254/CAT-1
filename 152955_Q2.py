#Student class with a dictionary
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # Dictionary to store subject and grade 

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count

    def __str__(self):
        return f"Student(name={self.name}, grades={self.grades})"

#methods
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):        # adding students
        self.students.append(student)

    def display_students(self):         # display students
        if not self.students:
            print("No students in the classroom.")
        else:
            for student in self.students:
                print(student)

    def get_student_average(self, student_name):        # student average
        for student in self.students:
            if student.name == student_name:
                return student.get_average_grade()
        return None

    def get_class_average_for_subject(self, subject):       #class average
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return None
        return total / count

# using an instance of classroom to demonstrate functionalities
if __name__ == "__main__":
    # Creating a classroom
    my_classroom = Classroom()
    
    # Adding students
    student1 = Student("George")
    student1.add_grade("Calculus", 65)
    student1.add_grade("DSA", 55)
    my_classroom.add_student(student1)
    
    student2 = Student("Lokong")
    student2.add_grade("Calculus", 71)
    student2.add_grade("DSA", 67)
    my_classroom.add_student(student2)
    
    # Display all students
    print("All students:")
    my_classroom.display_students()
    
    # Get average grade of a student
    student_name = "George"
    avg_grade = my_classroom.get_student_average(student_name)
    if avg_grade is not None:
        print(f"Average grade for {student_name}: {avg_grade}")
    else:
        print(f"Student {student_name} not found.")
    
    # Get class average for a subject
    subject = "Calculus"
    class_avg = my_classroom.get_class_average_for_subject(subject)
    if class_avg is not None:
        print(f"Class average for {subject}: {class_avg}")
    else:
        print(f"No grades recorded for {subject}.")
