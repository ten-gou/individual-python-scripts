import random


def main():
    print('Please input a string to scramble, or input QUIT to quit')
    baseString = input()

    while baseString != "QUIT":
        baseLength = len(baseString) - 1
        baseArray = [*baseString]
        print("Scrambling '" + baseString + "', with a length of " + str(baseLength + 1))

        scrambledString = ""
        i = 0

        while i <= baseLength:
            y = random.randint(0, len(baseArray) - 1)
            scrambledString += baseArray[y]
            baseArray.pop(y)
            i += 1

        print(scrambledString)
        print('Please input a string to scramble, or input QUIT to quit')
        baseString = input()

main()