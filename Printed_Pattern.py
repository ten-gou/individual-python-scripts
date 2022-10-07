size = 6

for row in range (1, size):
    for col in range (1, size):
        if row == 1 or row == size-1 or col == 1 or col == size-1:
            print("*", end = " ")
        else:
            print("-", end = " ")
    print()