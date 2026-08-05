max_value = int(input("Input max number:"))


for i in range (max_value, 1, -1):
    for k in range (i):
        print(i, end="")
    print()
if i == 2:
    min_value = 1
    print(min_value)
    for i in range (min_value, max_value + 1, 1):
        for k in range (i):
            print(i, end="")
        print()