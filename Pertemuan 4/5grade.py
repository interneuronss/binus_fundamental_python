# Grade conversion dictionary defined at the top
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

total_points = 0.0
count = 0

# Start input loop
status = True
while status:
    user_grade = input("Enter Grade Category (Press Enter to Stop): ").strip().upper()

    if user_grade == "":
        status = False
        break

    # Check if the entered grade exists in our dictionary
    if user_grade in grade_to_gpa:
        total_points += grade_to_gpa[user_grade]
        count += 1
    else:
        print("Invalid Grade Entered")


if count == 0:
    print("No Grade Entered\nRetry Program")
    quit()


average = total_points / count


closest_designation = "A"
smallest_difference = 100

for grade, point_value in grade_to_gpa.items():
    difference = abs(point_value - average)

    if difference < smallest_difference:
        smallest_difference = difference
        closest_designation = grade

print(f"The average grade is {average:.2f} with a designation of {closest_designation}")