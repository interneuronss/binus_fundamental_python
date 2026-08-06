
grade_to_gpa = {
    "A": 4.00,
    "A-": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.00,
    "C-": 1.75,
    "D": 1.50,
    "E": 1.20,
}

grade_points = 0.0
count = 0


status = True
while status:
    grade_input = input("Enter Grade Category (Press Enter to Stop): ").strip()
    
    if grade_input == "":
        status = False
        break
        
    if grade_input in grade_to_gpa:
        grade_points += grade_to_gpa[grade_input]
        count += 1
    else:
        print("Invalid Grade Entered")


if count == 0:
    print("No Grade Entered\nRetry Program")
    quit()

average = grade_points / count

closest_designation = "A"
smallest_difference = float("inf")

for letter_grade, point_value in grade_to_gpa.items():
    difference = abs(point_value - average)
    if difference < smallest_difference:
        smallest_difference = difference
        closest_designation = letter_grade

print(
    f"The average grade is {average} with a designation of {closest_designation}"
)
