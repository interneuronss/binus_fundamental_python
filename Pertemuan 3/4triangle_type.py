a = float(input("Side A:"))
b = float(input("Side B:"))
c = float(input("Side C:"))

#Triangle check

if (a + b <= c) or (b + c <= a) or (a + c <= b):
    print("Not Triangle")
else:
    if (a**2 + b**2 == c**2) or (c**2 + a**2 == b**2) or (c**2 + b**2 == a**2):
        print("Right-angled triangle")
    elif (a == c) and (a == b):
        print ("Equilateral triangle")
    elif (a == c) or (a == b) or (b == c):
        print ("Isosceles triangle")
    else:
        print("Scalene triangle")
    