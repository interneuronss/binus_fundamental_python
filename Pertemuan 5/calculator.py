# Exercise calculator

def user_info():
    print("Azzura")
    print("Jakarta, Indonesia")


# Calculator
def calculator():
    option = input("Enter Menu (+|-|/|*|%|stop): ")

    if option == "stop":
        return option, None, None

    value_1 = float(input("Enter value 1: "))
    value_2 = float(input("Enter value 2: "))
    return option, value_1, value_2


def add(v1, v2):
    print(v1 + v2)


def sub(v1, v2):
    print(v1 - v2)


def div(v1, v2):
    if v2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(v1 / v2)


def mul(v1, v2):
    print(v1 * v2)


def modulo(v1, v2):
    if v2 == 0:
        print("Error: Cannot perform modulo by zero!")
    else:
        print(v1 % v2)


# Main program

user_info()

option = ""
status = True

while (status):
    option, value_1, value_2 = calculator()

    if option == "stop":
        print("Program stopped. Thank you for using my program")
        status = False
    elif option == "+":
        add(value_1, value_2)
    elif option == "-":
        sub(value_1, value_2)
    elif option == "/":
        div(value_1, value_2)
    elif option == "*":
        mul(value_1, value_2)
    elif option == "%":
        modulo(value_1, value_2)
    else:
        print("Invalid option")
