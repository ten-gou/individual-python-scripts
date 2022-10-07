import string

#str input and stores as a variable
print('Enter a string below:')
inputStr = input()

#returns the str
print('You inputted this: ' + inputStr)

#checks if the str is an int or not
decCheck = inputStr.isdecimal()

#if statement based on whether int or not
if decCheck == True:
    print('The string that you have inputted is an integer!')

    #squares input and stores in variable
    outputNum = int(inputStr) ** 2

    #prints output to terminal
    print('Knowing this, we can use multiplication to square this number, leading to: ' + str(outputNum))
else:
    #prints that answer is not int
    print('The string that you have inputted is not an integer!')