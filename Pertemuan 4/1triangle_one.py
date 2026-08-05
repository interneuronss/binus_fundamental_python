max_value = int(input("Input max number:"))

for i in range (max_value, 0, -1):
    for k in range (i):
        print(i, end="")
    print()