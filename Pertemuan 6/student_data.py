class Student:
    stuCount = 0

# Nama, kelas, lokasi sekolah, total murid
    def __init__(self, name="Student", grade=0, location="School A"):
        self.name = name
        self.grade = grade
        self.location = location
        Student.stuCount += 1

    def displayCount(self):
        print("Total students: ", Student.stuCount)

    def printStudent(self):
        print("Student Name : ", self.name, "\nStudent Grade : ", self.grade, "\nStudent Location : ", self.location)

student1 = Student("A", 10, "School A")
student1.printStudent()
student1.displayCount()

student2 = Student("B", 7, "School B")
student2.printStudent()
student2.displayCount()