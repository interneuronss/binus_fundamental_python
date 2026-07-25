import math as m

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if (a == 0) or (b == 0) or (c == 0):
    print("Not a quadratic equation")
else:
    disc = (b ** 2) - (4 * a * c)
    print(f"Quadratic Equation: {a}x² + {b}x + {c}")
    print("Discriminant value:", disc)

if (disc > 0):
    #distinct roots
    x1 = (-b + m.sqrt(disc)) / (2 * a)
    x2 = (-b - m.sqrt(disc)) / (2 * a)
    
    print("It has 2 distinct roots")
    print("Root 1:", x1)
    print("Root 2:", x2)
    
elif (disc < 0):
    #imaginary roots
    re = -b / (2 * a)
    im = m.sqrt(-disc) / (2 * a)

    print("It has imaginary roots")
    print(f"x1 = {re} + {im}i")
    print(f"x2 = {re} - {im}i")
    
elif (disc == 0):
    #double root
    x = -b / (2 * a)

    print("It has a double root")
    print("Root = ", x)
    