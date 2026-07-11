Title: Converting temperature units
Declaration: grade
Implementation:
Input grade

if grade < 0 or grade > 100:
    Display Invalid grade
elif grade >= 90:
    Display A - Pass
elif grade >= 80:
    Display B - Pass
elif grade >= 70:
    Display C - Pass
elif grade >= 60:
    Display D - Pass
else:
    Display Fail
