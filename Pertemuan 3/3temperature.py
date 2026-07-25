#Display Options
print("1 - Celsius to Fahrenheit")
print("2 - Celsius to Kelvin")
print("3 - Fahrenheit to Celsius")
print("4 - Fahrenheit to Kelvin")
print("5 - Kelvin to Celsius")
print("6 - Kelvin to Fahrenheit")

option = input("Select option: ")
option = int(option)

#calculate
if option == 1:
    celsius = float(input("Enter celsius:"))
    fahrenheit = (celsius * 1.8) + 32
    print("Fahrenheit:", fahrenheit)
elif option == 2:
    celsius = float(input("Enter celsius:"))
    kelvin = celsius + 273.15
    print("Kelvin:", kelvin)
elif option == 3:
    fahrenheit = float(input("Enter fahrenheit:"))
    celsius = (fahrenheit - 32) / 1.8
    print("Celsius:", celsius)
elif option == 4:
    fahrenheit = float(input("Enter fahrenheit:"))
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    print("Kelvin:", kelvin)
elif option == 5:
    kelvin = float(input("Enter kelvin:"))
    celsius = kelvin - 273.15
    print("Celsius:", celsius)
elif option == 6:
    kelvin = float(input("Enter kelvin:"))
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    print("Fahrenheit:", fahrenheit)
else:
    print("invalid option")
    