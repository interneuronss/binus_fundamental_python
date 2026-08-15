
class Student:

# Nama, nilai
    def __init__(self, name="None", score=0):
        self.name = name
        self.score = score


    def printStudent(self):
        print("-----Student Info-----")
        print("Student Name : ", self.name, "\nScore : ", self.score)

    def getName(self):
        return self.name
    def getScore(self):
        return self.score

    def setName(self, name):
        self.name = name
    def setScore(self, score):
        self.score = score

def menu():
    print("-----Pick an option-----")
    print("1. Declare Name and Score\n2. Display Name and Score\n3. Change Name and Score\n4. Delete Name and Score\n5. Exit Program")

    option = int(input("Enter your choice (1-5): "))
    return option



def main():
    student = None
    status = True

    while status:
        option = menu()
    # OPTION 1
        if option == 1:
            name = input("Enter Student Name: ")
            score = int(input("Enter Student Score: "))
            student = Student(name, score)
            print(">> Data successfully added.")
    # OPTION 2
        elif option == 2:
            if student is not None:
                student.printStudent()
            else:
                print("Name: None\nScore: None")
                print(">> Student data not found.")

    # OPTION 3
        elif option == 3:
            if student is not None:
                name_or_score = input("What would you like to change? (Name/Score):")
                if name_or_score == "Name":
                    new_name = input("Enter Student Name: ")
                    student.setName(new_name)
                    print(">> Data successfully updated.")
                elif name_or_score == "Score":
                    new_score = int(input("Enter Student Score (0-100): "))
                    if new_score > 100 or new_score < 0:
                        print(">>Score must be between 0 and 100")
                    else:
                        student.setScore(new_score)
                        print(">> Data successfully updated.")
                else:
                    print("Invalid input. Please try again.")
            else:
                print(">> No student data found to update.")
    # OPTION 4
        elif option == 4:
            if student is not None:
                student = None
                score = 0
                print(">> Data successfully deleted.")
            else:
                print(">>No student record to delete.")
    # OPTION 5
        elif option == 5:
            print(">>Thank you for using my program.")
            status = False

        else:
            print("Invalid input. Please try again.")


main()













