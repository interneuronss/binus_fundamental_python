status = True

while(status):
    num = int(input("Enter any number:"))
    check = num % 2
    if (check == 1):
        print("The number", num, "is odd")
    else:
        print("The number", num, "is even")
    
    Y_N = input("Do you want to repeat? Y/N:")
    if Y_N == "Y":
        continue
    else:
        print("Program Stops\nThank you for using my program ^^")
        status = False
        break
        